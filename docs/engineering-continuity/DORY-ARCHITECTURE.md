# DORY architecture reference

**Class:** stable architecture. Operational numbers in the dated checkpoints are not repeated here as protocol constants.  
**Control contract:** `eejonathangomez/dory-loop-control` `docs/DORY_CURRENT_ARCHITECTURE.md` on `main`.  
**Observation base:** local and GitHub control `main` `824cf59cc63586374126d428fa3557c6b6b73836`.  
**Authority:** none.

DORY is an independent engineering control platform. Donum Dei is the current product it can route. Family Kanban is a separate product. Atlas is the institutional knowledge home. Atlas is not DORY.

## 1. Purpose, mission, and design principles

**Implemented.** DORY hands one bounded engineering task to a worker and takes the turn back. It exists so product work, campaign intent, notes, and health status are not mistaken for permission to execute.

Design principles that the control contract and handshake both state:

- Keep the runner boring. The live loop does not modify the live runner.
- One atomic publisher creates execution authority.
- Fail closed. STOP, dirty control state, unpublished non-telemetry commits, and invalid envelopes refuse work.
- Knowledge may cross projects. Authority may not.
- Recovery restores a healthy control plane. Recovery does not publish stored work.
- LIVE trading is not inferred from documentation, lessons, or campaign text.

**Proposed, not authority.** Uncommitted section 11 text in the isolated product-integrity candidate records founding objectives as `PROPOSED_FUTURE_CAPABILITY`. It is not part of control `main`.

## 2. Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder

**Implemented as roles and transport. Not a running process at the 2026-11-20 observation.**

| Role | Owns | Does not own |
|------|------|----------------|
| Founder | Vision, boundaries, authorization, STOP, activation | Automatic execution |
| Atlas | Strategy, smallest complete objective, knowledge, request data | Mailbox publication |
| DORY | Sequences, mailbox, runner, registry, campaign flag, fail-closed gates | Product source |
| Cursor | Implementation and evidence under the authorized task | The next sequence |
| Git | Durable history | Current liveness |

The collaboration order is the handshake efficiency loop. A request file, a lesson, a qualification report, and this document are data. They become execution only after `Publish-DoryAtomicReadyMailbox` publishes one `CURSOR` / `READY` commit.

## 3. Control-plane architecture

**Implemented on control `main`.**

| Component | Path | Responsibility |
|-----------|------|----------------|
| Runner | `v2/dory_v2_runner.ps1` | Poll, integrity, adoption, spawn, completion or block |
| Start entry | `v2/start_dory.ps1` | Starts the runner. Default runner action is status, not run |
| Lock | `v2/runner.lock` | One lock per repository path. Created only while a runner holds it |
| Atomic mailbox | `v2/DoryAtomicMailbox.ps1` | `Publish-DoryAtomicReadyMailbox` |
| Publisher entry | `v2/Publish-DoryAtomicMailbox.ps1` | Wrapper around the same publisher |
| Atlas request adoption | `v2/Invoke-DoryAtlasPublicationRequest.ps1` | Parses request data and calls only the publisher |
| Project registry | `v2/project-registry.json`, `v2/DoryProjectRegistry.ps1` | Project identity, workspace, safe point, park bit |
| Project lifecycle | `v2/DoryProjectLifecycle.ps1` | Park, unpark, switch |
| Campaign | `v2/campaign-continuation.json` | Candidate selection. Publication requires `publish_enabled` |
| Operating state | `v2/DoryOperatingState.ps1` | Lessons reader and non-authorizing transition contract |
| Learning store | `v2/learning/lessons.json`, `v2/DorySharedLearning.ps1` | Advisory lessons. Writer refuses `authority` true |
| Telemetry | `v2/telemetry/`, `v2/DoryTelemetry.ps1` | Status, tail, sync circuit. Not mailbox authority |
| Post-exec audit | runner functions `Invoke-DoryPostExecutionErrorAudit`, `Invoke-DoryPostExecutionHealth` | Evidence and control-plane health |
| Supervisor | `v2/DorySupervisor.ps1` | Deprecated wrapper. No automatic restart supervisor |

The worker adapter is `Invoke-DorySpawnCursorAgent`, which launches `agent.cmd`. A vendor-neutral adapter is **not implemented**.

## 4. Atomic TASK + STATE publication

**Implemented.**

Execution authority is one commit that contains `v2/TASK.md` and `v2/STATE.json` with `turn=CURSOR` and `status=READY`, produced by `Publish-DoryAtomicReadyMailbox`.

`Test-DoryReadyEnvelope` refuses envelopes that do not match the permission shape before the publisher writes the mailbox. Split publication of TASK and STATE is forbidden. TASK existence alone is not authority.

Commit subject for that publication is the READY publish subject recognized by `Test-DoryInFlightMailboxPublication`.

## 5. Atlas ingress and request validation

**Implemented. Non-authority.**

