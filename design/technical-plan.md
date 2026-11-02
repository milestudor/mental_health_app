# Current integration architecture

Vue owns exercise state, phase/count timing, grounding Next/Skip, Pause/Resume/Stop, independent support, reduced motion and stale-request guards. FastAPI owns validation, context assembly, model adapters and transactional SQLite writes. FastAPI serves the production Vue build and JSON endpoints on localhost.

`Session.skill_id` accepts only `breathing-v1` or `grounding-v1`; missing values retain the breathing default for old callers. Each browser session gets an idempotent UUID. SQLite `BEGIN IMMEDIATE`, profile ownership checks and terminal-status guards protect persisted identity and completion from stale state changes. The frontend serializes ordinary checkpoints. A localStorage checkpoint supports recording an interruption after refresh. This is not synchronization across tabs.

Breathing uses a monotonic animation-frame clock: six four-second inhales and six six-second exhales. Hidden tabs or callback gaps over 1.5 seconds pause rather than skip unseen time. Grounding accumulates active time but has no duration limit and only explicit Next/Skip advances it. Opening support pauses either exercise. Skip and Next have identical advancement semantics; no answers or individual skipped-sense flags are recorded. Completion does not prove any prompt was followed.

Profiles persist explicit names/goals/display/motion/no-typing settings. The latest check-in category and aggregate status counts can be included in context. Current-view override is separate from saved default. History and response snapshots are profile-scoped; older transcripts are excluded from model personalization, while at most four current-conversation messages support follow-ups. All data must be fictional.

Default mock mode maps explicit intents to reviewed text. The optional live adapter uses the inherited Chat Completions Structured Outputs request and validates a one-field reply, 90 words/600 characters maximum. Schema validation does not establish semantic safety. Only reviewed feature facts are supplied; mocked-mode assertions are omitted from live app facts. Provider failure, timeout or invalid output produces a fixed fallback. Pending and terminal outcomes are persisted. Vue renders text without HTML interpretation.

A per-process counter increments before each provider attempt. The 51st would-be attempt selects mocked catalog text instead. One worker/process and host session accounting are required; restart-resistant budgets and multi-instance coordination are outside scope. Browser chat status reports mock mode after the cap when refreshed; individual message outcomes are always labeled.

Tests: pytest API/SQLite fixtures and replaced provider transports for deterministic checks; Playwright for actual browser controls, foreground timing, narrow layout and request interception. Network failures in browser evidence are intercepted requests, not a claim of an actual provider outage. No clinical or participant study is performed.
