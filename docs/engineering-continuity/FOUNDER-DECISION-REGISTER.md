# Founder decision register

GitHub Atlas `main` has no Founder decision register. Branch `atlas/planning` at GitHub tip `f792d76ba66e6e69469021de9f798f65d8da0b83` already contains `docs/decisions/FOUNDER-DECISION-REGISTER.md`, including decisions `FD-2026-11-15-01` through `FD-2026-11-15-07`. That file is not in this branch. This supplement records the 2026-11-20 engineering observation. It does not replace the planning register and it does not create authority.

Local planning commit `93c9db984e4d479c26bf4a438a6c005ed38bdff0` is one commit ahead of the GitHub planning tip and is not part of this publication candidate.

| Decision | Class | Evidence | Status on 2026-11-20 |
|----------|-------|----------|----------------------|
| DORY is an independent control platform. Donum is the current product. Family is a separate product | VERIFIED as documented intent | `docs/DORY_CURRENT_ARCHITECTURE.md` section 1; Atlas strategic map | Standing |
| Knowledge may cross projects. Authority may not | VERIFIED | Handshake protocol `DORY-EFFICIENCY-LOOP-HANDSHAKE-V1` | Standing |
| Execution authority exists only after `Publish-DoryAtomicReadyMailbox` | VERIFIED in control contract | `v2/DoryAtomicMailbox.ps1` | Standing |
| Campaign publication stays disabled until a separate Founder activation | VERIFIED file state | `v2/campaign-continuation.json` `publish_enabled` false | In force |
| LIVE trading, PAPER orders, cancels, and broker-state changes stay prohibited for the commissioned campaign | VERIFIED file text | Same campaign file, `runtime.live_prohibited` true | In force |
| STOP dominates publication and spawn | VERIFIED file bytes `STOP` + LF, and control contract | `v2/STOP` | In force at observation. Re-verify before any start |
| AUTO-READY is not granted | VERIFIED absence of `v2/AUTO-READY`; tracked control telemetry dirt remains | Live control `git status` | NO |
| Product-integrity candidate is not activated | VERIFIED isolated dirty tree; live runner has no product-workspace snapshot function | Candidate `DORY_ProductIntegrityGate_824cf59` | NOT AUTHORIZED |
| Sequence 632 is a dated runtime snapshot, not permanent current truth | VERIFIED mailbox at observation; historical relative to the next live read | `v2/STATE.json` | Observation only |
| Sequence 630 is the last COMPLETE commit before the later backup-period snapshot | VERIFIED commit existence. The operating meaning is HISTORICAL | `a67cea92c66b14014ed601fc430e412def283db6` | Historical reference |
| Protected Donum WIP is not cleaned | VERIFIED 12 tracked hashes match the supervised baseline, 0 mismatches | `DORY_Supervised632/donum-tracked-dirty-before.txt` | In force |
| Historical handshake branch is not merged by the continuity candidate | VERIFIED branch tip, not contained in local `main` | `feb9b53090a4a77d9b376b653b0eee89e7c20e68` | Not merged |
| Section 11 founding-objectives text in the isolated candidate is proposed | VERIFIED uncommitted doc append, classed by its own text as proposed | Candidate `docs/DORY_ENGINEERING_OS_V1_FOUNDATION.md` | Not authority |

## Decisions completed after the 2026-11-20 observation

At commit `a28374af348a58c3086c4e7cd9f2d35a24b98666` the publication question was still listed as open. This section records what happened after that commit. It does not rewrite the observation-time table above.

| Decision | Evidence | Status |
|----------|----------|--------|
| The Founder authorized one documentation commit and one push of `docs/dory-donum-engineering-continuity-2026-11-20`, and that publication completed | GitHub commit `a28374af348a58c3086c4e7cd9f2d35a24b98666`, parent `f46de55a6cb074879c29ce0c2dfc3d4873f97b91`, timestamp `2026-11-21T07:28:01Z`. Recorded in [the publication event](../../reports/engineering-continuity/2026-11-21/PUBLICATION-EVENT.md) | Completed. Documentation only |

That authorization did not include a merge, DORY activation, STOP release, AUTO-READY, campaign publication, or Donum development. Those remain unauthorized.

The 2026-11-15 register on `atlas/planning` is unchanged. This section does not replace `FD-2026-11-15-01` through `FD-2026-11-15-07`.

## Open decisions

| Question | Why it is open |
|----------|----------------|
| Whether to correct the published-RUNNING product resume bypass | The deferred-reconciliation hole is closed only in the inactive candidate |
| Whether `DONUM-CHART-CANCEL-TRUTH-V1` remains the next product execution | The campaign file names it, publication is false, and protected manual-trading WIP is present |
| Whether to reconcile live control telemetry dirt | AUTO-READY stays blocked while those tracked files are dirty. The publication did not restore or commit them |
| Whether to merge this documentation branch | The branch is published and is not in `main`. Merge was not authorized |
