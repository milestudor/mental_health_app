# Curated, redacted evidence log

All inputs are fictional. This is selected evidence, not a full chat export. Credentials, personal information and private third-party content are excluded.

| Prompt or observation | Change/check | Evidence | Resulting decision |
|---|---|---|---|
| User: complete Part 3.3; consider another exercise and interface improvements | Inspected supplied Parts 3.1/3.2 and current implementation | Historical design copies; current decisions | Finish integration rather than treating a new feature list as evaluation |
| Earlier checkpoint: user had no model configured | Prepared six-attempt opt-in runner; no calls at that stage | scripts/live_variation.py; prior Git checkpoint | Keep unfinished live evidence explicit; later student-run evidence is documented below |
| Baseline accepts new skill field but readback says breathing | Executed request against unmodified 3.2 with temporary fictional SQLite | baseline-failure.json | Validate/store skill identity and reject mid-session identity changes |
| New sensory flow needs user pacing | Implemented Next, Skip, Pause, immediate Stop; no input collection | browser-results.json; mock-tests.xml | Self-paced display replaces an unmeasured duration promise |
| First browser runner failed: `expect is not a function` | Corrected assertion import from playwright/test | Runner source and successful full rerun | Tooling failure is separate from app behavior; first attempt is not counted as a pass |
| Screenshot review showed long scroll before both choices | Desktop two-column cards; mobile stacked; optional check-in after choices | home-desktop.png; home-mobile.png | Reduce initial reading while retaining equal choice; human benefit remains untested |
| Simulated request failure during chat/save | Browser request interception, no paid calls | browser-results.json; screencast | Retain separate support and immediate Stop; label unsaved status and explicit Retry |
| Fresh dependency install initially could not reach package index inside sandbox | Installed into isolated fresh environment with authorized network access | clean-setup.json | Distinguish environment restriction from a broken requirements file |
| Existing cap produced fallback rather than returning to mocks | Replaced transport must not be invoked at attempt 51 | test_live_budget_returns_to_mock_without_provider | Cap selects catalog; host must still enforce session allowance across restarts |

The source of the initial code is the supplied 3.2 folder. Earlier submissions and their runtime data were left unchanged. Dates/timings in older milestones describe those versions, not this one.

Clean-checkout review also found an inherited Figma capture script loading from a third-party domain in production HTML. It was removed: the final interface needs no capture helper, and ordinary exercise/support rendering should use local assets. The served-asset smoke check was corrected to select the local production module. The final clone was rebuilt and rechecked.

## Follow-up: student-run live evidence and requested review

- **User request:** “now that I’ve done 1 and 2,” complete the response comparison and documentation and show the work before confirmation.
- **Recorded evidence:** six attempts, all `live`, configured/returned model `gpt-6.1-sol`. The original response file is unchanged. No exact execution timestamp or provider request metadata was saved; November 2, 2026 is the assisted review date.
- **Comparison:** L1 preserves the same breathing procedure; L2 preserves self-pacing and explicit skip choice; L3 varies its explanation of the limits of saved records without inferring wellbeing. Full expected/observed reasoning and response-length checks are in live-review.md/live-review.json.
- **Decision:** retain current facts and controls; consider but decline forcing identical catalog wording or expanding paid testing for this small selection. Six outcomes do not establish general reliability. No new live call, app-code change or human sign-off is claimed.
- **Documentation changes:** add live comparison; update report, verification, AI disclosure, README and current design notes; correct stale publication status and “course-approved model” wording. The professor does not require a particular model. The existing recording’s closing live-pending caption is marked historical in its guide.
- **Publication boundary:** checkpoint `dfe0eec` and `assignment-3.3-submission` were already pushed. This follow-up remains uncommitted/unpushed for review; the existing checkpoint tag is unchanged.

## Subsequent request: open-ended live chatbot

- User requested general questions and relevant generated responses. Inspection found both a mock preview and an app-only live prompt.
- Revised live scope, bounded replies (350 words/4000 characters), 12-message context, profile sharing off by default in the browser, New chat and accurate no-browsing disclosures. Narrowed overbroad clinical matching so educational water-treatment and computer-diagnosis questions reach the model.
- Mocked regression: 70 checks passed; provider transports replaced. No paid calls are included in that number. Build passed.
- Two real requests through the browser UI produced relevant sky-color explanations and the requested two-sentence follow-up; recorded model gpt-6.1-sol, prompt v5, profile context off. Selected fictional messages only are saved to general-chat-live.json, alongside a screenshot. The previous six-call evidence remains unchanged.
- New chat and independent support were checked without another model call or contacting a support service. Existing breathing timing was not modified. Broad arbitrary-topic reliability and long-conversation behavior are untested. These findings justify enabling the local live preview, not a clinical or universal-quality claim.
- The earlier app-only six-call report and demo recording are historical evidence; current docs distinguish their scope from this revision. No commit/push or student sign-off is claimed.

## Authorized finalization

The student confirmed review and understanding of the original live comparison, approved the recording without narration, confirmed professor access and requested final commit/push plus a remaining-requirements audit. See student-review.md.

The current-source live comparison used three fictional cases twice. Initial grounding replies omitted the expected Pause/Stop reminder despite transport success; first-pass results were preserved. One targeted prompt sentence was added and the same selection repeated. The revised answers explicitly retain Pause/Stop, while one leaves self-pacing implicit in voluntary progression/noncompletion. This is recorded without claiming universal semantic safety. Finalization used 12 model attempts, below the session cap. The original six-call file is unchanged. Final mocked regression remains 70 checks, with final clean-checkout evidence and requirement mapping added. Publishing is authorized; Canvas submission remains for the student.
