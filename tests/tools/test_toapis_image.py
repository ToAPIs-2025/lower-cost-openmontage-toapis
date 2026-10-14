from pathlib import Path
import unittest,os,json,base64,tempfile,io
from unittest.mock import patch
from types import SimpleNamespace
from tools.graphics.toapis_image import ToAPIsImage
from tools.tool_registry import registry
from tools.graphics import toapis_image
from tools.toapis_async import build_request,ToAPIsClient
from tools.provider_routing import filter_explicit_route

class NativeTests(unittest.TestCase):
 def test_registry_and_exact_route(self):
  self.assertEqual(registry.register_module(toapis_image),['toapis_image'])
  tool=registry.get('toapis_image');self.assertEqual(tool.provider,'toapis')
  self.assertEqual(filter_explicit_route({'preferred_tool':'toapis_image','hosting_provider':'toapis','model':'gpt-image-2-vip'},[tool]),[tool])
  self.assertEqual(filter_explicit_route({'model':'gpt-image-2.5'},[tool]),[])
 def test_bearer_origin_normalization(self):
  with tempfile.TemporaryDirectory() as d:
   c=ToAPIsClient('fake-test','https://toapis.com/v1',state_dir=d)
   self.assertEqual(c.origin,'https://toapis.com')
 def test_aspect_ratio_mapping(self):
  r,_=build_request({'model':'gpt-image-2-vip','prompt':'x','size':'1024x576','quality':'low','n':1})
  self.assertEqual(r['size'],'16:9');self.assertEqual(r['resolution'],'1K')
 def test_unknown_tiers_mask_n_rejected_before_quote(self):
  with patch.object(ToAPIsImage,'_client') as client:
   for params in [{'quality':'high'},{'n':2},{'mask_path':'x'},{'resolution':'4K'},{'model':'unknown-model'}]:
    self.assertFalse(ToAPIsImage().execute({'prompt':'x',**params}).success)
   client.assert_not_called()
 def test_mode_mismatch_before_client(self):
  with patch.object(ToAPIsImage,'_client') as c:
   self.assertFalse(ToAPIsImage().execute({'prompt':'x','generation_mode':'edit'}).success);c.assert_not_called()
 def test_null_billing_preserved_native_file(self):
  with tempfile.TemporaryDirectory() as d:
   from PIL import Image
   buf=io.BytesIO();Image.new('RGB',(2,2),'red').save(buf,format='PNG');fixture=buf.getvalue()
   fake=SimpleNamespace(last_receipt={'task_id':'fake-task','request':{'model':'gpt-image-2-vip'},'state':'completed','billing':None})
   fake.generate=lambda **k:SimpleNamespace(data=[SimpleNamespace(b64_json=base64.b64encode(fixture).decode())])
   with patch.object(ToAPIsImage,'_client',return_value=fake),patch.object(ToAPIsImage,'_quote',return_value=__import__('decimal').Decimal('.0019')):
    r=ToAPIsImage().execute({'prompt':'x','output_path':d+'/out.png'})
   self.assertTrue(r.success);self.assertIsNone(r.cost_usd);self.assertEqual(r.data['cost_status'],'unsettled');self.assertEqual(Path(d+'/out.png').read_bytes(),fixture)
 def test_ambiguous_submission_blocks_second_post(self):
  with tempfile.TemporaryDirectory() as d:
   c=ToAPIsClient('fake-test',state_dir=d)
   with patch.object(c,'_json',side_effect=RuntimeError('offline')) as http:
    for _ in range(2):
     with self.assertRaises(RuntimeError):c.generate(model='gpt-image-2-vip',prompt='same',size='1024x1024',quality='low',n=1)
    self.assertEqual(http.call_count,1)
 def test_multi_model_payloads(self):
  from tools.toapis_models import MODEL_ROUTES
  for model,route in MODEL_ROUTES.items():
   body,_=build_request({'model':model,'prompt':'same','size':'1024x1024','n':1,'quality':route['quality']})
   self.assertEqual(body['model'],model);self.assertEqual(body['size'],'1:1')
   if model=='gpt-image-2-vip':self.assertEqual(body['resolution'],'1K')
   else:self.assertEqual(body['metadata']['resolution'],'1K')
   if model=='gpt-image-2.5-flare':self.assertEqual(body['quality'],'high')
 def test_non_vip_edit_rejected_before_network(self):
  with patch.object(ToAPIsImage,'_client') as c:
   self.assertFalse(ToAPIsImage().execute({'prompt':'x','model':'nano_banana','generation_mode':'edit','image_path':'x.png'}).success);c.assert_not_called()
 def test_jpeg_preserved_and_local_png_saved(self):
  from PIL import Image
  with tempfile.TemporaryDirectory() as d:
   buf=io.BytesIO();Image.new('RGB',(2,2),'blue').save(buf,format='JPEG');raw=buf.getvalue()
   fake=SimpleNamespace(last_receipt={'task_id':'fake','request':{},'state':'completed','billing':None},generate=lambda **k:SimpleNamespace(data=[SimpleNamespace(b64_json=base64.b64encode(raw).decode())]))
   with patch.object(ToAPIsImage,'_client',return_value=fake),patch.object(ToAPIsImage,'_quote',return_value=__import__('decimal').Decimal('.0019')):
    r=ToAPIsImage().execute({'prompt':'x','model':'nano_banana','output_path':d+'/out.png'})
   self.assertTrue(r.success);self.assertTrue(r.data['locally_converted']);self.assertEqual(Path(d+'/out-original.jpg').read_bytes(),raw)
   with Image.open(d+'/out.png') as im:self.assertEqual(im.format,'PNG')

if __name__=='__main__':unittest.main()
