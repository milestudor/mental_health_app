# Implementation plan

## Responsibilities and structure

Proposed directories: `frontend/` for Vue, `backend/` for FastAPI, `backend/context/` for reviewed skill/app context, `tests/fixtures/` for fictional inputs and mocked responses, and `docs/` for maintained design and evidence. Bind both services to localhost. No public deployment, accounts, speech, diagnosis features, or clinical outcome tracking is planned.

Vue owns the global prototype notice and crisis panel, one-instruction exercise view, monotonic pacing, keyboard controls, and immediate pause/stop. FastAPI owns validation, approved context retrieval, model access, and database transactions. SQLite holds local history. Model credentials remain server-side in an ignored environment file; examples contain placeholders only.

Proposed API: `POST /sessions`, `PATCH /sessions/{id}`, `GET /sessions`, `GET /sessions/{id}`, `DELETE /sessions/{id}`, `DELETE /history`, `GET/PATCH /preferences`, and `POST /conversations/{id}/messages`. API success is not required for a local exercise to continue or for crisis information to open. If saving fails, display “Not saved” and allow an explicit retry using an idempotency key. Do not silently call an unsaved record persistent. The later implementation will define and test these interfaces; they do not exist yet.

## Useful, limited model contribution

Optional chat example (fictional): “I am stressed about a made-up exam and do not want to type much.” The model can acknowledge the preference and explain that both skills can be completed without typing. It cannot decide the user's distress level, diagnose, or add advice. The same two skill buttons remain available below the response.

Retrieve small, versioned snippets from a reviewed catalog using explicit skill identifiers and app-intent keywords. For general choice questions, include both approved skill descriptions and the no-typing explanation. For a breathing question, retrieve only that skill's fixed description and controls. For out-of-scope treatment questions, use a fixed boundary response. Do not retrieve arbitrary dataset responses or external documents. An embedding database is unnecessary for this small catalog; relevant-context retrieval is still explicit and logged.

Model context includes system boundaries, retrieved snippets, explicit display preference, and at most the latest four messages from the current conversation. Older conversations are excluded by default. User content is delimited as untrusted text: instructions inside it cannot alter the system contract. Retrieval source IDs and prompt version are stored with a response so context use can be reviewed.

Proposed system instructions:

> You explain a localhost coursework skills prototype using only the approved context supplied. Testing is fictional. Do not claim to be a therapist, diagnose, prescribe, promise improvement, or imply monitoring. Do not invent or modify skill steps. Acknowledge optional user text briefly and explain the available choices without requiring disclosure. Never start or stop an exercise, infer distress, or claim a record was saved. Return only the allowed structured response.

The structured response has only `acknowledgement_key` and `explanation_key`, drawn from small approved phrase catalogs; maximum combined displayed text is 45 words. The model selects a relevant pairing from context instead of writing arbitrary therapeutic text. Example keys: `prefers_no_typing` and `both_skills_silent`. This constrains expressiveness but makes the output reviewable and deterministic after rendering. Additional fields, unknown keys, malformed output, or unsafe/out-of-scope requests trigger fixed fallback copy. The server, not the model, inserts buttons and renders the corresponding catalog text.

This design still requires meaningful live-model checks: can it select relevant approved explanations across paraphrases, and does variation confuse the user? A structured schema alone does not establish semantic relevance. Mock results establish application behavior, not live-model quality. Provider and model identifier are undecided; choose a course-approved model and record its exact returned identifier before Part 3.2. Use mock mode by default and permit no more than 50 live calls per peer session.

## Proposed SQLite schema

| Table | Main fields | Purpose |
| --- | --- | --- |
| preferences | singleton ID, simpler_view, motion_mode, last_skill, updated_at | Remember explicit display choices and recent skill; no inferred diagnosis. |
| conversations | ID, created_at, updated_at | Group optional chat messages. |
| messages | ID, conversation_id FK, role, text, created_at, response_status, model_id, prompt_version, context_ids | Persistent transcript; distinguish generated/catalog-rendered responses from fallback. |
| sessions | ID, conversation_id nullable FK, skill_id, skill_version, status, started_at, ended_at, active_ms, paused_ms, wall_ms, checkpoint, idempotency_key | Exercise history; completion, interruption, and resume state. |
| feedback | session_id FK, format_useful nullable, created_at | Optional yes/no format feedback; no clinical score. |

Use foreign keys, constrained role/status/skill values, parameterized queries, and transactions. Session states: ready → active ↔ paused → completed or interrupted. Stop takes effect locally immediately, then saves interrupted state. Opening support pauses the active session; the request is never sent to the model. Each transition checkpoints so an unexpected close can later be reconciled as interrupted rather than completed. A best-effort unload event is insufficient on its own.

Persist messages before model invocation, then persist the response or error outcome. Do not store credentials, complete provider payloads, participant data, or inferred diagnoses. Optional fictional transcripts are saved locally and clearly disclosed. History deletion cascades to session feedback; clearing all history removes messages/conversations/sessions and clears last_skill. Resetting preferences is separate and explicit. Local deletion does not promise deletion of provider-side request records. No full transcript is sent for personalization.

## Failure and exit behavior

| Event | Expected behavior |
| --- | --- |
| Model timeout, unavailable provider, malformed output | Cancel or expire after 8 seconds; fixed brief fallback; skill choices and crisis control remain available. |
| Late response after navigation or Stop | Ignore stale request ID; never restart or change exercise state. |
| SQLite/API failure | Exercise and support still work locally; indicate unsaved history and offer retry. |
| Browser tab hidden or pacing callback gap | Pause without skipping; resume only through user action. |
| User stops or changes skill | Mark old session interrupted; require a fresh Start for the new skill. |
| Reload | Reconcile checkpoint; show explicit resume/restart choice, or mark interrupted if state cannot be trusted. |
| Crisis-related text | Fixed application response and foregrounded bundled information; no generated crisis advice or forced routing. |

The first version must complete at least one skill end to end with model contribution and SQLite persistence. Breathing is the implementation priority; grounding may follow once persistence and failure behavior work. This prioritization does not change the two-skill design proposal. The existing hotel chatbot was inspected on the travel repository’s `rag_integration` branch. [The reuse plan](reuse-plan.md) identifies its chat UI, model wrapper, persistent conversation handling, migration patterns, and mocked tests, with required adaptations. This milestone applies those choices to the design; code porting remains implementation work.
