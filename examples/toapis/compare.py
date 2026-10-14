"""One common prompt, six requested alternatives; native provider calls.

Dry-run by default. Charges remain unknown until backend settlement confirms them.
"""
from pathlib import Path
import argparse,json,os,sys,hashlib,time
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from tools.toapis_models import MODEL_ROUTES
from tools.graphics import toapis_image
from tools.tool_registry import registry

def main():
 p=argparse.ArgumentParser();p.add_argument('--live',action='store_true');p.add_argument('--output',type=Path,default=ROOT/'projects/toapis-model-comparison/assets/images');a=p.parse_args()
 cases=json.loads(Path(__file__).with_name('cases.json').read_text(encoding='utf-8'));prompt=cases[0]['prompt'];models=[m for m in MODEL_ROUTES if m!='gpt-image-2-vip']
 registry.register_module(toapis_image);tool=registry.get('toapis_image')
 if not a.live:print(json.dumps({'mode':'dry-run','common_prompt':prompt,'models':models,'routes':MODEL_ROUTES},indent=2));return
 a.output.mkdir(parents=True,exist_ok=True);os.environ.setdefault('TOAPIS_STATE_DIR',str(a.output/'private-state'))
 quotes={m:tool.estimate_cost({'prompt':prompt,'model':m}) for m in models}
 if sum(quotes.values())>0.50:raise SystemExit('Comparison quote exceeds $0.50 sub-cap; no submission')
 print(json.dumps({'quotes':quotes,'quoted_total_usd':sum(quotes.values())}),flush=True);rows=[]
 for model in models:
  folder=a.output/model;folder.mkdir(exist_ok=True);evidence=folder/'evidence.json'
  if evidence.exists():rows.append(json.loads(evidence.read_text(encoding='utf-8')));continue
  params={'prompt':prompt,'model':model,'size':'1024x1024','resolution':'1K','n':1,'generation_mode':'generate','output_path':str(folder/'result.png'),'run_id':'om14-compare-'+model}
  started=time.monotonic();result=tool.execute(params)
  if not result.success:
   (folder/'failure.json').write_text(json.dumps({'model':model,'error':result.error,'actual_cost_usd':None,'scope':'No automatic resubmission'},indent=2),encoding='utf-8');raise SystemExit(result.error)
  from PIL import Image
  with Image.open(folder/'result.png') as im:width,height=im.size;fmt=im.format
  row={k:v for k,v in result.data.items() if k not in ('output','outputs')}
  row.update(date='2026-10-14',tool=tool.name,common_prompt=prompt,output_dimensions=[width,height],output_format=fmt,sha256=hashlib.sha256((folder/'result.png').read_bytes()).hexdigest(),elapsed_seconds=round(time.monotonic()-started,2),actual_cost_usd=None,actual_credits=None,comparison='One unseeded text-to-image sample per model; quality tiers differ; not a benchmark',scope='Native ToolRegistry + ToAPIsImage.execute')
  evidence.write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf-8');rows.append(row)
  print(json.dumps({k:row[k] for k in ['model','task_id','status','billing','unit_quote_usd','output_dimensions','elapsed_seconds']}),flush=True)
 (a.output/'runs.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
