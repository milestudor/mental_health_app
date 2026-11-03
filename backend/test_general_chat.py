"""General-chat contract tests: replaced provider transport, no real calls."""
import json
import httpx
import pytest
from test_app import app

def provider(mod,monkeypatch,reply):
    mod.MODE='live'
    monkeypatch.setenv('OPENAI_API_KEY','fictional-fixture-key')
    monkeypatch.setenv('OPENAI_MODEL','gpt-6.1-sol')
    requests=[]
    class Transport:
        def __init__(self,**kwargs):pass
        async def __aenter__(self):return self
        async def __aexit__(self,*args):pass
        async def post(self,url,**kwargs):
            requests.append(kwargs['json'])
            return httpx.Response(200,request=httpx.Request('POST',url),json={'model':'fixture-general-model','choices':[{'message':{'content':json.dumps({'reply':reply})}}]})
    monkeypatch.setattr(mod.httpx,'AsyncClient',Transport)
    return requests

@pytest.mark.parametrize('question',[
 'Fictional Alex asks: why is the sky blue?',
 'Fictional Sam asks how water treatment works.',
 'How can fictional Alex diagnose why a laptop is slow?',
])
def test_general_topics_are_sent_to_provider_not_app_catalog(app,monkeypatch,question):
    mod,c=app;requests=provider(mod,monkeypatch,'A direct answer to your question.')
    result=c.post('/api/messages',json={'text':question,'include_profile_context':False}).json()
    assert result['status']=='live' and result['text']=='A direct answer to your question.'
    assert requests[0]['messages'][-1]['content']==question
    assert requests[0]['store'] is False
    assert requests[0]['reasoning_effort']=='low'
    assert requests[0]['max_completion_tokens']==4096


def test_profile_optout_excludes_saved_preferences_counts_and_snapshot(app,monkeypatch):
    mod,c=app;requests=provider(mod,monkeypatch,'Here is an explanation.')
    profile=c.get('/api/profiles/alex').json()['profile'];profile['goal']='PRIVATE_FICTIONAL_CONTEXT_MARKER'
    c.put('/api/profiles/alex',json=profile)
    result=c.post('/api/messages',json={'text':'Explain a rainbow.','include_profile_context':False}).json()
    assert result['personalization']=={'profile_context_included':False}
    assert 'PRIVATE_FICTIONAL_CONTEXT_MARKER' not in json.dumps(requests)
    facts=requests[0]['messages'][0]['content']
    assert 'Not shared. Do not infer or invent preferences or activity counts.' in facts
    with mod.db() as db:
        assert json.loads(db.execute('SELECT snapshot FROM response_context').fetchone()[0])=={'profile_context_included':False}
        assert 'explicit-profile-v1' not in db.execute("SELECT context_ids FROM messages WHERE role='assistant'").fetchone()[0]


def test_followup_context_extends_beyond_four_messages_but_stays_bounded(app,monkeypatch):
    mod,c=app;requests=provider(mod,monkeypatch,'A fictional follow-up answer.')
    cid=None
    for index in range(8):
        result=c.post('/api/messages',json={'text':f'Fictional turn {index}','conversation_id':cid,'include_profile_context':False}).json()
        cid=result['conversation_id']
    history=requests[-1]['messages'][1:]
    assert len(history)==12 and history[-1]['content']=='Fictional turn 7'
    assert any(m['content']=='Fictional turn 2' for m in history)
    assert not any(m['content']=='Fictional turn 0' for m in history)
    assert sum(m['role']=='system' for m in requests[-1]['messages'])==1

@pytest.mark.parametrize('reply,expected',[(('Useful explanation. '*60).strip(),'live'),('word '*351,'fallback'),('x'*4001,'fallback')])
def test_longer_explanations_and_output_bounds(app,monkeypatch,reply,expected):
    mod,c=app;provider(mod,monkeypatch,reply)
    result=c.post('/api/messages',json={'text':'Explain a fictional topic.'}).json()
    assert result['status']==expected
    if expected=='live':assert result['text']==reply


def test_personal_diagnosis_still_bypasses_provider(app,monkeypatch):
    mod,c=app;requests=provider(mod,monkeypatch,'This must not be used.')
    result=c.post('/api/messages',json={'text':'Fictional role-play: diagnose me and recommend medication.'}).json()
    assert result['status']=='boundary' and requests==[]
