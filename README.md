# One Step — Part 3.3

Local coursework skills prototype, evaluated with fictional scenarios only. It does not diagnose, provide therapy, assess safety, or monitor anyone. Do not deploy, offer, link or recommend it as something to rely on during a difficult moment. Testers must role-play fictional cases; nobody in real distress may be a test participant.

Breathing provides six 4/6 cycles (60 active seconds). Sensory grounding offers five self-paced prompts with Next, Skip, Pause and immediate Stop. Neither requires typing or speaking. Profiles, optional check-ins, exercise records and optional fictional chat are stored locally. Completion is an activity record, not improvement; grounding completion can include skipped senses. A labeled support panel remains independent of the API and model.

## Clean setup

Install Python 3.13 and Node 22+ with npm. After cloning the submitted repository and selecting the submission tag, work in the directory containing this README and `backend/` and `frontend/`. Network access is needed to install packages. No API key is needed.

```sh
git clone https://github.com/milestudor/mental_health_app.git
cd mental_health_app
git checkout assignment-3.3-submission
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cd frontend
npm ci
npm run build
cd ..
MODEL_MODE=mock .venv/bin/uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000. Stop with Ctrl+C. Rebuild after frontend edits; restart after backend edits. If port 8000 is occupied, stop the old server or choose another port and open that port. This repository/tag has been prepared locally; publication to the confirmed remote is still required before the clone command can retrieve this version.

On Windows use `.venv\Scripts\python -m pip`, `.venv\Scripts\python -m uvicorn`, and set `MODEL_MODE` with the shell's environment syntax. Windows setup has not been tested. Optional frontend development uses `npm run dev` inside frontend with the backend at port 8000.

The database is created automatically at `backend/history.sqlite3`. Use `DATABASE_PATH` to isolate a fictional test session. No database, secret configuration, dependencies, or build output is committed. Clear this profile’s history removes its sessions, chat, check-ins and response-context snapshots, retaining preferences. Live provider-side records are outside local deletion. Reload records a recoverable session as interrupted and requires a new Start.

## Verification

```sh
MODEL_MODE=mock .venv/bin/pytest backend -q --junitxml=evidence/mock-tests.xml
```

Current results: 61 automated checks, 18 explicitly recorded fictional API scenarios, and three cross-case browser checks. These are mocked tests, including provider transports replaced with fixtures. See [scenarios](evidence/scenarios.md), [browser results](evidence/browser-results.json), [verification](evidence/verification.md), and [clean checkout](evidence/clean-setup.json). Python currently emits one upstream Starlette/httpx deprecation warning; tests pass.

To repeat the browser checks, install the optional tooling in a temporary folder and use an isolated server. This script deletes Alex’s fictional history on the dedicated test server at port 8033. Never point it at records you wish to keep.

```sh
npm install --prefix /tmp/one-step-browser-tools playwright@1.56.1
MODEL_MODE=mock DATABASE_PATH=/tmp/one-step-browser.sqlite3 .venv/bin/uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8033
# In a second terminal, from this repository:
NODE_PATH=/tmp/one-step-browser-tools/node_modules node scripts/browser-check.cjs
```

Google Chrome must be installed (`channel: chrome`). The submitted run used the bundled Playwright version recorded in verification. The optional installation command above is a portable recipe, not a claim that this precise optional version was used. The script records an actual foreground 60-second breathing interval, screenshots and a silent captioned screencast. Allow about two minutes. It neither contacts a support service nor calls a real model.

## Optional live evaluation — not yet performed

The user confirmed no model is configured. Choose a course-approved OpenAI model supporting the existing Structured Outputs adapter, then configure it locally without sharing keys:

```sh
.venv/bin/python backend/configure_live.py
.venv/bin/python scripts/live_variation.py --run-live
```

The evaluation script uses a temporary fictional database and attempts at most six calls (three prompts twice). It saves returned model identifiers and fictional replies to `evidence/live-results.json`; review paired replies for factual consistency, relevance, role boundaries and variation. A fallback is not a successful live response. No flag means no call. Routine checks and peer testing default to mock mode.

For an optional live peer session the host must use one server process, one worker, and a session limit of **at most 50 model attempts**. Keep that process running for the whole session; restarting resets its process counter and must not reset the host’s session allowance. At the cap the adapter returns to labeled mocked catalog replies. The host should explicitly restart with `MODEL_MODE=mock` when ending the live selection. The live runner is a separate host session with its own lower limit of six. The configuration file is local and ignored.

## Review and submission

[Part 3.3 report](report.md) · [design decisions](design/decisions.md) · [current architecture](design/technical-plan.md) · [AI disclosure](AI-USE.md) · [curated evidence](evidence/evidence-log.md) · [captioned demonstration/process recording](evidence/demonstration-and-process.webm) · [recording guide](evidence/recording-guide.md).

Live-model variation, human peer usability observations, and remote publication remain unresolved. The recording is automated and captioned; the student should review it, verify access for the instructor, and be prepared to explain the code in their own words. No human testing or clinical effectiveness is claimed.
