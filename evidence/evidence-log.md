# Curated, redacted evidence log

All inputs are fictional. This is selected evidence, not a full chat export. Credentials, personal information and private third-party content are excluded.

| Prompt or observation | Change/check | Evidence | Resulting decision |
|---|---|---|---|
| User: complete Part 3.3; consider another exercise and interface improvements | Inspected supplied Parts 3.1/3.2 and current implementation | Historical design copies; current decisions | Finish integration rather than treating a new feature list as evaluation |
| User confirmed no model configured | Prepared six-attempt opt-in runner; no real calls | live-results.json | Leave live variation explicitly incomplete; never relabel mocked transport as live evidence |
| Baseline accepts new skill field but readback says breathing | Executed request against unmodified 3.2 with temporary fictional SQLite | baseline-failure.json | Validate/store skill identity and reject mid-session identity changes |
| New sensory flow needs user pacing | Implemented Next, Skip, Pause, immediate Stop; no input collection | browser-results.json; mock-tests.xml | Self-paced display replaces an unmeasured duration promise |
| First browser runner failed: `expect is not a function` | Corrected assertion import from playwright/test | Runner source and successful full rerun | Tooling failure is separate from app behavior; first attempt is not counted as a pass |
| Screenshot review showed long scroll before both choices | Desktop two-column cards; mobile stacked; optional check-in after choices | home-desktop.png; home-mobile.png | Reduce initial reading while retaining equal choice; human benefit remains untested |
| Simulated request failure during chat/save | Browser request interception, no paid calls | browser-results.json; screencast | Retain separate support and immediate Stop; label unsaved status and explicit Retry |
| Fresh dependency install initially could not reach package index inside sandbox | Installed into isolated fresh environment with authorized network access | clean-setup.json | Distinguish environment restriction from a broken requirements file |
| Existing cap produced fallback rather than returning to mocks | Replaced transport must not be invoked at attempt 51 | test_live_budget_returns_to_mock_without_provider | Cap selects catalog; host must still enforce session allowance across restarts |

The source of the initial code is the supplied 3.2 folder. Earlier submissions and their runtime data were left unchanged. Dates/timings in older milestones describe those versions, not this one.
