# Reuse plan: existing hotel chatbot

The student has approved reusing the hotel chatbot. Source: [expedia_project, rag_integration](https://github.com/milestudor/expedia_project/tree/13c7f8aa55aac576672fcfb121eb4a6803b1d1d7), inspected October 12, 2026. This document records verified existing components and planned adaptations; no application code has been ported at the 3.1 design milestone.

| Existing component | Planned reuse and required adaptation |
| --- | --- |
| `frontend/src/HotelChat.vue` | Adapt Vue input, loading/error states, saved-conversation selection, and transcript display. Remove hotel results, money formatting, hotel-ID cleanup, and travel copy. Keep optional chat separate from the exercise. Add cancellation/stale-response handling; never disable Stop or crisis access while waiting. |
| `backend/app/chat_history.py` | Adapt application-owned SQLite writes, UUID conversation/turn identifiers, transactions, pending/succeeded/failed states, and recovery of interrupted requests. Remove previous-stay context, add session links and deletion, and reduce current-conversation context from 12 to at most four messages. Do not migrate old travel conversations into this app. |
| `backend/app/hotel_chat.py` | Adapt server-only credential access, HTTP error handling, strict structured validation, and prompt hashing. Replace the two-call model-generated SQL workflow with one bounded request selecting approved response keys from retrieved skill/app context. Replace the existing 60-second provider timeout with the proposed eight-second request deadline. Provider request parameters require fresh compatibility checks when selecting the implementation model. |
| `backend/app/migrations.py` and SQLite connection helpers | Reuse the additive migration, foreign-key, and transaction patterns for a new skills database; build new tables rather than copying hotel/rate schemas or seed records. |
| `frontend/src/HotelChat.test.js`, `backend/tests/test_hotel_chat.py`, and `backend/tests/rag_fixture_server.py` | Adapt mocked transport and failure-fixture patterns to approved-key output, timeout, interruption, history, and independent crisis-access checks. Existing test results are not evidence for the new app. |
| `frontend/vite.config.js` and backend config pattern | Reuse localhost API proxy and server-side environment configuration. Record new dependencies/start instructions once a runnable implementation exists. Do not copy private environment files or API keys. |

## What stays conceptually the same

Relevant context informs a bounded model contribution, while application code owns database writes and workflow state. Persisted conversations can be reviewed instead of relying on browser-only messages. Prompt versions and failure outcomes provide useful debugging evidence.

## What changes for this domain

The model gets no SQL-generation role, hotel inventory, travel history, or arbitrary dataset advice. Reviewed skill descriptions and interface guidance replace hotel evidence. The exercise remains independent of chat. The global crisis panel and unconditional Stop controls are new requirements; the hotel chatbot cannot be treated as already satisfying them.

This reuse saves work on conversation plumbing and verification infrastructure without claiming that travel-domain prompts or tests establish suitability for skills practice. During implementation, record exactly which functions/components were copied or adapted, their source commit, changes, and new verification results in AI-USE.md and the evidence log.
