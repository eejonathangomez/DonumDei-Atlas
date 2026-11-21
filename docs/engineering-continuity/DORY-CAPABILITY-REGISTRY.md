# DORY capability registry

**Last verification date:** 2026-11-20  
**Rule:** historical completion evidence is not current runner liveness. Isolated qualification is not deployment.

Deployment words used here:

| Word | Meaning |
|------|---------|
| DEPLOYED-INACTIVE | Present on control `main` `824cf59cc63586374126d428fa3557c6b6b73836`, which matches GitHub `main`. Runner process count observed as 0 |
| QUALIFIED-ISOLATED | Passed in temporary repositories against an uncommitted candidate. Not installed |
| HISTORICAL | Previously demonstrated |
| NOT IMPLEMENTED | No current implementation |
| PROPOSED | Written as future intent only |

## Registry

| Capability | Purpose | Implementation | Qualification | Historical evidence | Deployment | Known defects | Last verification |
|------------|---------|----------------|---------------|---------------------|------------|---------------|-------------------|
| Atomic READY publication | One commit grants execution | `v2/DoryAtomicMailbox.ps1` `Publish-DoryAtomicReadyMailbox` | Runner qualification suites on control `main`. Not re-executed as a live publication on 2026-11-20 | Sequences through 632 exist as git history | DEPLOYED-INACTIVE | Invalid envelopes are refused. Sequence 545 request remains the documented refusal example | 2026-11-20 code path cited. Live publish not performed |
| Runner poll and spawn | Adopt READY, spawn Cursor, return the turn | `v2/dory_v2_runner.ps1` `Invoke-Consume`, `Invoke-DorySpawnCursorAgent` | `tests/runner/Qualify-*.ps1` exist. Live process not started | See historical throughput below | DEPLOYED-INACTIVE | No automatic supervisor | 2026-11-20 process observation: count 0, lock absent |
| Exact STOP | Halt publication and spawn | `Read-StopAsserted` in the runner. HEAD subject `DORY: reassert exact-match STOP` | STOP bytes observed `53-54-4F-50-0A` | Sequence 630 commit contains STOP text `CLEAR` | DEPLOYED-INACTIVE. File currently `STOP` | Older architecture prose still says the file is `CLEAR` | 2026-11-20 |
| Git sync and SYNC_STOP | Refuse unpublished or divergent mailbox history | `Sync-Pull`, `Invoke-DorySyncStop`, `Test-DoryInFlightMailboxPublication` | In-flight and mailbox suites exist. Not re-run on the live repo this session | Reconcile subject is unrecognized in-flight | DEPLOYED-INACTIVE | Telemetry dirt versus SYNC_STOP behavior was not executed live this session | 2026-11-20 source and status |
| Campaign continuation | Select a stored candidate without implying publication | `v2/campaign-continuation.json`, `Invoke-DoryCampaignContinuationPass` | Flag observed false | Control doc reports sequences 455–502, one task shape, ending `20b2468a`. That count was not re-derived on 2026-11-20 | DEPLOYED-INACTIVE and disarmed | `CONTINUE` plus `published=False` can be misread | 2026-11-20 file read. Historical count REPORTED |
| Project registry, park, switch | Route a project without granting READY | `v2/project-registry.json`, `v2/DoryProjectLifecycle.ps1` | Not re-run this session | Donum ACTIVE unparked, Family IDLE parked, Founder/Architect IDLE unparked | DEPLOYED-INACTIVE | Registry active id and STATE active id are different fields | 2026-11-20 registry read |
| Atlas request ingress | Accept data and refuse non-publisher authority | `v2/Invoke-DoryAtlasPublicationRequest.ps1` | Envelope refusal is the control-doc example | Sequence 545 was not created | DEPLOYED-INACTIVE | Request presence is still easy to mistake for READY if the handshake is skipped | 2026-11-20 contract read |
| Post-execution audit | Accept only structured COMPLETE or BLOCKED evidence | `Invoke-DoryPostExecutionErrorAudit` | `Qualify-PostExecutionAuditEvidence.ps1` PASS checks=55 on the isolated candidate, 2026-11-20 | Sequence 542 is the control doc's example of audit failure distinct from health | QUALIFIED-ISOLATED against candidate. Mechanism exists on `main` | Free-form prose is not scanned, by design | 2026-11-20 |
| Completion identity | Do not advance `last_completed_sequence` for a false completion | Completion publishers in the runner | `Qualify-CompletionIdentity.ps1` PASS checks=73 on the isolated candidate | Mailbox at observation has last completed 632 | QUALIFIED-ISOLATED against candidate. Mechanism exists on `main` | None newly found this session | 2026-11-20 |
| Product-integrity gate | Refuse COMPLETE when a product workspace changes without authority | Isolated `v2/dory_v2_runner.ps1` only. Functions `Get-DoryProductWorkspaceSnapshot`, `Test-DoryProductWorkspaceIntegrity` | `Qualify-ProductIntegrityGate.ps1` PASS checks=43 | None on the live runner | QUALIFIED-ISOLATED. NOT ACTIVATED | Live runner lacks the gate | 2026-11-20 |
| Fail-closed stale RUNNING and recovery | Missing product baseline blocks replacement completion | Isolated runner `Test-DoryProductIntegrityBaselineVerified`, recovery refusals `PRODUCT_BASELINE_REQUIRED` | Included in fail-closed checks | Prior restart qualification showed COMPLETE before this correction | QUALIFIED-ISOLATED. NOT ACTIVATED | Does not by itself cover a later poll after deferred publication | 2026-11-20 |
| Deferred-reconciliation closure | Stop a published reconcile commit from becoming a fresh product execution | Isolated `Test-DorySequenceReconciledFromStaleRunning` | Fail-closed suite PASS checks=70, including multi-poll and a fresh process | Pre-fix reproduction: fresh process published COMPLETE, 1 spawn, last completed 20 | QUALIFIED-ISOLATED. NOT ACTIVATED | Published-RUNNING resume bypass. HEAD-only ancestry. Uncommitted | 2026-11-20 |
| Manual-result publication | Preserve Cursor manual reports outside the mailbox | `atlas/manual-results/Publish-ManualResult.ps1` on branch `atlas/manual-results` | `LATEST.md` reports `QUALIFY_MANUAL_RESULT_PUBLICATION=PASS checks=159`. Not rerun this session | Branch tip `f14a96c69f93ce8a8998fd6e0b23fccba55d0f23`. Cited control main `c900e10399726af0a31c6d68bae4abc80ac7df68`, which is not current `main` | HISTORICAL relative to current `main`. Branch exists | Not current operational truth | 2026-11-20 GitHub read |
| Lessons store | Advisory memory that cannot grant authority | `v2/DorySharedLearning.ps1` | Writer refuses `authority` true, per control contract | Not re-qualified this session | DEPLOYED-INACTIVE | A person can still copy lesson text into a future request. The request must still pass the publisher | REPORTED |
| Transition snapshot | Non-authorizing close/protect/select/restore/verify/resume contract | `Get-DoryTransitionContract` in `v2/DoryOperatingState.ps1` | Snapshot flags force authority false | Sequence 545 durable-checkpoint request was refused | DEPLOYED-INACTIVE as a contract. Not an automatic resume engine | Not a continuity substitute for this Atlas record | REPORTED |

