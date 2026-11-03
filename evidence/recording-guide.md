# Demonstration and process screencast

[Play the captioned recording](demonstration-and-process.webm). About 1 minute 46 seconds, silent with on-screen captions. Recorded by automated fictional role-play, not a human peer test. A full 60-second breathing interval is included. The final source additionally removes an unused external Figma capture helper; it does not change the recorded interactions.

| Time | Evidence/section |
|---|---|
| 0:00 | 1 · FINISHED APPLICATION — Fictional Alex. Mocked replies. No clinical or effectiveness claim. |
| 0:03 | Self-paced grounding is an alternative to a breathing timer. No typed answers; any sense can be skipped. |
| 0:07 | Support opens independently. Closing it leaves the exercise paused. Resume is an explicit choice. |
| 0:09 | History preserves the skill identity. Completed means the sequence ended, including skipped senses; it is not an outcome score. |
| 0:12 | Breathing retains its original 6 × (4 + 6) sequence. This segment runs in real time. |
| 1:12 | Mocked personalization uses actual profile-scoped counts, not old transcripts or an inferred emotional state. |
| 1:15 | Actual baseline API evidence: HTTP 200 concealed a wrong skill label. Earlier code defaulted every session to breathing. |
| 1:24 | Code walkthrough — validation, identity guard and parameterized persistence. These checks establish software behavior only. |
| 1:33 | 4 · FAILURE DEMONSTRATION — Intercepted chat request fails. No live provider is contacted. |
| 1:35 | B3 · Independent support remains available after failed chat. This recording never calls or messages a support service. |
| 1:37 | Saving failure is visible; Stop returned home immediately. Restoring requests and Retry saves one interrupted session. |
| 1:40 | Limits: automated fictional evaluation only. Live-model variation and human peer usability testing remain pending. |

The failure evidence page shows the real baseline API result, not an app screen. The next page explains the actual generated validation/persistence code. The final section shows intercepted chat and save failures in the working app. No support service is contacted. The baseline fixture and browser checks are separate observations, clearly labeled.

The student has watched and approved this recording, stated no additional narration is needed, and confirmed professor access; see [student-review.md](student-review.md). No peer-participant test or narrated student rehearsal is claimed.

Update after the recording: the student subsequently ran six live-model checks; see [original results](live-results.json) and [assisted comparison](live-review.md). The final on-screen caption saying live variation is pending refers to the recorded checkpoint and is not the current written evidence status. No recording has been altered or rerecorded as part of this documentation review.

The later general-chat revision is also outside this recording’s scope. See [current design/evidence](../design/general-chat.md), [two real UI calls](general-chat-live.json) and [screenshot](general-chat-preview.png). The historical recording still documents exercise flow and the selected failure/process evidence; it is not a recording of the current general chatbot.
