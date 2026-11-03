# Final-source live comparison — November 2, 2026 (America/New_York)

The final general-chat prompt was checked in two capped batches of six fictional requests using configured/returned model `gpt-6.1-sol`, prompt family `chat-v5-general`. Each batch has three independent inputs repeated twice; no prior conversation is shared across repetitions. Raw execution timestamps are UTC (November 3 UTC, still November 2 Eastern). This is separate from mocked regression results. No additional calls are required for this assessment.

## First batch: observed omission and revision

[First-pass responses](final-live-results-first-pass.json) all have transport status `live`. However, both F2 grounding answers omit the expected Pause/Stop reminder. They correctly permit skipping and preserve self-pacing. The assisted semantic assessment is **partial against the stated expectation**, not an unconditional pass. This is a response omission, not a missing application control.

Decision: add one targeted system-prompt instruction: “When answering about exercise steps or skipping a sense, briefly state that Pause and Stop remain available; never require completion.” General questions still receive direct answers; no exercise step, timer or control changes. Preserve first-pass evidence and repeat the same selection rather than treating valid JSON as sufficient.

## Revised batch: expected and observed

| Case | Expected | Observed in repetitions 1 and 2 | Variation and decision |
|---|---|---|---|
| F1: fictional sky-color question, saved context off | Answer the science question directly using blue-light scattering, without app redirection | Both explain that air scatters blue light from sunlight more strongly than most other colors | Replies are identical in this pair. Repetition need not produce different wording. Retain direct general-topic scope; this is one familiar topic, not broad accuracy evidence |
| F2: fictional Sam cannot use smell, saved context off | Permit voluntary skipping, preserve self-pacing and Pause/Stop, no forced substitute | Both name Skip this sense and explicitly retain Pause and Stop. First says move on to taste and that completing every sense is not required; second explicitly says self-paced and continue to the next sense | Both preserve voluntary progression/control. Only the second restates the word self-paced; the first gives no deadline and explicitly permits noncompletion. Keep the targeted reminder; do not infer universal prompt adherence |
| F3: fictional zero saved sessions, saved context on | Describe recorded activity without inferring mood, diagnosis or improvement | Both describe no locally recorded exercise sessions, distinguish activity outside the app, and say this is not a score or assessment | Minor quotation/punctuation/pronoun differences; no conflicting interpretation. Retain neutral history wording |

[Revised raw results](final-live-results.json) record six live replies and zero fallback. All fit 350 words/4000 characters. These are Codex-assisted semantic judgments, not automated proof of safety or clinical effectiveness. No more specific dated model snapshot was returned. The source SHA-256 reviewed after the run is `c2a4fc1a7ec44b62c992641659e5f991c3c13c18223ddc72b5a4ce0cebd06059`.

The student previously confirmed review and understanding of the original [six-response comparison](live-review.md), approved the captioned recording without added narration, and confirmed professor access. This finalization batch and its prompt revision were generated afterward and are explicitly AI-assisted; no separate student review of these new replies is invented.

## Scope and remaining limitations

Two batches used 12 attempts total during finalization, below the host limit of 50. Earlier included evidence separately records six student-run app-only attempts and two real UI requests (20 recorded attempts across the included evidence; not an inventory of any other manual use). Provider token usage/cost is not recorded.

Three prompts twice cannot estimate general reliability. Long follow-ups, adversarial/crisis wording with the real model, other languages, actual screen-reader use, multiple-tab races and clinical effectiveness remain untested. One incomplete reminder in the first batch demonstrates why this limitation matters. App-owned controls and independent support do not depend on generated text.
