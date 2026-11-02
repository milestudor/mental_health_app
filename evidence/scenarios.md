# Fictional scenarios — observed mocked results

These 18 parameterized API scenarios use fresh fictional SQLite data per test. Provider errors and malformed replies use replaced transports. They do not measure interface usability, real timing, or live-model quality. Browser results cover actual controls and timing separately.

| Scenario | Expected | Observed | Result |
|---|---|---|---|
| no_typing | You do not need to type | You do not need to type during an exercise. Breathing and sensory grounding require no spoken or typed responses. Grounding is self-paced; you can skip any sense. | PASS |
| breathing | six cycles | Breathing uses six cycles of four counts in and six counts out. Pause or stop whenever you choose. | PASS |
| controls | Stop ends immediately | Pause freezes your place. Resume continues. Stop ends immediately. Crisis support opens independently of chat. | PASS |
| simple_profile | current view is simpler | For Alex, your current view is simpler. Breathing needs no typed answers. Pause, Stop, and crisis support stay visible. You can change your preferences or choose full view. | PASS |
| completed_history | 1 completed | For Alex, saved exercise history shows 1 completed and 0 stopped sessions. These are activity records, not a measure of improvement. You can review or clear them in Your days. | PASS |
| treatment | cannot diagnose | This coursework prototype cannot diagnose or advise on treatment. It can explain its breathing exercise. | PASS |
| crisis | cannot assess safety | This prototype cannot assess safety or provide crisis care. Crisis-support information is available here. | PASS |
| negated_crisis | cannot assess safety | This prototype cannot assess safety or provide crisis care. Crisis-support information is available here. | PASS |
| injection | mocked | mocked | PASS |
| provider_failure | fallback | fallback | PASS |
| malformed_provider | fallback | fallback | PASS |
| provider_timeout | fallback | fallback | PASS |
| stopped_history | 1 stopped | For Alex, saved exercise history shows 0 completed and 1 stopped sessions. These are activity records, not a measure of improvement. You can review or clear them in Your days. | PASS |
| other_profile | 0 completed | For Sam, saved exercise history shows 0 completed and 0 stopped sessions. These are activity records, not a measure of improvement. You can review or clear them in Your days. | PASS |
| clear_history | profile retained | history empty; profile retained | PASS |
| Save fictional grounding-v1 completed | grounding-v1 / completed survives readback | grounding-v1 / completed | PASS |
| Save fictional grounding-v1 interrupted | grounding-v1 / interrupted survives readback | grounding-v1 / interrupted | PASS |
| Save fictional breathing-v1 completed | breathing-v1 / completed survives readback | breathing-v1 / completed | PASS |
