# Curated evidence log — Part 3.1

Only actual inspections and design revisions are recorded here. No browser, clinical, runtime, or live-model tests were performed.

| Evidence | Observation | Decision |
| --- | --- | --- |
| User request: complete 3.1 using assignment and dataset | Part 1 asks for explainable design; working app is not expected | Deliver design artifacts and future verification plan, not a fabricated implementation result. |
| Supplied assignment text and research-table image | R1–R4 and D1–D6 support short exercises, persistent safety, control, low effort, and restrained language | Map each code explicitly; do not interpret mention counts as effectiveness. |
| ZIP inventory and parsed JSON, October 12, 2026 | One file, 80 intents, 232 patterns, 156 responses, one whitespace-empty pattern; “not really” appears twice | Treat as intent fixtures rather than therapist transcripts or reliable classification labels. |
| Response inspection: about/not-talking/suicide categories | Therapy-role claims, pressure to disclose, and an unverified phone number conflict with the assignment | Reject direct retrieval of canned responses; use approved skill/app context and official crisis information. |
| Revised approach: unrestricted supportive chat considered during design | Allowing arbitrary generated explanations would require stronger semantic review and could introduce therapeutic advice | Use model selection of reviewed acknowledgement/explanation keys; render text in application code. This is a design revision, not a failed runtime test. |
| Revised approach: automatic grounding advancement considered | A timer could skip items before a person notices them, undermining control | Keep user-controlled Next; label the timing assumption and test whether intended pace remains ≤90 seconds. |
| Official crisis-resource web check | 988 site identifies call/text/chat and immediate-danger emergency access | Bundle labeled U.S. information; do not reuse the dataset phone number. |

Dataset member SHA-256: `951adaf58cea29def0011a17b8a04de013a35faddc14a2f9a382336c40ec6fb9`.

Sources: user-supplied assignment text; user-supplied R/D image; user-supplied ZIP member `intents.json`; [988 contact page](https://988lifeline.org/contact-us/); [SAMHSA crisis information](https://www.samhsa.gov/find-support/in-crisis). Official resources checked October 12, 2026. The attachment's original publisher/license has not been independently verified; no redistribution of the full dataset is included.

Selected prompt record: “Given the following instructions and dataset, please complete 3.1.” AI assistance inspected the provided materials and drafted these artifacts. No credentials, real patient information, or full third-party conversations are included. The missing research table in the first pasted text was subsequently supplied as an image; the final mapping uses that table.

## Authorized source inspection and reuse revision

After the student approved the design and explicitly requested chatbot reuse and GitHub upload, the existing travel repository was inspected. Main lacked the chatbot; the `rag_integration` branch contained it at commit `13c7f8aa55aac576672fcfb121eb4a6803b1d1d7`. Reviewed files included HotelChat.vue, hotel_chat.py, chat_history.py, migrations.py, and the test-file inventory. The design now plans specific adaptations rather than describing reuse as an unverified possibility. No runtime tests were executed or prior test results imported as new-app evidence. See [reuse plan](../design/reuse-plan.md).
