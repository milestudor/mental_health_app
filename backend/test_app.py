import importlib, os
from fastapi.testclient import TestClient
import pytest
@pytest.fixture
def app(tmp_path, monkeypatch):
    monkeypatch.setenv('DATABASE_PATH',str(tmp_path/'test.sqlite'))
    import app as module
    importlib.reload(module)
    module.MODE='mock'
    return module, TestClient(module.app)
def test_transcript_and_context_persist(app):
    mod,c=app
    r=c.post('/api/messages',json={'text':'I prefer no typing for a fictional exam scenario'}).json()
    assert r['status']=='mocked' and 'do not need to type' in r['text']
    h=c.get('/api/history').json()
    assert len(h['messages'])==2
    assert 'no-typing-v1' in h['messages'][0]['context_ids']
    with mod.db() as db: assert db.execute('select count(*) from messages').fetchone()[0]==2
def test_failure_and_crisis_boundary(app):
    mod,c=app;mod.MODE='failure'
    assert c.post('/api/messages',json={'text':'Explain breathing'}).json()['status']=='fallback'
    r=c.post('/api/messages',json={'text':'Fictional quote: kill myself'}).json()
    assert r['crisis'] and r['status']=='boundary'
    assert len(c.get('/api/history').json()['messages'])==4
def test_idempotent_checkpoint_delete_and_validation(app):
    mod,c=app
    b={'id':'fictional','status':'active','active_ms':2000,'paused_ms':0,'wall_ms':2000,'checkpoint':'intro'}
    assert c.put('/api/sessions/fictional',json=b).status_code==200
    b.update(status='interrupted',active_ms=4000,wall_ms=4000)
    c.put('/api/sessions/fictional',json=b)
    h=c.get('/api/history').json();assert len(h['sessions'])==1 and h['sessions'][0]['status']=='interrupted'
    assert c.put('/api/sessions/fictional',json={**b,'active_ms':-1}).status_code==422
    c.post('/api/messages',json={'text':'fictional message'})
    c.delete('/api/history');h=c.get('/api/history').json()
    assert all(not x for x in h.values())
def test_restart_marks_unresolved_session_interrupted(app):
    mod,c=app
    c.put('/api/sessions/x',json={'id':'x','status':'active','active_ms':100,'paused_ms':0,'wall_ms':100,'checkpoint':'intro'})
    importlib.reload(mod)
    assert c.get('/api/history').json()['sessions'][0]['status']=='interrupted'
def test_introduction_demo_is_labeled_stateless_and_validated(app):
    mod,c=app
    result=c.get('/api/demo-introduction?mode=mock').json()
    assert result['status']=='mocked' and result['persisted'] is False
    assert c.get('/api/demo-introduction?mode=failed').status_code==503
    assert c.get('/api/demo-introduction?mode=unknown').status_code==422
    assert not c.get('/api/history').json()['messages']

def test_profile_edit_checkin_and_personalized_reply(app):
    mod,c=app
    profile={'name':'Alex','goal':'A fictional classroom presentation','display_mode':'simple','motion':False,'no_typing':True}
    assert c.put('/api/profiles/alex',json=profile).status_code==200
    assert c.get('/api/profiles/alex').json()['profile']['motion']==0
    assert c.post('/api/checkins',json={'profile_id':'alex','state':'more_going_on','note':'Fictional check-in'}).status_code==200
    response=c.post('/api/messages',json={'profile_id':'alex','text':'How do my preferences work?'}).json()
    assert 'current view is simpler' in response['text']
    assert response['personalization']['latest_checkin']['state']=='more_going_on'
    assert response['personalization']['profile']['goal']==profile['goal']
    with mod.db() as db: assert db.execute('select count(*) from response_context').fetchone()[0]==1

def test_profiles_isolate_history_and_conversation(app):
    mod,c=app
    body={'id':'a','profile_id':'alex','status':'completed','active_ms':64000,'paused_ms':0,'wall_ms':64000,'checkpoint':'done'}
    c.put('/api/sessions/a',json=body)
    r=c.post('/api/messages',json={'profile_id':'alex','text':'What does my history show?'}).json()
    assert '1 completed' in r['text']
    assert c.get('/api/history?profile_id=sam').json()['messages']==[]
    assert c.post('/api/messages',json={'profile_id':'sam','conversation_id':r['conversation_id'],'text':'Fictional message'}).status_code==404
    assert c.put('/api/sessions/a',json={**body,'profile_id':'sam'}).status_code==404
    c.delete('/api/history?profile_id=sam')
    assert len(c.get('/api/history?profile_id=alex').json()['sessions'])==1
    c.delete('/api/history?profile_id=alex')
    assert c.get('/api/history?profile_id=alex').json()['messages']==[]
    assert c.get('/api/profiles/alex').status_code==200

def test_current_view_override_reaches_chat_without_changing_default(app):
    mod,c=app
    r=c.post('/api/messages',json={'profile_id':'alex','display_mode':'simple','text':'How do my saved preferences work?'}).json()
    assert 'current view is simpler' in r['text']
    assert r['personalization']['current_view']=='simple'
    assert c.get('/api/profiles/alex').json()['profile']['display_mode']=='full'

def test_older_history_migrates_without_assigning_it_to_a_new_persona(tmp_path,monkeypatch):
    import sqlite3,importlib
    path=tmp_path/'old.sqlite3'
    c=sqlite3.connect(path)
    c.execute("CREATE TABLE sessions(id TEXT PRIMARY KEY,status TEXT,active_ms INTEGER,paused_ms INTEGER,wall_ms INTEGER,checkpoint TEXT,created_at TEXT,skill_id TEXT DEFAULT 'breathing-v1')")
    c.execute("INSERT INTO sessions VALUES('old','completed',64000,0,64000,'done','2026-10-22T12:00:00+00:00','breathing-v1')")
    c.commit();c.close()
    monkeypatch.setenv('DATABASE_PATH',str(path))
    import app as module
    importlib.reload(module)
    client=TestClient(module.app)
    assert len(client.get('/api/history?profile_id=legacy').json()['sessions'])==1
    assert client.get('/api/history?profile_id=alex').json()['sessions']==[]
    assert client.get('/api/profiles/legacy').json()['profile']['name']=='Earlier demo'

def test_finished_session_cannot_be_downgraded_by_a_stale_checkpoint(app):
    mod,c=app
    body={'id':'terminal','profile_id':'alex','status':'completed','active_ms':64000,'paused_ms':0,'wall_ms':64000,'checkpoint':'done'}
    assert c.put('/api/sessions/terminal',json=body).status_code==200
    assert c.put('/api/sessions/terminal',json={**body,'status':'interrupted'}).status_code==409
    assert c.get('/api/history?profile_id=alex').json()['sessions'][0]['status']=='completed'
