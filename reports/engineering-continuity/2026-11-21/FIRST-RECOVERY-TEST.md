# First continuity recovery test

**Result:** PASS WITH CONDITIONS. This record does not upgrade that result to an unconditional PASS.  
**Request time supplied with the recovery task:** 2026-11-20 11:32 PM America/Los_Angeles. That is after publication commit `a28374af348a58c3086c4e7cd9f2d35a24b98666` (`2026-11-21T07:28:01Z`).  
**Authority:** none.

The test asked a new session to recover DORY and Donum from the published branch, starting at the handshake and the continuity index. The returned result was PASS WITH CONDITIONS because recovery succeeded and several published sentences still described publication as pending.

## GitHub facts verified again for this reconciliation

| Fact | Value |
|------|-------|
| Continuity branch tip | `a28374af348a58c3086c4e7cd9f2d35a24b98666` |
| Parent | `f46de55a6cb074879c29ce0c2dfc3d4873f97b91` |
| Atlas `main` | `f46de55a6cb074879c29ce0c2dfc3d4873f97b91` |
| `atlas/planning` | `f792d76ba66e6e69469021de9f798f65d8da0b83` |
| Historical capability branch | `feb9b53090a4a77d9b376b653b0eee89e7c20e68` |
| Control `main` | `824cf59cc63586374126d428fa3557c6b6b73836` |
| Manual-results branch | `f14a96c69f93ce8a8998fd6e0b23fccba55d0f23` |

Manual-results `LATEST.md` remains the byte-integrity report. It cites control main `c900e10399726af0a31c6d68bae4abc80ac7df68`. It is not current control `main` and it is not mailbox authority.

## Local runtime observations

The recovery task reported sequence 632, turn DORY, status COMPLETE, STOP `STOP` plus LF, runner count 0, campaign publication false, Donum branch `stage-2/ux-workflow-001`, and Donum HEAD `4dcf67d8cf2bd3fd498622a1e29173c8c027a968`.

This reconciliation re-read those same facts without changing files. They still match. That re-read is a later observation. It does not replace the 2026-11-20 checkpoint and it does not prove the runner stays stopped after this read.

These recovery statements were not re-checked here and stay as reported by that test:

- Donum tracked count 12 and untracked count 61
- Hash match against the supervised baseline
- Two tracked telemetry paths
- Campaign id `DONUM-BOUNDED-ENGINEERING` and `live_prohibited` true
- Product-integrity candidate worktree

## Historical evidence

October 30 and 31 COMPLETE counts, sequence 630, and the older control-architecture sentences remain historical. October 26 and 29 counts remain reported by the historical capability branch and were not re-counted.

## Unknowns left by the test

`SYNC_STOP` was not executed. Donum tests and stage certification were not run. The Family production URL was not fetched. The product-integrity candidate was not re-read. A process whose command line does not contain `dory_v2_runner` would not have been counted.

## Gaps the test found

- `LATEST.md` at `a28374a` said the candidate was uncommitted and unpublished.
- The Founder register still listed publication as an open question.
- The DORY checkpoint's next-task sentence still said to publish the candidate. That sentence is left in place because it was true when that checkpoint was written.
- `CURRENT-CHECKPOINT.md` and `LATEST.md` also exist on `atlas/planning` with different contents.

This file records the test. The pointer updates in this reconciliation are the correction. They are not a rewrite of the 2026-11-20 checkpoints.
