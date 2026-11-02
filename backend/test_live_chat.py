"""Live-adapter tests use replaced transport, never a real model."""
import httpx
import pytest
from test_app import app

@pytest.mark.parametrize('reply,valid', [('Hi. What would you like to know about the breathing exercise?',True),('',False),('x'*601,False)])
def test_live_reply_validation_and_context(app,monkeypatch,reply,valid):
 mod,c=app;mod.MODE='live'
 monkeypatch.setenv('OPENAI_API_KEY','fixture-only')
 monkeypatch.setenv('OPENAI_MODEL','fixture-model')
 requests=[]
 class Transport:
  def __init__(self,**kwargs):pass
  async def __aenter__(self):return self
  async def __aexit__(self,*args):pass
  async def post(self,url,**kwargs):
   import json
   requests.append(kwargs['json'])
   return httpx.Response(200,request=httpx.Request('POST',url),json={'model':'fixture-model','choices':[{'message':{'content':json.dumps({'reply':reply})}}]})
 monkeypatch.setattr(mod.httpx,'AsyncClient',Transport)
 first=c.post('/api/messages',json={'text':'Hello'}).json()
 assert first['status']==('live' if valid else 'fallback')
 if valid:
  assert first['text']==reply
  c.post('/api/messages',json={'text':'Tell me more','conversation_id':first['conversation_id']})
  assert any(m['role']=='assistant' and m['content']==reply for m in requests[-1]['messages'])
 assert requests[0]['store'] is False
 assert requests[0]['response_format']['json_schema']['strict'] is True
 assert 'fixture-only' not in str(requests[0])

def test_status_does_not_expose_credentials(app,monkeypatch):
 mod,c=app;mod.MODE='live'
 monkeypatch.delenv('OPENAI_API_KEY',raising=False)
 monkeypatch.delenv('OPENAI_MODEL',raising=False)
 assert c.get('/api/chat-status').json()=={'mode':'live','configured':False,'available':False}
 r=c.post('/api/messages',json={'text':'Hello'}).json()
 assert r['status']=='fallback'