## Isolated product-integrity candidate

| Field | Value |
|-------|-------|
| Path | `C:\Users\eejon\AppData\Local\DORY_ProductIntegrityGate_824cf59` |
| Base | `824cf59cc63586374126d428fa3557c6b6b73836` |
| Combined isolated regression | 241 passing checks: fail-closed 70, product-integrity gate 43, completion identity 73, post-execution audit 55. All exit 0 on 2026-11-20 |
| Deferred-reconciliation correction | Present, uncommitted |
| Published-RUNNING resume bypass | Open. A published RUNNING commit can still resume and capture a new baseline |
| HEAD-only ancestry limitation | The reconcile subject is detected only when it is HEAD. A later commit on top of it hides the marker |
| Git state | Uncommitted. Runner 237 insertions. Fail-closed and gate tests untracked. Unrelated section 11 doc append 24 insertions, preserved and not authority |
| Activation | NOT AUTHORIZED. Not installed in the live runner |

## Historical execution before the backup pause

These facts were rechecked against control git history on 2026-11-20. They do not mean a runner is active.

| Evidence | Result | Class |
|----------|--------|-------|
| COMPLETE subjects on 2026-10-30 | 78 | VERIFIED count |
| COMPLETE subjects on 2026-10-31 | 13 | VERIFIED count |
| COMPLETE subjects on 2026-10-26 and 2026-10-29 | 39 and 34, spans 318–359 and 408–447 | REPORTED by handshake section on `docs/historical-dory-capability-2026-11` at `feb9b530`. Not re-counted here |
| Sequence 630 COMPLETE commit | `a67cea92c66b14014ed601fc430e412def283db6`, 2026-11-10 07:48:17 -0800, subject `DORY v2: sequence 630 COMPLETE return to DORY` | VERIFIED |
| STOP blob at that commit | `CLEAR` | VERIFIED historical file content |
| Sustained campaign sequences 455–502 | Named by `docs/DORY_CURRENT_ARCHITECTURE.md` as 48 cycles of one task shape ending `20b2468a` | REPORTED. Not re-counted this session |
| Current mailbox | Sequence 632 COMPLETE, not a claim that 632 sequences are all product features | VERIFIED as mailbox identity only |

## Current liveness

On 2026-11-20 the process query for `dory_v2_runner` and `DORY_LOOP_CONTROL` returned count 0. `v2/runner.lock` was absent. That is the liveness fact. GitHub history cannot establish it.
