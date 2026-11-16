# Current operating roadmap

This file is the retrieval record for the operating plan. It is not execution authority, not a second handshake, and not an approved master roadmap.

| Field | Value |
| --- | --- |
| Project | Donum Dei, with Atlas knowledge, DORY control, and Family Kanban |
| Mission | Recover the approved plan, the current milestone, decisions, and evidence from files |
| Record revision | `OPERATING-ROADMAP-RECORD-2026-11-15` |
| Approved roadmap version | `NONE` |
| Founder approval | NOT APPROVED. This revision does not approve a master roadmap |
| Provenance | Founder task `ATLAS PERSISTENT PLANNING AND HANDSHAKE IMPLEMENTATION — PHASE 1`, 2026-11-15. Parent Atlas commit `0a4a825f259a0c245a71aac6a96ab98df739a315` |
| Authorization status | NOT AUTHORIZED. A roadmap row cannot grant READY |

Chat memory cannot fill a missing field. Report `UNKNOWN` and name the missing file.

## Retained constraints

These constraints are retained by the Phase 1 task. They do not approve the milestones below.

| Constraint | Owner |
| --- | --- |
| Order remains Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder | `docs/EFFICIENCY-LOOP-HANDSHAKE.md` |
| DORY execution still requires the existing publication path and safety authorization | `Publish-DoryAtomicReadyMailbox` only |
| Disaster recovery keeps three workstreams and the seven-step sequence | The recovery procedure. This file does not replace it |
| Family Kanban recovery includes source code and development history, and excludes live board data, session history, and the ticket ledger | Founder decision `FD-2026-11-15-04` |
| DORY production hardening stays separate from disaster recovery | No shared sequence |
| A proposal does not interrupt active work without approval | `planning/` on branch `atlas/planning` |

## Ordered milestones

An ordered list is not an approved sequence while the approved version is `NONE`.

| Order | Milestone | Status | Authoritative plan |
| --- | --- | --- | --- |
| 1 | Atlas knowledge foundation, curation, and discovery | REQUIRES RECONCILIATION | `ROADMAP.md`. Knowledge phases only. Last stated update 2026-07-08 |
| 2 | Founder-Away operating checkpoint | REQUIRES RECONCILIATION | `DORY_LOOP_CONTROL/atlas/README.md`, reconciled 2026-11-06. It contains stale runtime facts and is not current truth |
| 3 | Disaster recovery | RETAINED, not re-approved as a new plan | Three workstreams: recoverable data and credentials; one clean-environment drill; one maintained procedure. Seven steps: credential capture; independent restore proof; disposable `qualify-synth`; Donum, Family, and Atlas smoke; synthetic runner lock and shutdown; update the existing recovery procedure; archive historical qualification gates. Procedure home: `C:\Users\eejon\AppData\Local\DORY_DR_Preparation\docs\RECOVERY.md` |
| 4 | DORY production hardening | SEPARATE. NOT APPROVED for `main` | Preservation ref `refs/heads/atlas/dory-stop-detection-qualified-v1` at `05744c4b96ea1e3bc85509e15847251d34a78bb3`. Advancing `main` is a separate decision |
| 5 | Persistent planning records | DOCUMENTATION ONLY | This file, the decision register, and `planning/` on `atlas/planning` |

No local file was found for a six-phase DORY operating roadmap. If that plan exists only in chat, its source is missing and its status is `UNKNOWN`.

## Current milestone

`UNKNOWN`. No approved roadmap version names a current product milestone.

Phase 1 documentation on `atlas/planning` is the bounded writing authorized by the Phase 1 task. That authorization does not grant READY and does not select the next product milestone.

## Acceptance criteria

An approved version exists only after a Founder decision names all of the following:

- The approved roadmap version, replacing `NONE`
- The current milestone
- The acceptance checklist for that milestone
- The next authorized action

Until then, readers use the retained constraints and report the current milestone as `UNKNOWN`.

## Dependencies and blockers

| Item | State |
| --- | --- |
| Atlas alias commit `0a4a825` on GitHub | Not on `origin/main` `f46de55a6cb074879c29ce0c2dfc3d4873f97b91` at the Phase 1 preflight. Push is not authorized |
| Control-repo GitHub tip | Not re-read during Phase 1. Do not treat a stored tracking ref as a fresh remote confirmation |
| Live mailbox, STOP, SYNC_STOP, AUTO-READY, and protected work | Must be read at retrieval time. Values below are observations, not protocol |
| Off-laptop recovery credentials and an independent restore | Still open inside the retained recovery sequence. This file does not execute them |

## Last verified execution evidence

Observed while preparing this record. Re-read before treating any line as current.

| Evidence | Observation |
| --- | --- |
| Atlas local `main` and new `atlas/planning` base | `0a4a825f259a0c245a71aac6a96ab98df739a315` |
| Atlas GitHub `main` | `f46de55a6cb074879c29ce0c2dfc3d4873f97b91` |
| Atlas `main` worktree | Clean at preflight |
| Control `v2/STATE.json` | Sequence 630, task `DORY-R8C-SEQ630-ATLAS-INGRESS-COMMISSIONING-V1`, turn DORY, status COMPLETE |
| Control `v2/STOP` | `CLEAR` |
| Control `v2/READY`, `v2/SYNC_STOP`, `v2/AUTO-READY` | Absent |
| Control `v2/TASK.md` and `v2/RESULT.md` | Present for sequence 630. The result text still describes an earlier CURSOR/RUNNING state. Current `STATE.json` wins |
| Runner liveness | `UNKNOWN`. Not enumerated for this record |
| Protected product WIP | Not re-inventoried. Do not claim it from chat |

## Next proposed action

Founder reviews record revision `OPERATING-ROADMAP-RECORD-2026-11-15` and either assigns an approved roadmap version or leaves the version at `NONE`.

Authorization status: `NOT AUTHORIZED`. Next action until that review: `AWAIT FOUNDER`.
