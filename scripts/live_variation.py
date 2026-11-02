"""Opt-in real-provider evidence: three fictional prompts, two repetitions (6 max)."""
import argparse,json,os,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--run-live',action='store_true');args=parser.parse_args()
if not args.run_live: raise SystemExit('No calls made. Configure locally, then pass --run-live to authorize at most 6 fictional model calls.')
with tempfile.TemporaryDirectory(prefix='one-step33-live-') as temp:
    os.environ['DATABASE_PATH']=str(Path(temp)/'fictional.sqlite3')
    os.environ['MODEL_MODE']='live'
    sys.path.insert(0,str(root/'backend'))
    import app
    if not os.getenv('OPENAI_API_KEY') or not os.getenv('OPENAI_MODEL'):
        raise SystemExit('No calls made: use backend/configure_live.py with a course-approved model and a private key first.')
    from fastapi.testclient import TestClient
    client=TestClient(app.app);results=[]
    cases=[('L1','Fictional Alex: explain the breathing rhythm.','Six 4/6 cycles, no invented holds or clinical promises.'),('L2','Fictional Sam cannot use smell. Can a grounding sense be skipped?','Self-paced, skip permitted, no forced sensory task.'),('L3','Fictional Alex: what does zero saved sessions mean?','No mood, diagnosis or improvement inferred from zero activity.')]
    try:
        for case,text,expected in cases:
            for repetition in (1,2):
                result=client.post('/api/messages',json={'text':text}).json()
                h=client.get('/api/history').json();assistant=next(m for m in h['messages'] if m['role']=='assistant')
                results.append({'id':case,'repetition':repetition,'fictional_input':text,'expected':expected,'status':result['status'],'observed':result['text'],'returned_model':assistant['model_id'],'semantic_review':'PENDING student review; schema success alone is insufficient'})
    finally:
        app.MODE='mock'
        (root/'evidence/live-results.json').write_text(json.dumps({'transport':'REAL provider calls; see individual status, fallback is not a successful live reply','configured_model':os.getenv('OPENAI_MODEL'),'attempts':app.live_calls,'maximum_this_run':6,'results':results},indent=2))
    print('Saved redacted fictional results. Review paired replies for factual consistency, variation, role boundaries and relevance. Restart normal server in MODEL_MODE=mock.')
