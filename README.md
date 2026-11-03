# One Step — Part 3.3

Local coursework skills prototype, evaluated with fictional scenarios only. It does not diagnose, provide therapy, assess safety, or monitor anyone. Do not deploy, offer, link or recommend it as something to rely on during a difficult moment. Testers must role-play fictional cases; nobody in real distress may be a test participant.

Breathing provides six 4/6 cycles (60 active seconds). Sensory grounding offers five self-paced prompts with Next, Skip, Pause and immediate Stop. Neither requires typing or speaking. Profiles, optional check-ins, exercise records and optional fictional chat are stored locally. Completion is an activity record, not improvement; grounding completion can include skipped senses. A labeled support panel remains independent of the API and model.

## Clean setup

Install Python 3.13 and Node 22+ with npm. After cloning the submitted repository and selecting the submission tag, work in the directory containing this README and `backend/` and `frontend/`. Network access is needed to install packages. No API key is needed.

```sh
git clone https://github.com/milestudor/mental_health_app.git
cd mental_health_app
git checkout assignment-3.3-final
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cd frontend
npm ci
npm run build
cd ..
MODEL_MODE=mock .venv/bin/uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000. Stop with Ctrl+C. Rebuild after frontend edits; restart after backend edits. If port 8000 is occupied, stop the old server or choose another port and open that port. Use the final `assignment-3.3-final` tag for this milestone. The earlier `assignment-3.3-submission` tag remains preserved as a checkpoint and does not contain the later live evidence or general chatbot.

On Windows use `.venv\Scripts\python -m pip`, `.venv\Scripts\python -m uvicorn`, and set `MODEL_MODE` with the shell's environment syntax. Windows setup has not been tested. Optional frontend development uses `npm run dev` inside frontend with the backend at port 8000.

The database is created automatically at `backend/history.sqlite3`. Use `DATABASE_PATH` to isolate a fictional test session. No database, secret configuration, dependencies, or build output is committed. Clear this profile’s history removes its sessions, chat, check-ins and response-context snapshots, retaining preferences. Live provider-side records are outside local deletion. Reload records a recoverable session as interrupted and requires a new Start.

## Verification

```sh
MODEL_MODE=mock .venv/bin/pytest backend -q --junitxml=evidence/mock-tests.xml
```

Current regression results: 70 automated checks ([general-chat XML](evidence/general-chat-tests.xml)); the earlier milestone recorded 61. There are 18 explicitly recorded fictional API scenarios, and three cross-case browser checks. These are mocked tests, including provider transports replaced with fixtures. The [general-chat live check](evidence/general-chat-live.json) separately records two actual model calls. See [scenarios](evidence/scenarios.md), [browser results](evidence/browser-results.json), [verification](evidence/verification.md), and [clean checkout](evidence/clean-setup.json). Python currently emits one upstream Starlette/httpx deprecation warning; tests pass.

To repeat the browser checks, install the optional tooling in a temporary folder and use an isolated server. This script deletes Alex’s fictional history on the dedicated test server at port 8033. Never point it at records you wish to keep.

```sh
npm install --prefix /tmp/one-step-browser-tools playwright@1.62.1
MODEL_MODE=mock DATABASE_PATH=/tmp/one-step-browser.sqlite3 .venv/bin/uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8033
# In a second terminal, from this repository:
NODE_PATH=/tmp/one-step-browser-tools/node_modules node scripts/browser-check.cjs
```

Google Chrome must be installed (`channel: chrome`). The submitted run used Playwright 1.62.1; see verification for browser versions. The script records an actual foreground 60-second breathing interval, screenshots and a silent captioned screencast. Allow about two minutes. It neither contacts a support service nor calls a real model.

## Live evaluation and repeatable optional runner

The student has now run six fictional live checks using `gpt-6.1-sol`; all six stored outcomes are `live`. See [original responses](evidence/live-results.json) and [assisted pairwise review](evidence/live-review.md). No further live calls are needed solely to repeat this review. The professor does not require a particular model; choose one compatible with the existing Structured Outputs adapter. For a future deliberate rerun, configure it locally without sharing keys:

```sh
.venv/bin/python backend/configure_live.py
.venv/bin/python scripts/live_variation.py --run-live
```

Rerunning overwrites `evidence/live-results.json`, so preserve prior evidence first. The evaluation script uses a temporary fictional database and attempts at most six calls (three prompts twice). It saves returned model identifiers and fictional replies to `evidence/live-results.json`; review paired replies for factual consistency, relevance, role boundaries and variation. A fallback is not a successful live response. No flag means no call. Routine checks and peer testing default to mock mode.

For an optional live peer session the host must use one server process, one worker, and a session limit of **at most 50 model attempts**. Keep that process running for the whole session; restarting resets its process counter and must not reset the host’s session allowance. At the cap the adapter returns to labeled mocked catalog replies. The host should explicitly restart with `MODEL_MODE=mock` when ending the live selection. The live runner is a separate host session with its own lower limit of six. The configuration file is local and ignored.

## Review and submission

[Part 3.3 report](report.md) · [design decisions](design/decisions.md) · [current architecture](design/technical-plan.md) · [AI disclosure](AI-USE.md) · [curated evidence](evidence/evidence-log.md) · [captioned demonstration/process recording](evidence/demonstration-and-process.webm) · [recording guide](evidence/recording-guide.md).

The student has reviewed and accepted the original live comparison and recording and confirmed professor access. The [final-source repeated selection](evidence/final-live-review.md) supplements that original comparison and documents a prompt refinement. Canvas upload remains the student’s final action. Human peer usability observations remain uncollected, and are not claimed as a mandatory session. The automated captioned recording predates the live run; its final live-pending caption describes the earlier checkpoint. Review it and be prepared to explain the code. No human testing or clinical effectiveness is claimed.

## General conversational chat — current revision

Live chat now answers general questions about learning, writing, planning and everyday topics instead of redirecting them to app features. It uses the configured `gpt-6.1-sol` model, not the mock catalog. To run the local preview in this mode after private configuration:

```sh
MODEL_MODE=live .venv/bin/uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8033
```

Mock mode remains the default for routine/peer evaluation. General questions require live mode; the mock catalog is still a small app-specific fixture set, clearly labeled in the UI. No answer is guaranteed correct. There is no browsing/current-information verification, therapy, diagnosis or monitoring. Testing remains fictional only.

The browser starts with profile/activity sharing off. The optional checkbox includes those saved fields only when selected. Up to 12 recent messages from this conversation are sent for follow-ups. Switching the checkbox off does not erase earlier conversational messages; New chat starts a fresh conversation without deleting saved transcripts. Replies allow up to 350 words/4000 characters. No model output can start an exercise or change storage/preferences. The 50-attempt server cap still returns replies to mock mode, with the connection status refreshed after each reply.

[Current change and evidence](design/general-chat.md) documents 70 mocked regression checks plus two separate real-model UI requests. The original six-case live review remains evidence for the earlier app-only prompt, not proof of the new broad scope. The historical demo recording predates this change; the [current screenshot](evidence/general-chat-preview.png) and new live evidence supplement it. The final tag includes this chat revision and its evidence. The earlier recording documents the core exercise and failure/process demonstration; current-chat screenshots and live records supplement it.

## Final submission evidence

[Requirement audit](evidence/requirements-audit.md) maps every supplied Part 3.3 requirement to evidence. [Final live comparison](evidence/final-live-review.md) includes three current-source prompts repeated twice, an initial omission, and the revised repeat. [Final clean-checkout results](evidence/final-clean-setup.json) record 70 mocked checks and production-build/runtime checks for the final app source; historical 61-check evidence remains labeled. [Student confirmation](evidence/student-review.md) records review and access status. Upload the final standalone `report.md` after publication; no Canvas submission is performed by this repository workflow.
