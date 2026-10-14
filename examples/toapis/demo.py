"""Native tool smoke test; dry-run by default, --live authorizes billed tasks."""
from pathlib import Path
import argparse,hashlib,json,os,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.tool_registry import registry
from tools.graphics import toapis_image

def main():
    p=argparse.ArgumentParser();p.add_argument('--live',action='store_true');p.add_argument('--output',type=Path,default=ROOT/'projects/toapis-orbital-storyboard/assets/images');args=p.parse_args()
    cases=json.loads(Path(__file__).with_name('cases.json').read_text(encoding='utf-8'))
    registry.register_module(toapis_image)
    tool=registry.get('toapis_image')
    if not args.live:
        print(json.dumps({'mode':'dry-run','tool':tool.name,'provider':tool.provider,'cases':cases},ensure_ascii=False,indent=2));return
    args.output.mkdir(parents=True,exist_ok=True)
    os.environ.setdefault('TOAPIS_STATE_DIR',str(args.output/'private-state'))
    rows=[]
    for case in cases:
        folder=args.output/case['id'];folder.mkdir(exist_ok=True);evidence=folder/'evidence.json'
        if evidence.exists():rows.append(json.loads(evidence.read_text(encoding='utf-8')));continue
        params={'prompt':case['prompt'],'model':'gpt-image-2-vip','quality':'low','resolution':'1K','n':1,'size':'1024x1024','output_format':'png','generation_mode':case['mode'],'output_path':str(folder/'result.png'),'run_id':'openmontage-1014-'+case['id']}
        if case['reference']:params['image_path']=str(args.output/case['reference']/'result.png')
        result=tool.execute(params)
        if not result.success:raise SystemExit(result.error)
        from PIL import Image
        with Image.open(folder/'result.png') as im:width,height=im.size
        row={k:v for k,v in result.data.items() if k not in ('output','outputs')}
        row.update(case_id=case['id'],date='2026-10-14',tool=tool.name,output_dimensions=[width,height],sha256=hashlib.sha256((folder/'result.png').read_bytes()).hexdigest(),actual_cost_usd=None,actual_credits=None,scope='Native ToAPIsImage.execute through upstream ToolRegistry; complete video pipeline not tested')
        evidence.write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf-8');rows.append(row)
        print(json.dumps({k:row[k] for k in ['case_id','task_id','status','billing','output_dimensions']},ensure_ascii=False),flush=True)
    (args.output/'runs.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
