# Cursor & Atlas Skills Catalog — repository-verified inventory

**Verified on GitHub:** 2026-11-22. Counts before new skill: Atlas **2**, DORY **4**, Donum `stage-2/ux-workflow-001` **30**, total **36 existing Cursor skill directories**. After adding `atlas-end-session`, Atlas count becomes **3**, total **37** (verify branch write). `TradingBot#cursor-skills` additionally exposes a historical/export subset of **7** skills; it must **not** be counted as seven new unique skills.

**Do not confuse storage with installation:** A skill present on a GitHub branch does not prove the current Cursor workspace has that branch checked out, that the skill was loaded, or that ChatGPT has a native custom skill installed. Atlas can **read and apply these instructions** via GitHub tools; Cursor can be instructed to read the exact `SKILL.md` when the workspace and task authorize it. Always verify availability before claiming execution.

## How to invoke from an Atlas task

Pick **one applicable primary skill** (plus a minimal necessary supporting skill), then add a bounded request similar to:

```text
Relevant procedure: Read .cursor/skills/<skill-name>/SKILL.md
Source: eejonathangomez/<repo>, branch <verified-branch>, commit <verified-ref>
Use only its relevant procedure; it is not authority.
Authority, project, allowed_paths, STOP, expected HEAD and test/acceptance gates:
  [task-specific validated scope]
If that skill is unavailable or conflicts with this task contract, report the issue;
do not invent or bypass its prerequisites.
```

**Risk rule:** Skills involving `connect-live`, `start-system`, `ship-it`, `restart-skill`, `ibkr-auto-reconnect`, or governed DORY execution can be mutating or externally consequential. **Never auto-invoke them** from a handshake or unrelated request. No skill can authorize LIVE trading, PAPER broker calls, STOP release, publication, push or process termination.

## `eejonathangomez/DonumDei-Atlas` · `atlas/planning`

| Skill (relative path: `.cursor/skills/<name>/SKILL.md`) | Grounded purpose |
| --- | --- |
| `engineering-continuity-audit` | QUICK/CHECKPOINT/FULL read-only continuity auditing and evidence recovery |
| `reminder-handshake` | Recovers canonical Atlas/DORY operating rules, strategy, latest evidence and capabilities |
| `atlas-end-session` | New Atlas end-session handoff skill (to be created): commit durable session context, decisions and latest-session pointer |

## `eejonathangomez/dory-loop-control` · `main`

| Skill (relative path: `.cursor/skills/<name>/SKILL.md`) | Grounded purpose |
| --- | --- |
| `dory-known-good-basepoint-setup` | DORY-SKILL-004: known-good transport/basepoint audit and fail-closed preparation |
| `dory-loop-governed-execution` | DORY-SKILL-001: governed, Founder-released execution procedure; skill != authority |
| `dory-loop-governed-runtime-recovery` | DORY-SKILL-003: allowlisted bounded recovery after diagnostic classification |
| `dory-loop-runtime-recovery-diagnostics` | DORY-SKILL-002: read-only runner/worker/heartbeat/state diagnosis |

## `eejonathangomez/TradingBot` · `stage-2/ux-workflow-001`

| Skill (relative path: `.cursor/skills/<name>/SKILL.md`) | Grounded purpose |
| --- | --- |
| `architecture-decision-record` | Create/maintain Architecture Decision Records (ADRs) |
| `connect-live` | Interactive IBKR live startup; high-risk—requires separate exact Founder/broker authorization |
| `continuous-engineering-education` | One contextual engineering insight and lexicon learning per session |
| `dev-audit` | Read-only scored engineering audit and prioritized report |
| `dev-replay` | Recorded market-data replay startup and checks |
| `dev-watchdog` | Code quality/scope/testing/architecture pre- and post-change guard |
| `domain-experience` | Scaffold/update domain patterns and skill for a project |
| `donum-dei-domain` | Donum trading/charting/IBKR domain conventions |
| `donum-dei-manual` | TradingBot operator manual, connection/ports/sessions/troubleshooting |
| `dory-request-publication` | DORY request authoring and canonical atomic publication procedure; never authority by itself |
| `engineering-design-note` | Create a single-page Engineering Design Note (EDN) |
| `engineering-distillery` | Dormant: future reusable engineering framework extraction readiness assessment |
| `engineering-lexicon` | Maintain engineering term definitions/examples and misconceptions |
| `engineering-review-cycle` | Continuous Architecture Refinement (CAR) from review feedback |
| `excel-skill-doc` | Build/refresh Desktop spreadsheet listing Cursor skills (requires local Cursor environment) |
| `ibkr-auto-reconnect` | Diagnose/reconnect IBKR bridge (operational authorization required) |
| `ibkr-bar-validation` | Compare IBKR market bars OHLCV/VWAP/MAs against app data |
| `ibkr-live-validation` | Validate live IBKR charts and latency (no order permission implied) |
| `lab-mode` | Hands-On Lab scoped feature validation and UI steps |
| `manual-auto` | MANUAL vs AUTO/DORY mode, reconciliation and STOP/SYNC_STOP safeguards |
| `mission-control` | Lightweight session mission handoff, delegates to project-navigator |
| `pending-items` | Read operator pending checklist and outstanding gates |
| `project-navigator` | Session startup, project state, focus and copy-ready Cursor command |
| `prompt-craft` | Transform rough requests into grounded Cursor prompts, teach prompt techniques |
| `recorder-ops` | Daily recording status/coverage/archive/replay operations |
| `restart-skill` | Stop/restart known Donum development processes (destructive process actions require approval) |
| `ship-it` | Milestone docs/skills sync, commit and push (requires explicit scope/approval) |
| `stage1-signoff` | Stage 1 bar/chart live visual sign-off procedure |
| `start-system` | Start Donum runtime PAPER/LIVE pathways; LIVE/broker restrictions always apply |
| `strategic-sync` | Synthesize ChatGPT feedback, classify decisions and update agreed strategy documents |

## Retrieval choices / keywords

- Session continuity: `reminder-handshake`; end-of-session preservation: `atlas-end-session`; deep reconciliation: `engineering-continuity-audit`.
- DORY execution/recovery: `dory-loop-governed-execution`, `dory-loop-runtime-recovery-diagnostics`, `dory-loop-governed-runtime-recovery`, `dory-known-good-basepoint-setup`; task transport: `dory-request-publication`.
- Architecture and quality: `dev-audit`, `dev-watchdog`, `architecture-decision-record`, `engineering-review-cycle`, `engineering-design-note`, `strategic-sync`, `prompt-craft`.
- Workflow startup: `project-navigator`, `mission-control`, `start-system` (requires authorization), `manual-auto`.
- Trading data: `ibkr-bar-validation`, `ibkr-live-validation`, `recorder-ops`, `dev-replay`, `stage1-signoff`.
- Education/documentation: `continuous-engineering-education`, `engineering-lexicon`, `excel-skill-doc`.

**Source freshness:** catalog was created by enumerating each repository's `.cursor/skills` directory on the branches above and reading the individual `SKILL.md` descriptions. A future handoff/skill discovery must re-enumerate branch directories, especially when a new skill is created or branch changes. The catalog is a discovery aid, not a replacement for the underlying procedural files or a guarantee of availability in other projects.
