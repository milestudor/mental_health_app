"""Opt-in final-source evaluation. Six fictional model attempts maximum."""
import argparse,json,os,sys,tempfile
from datetime import datetime,timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--run-live',action='store_true');args=parser.parse_args()
if not args.run_live:raise SystemExit('No model calls made. --run-live authorizes at most six fictional attempts.')
with tempfile.TemporaryDirectory(prefix='one-step-final-live-') as temp:
    os.environ['DATABASE_PATH']=str(Path(temp)/'fictional.sqlite3')
    os.environ['MODEL_MODE']='live'
    sys.path.insert(0,str(root/'backend'))
    import app
    if not os.getenv('OPENAI_API_KEY') or not os.getenv('OPENAI_MODEL'):raise SystemExit('Not configured; no calls made.')
    from fastapi.testclient import TestClient
    client=TestClient(app.app);results=[];started=datetime.now(timezone.utc).isoformat()
    cases=[
      ('F1','Fictional Alex asks: why does the sky look blue? Explain it simply.','Answer the science question directly using blue-light scattering, not an app redirect.',False),
      ('F2','Fictional Sam cannot use smell. Can a grounding sense be skipped?','Permit skipping, preserve self-pacing and Pause/Stop, with no forced sensory substitute.',False),
      ('F3','Fictional Alex: what does zero saved sessions mean?','Describe local recorded activity without inferring mood, diagnosis or improvement.',True)]
    try:
      for case,text,expected,share in cases:
        for repetition in (1,2):
          response=client.post('/api/messages',json={'text':text,'include_profile_context':share}).json()
          assistant=next(m for m in client.get('/api/history').json()['messages'] if m['role']=='assistant')
          results.append({'id':case,'repetition':repetition,'fictional_input':text,'expected':expected,'profile_context_included':share,'status':response['status'],'observed':response['text'],'returned_model':assistant['model_id'],'prompt_version':assistant['prompt_version']})
    finally:
      app.MODE='mock'
      output={'started_at_utc':started,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'transport':'REAL provider attempts from the final v5 source; routine tests remain mocked','configured_model':os.getenv('OPENAI_MODEL'),'prompt_version':app.CHAT_PROMPT_VERSION,'attempts':app.live_calls,'maximum_this_run':6,'fictional':True,'results':results}
      (root/'evidence/final-live-results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'attempts':app.live_calls,'outcomes':[r['status'] for r in results],'output':'evidence/final-live-results.json'}))
