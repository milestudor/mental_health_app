# Observed verification — November 2, 2026

61 pytest checks passed in the working source and in a genuinely separate local Git clone with a newly installed Python environment. The [XML](mock-tests.xml) records test outcomes; [18 fictional scenario rows](scenarios.md) provide expected and observed API results. Provider failures, timeouts and malformed replies use replaced transports. A successful mocked live-adapter fixture is not a real live-model check. [Live evidence](live-results.json) is explicitly NOT RUN.

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

Not tested: multiple browser tabs concurrently clearing/retrying the same profile; restart-resistant session-wide model-call budgets; actual assistive-technology or peer usability; live semantic adherence and variability; Windows/Linux setup. Completion, active duration and counts cannot establish clinical effectiveness, improvement or sensory-task engagement. Grounding can be completed with every sense skipped, and individual skips are not persisted.

[Clean setup](clean-setup.json) distinguishes a local clean clone from unverified remote access. Python 3.13.10 and Node 24.20.0 were used. One upstream Starlette/httpx TestClient deprecation warning remains; it does not fail tests. Python packages and npm artifacts were available through local caches, so this does not prove that a completely uncached installation works on every platform. An inherited external Figma capture helper was removed from the final HTML and local production assets rechecked.
