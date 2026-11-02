# Assignment 3.1 — Design proposal: One Step

**Milestone:** Part 1, design and planning. **Date:** October 12, 2026.

**Repository URL:** [URLTO COMPLETE: insert your course repository ].  
**Submitted commit:** [assignment-3.1-submission](https://github.com/milestudor/mental_health_app/tree/assignment-3.1-submission) — Git tag identifying the submitted commit.

## Proposal and scope

One Step is a localhost coursework prototype for practicing a short, fixed skills sequence using fictional scenarios. It is not therapy, a diagnostic tool, or a monitored service. The planned stack is Vue, FastAPI, and SQLite. The first implementation will support paced breathing (4–6) and 5-4-3-2-1 sensory grounding. These two skills offer a useful choice without requiring a distress narrative, and both can be presented without typing. STOP and cognitive reframe are deferred: reframe demands more disclosure and reasoning, while adding all four skills would reduce the time available to verify the complete experience.

The main experience is: choose a skill, start it, follow one instruction at a time, and optionally record lightweight feedback. A conversational model can briefly acknowledge an optional fictional message and explain the two available choices using approved context. The user can skip the conversation entirely. Application code controls every exercise step, timer, exit, saved state, and crisis-support route.

## Design materials

- [Design rationale, screens, flow, research mapping, and timing](design/experience.md)
- [Architecture, model contract, retrieval, persistence, and failure behavior](design/technical-plan.md)
- [Verified hotel-chatbot source and reuse plan](design/reuse-plan.md)
- [Dataset inspection and curated evidence log](evidence/evidence-log.md)
- [Planned checks and fictional scenarios](evidence/verification-plan.md)
- [Project navigation and milestone status](README.md)
- [Coding-agent instructions](AGENTS.md)
- [AI-use disclosure](AI-USE.md)

These relative links are intended to resolve within the submitted repository. Before upload, replace the repository and commit fields above and ensure the linked files are accessible to the instructor at that commit. No recordings were produced for this design milestone; the finished-app demonstration and failure-process screencast belong to Part 3.3.

## Research-grounded decisions

The supplied study involved 15 patients, 13 clinicians, and 15 prototype evaluation sessions, with 150 coded participant–task combinations. Its mention counts describe feedback and behavior, not clinical effectiveness. The attached R/D table is the source for the mappings below.

R1 motivates an approximately 64-second breathing sequence and an approximately 80-second grounding sequence, with entry time reported separately. R2 and D4 require a labeled crisis-support control on every screen, including errors and exercises. R3 requires immediately available pause and stop controls without persuasion or penalties. R4 requires offering both skills rather than letting the model route the person automatically.

D1 motivates an explicitly chosen “Simpler view,” rather than guessing distress from text. D2 motivates one current exercise instruction per screen. D3 motivates no mandatory narrative, sensory-item entry, or post-exercise rating. D5 motivates remembering the most recently chosen skill and display preference with no setup questionnaire. D6 motivates neutral language, restrained color, and a static pacing option. The design document explains the gains, costs, and rejected alternatives for each decision.

## Dataset use and model boundaries

The supplied ZIP contains one `intents.json` file: 80 intent entries, 232 patterns, and 156 canned responses. It is an intent/response collection, not a set of therapist dialogue transcripts or the study's coded research dataset. It contains an empty pattern, a duplicated pattern, therapy-role claims, pressure to disclose, and an unverified crisis phone number. The design uses selected patterns only as fictional test fixtures. It will not fine-tune on the dataset or retrieve its responses as advice. The supplied assignment's skill descriptions and reviewed application guidance will be the model's context.

The model's proposed role is deliberately small but useful: acknowledge optional text without diagnosis and explain a choice in plain language. Users retain the same buttons when the model fails. Model-generated advice cannot become an exercise instruction. Backend validation and approved fallback text are required in addition to a system prompt.

## Personalization and saved history

SQLite will persist conversations, messages, sessions, optional feedback, and a small set of preferences. History will show the chosen skill, date, active duration, completion or interruption, and optional feedback; a conversation detail view will show saved messages. The latest chosen skill can receive a “Last used” label, but neither skill is hidden or automatically started. This reduces repeated decisions while avoiding a claim that the app knows which skill works clinically. Simpler view can be reversed at any time, and users can delete saved history and reset preferences.

The interface will disclose that optional chat text is sent to the selected model provider, while exercise progress and preferences stay local unless deliberately included in a model request. Only fictional text is allowed in testing. SQLite is not assumed encrypted, and localhost is not a guarantee of confidentiality.

## What is complete and what remains

Complete for this draft: experience design, research mapping, flow and screen sketches, timing budgets, dataset inspection, model and storage plan, crisis/failure decisions, AI disclosure, and a repeatable verification plan. No working application, live-model evaluation, browser test, or measured runtime is claimed. Timing figures are design budgets, not observed performance.

The student approved this design and reuse of the existing hotel chatbot. Its `rag_integration` branch was inspected; the reuse plan identifies concrete components and required adaptations. Source inspection and reuse planning are complete; application code has not yet been ported. The repository URL and submission tag identify this design version. Before Part 3.2, implementation must establish actual timing, persistence, crisis availability during failures, and model contribution. Open questions include browser timer behavior, grounding pace, model/provider choice and response variability, and whether the reduced interface is usable by keyboard and screen reader.
