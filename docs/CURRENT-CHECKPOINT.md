# Current checkpoint pointer

This file is a stable pointer. It is not the operational snapshot and it is not execution authority.

The latest accepted engineering checkpoints are named in [reports/engineering-continuity/LATEST.md](../reports/engineering-continuity/LATEST.md).

Before acting, re-read live DORY `v2/STATE.json`, `v2/STOP`, `v2/campaign-continuation.json`, and runner process evidence. A checkpoint date is an observation, not a claim that the runner is still in that state.

As of the continuity candidate authored on 2026-11-20, `LATEST.md` points at:

- `reports/engineering-continuity/2026-11-20/DORY-OPERATIONAL-CHECKPOINT-2026-11-20.md`
- `reports/engineering-continuity/2026-11-20/DONUM-ENGINEERING-CHECKPOINT-2026-11-20.md`

Those files are absent from GitHub `main` (`f46de55a6cb074879c29ce0c2dfc3d4873f97b91`). Branch `atlas/planning` has a different `docs/CURRENT-CHECKPOINT.md`. That file is a 2026-11-15 living checkpoint and is not replaced by this pointer. Do not merge the two branches without resolving the shared filename.
