"""Intent relevance regressions with fictional messages and no provider calls."""
import pytest
from test_app import app

@pytest.mark.parametrize('question,expected',[
 ('Hello!','Hello.'),
 ('I am nervous about a fictional presentation','Thanks for telling me'),
 ('How do I start?','first inhale begins immediately'),
 ('How long does breathing take?','60 seconds'),
 ('How many seconds is it?','60 seconds'),
 ('How do I turn off the animation?','Gentle motion off'),
 ('Where is my data saved?','SQLite'),
 ('Delete my history?','Clear this profile'),
 ('What does my history show?','0 completed'),
 ('What is a check-in?','not a clinical assessment'),
 ('Can you hear me through a microphone?','no spoken or typed'),
 ('I feel dizzy during breathing','stop now'),
 ('Are you a therapist?','not a therapist'),
 ('What is the capital of France?','Could you rephrase'),
 ('Thanks','welcome'),
])
def test_relevant_catalog_reply(app,question,expected):
 mod,c=app
 result=c.post('/api/messages',json={'text':question}).json()
 assert result['status']=='mocked'
 assert expected.lower() in result['text'].lower()
 with mod.db() as db:
  context=db.execute("select context_ids from messages where role='assistant'").fetchone()[0]
  assert 'catalog-' in context

def test_followup_uses_current_conversation_only(app):
 mod,c=app
 r=c.post('/api/messages',json={'text':'How long is it?'}).json()
 follow=c.post('/api/messages',json={'text':'Tell me more','conversation_id':r['conversation_id']}).json()
 assert '60 seconds' in follow['text']
 separate=c.post('/api/messages',json={'text':'Tell me more'}).json()
 assert 'Could you rephrase' in separate['text']

@pytest.mark.parametrize('opening',[
 'How long is it?', 'Explain breathing', 'Can I pause?',
 'How do I start?', 'What is a check-in?', 'What does my history show?',
 'Where is my data saved?', 'I feel nervous', 'How do I change motion?'
])
def test_followups_add_detail_then_ask_focused_question(app,opening):
 mod,c=app
 first=c.post('/api/messages',json={'text':opening}).json()
 second=c.post('/api/messages',json={'text':'Tell me more','conversation_id':first['conversation_id']}).json()
 third=c.post('/api/messages',json={'text':'What do you mean?','conversation_id':first['conversation_id']}).json()
 assert len({first['text'],second['text'],third['text']})==3
 assert '?' in third['text']
 assert all(x['status']=='mocked' for x in [first,second,third])

def test_followup_topic_switch_and_boundary(app):
 mod,c=app
 first=c.post('/api/messages',json={'text':'How long is it?'}).json()
 changed=c.post('/api/messages',json={'text':'Where is my data saved?','conversation_id':first['conversation_id']}).json()
 assert 'SQLite' in changed['text'] and '60 seconds' not in changed['text']
 boundary=c.post('/api/messages',json={'text':'Can you diagnose me?','conversation_id':first['conversation_id']}).json()
 assert boundary['status']=='boundary'
