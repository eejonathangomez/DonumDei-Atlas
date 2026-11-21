# DORY operational checkpoint — 2026-11-20

**Observation window:** 2026-11-20 evening, America/Los_Angeles, during the engineering continuity session.  
**Authority:** none. Re-verify before any start, STOP change, or publication.  
**This file is a dated observation.** It is not updated in place. A later checkpoint gets a new date, and `LATEST.md` moves its pointer.

## Control identity

| Fact | Value | Class |
|------|-------|-------|
| Repository | `eejonathangomez/dory-loop-control` | VERIFIED |
| Local path | `C:\Users\eejon\OneDrive\Desktop\DORY_LOOP_CONTROL` | VERIFIED |
| Branch | `main` | VERIFIED |
| Local HEAD | `824cf59cc63586374126d428fa3557c6b6b73836` | VERIFIED |
| GitHub `main` | `824cf59cc63586374126d428fa3557c6b6b73836` | VERIFIED via `gh` |
| HEAD subject | `DORY: reassert exact-match STOP` | VERIFIED |

## Runner

| Fact | Value | Class |
|------|-------|-------|
| Process count | 0. Query matched command lines containing `dory_v2_runner` or `DORY_LOOP_CONTROL` | VERIFIED |
| PID | none observed | VERIFIED |
| Lifecycle | not running | VERIFIED for that query. A process launched without those strings would be UNKNOWN |
| `v2/runner.lock` | absent | VERIFIED |

GitHub history was not used to decide liveness.

## Mailbox

| Fact | Value | Class |
|------|-------|-------|
| Protocol | `DORY-v2` | VERIFIED |
| Sequence | 632 | VERIFIED |
| Task | `DORY-CONTROL-SAFE-POINT-READ-632` | VERIFIED |
| Turn | `DORY` | VERIFIED |
| Status | `COMPLETE` | VERIFIED |
| `last_completed_sequence` | 632 | VERIFIED |
| `active_project_id` | `donum-dei` | VERIFIED |
| `global_qualification` | `YELLOW` | VERIFIED field. Meaning not re-derived |
| Sequence 633 | no mailbox sequence 633. `git log --grep="sequence 633 "` returned no subject | VERIFIED as absence of that subject and of a 633 mailbox |

## Safety

| Fact | Value | Class |
|------|-------|-------|
| STOP bytes | `53-54-4F-50-0A` (`STOP` plus LF) | VERIFIED |
| STOP meaning | asserted. Exact `CLEAR` is the only execution permit | VERIFIED file. Runtime enforcement not exercised because the runner was not started |
| SYNC_STOP | not a file. Mechanism exists in `Sync-Pull` | VERIFIED as code. Not executed against the live repo this session |
| Tracked control dirt | `v2/telemetry/DORY-TAIL.log`, `v2/telemetry/STATUS.json` | VERIFIED |
| AUTO-READY file | `v2/AUTO-READY` absent | VERIFIED |
| AUTO-READY decision | NO | VERIFIED as the operating decision. Tracked dirt remains |
| Campaign file | `v2/campaign-continuation.json` | VERIFIED |
| Campaign id | `DONUM-BOUNDED-ENGINEERING` | VERIFIED |
| Campaign state | `COMMISSIONED` | VERIFIED |
| `publish_enabled` | false | VERIFIED |
| `bounded_campaign` | true | VERIFIED |
| `max_complete_tasks` | 15 | VERIFIED |
| Objective id | `DONUM-CHART-CANCEL-TRUTH-V1` | VERIFIED |
| `objective_complete` | false | VERIFIED |
| `runtime.live_prohibited` | true | VERIFIED |
| Candidate allowed paths | five `frontend/src/lib/chartOrderMarkers` files | VERIFIED |
| Broker actions | prohibited by the campaign text | VERIFIED as text. No broker call was made |

## Registry

| Project | Status | Parked | Branch | Repository | Class |
|---------|--------|--------|--------|------------|-------|
| `donum-dei` | ACTIVE | false | `stage-2/ux-workflow-001` | `eejonathangomez/TradingBot` | VERIFIED |
| `family-routine-board` | IDLE | true | `main` | `eejonathangomez/kanban` | VERIFIED |
| `founder-architect-knowledge` | IDLE | false | `main` | `eejonathangomez/DonumDei-Atlas` | VERIFIED |

Registry `active_project_id` is `donum-dei`. ACTIVE is not execution authority.

## Protected control changes

The two telemetry files are the only tracked modifications. They were not staged, restored, or committed. Numerous pre-existing untracked control paths were left untouched.

## Isolated candidate

| Fact | Value | Class |
|------|-------|-------|
| Path | `C:\Users\eejon\AppData\Local\DORY_ProductIntegrityGate_824cf59` | VERIFIED |
| Base | `824cf59cc63586374126d428fa3557c6b6b73836` | VERIFIED |
| Runner diff | 237 insertions, 0 deletions, uncommitted | VERIFIED |
| Tests | untracked `Qualify-ProductIntegrityFailClosed.ps1`, `Qualify-ProductIntegrityGate.ps1` | VERIFIED |
| Unrelated doc append | `docs/DORY_ENGINEERING_OS_V1_FOUNDATION.md`, 24 insertions | VERIFIED present. Not edited by the continuity task |
| Activation | NOT AUTHORIZED | VERIFIED as decision and as absence from the live runner |

## Outstanding defects

1. Deployed runner can still reconcile an interrupted product-bound RUNNING sequence to READY and, after publication, treat it as fresh work.
2. Isolated correction of the deferred path is uncommitted and inactive.
3. Published RUNNING resume can still capture a new product baseline.
4. Reconcile detection in the candidate is HEAD-only.
5. Ignored product files and out-of-workspace writes are outside the gate.
6. Control architecture doc still narrates sequence 544 and STOP `CLEAR`.
7. Tracked telemetry dirt blocks AUTO-READY.
8. `atlas/manual-results` `LATEST.md` cites control main `c900e10399726af0a31c6d68bae4abc80ac7df68`, which is not current `main`.

## Next proposed engineering task

Review and, only under a separate authorization, publish this continuity candidate. Do not start the runner, clear STOP, enable campaign publication, or install the product-integrity candidate as part of that review.

The next DORY code proposal, if the Founder wants it, is a separate correction for the published-RUNNING product resume bypass. It is not authorized by this checkpoint.
