# Fresh-session recovery qualification — 2026-11-20

**Method:** answer the ten recovery questions from the isolated documentation candidate plus GitHub evidence available on 2026-11-20. Do not use chat memory. Mark any fact that exists only as unobserved local runtime UNKNOWN.

**Review checkout:** `C:\Users\eejon\AppData\Local\DORY_ContinuityCheckpoint_0a4a825` remains on local base `0a4a825f259a0c245a71aac6a96ab98df739a315` and is not the publication parent.  
**Clean publication candidate:** `C:\Users\eejon\AppData\Local\DORY_ContinuityPublication_f46de55`, proposed branch `docs/dory-donum-engineering-continuity-2026-11-20`, parent GitHub `main` `f46de55a6cb074879c29ce0c2dfc3d4873f97b91`. Uncommitted. Not pushed.

## Answers from the proposed documents

| # | Question | Answer available from the candidate | Evidence class inside the answer |
|---|----------|-------------------------------------|----------------------------------|
| 1 | What is DORY? | An independent control platform that hands one bounded task to a worker and takes the turn back. Atlas is not DORY | Stable architecture |
| 2 | Why was it created? | To stop product work, campaign intent, notes, and health from being treated as execution permission | Stable architecture |
| 3 | How does the architecture work? | Founder, Atlas, publisher, mailbox, runner, Cursor, result, audit, COMPLETE or BLOCKED. Paths are named | Stable architecture |
| 4 | Which capabilities are implemented and proven? | Registry separates deployed-inactive, qualified-isolated, historical, and proposed | Registry |
| 5 | Last verified operational status? | Sequence 632 COMPLETE, turn DORY, STOP asserted, runner count 0, campaign publication false, dated 2026-11-20 | Dated observation. A later session must re-verify. After that timestamp, liveness is UNKNOWN until rechecked |
| 6 | Donum's latest verified engineering state? | Branch `stage-2/ux-workflow-001`, HEAD `4dcf67d8cf2bd3fd498622a1e29173c8c027a968`, 12 tracked and 61 untracked protected paths | Dated observation |
| 7 | Unresolved defects? | Deferred product reconcile on the live runner, published-RUNNING resume, HEAD-only marker, inactive candidate, telemetry dirt, stale architecture prose | Registry and checkpoints |
| 8 | Protected work? | Two control telemetry files, 12 Donum tracked files with matching hashes, 61 Donum untracked paths, isolated candidate, section 11 append | Dated observation |
| 9 | Safety restrictions? | STOP asserted, AUTO-READY no, publication false, LIVE and broker actions prohibited, candidate not activated, no new sequence | Decision register and checkpoints |
| 10 | Next proposed task for each project? | DORY: review this candidate, do not activate. Donum: choose between protected manual-trading WIP and the disarmed chart-cancel candidate. Family: no change | Proposed, not authorized |

## GitHub-only session, without this unpublished candidate

| Source | What it can answer | What remains missing |
|--------|--------------------|----------------------|
| Atlas GitHub `main` `f46de55a6cb074879c29ce0c2dfc3d4873f97b91` | Handshake through the efficiency-loop method commit. `docs/CURRENT-CHECKPOINT.md` and `reports/engineering-continuity/LATEST.md` return 404 on `main` | This continuity candidate, and local handshake consolidation `0a4a825` |
| Atlas GitHub `atlas/planning` `f792d76ba66e6e69469021de9f798f65d8da0b83` | 2026-11-15 archive, a living checkpoint, and `docs/decisions/FOUNDER-DECISION-REGISTER.md`. That checkpoint reports sequence 630 as not re-read | The 2026-11-20 DORY and Donum observations. Local planning tip `93c9db9` is not on GitHub |
| Atlas branch `docs/historical-dory-capability-2026-11` `feb9b53090a4a77d9b376b653b0eee89e7c20e68` | Handshake section with COMPLETE counts for 2026-10-26, 10-29, 10-30, and 10-31, plus sequence 630 context | Not merged. Parent `0a4a825` is not on `main`. Does not contain this continuity index |
| DORY GitHub `main` `824cf59` | Control architecture, mailbox protocol, current committed code. Cannot show runner PID or today's STOP bytes | Process liveness UNKNOWN from git alone. Architecture prose is stale about sequence 544 and STOP `CLEAR` |
| DORY branch `atlas/manual-results` `f14a96c69f93ce8a8998fd6e0b23fccba55d0f23` | `LATEST.md` blob `02a5a544a8f2b2c5ffa6c8a1a6d3bf94167b25b4` for a manual-result byte-integrity report | Cited control main is `c900e103`, not current `main` |

A session that can read only current GitHub `main` of Atlas cannot answer questions 5 through 10 from this continuity system. Those answers exist in the isolated candidate and in live local files.

## Missing documents found before this candidate

| Expected by the mission | Result |
|-------------------------|--------|
| `docs/CURRENT-CHECKPOINT.md` | Absent locally and 404 on GitHub `main`. This candidate adds a pointer |
| `reports/engineering-continuity/LATEST.md` | Directory absent locally and 404 on GitHub `main`. This candidate adds it |
| Founder decision register | No matching file in the local Atlas tree. This candidate adds an evidence register |
| Operating roadmap for DORY and Donum | `ROADMAP.md` is an Atlas knowledge roadmap dated 2026-07-08. It is not current engineering status |
| Historical continuity report | `reports/EOS-V2-2026-10-20-CONTINUITY-CHECKPOINT.md` exists and is historical |

## Qualification result

PASS WITH CONDITIONS for the isolated candidate.

The proposed documents answer all ten questions, and they label live facts as dated observations. They do not answer current liveness for any moment after the observation window.

FAIL as a description of GitHub Atlas `main` today. Publication was not authorized, so that gap remains.
