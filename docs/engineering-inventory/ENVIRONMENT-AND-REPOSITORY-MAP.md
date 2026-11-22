# Atlas Engineering Environment & Repository Inventory

**Recorded:** 2026-11-22. **Scope:** discoverable GitHub repositories and branch names, Founder-reported infrastructure, confirmed source contracts. **Authority:** knowledge/reference only, never READY, STOP release, runner access, broker action, or approval to mutate production.

## How to use this inventory

- On `Atlas, Handshake`: read this index to know available domains, tools, skills, and where current information lives. Return a compact *tool awareness* and environment status, not all branches in the user-visible handshake.
- On `branches`, `where is the work`, `find a branch`, or selecting a workspace: **re-enumerate GitHub remote branches**, inspect relevant branch content and ancestry, verify local tracking/WIP if available, then select based on evidence. Never assume a branch is merged, safe, active or deployable merely because it exists or its name suggests a purpose.
- On `skills` / `what can Cursor do`: read [the Cursor skills catalog](CURSOR-SKILLS-CATALOG.md), then retrieve the exact referenced `SKILL.md` on the correct branch before composing an instruction that invokes it. Skills are *procedures*, not authorization; a file in a repository doesn't prove Cursor loaded it.
- On `status`: freshness of DORY control GitHub and local runtime always outranks this dated index. On `send it`: validate authorization/STOP/progression before using canonical DORY request transport.
- On `Atlas, End Session`: use [Atlas End Session](../skills/atlas-end-session/SKILL.md) to write a dated session handoff, track decisions and preserve newly discovered capabilities; do not append transient statuses here unless explicitly noted as a dated example.

## Repositories and branch inventory (GitHub search verified 2026-11-22)

**Completeness:** branches enumerated via connected GitHub branch search with pagination exhausted; counts and names verified at time of lookup. Descriptions labeled **inferred** are *working navigation hints*, NOT a claim that the source code was reviewed or the branch is current. Remote-only listing does **not** include local-only branches, untracked worktrees or protected dirty files. Check those with an authorized local inspection before operations.

### `eejonathangomez/DonumDei-Atlas` (5 remote branches)

| Branch | Purpose / description |
| --- | --- |
| `atlas/planning` | Founder–Atlas plans, handshake, decisions, continuity; active documentation home (verified by file reads) |
| `docs/ai-engineering-architecture-pointer` | AI engineering architecture pointer / docs (purpose inferred from name) |
| `docs/dory-donum-engineering-continuity-2026-11-20` | DORY/Donum engineering continuity docs, dated Nov 20 (inferred) |
| `docs/historical-dory-capability-2026-11` | Historical DORY capability docs (inferred) |
| `main` | Repository default/base development line; not the current Atlas planning home (branch role from name) |

### `eejonathangomez/dory-loop-control` (16 remote branches)

| Branch | Purpose / description |
| --- | --- |
| `atlas/manual-results` | Separate evidence-only manual Cursor result history (verified via LATEST.md) |
| `atlas-atomic-transport-lab` | Experimental Atlas atomic transport lab (inferred) |
| `atlas-atomic-transport-lab-2` | Second Atlas atomic transport lab (inferred) |
| `atlas-founder/architecture` | Founder/Atlas architecture work (inferred) |
| `docs/atlas-donum-full-map-continuity-20261105` | Atlas/Donum continuity map dated Nov 5 (inferred) |
| `docs/dory-efficiency-loop-v1` | DORY efficiency-loop documentation (inferred) |
| `fix/dory-post-execution-health-gate` | Post-execution health gate fix branch (inferred) |
| `fix/dory-task-permission-prompt-20260822` | Task permission/prompt correction (inferred) |
| `fix/dory-terminal-health-gate-seam` | Terminal/health-gate integration correction (inferred) |
| `main` | Current control mailbox / runner / authority source; last verified 634 BLOCKED at c478e319 (recheck) |
| `maintenance/dory-multi-project-v1-pr` | Multi-project maintenance pull-request preparation (inferred) |
| `maintenance/dory-multi-project-v1-review` | Multi-project maintenance review (inferred) |
| `maintenance/dory-multi-project-v1` | Multi-project maintenance work (inferred) |
| `manual/seq237` | Historical/manual sequence 237 work (inferred) |
| `noop-should-not-use` | Named non-use / test branch; DO NOT SELECT by default (inferred) |
| `simplify/dory-boring-loop-20260822` | DORY simplification work dated Aug 22 (inferred) |

