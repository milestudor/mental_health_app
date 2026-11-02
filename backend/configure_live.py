"""Run locally in Terminal. The API key is hidden and never printed."""
import getpass, json, os
from pathlib import Path

def main():
    print('One Step live-chat setup. Use a course-approved model supporting Structured Outputs.')
    print('Fictional chat and the displayed profile context will be sent to OpenAI when you send a message.')
    model=input('OPENAI_MODEL: ').strip()
    key=getpass.getpass('OPENAI_API_KEY (hidden): ').strip()
    if not model or not key:
        raise SystemExit('Both values are required. No configuration saved.')
    target=Path(__file__).with_name('.env.local')
    fd=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
    os.fchmod(fd,0o600)
    with os.fdopen(fd,'w') as f:
        for name,value in {'MODEL_MODE':'live','OPENAI_MODEL':model,'OPENAI_API_KEY':key}.items():
            f.write(name+'='+json.dumps(value)+'\n')
    print('Local configuration saved. Restart the app to connect. No API call has been made.')
if __name__=='__main__':main()
