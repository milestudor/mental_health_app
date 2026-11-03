# General conversation — requested scope change

The student asked for chat to answer general questions with relevant generated responses. The earlier preview used mocked presets, and its live prompt separately redirected non-app topics to app features. Those two mechanisms explained the observed limitation.

## Implemented behavior

- Live mode answers general questions and follows the current conversation. Reviewed facts constrain claims about this app; they no longer restrict unrelated topics to the app catalog. No web tools are connected, and the prompt/UI disclose uncertainty for current information.
- The one-field structured reply remains validated but permits 350 words/4000 characters rather than 90/600. Requests cap completion tokens at 4096. GPT-5/6 models use low reasoning effort; no sampling-temperature parameter is added. Provider timeout is 25 seconds within a 30-second overall request limit, with a 35-second browser timeout.
- Up to 12 recent non-pending/non-failed messages from the same profile-owned conversation support follow-ups. Older conversations remain excluded. New chat cancels/reset state and starts a fresh conversation; it does not delete saved history.
- The browser defaults to no saved profile/activity sharing. An explicit checkbox controls including those fields. Opted-out response snapshots record only that sharing was off. Earlier messages may still contain details shared before opt-out; the UI explains using New chat for a clean conversational context. Existing API callers default to sharing for compatibility; the browser always sends an explicit choice.
- Local clinical-request matching now targets personal diagnosis or medication/treatment recommendation wording, avoiding generic terms that blocked computer diagnosis or water treatment. It is not a comprehensive semantic classifier. Existing crisis phrase routing, separate support, role boundaries and independent exercise controls remain. Broader generated replies still depend on model adherence and can be wrong.
- After 50 provider attempts, replies use the mock catalog and the UI refreshes its mode status. Mock mode remains the default for routine/peer checks and does not pretend to answer arbitrary questions.

## Evidence

[General-chat regression XML](../evidence/general-chat-tests.xml): **70 passing checks**, all provider transports mocked/replaced. Nine new cases exercise general topics, longer output acceptance/bounds, personal diagnosis routing, bounded multi-turn context, and omission of saved profile fields and snapshots when opted out. Existing isolation, persistence, fallback and cap checks remain passing. One existing Starlette/httpx deprecation warning remains.

[Real UI evidence](../evidence/general-chat-live.json): **two additional real calls**, `gpt-6.1-sol`, prompt `chat-v5-general`. The first answers a fictional question about why the sky is blue with light scattering, rather than an app redirect. The second follows “that” and produces the requested two-sentence explanation for a ten-year-old. Both are labeled live, and persisted context snapshots show profile sharing off. [Screenshot](../evidence/general-chat-preview.png) shows the live reply and disclosure. New chat cleared the visible conversation; independent support still opened/closed without contacting a service.

The original six-call evaluation is preserved unchanged and describes the prior prompt. This follow-up checks only one topic and its follow-up, not arbitrary-question accuracy, crisis/adversarial model behavior, medical safety or clinical effectiveness. Prompt instructions are not guarantees. The earlier full breathing browser recording is historical and was not rerun for a chat-only change; the routine script was updated to require mock mode before deleting test history and to explicitly opt in before asking about counts.

## Decision and alternatives

Retain default mocks for repeatable evaluation and enable the configured live adapter for the user’s requested local preview. Considered expanding preset topics; rejected because it would not provide open-ended conversation. Increasing the short reply allowance and context window helps ordinary explanations/follow-ups, with higher latency/cost possible. No web browsing, tools, deployment or claim of universal correctness was added. No key, provider authorization header or unrelated user transcript is included in evidence. The student has authorized final publication. The later [final-source comparison](../evidence/final-live-review.md) records a targeted Pause/Stop prompt reminder, an observed first-pass omission and a revised repeated selection.
