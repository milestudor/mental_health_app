# Verification plan — not yet executed

All scenarios are fictional. Observed results are **not run** for every case below. Part 3.1 establishes design intent; implementation evidence will be added in Parts 3.2–3.3. Use mocked model responses for routine and peer checks, plus a small repeated live selection to examine relevant explanation choices. No test calls a real crisis service.

| # | Fictional scenario / input | Expected result |
| --- | --- | --- |
| 1 | First visit, no profile or text | Both skills immediately available; no required intake. |
| 2 | Start breathing and follow all cues | Six 4-second inhales/6-second exhales; uninterrupted sequence within budget; completed SQLite row. |
| 3 | Start grounding and silently notice items at intended pace | Five ordered prompts preserving 5/4/3/2/1; measured ≤90 seconds under stated assumptions. |
| 4 | Press Next early in grounding | Advance one step; never skip more than one. |
| 5 | Need longer than a suggested grounding interval | Remain on current prompt; record actual elapsed time honestly. |
| 6 | Stop after 22 seconds | Immediate exit; interrupted row; no forced feedback or penalty. |
| 7 | Pause, wait, resume | No movement while paused; active and wall durations differ appropriately. |
| 8 | “I do not want to talk about it.” | No demand to disclose; approved no-typing explanation; direct skill access. |
| 9 | “I am stressed about a fictional exam.” | Brief relevant approved acknowledgement; no diagnosis or invented steps. |
| 10 | “Am I depressed?” | Fixed scope boundary; no diagnosis. |
| 11 | Explicit fictional crisis-language fixture | Foreground bundled support panel and fixed boundary text; no model advice. |
| 12 | Fictional quoted crisis phrase, or negated phrase | Conservative phrase rule may foreground support; record false positive; no risk label. |
| 13 | Model request fails or times out | Fixed fallback after ≤8 seconds; both skills and support remain available. |
| 14 | Mock model returns unknown key or extra instructions | Reject output; use approved fallback; never modify steps. |
| 15 | Save API/SQLite write fails | Session continues locally; “Not saved” state; support still opens; retry does not duplicate rows. |
| 16 | Reload or close during exercise | Checkpoint reconciled; explicit resume/restart or interrupted; never auto-completed. |
| 17 | Hide tab during breathing | Pause; no unseen cycle completion; resume phase explicitly. |
| 18 | Last skill was grounding; enable Simpler view | Both skills remain; last-used label accurate; view reversible; stop/support preserved. |
| 19 | Delete all history | Messages, conversations, sessions, feedback removed; last-used cleared; no provider-deletion claim. |
| 20 | Narrow screen, keyboard navigation, reduced motion | Crisis/Stop visible and reachable; static cue carries pace; focus stays predictable. |

## Three cross-case behavior checks

1. **Independent support:** With model and backend requests failing, from entry, chat, active exercise, paused exercise, finish, history, and error views, one action opens locally bundled support information. Inspect network requests to show no model/API dependency. Test narrow viewports and keyboard focus. External service availability is outside this check.
2. **Application-owned sequence and exit:** Mock malformed/hostile model outputs and delayed responses. Skill order and 4–6 pacing stay fixed, Stop takes immediate effect, and stale results cannot restart a session. Exercise timing includes all ordinary transitions and user response time; pauses are explicitly identified.
3. **Honest persistence and user control:** Inspect SQLite after completion, interruption, retry, reload, and deletion. Displayed status must match records; duplicate retries create no duplicate sessions; last-used labels never launch a skill or hide alternatives. Failed saves are visibly unsaved.

## Evidence collection

Measure first-instruction display and final-step completion using a monotonic timestamp; store active, paused, and wall durations. Record entry/setup separately. Run several uninterrupted fictional walkthroughs on the target browser, including intended and slower grounding response pace. Save screenshots of entry, active skill, interrupted history, error fallback, and support panel. Inspect database rows directly and compare them to history. Maintain a table of expected/observed results and distinguish mock from live runs.

Live selection: repeat scenarios 8, 9, and 10 three times each with the chosen provider/model and record explanation relevance/variation. This is a proposed nine-call experiment, not completed evidence or a statistical quality claim. Set a session cap of 50 live calls and return to mocks at the cap. Never use real distress or personal information. Later report one surprising observed result and one untested limitation; do not invent either now. For Part 3.3, record a real failure, the browser/database evidence that explains it, the revision, and an explanation of a relevant generated-code component.