| Input | Path | Rule |
|-------|------|------|
| Committed request | `v2/atlas-publication-request.json` | Protocol `DORY-ATLAS-PUBLICATION-REQUEST-V1`. Fields `protocol`, `request_id`, `task_text` only |
| Local ingress | `v2/atlas-ingress/request.json` | Same parser. Gitignored. Not a second mailbox |
| Direct task file | `Publish-DoryAtomicMailbox.ps1 -TaskFile` | Same publisher |

If the committed request and the ingress file both exist and differ, nothing is published. A command field in the request is refused. The worked example in the control architecture is request `atlas-seq545-durable-operating-checkpoint-v1`, which the envelope rejects before any mailbox write. Sequence 545 was not created by that request.

## 6. Runner lifecycle and Cursor spawn

**Implemented in code. Process liveness is operational and must be read from the dated checkpoint plus a fresh process check.**

`Invoke-Consume` checks STOP, synchronizes git, reads STATE, and only then considers spawn. `Test-DoryCursorSpawnPermitted` and `Invoke-DorySpawnCursorAgent` are the spawn boundary. `v2/runner.lock` plus `Test-DoryRunnerLockCoherent` enforce one runner. `Test-ActiveSpawnAlive` detects an existing worker. There is no supervisor that restarts a stopped runner.

Starting the runner does not authorize stored campaign work.

## 7. Mailbox state transitions and sequence ownership

**Implemented.**

Live files are `v2/TASK.md`, `v2/RESULT.md`, `v2/STATE.json`, and `v2/STOP`.

Allowed turns include `DORY`, `CURSOR`, `FOUNDER`, and `STOP`. Allowed statuses include `IDLE`, `READY`, `RUNNING`, `COMPLETE`, `BLOCKED`, and `MANUAL`. `turn=FOUNDER` with `status=MANUAL` is Founder Manual Session and must not spawn Cursor.

The global sequence is the idempotency key. `last_completed_sequence` advances when a completion is published. `Set-AdapterBlockedState` keeps `last_completed_sequence` and commits a BLOCKED adapter subject. BLOCKED history is not rewritten into COMPLETE.

`Test-DorySequenceAlreadyConsumed` and the completion publishers refuse a second completion of a consumed sequence. Completion-identity tests cover that contract.

Normal cycle:

```text
READY commit
→ runner adopts
→ RUNNING commit
→ Cursor
→ RESULT.md
→ post-exec audit and health
→ COMPLETE or BLOCKED
→ turn returns to DORY
```

## 8. Campaign management and project routing

**Implemented. Currently disarmed. See the operational checkpoint for the file values.**

`Invoke-DoryCampaignContinuationPass` may decide `CONTINUE`, `WAIT`, `BLOCKED`, or `COMPLETE`. `CONTINUE` selects a candidate. Publication occurs only when `publish_enabled` is true and only through the atomic publisher. A log line that says `CONTINUE` and `published=False` is selection without publication.

`v2/project-registry.json` binds `project_id` to repository, branch, workspace, safe point, park bit, and mutation policy. STATE `active_project_id` and registry `active_project_id` are different fields and may diverge. Autonomous consume may record the task project on STATE without rewriting the registry.

Park is not STOP. Unpark is not READY. Switch is not spawn. Precedence is STOP, then park, then routing.

## 9. Product worktree integrity and authorized changes

**Split status.**

| Behavior | Status |
|----------|--------|
| Envelope `allowed_paths`, project id, and mutation flags | Implemented on control `main` |
| Safe-point and dirty tracked product refusal for incompatible trees | Implemented in runner project checks |
| Control health gate does not treat Donum WIP as control dirt | Implemented. `CONTROL DIRT != DONUM WIP` |
| Same-process product snapshot before spawn and compare before COMPLETE | Implemented only in the uncommitted isolated candidate `DORY_ProductIntegrityGate_824cf59` |
| Same-call stale RUNNING block when the product baseline is missing | Same inactive candidate |
| Deferred reconcile subject check | Same inactive candidate. Not on the live runner |
| Published RUNNING resume without a baseline | Open defect, including in the candidate |
| Ignored product files and writes outside the workspace | Not covered |

The live runner at `824cf59` does not contain `Get-DoryProductWorkspaceSnapshot`. The candidate must not be described as deployed.

## 10. STOP, SYNC_STOP, AUTO-READY, and fail-closed behavior

**Implemented mechanisms.**

| Gate | Behavior |
|------|----------|
| STOP | `Read-StopAsserted` allows execution only for exact `CLEAR`. Exact `STOP` dominates publication, spawn, routing, and restart. Park and recovery do not clear it |
| SYNC_STOP | `Invoke-DorySyncStop` throws. Unpublished local commits that are not a recognized in-flight READY or RUNNING publication, or expected telemetry, stop the loop. Remote-ahead and divergence stop the loop |
| Health latch | Non-transient integrity failures stay fail-closed until a new process. `STALE_INDEX_STAT` is the automatic repair allowlist |
| AUTO-READY | Not a mailbox status. Absence of an AUTO-READY grant plus tracked control dirt keeps autonomous readiness off |
| Invalid envelope | Refused before mailbox mutation |
| Post-exec failure | Preserves RESULT, writes `v2/audit/post-exec-sequence-N.json`, leaves `last_completed_sequence` unchanged |

