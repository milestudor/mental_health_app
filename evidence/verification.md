# Observed verification — November 2, 2026

61 pytest checks passed in the working source and in a genuinely separate local Git clone with a newly installed Python environment. The [XML](mock-tests.xml) records test outcomes; [18 fictional scenario rows](scenarios.md) provide expected and observed API results. Provider failures, timeouts and malformed replies use replaced transports. A successful mocked live-adapter fixture is not a real live-model check. The student-run [live evidence](live-results.json) now records six live outcomes; [the assisted comparison](live-review.md) documents the meaning and variation separately. No automated/mock result is relabeled as live.

Browser: Playwright 1.62.1 and Google Chrome 156.0.8078.74, automated fictional role-play at 1100×900 and 375×812, reduced motion enabled. [Observed browser results](browser-results.json) include persisted SQLite readback through the API and zero page JavaScript errors. Actual foreground breathing ran approximately 60.36 seconds from Start interaction to detected completion; stored active time is 60,000 ms and wall time 60,013 ms. This is one browser observation, not a cross-device timing guarantee. Grounding has no completion-time target.

## Three explicit behavior checks

| Check that must hold across relevant cases | Cases exercised | Observed result and limits |
|---|---|---|
| B1: Display simplification preserves choice and independent support | Full/simpler home views, two skills, desktop and narrow viewport | Both exercise choices remain; mobile has no horizontal overflow. This does not establish screen-reader or human cognitive-load performance |
| B2: Support never causes automatic continuation | Grounding active → support → close; Pause blocks Next; inherited breathing support path retained | Dialog opens and closing leaves Resume available. Manual Resume is required. Browser covers grounding; no claim of exhaustive state coverage |
| B3: API/model failure cannot remove local exits or independent support | Intercepted chat request; intercepted session write; mocked provider error/timeout/malformed output | Chat fallback visible; support opens; failed save explicitly marked; Stop returns home immediately; restore requests and Retry stores one interrupted session. No real provider outage or support-service contact |

Additional checks cover profile/history isolation, explicit-question precedence over saved preferences, current-view overrides without changing defaults, restart and refresh interruption, terminal-state protection, grounding skill readback and identity locking, and transition to mocks at the 50-attempt cap. The cap test sets the counter to 50 and installs a forbidden provider transport; it does not spend 50 real calls.

## Findings and boundaries

Surprising: baseline HTTP 200 concealed wrong skill identity because the request schema ignored the new field while SQLite used its breathing default. Readback, rather than HTTP success, revealed the defect. [Baseline evidence](baseline-failure.json) motivated schema validation, persistence, and identity-change checks.

Not tested: multiple browser tabs concurrently clearing/retrying the same profile; restart-resistant session-wide model-call budgets; actual assistive-technology or peer usability; live semantic adherence and variability beyond the three selected prompts; Windows/Linux setup. Completion, active duration and counts cannot establish clinical effectiveness, improvement or sensory-task engagement. Grounding can be completed with every sense skipped, and individual skips are not persisted.

[Clean setup](clean-setup.json) distinguishes a local clean clone from unverified remote access. Python 3.13.10 and Node 24.20.0 were used. One upstream Starlette/httpx TestClient deprecation warning remains; it does not fail tests. Python packages and npm artifacts were available through local caches, so this does not prove that a completely uncached installation works on every platform. An inherited external Figma capture helper was removed from the final HTML and local production assets rechecked.

## Recorded live-model selection — assisted review November 2, 2026

Configured and returned identifier: `gpt-6.1-sol`. The saved runner output contains six attempts and six `live` outcomes, zero fallback; three independent fictional prompts repeated twice. Original replies are preserved in live-results.json. The file does not include an exact run timestamp, request IDs, token usage, latency or cost.

[Live-review.md](live-review.md) compares expected and observed meaning: both breathing replies preserve six 4/6 cycles/no holds; both grounding replies permit skipping an unavailable sense; both history replies avoid diagnosis or improvement inference. Breathing and grounding vary mainly in phrasing. History varies in which data limitation it explains, without a contradictory conclusion. Every saved reply fits 90 words and 600 characters; response-level counts and the source SHA-256 are in [live-review.json](live-review.json).

Decision: retain the present app facts and controls; no code/prompt/model change is warranted by these pairs. This is six satisfactory case outcomes, not a reliability estimate. It does not test live follow-up conversations, nonzero counts, real-model crisis/injection behavior or general safety. The meaning comparison is Codex-assisted; the student has now confirmed review and acceptance of this original comparison (student-review.md). No additional model calls were made to produce the analysis. The 61 prior mocked checks and browser results remain historical observations of unchanged application source; they were not rerun solely for this documentation review.

## Subsequent general-chat revision

Current regression: **70 passed**, all mocked/replaced provider transports, in [general-chat-tests.xml](general-chat-tests.xml). The original 61-check XML remains unchanged historical evidence. Production build passed. [General-chat-live.json](general-chat-live.json) records two additional real UI calls using `gpt-6.1-sol` and prompt v5: a relevant science explanation and contextual two-sentence follow-up. These are not part of the old six-call selection. [Current screenshot](general-chat-preview.png) shows a live answer and profile context off. New chat reset the visible transcript, and support remained accessible; no support service was contacted. The revised UI has not received a new full cross-device/peer usability evaluation. Broader answer accuracy, long conversations and live adversarial/crisis behavior remain untested.

## Final-source validation

[Final repeated live check](final-live-review.md) covers three current-source prompts twice; the initial batch and targeted controls-reminder revision are both preserved. The final batch has six live outcomes and no fallback. Transport success and semantic review are stated separately. Finalization made 12 attempts total across the two batches, within the host’s 50-attempt allowance. The [final mocked XML](final-regression-tests.xml) records 70 passing checks after the prompt refinement. [Final clean checkout](final-clean-setup.json) identifies the exact validated app-source commit and repeats the mock/build/runtime checks on an isolated clone. Windows/Linux, uncached installation, assistive technology, long/adversarial live exchanges and clinical effectiveness remain outside the evidence.

Student-confirmed comparison review, recording acceptance and professor access are recorded in student-review.md; permission was not independently audited by Codex. The original live-results.json is retained unchanged, including its historical pending-review placeholder.
