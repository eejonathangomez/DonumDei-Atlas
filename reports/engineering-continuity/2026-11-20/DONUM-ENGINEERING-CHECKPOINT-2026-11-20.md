# Donum engineering checkpoint — 2026-11-20

**Observation window:** 2026-11-20 evening, America/Los_Angeles.  
**Authority:** none. This checkpoint does not authorize product edits, broker calls, or campaign publication.

## Product architecture and purpose

Donum Dei is a market-understanding platform. `docs/VISION.md` states it is not a generic trading bot. The north star is trader plus platform, with automation as a later result of understanding. Visual truth comes before intelligence or execution.

**Class:** VERIFIED by reading `docs/VISION.md` in the product worktree. The full stage certification state was not re-audited in this session.

Technical requirements live in `AGENT.md`. Usage lives in `docs/USER-MANUAL.md`. Engineering standards live under `docs/engineering-framework/` and `docs/ENGINEERING-STANDARDS/`.

The DORY registry binds this product as `donum-dei`, repository `eejonathangomez/TradingBot`, workspace branch `stage-2/ux-workflow-001`.

## Latest branch and HEAD

| Fact | Value | Class |
|------|-------|-------|
| Local path | `C:\Users\eejon\OneDrive\Desktop\AI_Projects\DonumDei-TradingPlatform-ux-workflow-001` | VERIFIED |
| Branch | `stage-2/ux-workflow-001` | VERIFIED |
| HEAD | `4dcf67d8cf2bd3fd498622a1e29173c8c027a968` | VERIFIED |
| `origin/stage-2/ux-workflow-001` | same SHA | VERIFIED |
| Tracking line | `stage-2/ux-workflow-001...origin/stage-2/ux-workflow-001` with no ahead/behind count | VERIFIED |

## Current development phase

The branch name and the vision document place the work in Stage 2 UX workflow, after the Stage 1 visual-truth requirement. A fresh Stage 1 or Stage 2 certification ceremony was not run on 2026-11-20.

**Class:** REPORTED from branch name and `docs/VISION.md`. Certification completion is UNKNOWN for this session.

## Completed milestones

| Milestone | Class |
|-----------|-------|
| Product repository exists and matches its origin SHA | VERIFIED |
| Stage 1 visual-truth principle is written in the vision | VERIFIED as text |
| Historical DORY sequences completed while this product was the routed project | HISTORICAL. See the DORY capability registry. Not re-certified here |
| Adopted safe point used by prior supervised work | `4dcf67d8cf2bd3fd498622a1e29173c8c027a968`, which is also current HEAD | VERIFIED identity of HEAD. The safe-point adoption decision is HISTORICAL |

## Protected WIP

| Fact | Value | Class |
|------|-------|-------|
| Tracked dirty files | 12 | VERIFIED |
| Untracked paths | 61 | VERIFIED |
| Hash comparison to `C:\Users\eejon\AppData\Local\DORY_Supervised632\donum-tracked-dirty-before.txt` | 0 mismatches | VERIFIED |

Tracked paths, unchanged from that baseline:

- `.cursor/rules/final-response-protocol.mdc`
- `docs/engineering-framework/CURSOR-FINAL-RESPONSE-PROTOCOL.md`
- `frontend/src/components/ManualTradingConsole.safetyUx.test.tsx`
- `frontend/src/components/ManualTradingConsole.test.tsx`
- `frontend/src/components/ManualTradingConsole.tsx`
- `frontend/src/lib/executionInput/noOrderAction.guard.test.ts`
- `frontend/src/lib/manualTradingConsole/index.ts`
- `frontend/src/stores/executionInputStore.ts`
- `frontend/src/stores/manualTradingConsoleStore.ts`
- `reports/seq-222/qualification-matrix.json`
- `reports/seq-455/PAPER-EXTENDED-HOURS.md`
- `scripts/start-system/controlRepoReadiness.test.mjs`

Untracked work includes manual-trading execution context, overnight contract evidence, broker-truth refresh, IBKR bridge overnight and market-data queue files, campaign-03 reports, sequence report directories, and `.worktrees/`. This checkpoint did not modify them.

The protected product thread visible in the dirty tree is manual-trading console and execution-input work. The commissioned DORY campaign candidate is a different thread: chart cancellation marker truth, limited to five `chartOrderMarkers` paths.

## Open defects

| Defect | Class |
|--------|-------|
| Product-integrity gate is not installed, so DORY can still complete an interrupted product sequence after deferred reconciliation | VERIFIED as a DORY defect. Not a Donum source defect |
| Chart-cancel campaign objective is incomplete (`objective_complete` false) and publication is disabled | VERIFIED campaign file |
| Whether the manual-trading WIP itself contains a failing test | UNKNOWN. `npm test` was not run |
| Older control architecture prose describes a different Donum HEAD and porcelain count | HISTORICAL documentation drift |

## Tests and qualifications

No Donum `npm test` was run for this checkpoint. DORY isolated suites were not product tests. Test status of the protected WIP is UNKNOWN.

## Trading and broker safety

| Boundary | Evidence | Class |
|----------|----------|-------|
| LIVE trading prohibited by the commissioned campaign | `runtime.live_prohibited` true | VERIFIED text |
| PAPER orders, cancels, and broker-state changes prohibited by that campaign objective | campaign objective text | VERIFIED text |
| No broker call during this checkpoint | session constraint and absence of broker work | VERIFIED for this session |
| Vision: automation is not the starting point | `docs/VISION.md` | VERIFIED text |
| DORY recovery must not clean this WIP | continuity decision register | VERIFIED as a standing constraint |

## Outstanding recovery work

- Keep the 12 tracked files and 61 untracked paths.
- Do not reset, clean, commit, or push this worktree under the continuity task.
- Re-verify hashes against the supervised baseline before any future product task.
- Decide whether the next authorized product task is the manual-trading WIP or the disarmed chart-cancel candidate. Both cannot be treated as the same task.

## Next proposed product development task

Preserve the worktree. Do not start `DONUM-CHART-CANCEL-TRUTH-V1` while STOP is asserted and `publish_enabled` is false. The proposed next product step, after a separate Founder authorization, is to identify which of the two threads is current: the protected manual-trading console WIP, or the disarmed chart-cancel candidate. Until that choice, no product file should change.

## Family Kanban

Family is a separate deployed product. It was not modified.

| Fact | Value | Class |
|------|-------|-------|
| Local path | `C:\Users\eejon\OneDrive\Desktop\AI_Projects\kanban` | VERIFIED |
| GitHub | `eejonathangomez/kanban` | VERIFIED remote |
| Branch | `main` | VERIFIED |
| HEAD | `63e2993661e5d45456c5e4af8c88d1a174c58da2` | VERIFIED |
| Tracking | `main...origin/main` with no ahead/behind shown | VERIFIED |
| Tracked dirt | none | VERIFIED |
| DORY registry | IDLE and parked | VERIFIED |
| Purpose | Family routine board. Next.js static export. Local-first browser data | VERIFIED from `README.md` |
| Production URL | `https://family.donumdeitech.com` | REPORTED by `README.md`. The URL was not fetched this session |
| Deployment doc | `docs/hosted-browser-release.md` | REPORTED by the README link |

Family's parked bit means DORY will not publish Family campaign work. It does not change the hosted site.