The control architecture document still contains older sentences that say the STOP file text is `CLEAR` and that the mailbox is sequence 544. Those sentences are historical relative to a later live read. The dated operational checkpoint is the place for the latest observation.

## 11. Git synchronization, recovery, and restart handling

**Implemented.**

`Sync-Pull` fetches `origin/main`, classifies the tree, and compares `HEAD...origin/main`.

Recognized in-flight subjects are only:

- `DORY v2: publish sequence N READY` with a COMPLETE parent
- `DORY v2: sequence N RUNNING` with a READY parent

The stale-running reconcile subject `DORY v2: sequence N stale RUNNING reconciled to READY` is not an in-flight publication. While that commit is unpublished, the next poll throws `SYNC_STOP: unexpected unpublished local commit`.

`Reconcile-StaleRunningState` rewrites an interrupted RUNNING mailbox to READY and commits that subject. If the push is deferred, it returns before spawn. On the live runner, a later aligned READY poll can treat that sequence as fresh work. The isolated candidate blocks a product-bound case when that subject is still HEAD and no verified product baseline exists. That correction is inactive.

Restart does not resume work by itself. A new process re-reads STOP, git integrity, and the mailbox. Recovery procedures in Skill 003 and Skill 004, and `docs/DORY_V2_INCIDENT_LESSONS_GOLDEN_RECOVERY_RUNBOOK_V1.md`, are records. They do not publish READY.

## 12. Telemetry, logging, regression testing, and qualification

**Implemented.**

| Surface | Path |
|---------|------|
| Telemetry mirror | `v2/telemetry/STATUS.json`, `DORY-TAIL.log`, `LAST-ERROR.json` |
| Runner log | `v2/runner.log` |
| Post-exec evidence | `v2/audit/post-exec-sequence-N.json` |
| Qualification suites | `tests/runner/Qualify-*.ps1` |

Telemetry commits may move control HEAD without changing the operating contract or a product safe point. Health-gate text treats `v2/telemetry/` as ignored for `UNSAFE_WORKTREE`. Tracked telemetry dirt is still a git change and still blocks a manual AUTO-READY declaration. Those are different facts.

Qualification proves a mechanism in a test repository. It does not prove that a runner process is alive.

## 13. Backup, disaster recovery, and restoration boundaries

**Boundaries are implemented as refusals. A full clean-computer restore drill is not evidenced as complete.**

A known-good checkpoint in the control contract is four parts together: code truth, runtime truth, operational intent, and recovery contract. Restoring code without reading runtime truth is not a current checkpoint.

Restoration may repair the control plane. It must not:

- clear STOP
- set `publish_enabled` true
- publish a stored campaign candidate
- clean Donum WIP
- install an uncommitted runner candidate
- infer LIVE trading authority

Sequence 630, commit `a67cea92c66b14014ed601fc430e412def283db6` (2026-11-10), is a verified historical COMPLETE commit whose STOP blob at that commit is `CLEAR`. It is a historical reference, not the current mailbox. Sequence 632 is a later dated snapshot. Neither number is permanent protocol.

The Founder continuity standard in `docs/founder-architect/FOUNDER-ARCHITECT.md` is a requirement and direction. The handshake states it is not yet a proven clean-computer drill.

## 14. Current architectural limitations and technical debt

| Item | Class |
|------|-------|
| Live runner has no product-workspace baseline, so an interrupted product sequence can be reconciled to READY and later spawn | Open on deployed code |
| Isolated candidate closes the deferred-reconciliation path only while the reconcile commit is HEAD | Qualified, not deployed |
| Published RUNNING resume can still capture a new product baseline | Open in the candidate and on `main` |
| Ignored files and writes outside the registered workspace are outside the product gate | Open |
| `docs/DORY_CURRENT_ARCHITECTURE.md` embeds stale runtime sentences (sequence 544, STOP `CLEAR`, older Donum porcelain) | Documentation debt |
| Two Skill 004 directories. Canonical copy unresolved | REPORTED by the control architecture |
| `v2/DoryRuntime.ps1` publication journal was not fully traced | REPORTED |
| `CONTINUE` with `published=False` is easy to misread | Documentation hazard |
| Vendor-neutral worker adapter | Not implemented |
| Transition snapshot is not an automatic resume engine | By design |
| No supervisor restarts the runner | By design |
| Section 11 founding-objectives draft | Proposed only |

## Implemented versus proposed

| Capability | Classification |
|------------|----------------|
| Mailbox, publisher, runner, STOP, sync, registry, campaign flag, audit, lessons | Implemented on control `main` |
| Historical multi-sequence execution | Historical evidence. Not current liveness |
| Product-integrity completion gate and deferred-reconciliation block | Isolated, uncommitted, inactive |
| Durable pre-interruption product baseline file | Not implemented |
| Automatic campaign publication | Implemented and disarmed |
| Clean-computer continuity drill | Not proven |
| This Atlas continuity candidate | Documentation proposal. Unpublished |
