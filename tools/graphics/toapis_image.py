"""Community OpenMontage image tool: explicit ToAPIs async route.

New in the ToAPIs community fork, 2026-10-14. AGPL-3.0-or-later.
Only explicitly inspected 1K/n=1 model tiers are enabled.
"""
from contextlib import ExitStack
from decimal import Decimal
from pathlib import Path
import base64,os,time,io

from tools.graphics.openai_image import OpenAIImage
from tools.base_tool import ToolResult,ToolStatus
from tools.provider_pricing import PriceQuoteRequired
from tools.toapis_async import ToAPIsClient,normalize_origin
from tools.toapis_models import MODEL_ROUTES


class ToAPIsImage(OpenAIImage):
    name='toapis_image'
    version='0.1.0'
    provider='toapis'
    install_instructions='Set TOAPIS_API_KEY privately. TOAPIS_BASE_URL defaults to https://toapis.com. See docs/TOAPIS.md.'
    agent_skills=['toapis-image']
    supports={'image_edit':True,'multiple_reference_images':True,'mask':False,'transparent_background':False,'multiple_outputs':False}
    best_for=['Low-cost storyboard stills','Reference-guided scene variations']
    not_good_for=['Video generation','Masks or transparent output','Unverified model tiers']
    side_effects=['Submits a paid ToAPIs image task','Writes PNG and private task receipt']
    idempotency_key_fields=['prompt','model','size','quality','resolution','generation_mode','image_path','image_paths','run_id']
    input_schema={
        'type':'object','required':['prompt'],'additionalProperties':False,
        'properties':{
            'prompt':{'type':'string','minLength':1},
            'model':{'type':'string','enum':list(MODEL_ROUTES),'default':'gpt-image-2-vip'},
            'size':{'type':'string','enum':['1024x1024','1536x1024','1024x1536','1024x576','576x1024'],'default':'1024x1024'},
            'quality':{'type':['string','null'],'enum':['low','medium','high',None]},
            'resolution':{'type':'string','enum':['1K'],'default':'1K'},
            'n':{'type':'integer','enum':[1],'default':1},
            'output_format':{'type':'string','enum':['png'],'default':'png'},
            'output_path':{'type':'string'},
            'generation_mode':{'type':'string','enum':['generate','edit']},
            'image_path':{'type':'string'},
            'image_paths':{'type':'array','items':{'type':'string'},'maxItems':4},
            'run_id':{'type':'string','minLength':1}
        }
    }

    def get_status(self):
        if not os.environ.get('TOAPIS_API_KEY'):return ToolStatus.UNAVAILABLE
        try:normalize_origin(os.environ.get('TOAPIS_BASE_URL','https://toapis.com'))
        except ValueError:return ToolStatus.UNAVAILABLE
        return ToolStatus.AVAILABLE  # Configuration only, not account entitlement.

    def _client(self):
        return ToAPIsClient(os.environ.get('TOAPIS_API_KEY'),os.environ.get('TOAPIS_BASE_URL','https://toapis.com'),'1K')

    @staticmethod
    def _quote(client,model='gpt-image-2-vip'):
        route=MODEL_ROUTES[model]
        catalog=client._json('pricing?model='+model)
        prices=[p for m in catalog.get('data',[]) for p in m.get('prices',[])
                if m.get('id',m.get('model'))==model and p.get('unit')=='request'
                and p.get('conditions',{}).get('quality',route['quality'])==route['quality']
                and str(p.get('conditions',{}).get('resolution','1K')).upper()=='1K'
                and p.get('conditions',{}).get('n',1)==1
                and p.get('conditions',{}).get('input_image_count',route['quoted_input_count'])==route['quoted_input_count']]
        if not prices:raise PriceQuoteRequired('No matching model/tier price. No task submitted.')
        rate=max(Decimal(p['unit_price']) for p in prices)
        if rate<0 or rate>Decimal('0.10'):raise PriceQuoteRequired('Quote exceeds this tool demo sub-cap ($0.10 per task).')
        return rate

    def estimate_cost(self,inputs):
        from jsonschema import validate
        validate(inputs,self.input_schema)
        model=inputs.get('model','gpt-image-2-vip')
        if inputs.get('quality',MODEL_ROUTES[model]['quality'])!=MODEL_ROUTES[model]['quality']:raise ValueError('Quality does not match the inspected model tier')
        return float(self._quote(self._client(),model))

    def execute(self,inputs):
        started=time.monotonic()
        try:
            from jsonschema import validate
            validate(inputs,self.input_schema)
            model=inputs.get('model','gpt-image-2-vip');route=MODEL_ROUTES[model]
            if inputs.get('quality',route['quality'])!=route['quality']:raise ValueError('Quality does not match the inspected model tier')
            paths=list(inputs.get('image_paths') or [])
            if inputs.get('image_path'):paths.insert(0,inputs['image_path'])
            mode=inputs.get('generation_mode','edit' if paths else 'generate')
            if (mode=='edit')!=bool(paths) or len(paths)>4:raise ValueError('Edit needs 1–4 local references; generate accepts none.')
            if paths and model!='gpt-image-2-vip':raise ValueError('Non-VIP reference edits are not validated')
            client=self._client();rate=self._quote(client,model)
            # Run identity is scoped per call, without changing process-global env.
            client.run_id=inputs.get('run_id',os.environ.get('TOAPIS_RUN_ID','default'))
            with ExitStack() as stack:
                params={'model':model,'prompt':inputs['prompt'],'size':inputs.get('size','1024x1024'),'quality':route['quality'],'n':1,'output_format':'png'}
                if paths:params['image']=[stack.enter_context(open(p,'rb')) for p in paths]
                response=client.edit(**params) if paths else client.generate(**params)
            out=Path(inputs.get('output_path','generated_toapis.png'));out.parent.mkdir(parents=True,exist_ok=True)
            raw=base64.b64decode(response.data[0].b64_json)
            from PIL import Image
            with Image.open(io.BytesIO(raw)) as image:
                original_format=image.format;image.load()
                if original_format=='PNG':out.write_bytes(raw)
                else:
                    # Preserve upstream bytes, then serialize a local PNG for the pipeline.
                    suffix={'JPEG':'.jpg','WEBP':'.webp'}.get(original_format,'.bin')
                    original=out.with_name(out.stem+'-original'+suffix);original.write_bytes(raw)
                    image.save(out,format='PNG')
            receipt=client.last_receipt
            return ToolResult(success=True,data={'provider':'toapis','model':model,'operation':mode,'output':str(out),'outputs':[str(out)],'images_generated':1,'original_format':original_format,'saved_format':'PNG','locally_converted':original_format!='PNG','task_id':receipt['task_id'],'request':receipt['request'],'status':receipt['state'],'billing':receipt.get('billing'),'unit_quote_usd':str(rate),'cost_status':'unsettled' if receipt.get('billing') is None else 'billing_reported'},artifacts=[str(out)]+([str(original)] if original_format!='PNG' else []),cost_usd=None,duration_seconds=round(time.monotonic()-started,2),model=model)
        except Exception as exc:
            return ToolResult(success=False,error='ToAPIs image tool failed: '+str(exc))