### `eejonathangomez/TradingBot` (7 remote branches)

| Branch | Purpose / description |
| --- | --- |
| `checkpoint/c01-perf006-certified` | Certification/performance checkpoint (inferred) |
| `cursor-skills` | Exported/preserved Cursor skill subset; 7 directories observed |
| `docs/adr-008-ai-engineering-architecture` | Architecture decision record documentation (inferred) |
| `docs/donum-dei-founding-purpose` | Founding-purpose documentation (inferred) |
| `stage-1/phase-1` | Earlier Stage 1 engineering work (inferred) |
| `stage-2/foundation` | Stage 2 foundation development (inferred) |
| `stage-2/ux-workflow-001` | Donum UX product work branch; Cursor skills catalog home, protected WIP reported (verified path) |

### `eejonathangomez/kanban` (5 remote branches)

| Branch | Purpose / description |
| --- | --- |
| `audit/2026-10-baseline` | October baseline audit (inferred) |
| `fix/0.1.5-release-hardening` | v0.1.5 release hardening (inferred) |
| `fix/0.1.5-session-hardening` | v0.1.5 session persistence/hardening (inferred) |
| `main` | Family Kanban deployed-beta product baseline (deployment reported; branch exists verified) |
| `upgrade/dependencies-2026-10` | October dependency upgrades (inferred) |

**Branch-selection policy:** default read targets are `DonumDei-Atlas#atlas/planning` for Atlas institutional knowledge, `dory-loop-control#main` for the control plane, `dory-loop-control#atlas/manual-results` for independent manual results, `TradingBot#stage-2/ux-workflow-001` for the documented Donum UX product work, and `kanban#main` for Family Kanban. **Do not treat these as universal edit targets;** select exact repo/branch/commit for each request, preserve protected WIP, and use bounded Founder-approved edits only.

## Environment / tools and what they are for

| Tool or system | Use / relationship | Verification status and caution |
| --- | --- | --- |
| ChatGPT / Atlas | Architect, analysis, tasks, decisions, continuity, repo-connected GitHub actions | This session's connected GitHub read/write actions verified; tool availability may vary across sessions |
| GitHub | Source control, branch history, canonical control and Atlas planning records | Connected operations verified; per-session permissions and target ref must be checked |
| Cursor Agent / IDE | Executes engineering tasks, PowerShell/python/tests under approved task scope | Existing Cursor `.cursor/skills` catalogs enumerated; local execution is not implied by a ChatGPT response |
| DORY v2 / Windows PowerShell | Runner, canonical atomic mailbox, campaign selector, gated worker, telemetry/audit/reconciliation | As-built control source verified; live Windows runner/process state requires direct local evidence |
| Tailscale | Private network/remote connectivity used in the Founder's environment | **Founder-reported 2026-11-22**; active nodes, network reachability, identity/policy and installed state NOT verified here |
| Bitwarden | Credential/password-vault management in the Founder's environment | **Founder-reported 2026-11-22**; vault/account accessibility NOT verified; never copy secrets or recovery codes to GitHub/task reports |
| Backblaze | Backup/offsite backup ecosystem (Founder called it "Blackblaze") | **Founder-reported 2026-11-22**; destination, subscription, upload status, restore proof and retention NOT verified |
| Restic + Seagate external drive | Local snapshot/restore and recovery comparisons, per historical manual campaign reports | **Historically reported**, including snapshot IDs `0b6d5f6d` and `8c63b6ee`; not proof of current backup health |
| Hyper-V `DORY-Recovery-Test` | Isolated Windows disaster-recovery rehearsal VM (guest `DORY-RECOVERY`) | **Historically reported** offline/no NIC; current VM configuration/availability, containment and restore proof NOT live-verified |
| Windows / PowerShell / Git | Windows host and test tooling for runner, backups, VM/repo maintenance | Local host process state and uncommitted changes NOT accessible solely from GitHub |
| Donum Dei / IBKR | Product trading/broker integrations, replay and paper/live systems | Broker/LIVE/PAPER actions **not authorized** by this registry or a skill; explicit Founder and DORY gates required |
| Family Kanban | Deployed online beta, currently family usage, source/product/recovery | Deployment and local usage **Founder-reported**; live user data/backups require separate verification |

