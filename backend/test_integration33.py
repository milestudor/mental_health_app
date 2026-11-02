"""Fictional Part 3.3 checks. No provider network is used."""
import pytest
from test_app import app

@pytest.mark.parametrize('sid,skill,status', [('S16','grounding-v1','completed'),('S17','grounding-v1','interrupted'),('S18','breathing-v1','completed')])
def test_skill_identity(app,record_property,sid,skill,status):
    mod,c=app
    body=dict(id=sid,skill_id=skill,status=status,active_ms=2000,paused_ms=500,wall_ms=2500,checkpoint='Fictional exercise checkpoint')
    assert c.put('/api/sessions/'+sid,json=body).status_code==200
    actual=c.get('/api/history').json()['sessions'][0]
    assert (actual['skill_id'],actual['status'])==(skill,status)
    record_property('scenario','Save fictional '+skill+' '+status)
    record_property('expected',skill+' / '+status+' survives readback')
    record_property('observed',actual['skill_id']+' / '+actual['status'])
    record_property('transport','mocked; no live provider calls')

def test_skill_identity_cannot_change_mid_session(app):
    mod,c=app
    body=dict(id='fixed',skill_id='grounding-v1',status='active',active_ms=0,paused_ms=0,wall_ms=0,checkpoint='see')
    assert c.put('/api/sessions/fixed',json=body).status_code==200
    assert c.put('/api/sessions/fixed',json={**body,'skill_id':'breathing-v1'}).status_code==409
    assert c.put('/api/sessions/unknown',json={**body,'id':'unknown','skill_id':'invented'}).status_code==422

def test_grounding_context_and_history_are_honest(app):
    mod,c=app
    reply=c.post('/api/messages',json={'text':'Explain sensory grounding'}).json()
    assert reply['status']=='mocked' and 'self-paced' in reply['text']
    assert 'Do not seek out or taste' in reply['text']
    with mod.db() as db:
        assert 'grounding-v1' in db.execute("SELECT context_ids FROM messages WHERE role='assistant'").fetchone()[0]
    body=dict(id='g',skill_id='grounding-v1',status='completed',active_ms=2000,paused_ms=0,wall_ms=2000,checkpoint='finished')
    c.put('/api/sessions/g',json=body)
    reply=c.post('/api/messages',json={'text':'What does my history show?'}).json()
    assert 'exercise history' in reply['text'] and '1 completed' in reply['text']

def test_live_budget_returns_to_mock_without_provider(app,monkeypatch):
    mod,c=app;mod.MODE='live';mod.live_calls=50
    def forbidden(*a,**k): raise AssertionError('Provider must not be invoked after cap')
    monkeypatch.setattr(mod.httpx,'AsyncClient',forbidden)
    reply=c.post('/api/messages',json={'text':'Explain grounding'}).json()
    assert reply['status']=='mocked' and 'self-paced' in reply['text']
    assert mod.live_calls==50
    assert c.get('/api/chat-status').json()['mode']=='mock'