**Disaster-recovery map:** device/VM/network/vault/backup are different layers. A backup file is not a proven recoverable system; a working VM restore is not proof of independent-machine recovery, usable off-host credentials, or Backblaze offsite restoration. Track those separately. NEVER store vault exports, passwords, token values, recovery phrases, API keys or personal data in this inventory.

## Important keywords / retrieval map

| Founder term / keyword | Where Atlas looks first | What it must preserve |
| --- | --- | --- |
| `Atlas, Handshake`, `DORY handshake` | `docs/EFFICIENCY-LOOP-HANDSHAKE.md`, manifest, current Founder plan | Roles, authority, latest plan, status provenance, current Focus and next task |
| `status`, `DORY`, `runner`, `READY`, `STOP`, `SYNC_STOP` | `dory-loop-control#main/v2`, telemetry/audits, manual-results branch | Current GitHub truth versus unverified local processes |
| `send it`, `publish`, `task` | `v2/atlas-publication-request.json` + canonical `Publish-DoryAtomicReadyMailbox` | Request != READY != executing != accepted COMPLETE; safety gates always |
| `PLAN`, `FOCUS`, `EXECUTE`, `REVIEW` | Founder-approved plan, decision register, campaign policy | Versioned finite scope, permissions, exit criteria, anti-drift |
| `skills`, `Cursor`, `prompt-craft`, `dev-watchdog` | `CURSOR-SKILLS-CATALOG.md` and relevant exact repo/branch skill | Match skill to task and validate availability |
| `branches`, `GitHub`, `commit`, `WIP` | GitHub branch enumeration, exact files/commits, local inspection | No guessed branch HEAD, no hidden local WIP loss |
| `Tailscale`, `Bitwarden`, `Backblaze` | This environment map plus current authorized operator verification | Access/restore not assumed; no secrets in GitHub |
| `VM`, `Hyper-V`, `RecoveryAdmin`, `restic`, `Seagate` | Recovery campaign handoff, scripts/runbooks/local VM evidence | Isolated/no NIC status reported, not assumed; staged restore proof |
| `end-session`, `close session`, `Atlas, End Session` | `docs/skills/atlas-end-session/SKILL.md` | Dated durable handoff and verified read-back; no implicit operational mutation |
| `Donum`, `TradingBot` | `TradingBot` current product branch and standards | Protected WIP, broker restrictions, real user-facing product outcomes |
| `Family`, `Kanban` | `kanban#main` and family recovery records | Online beta, storage/export/restore limitations |
| `RAG`, `prompt engineering`, `recipe` | `docs/prompt-engineering/ATLAS-PROMPT-ENGINEERING-KNOWLEDGE-BASE.md` | Evidence-first, task-specific concise recipes; measure benefit |

## Inventory maintenance

This is a **navigation registry**, not live system truth or a separate operating authority. At each meaningful end-session record added or corrected tool definitions, repo purpose, new skills and promoted decisions with source and date. For branch inventories prefer refreshed enumeration and meaningful tips/ancestry only when they affect the action; do not mutate branch refs just to tidy this catalog. Changes to Founder authorization require explicit decision and actual publisher gates, not a registry edit.
