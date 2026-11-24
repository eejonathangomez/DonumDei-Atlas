# AI Organization and Provider Contracts — Architecture V1

**Recorded:** 2026-11-24  
**Status:** Founder-aligned target architecture; documented for planning. **NOT an implementation or execution authorization.**  
**Owner:** Founder. **Architectural steward:** Atlas. **Orchestration owner:** DORY.  
**Repository:** `eejonathangomez/DonumDei-Atlas`, `atlas/planning`  
**Authority:** This record cannot authorize READY, STOP release, runner startup, source edits, campaign activation, credentials, broker actions, or a new master roadmap version.

## 1. Purpose

Create a small, capable, vendor-independent AI engineering organization. Define **positions** (accountable responsibilities) separately from **contracted capabilities** (external services) and **providers** (companies/products delivering those services). Preserve DORY, the organization's policies, engineering knowledge, evidence, and intellectual property as our assets. A provider can change without changing who owns a decision or how work is accepted.

We are building an organization whose AI workers fill defined positions—not a loose collection of tool-specific agents.

## 2. Internal organization — positions, not brands

| Position | Accountable responsibility | Current arrangement | Non-delegable boundary |
| --- | --- | --- | --- |
| Founder | Direction, risk appetite, budgets, consequential approvals | Human Founder | Retains final strategic and high-impact authority |
| Atlas / Chief Architect | Systems architecture, evidence-first planning, task contracts, dissent, independent review | ChatGPT-supported role | Does not impersonate DORY or grant execution authority |
| DORY / Operations Control | Atomic task authorization, sequencing, runner supervision, safety gates, evidence, terminal acceptance | DORY control plane | Owns the execution authority boundary, independent of worker vendor |
| Engineering Worker | Implement, debug, test, return bounded deliverables | Cursor currently; Codex potential alternative | Cannot self-authorize, bypass scope, clear STOP, or certify its own acceptance |
| Independent Verification | Deterministic tests, Git/audit evidence, independent qualification | DORY gates and Atlas review; no separate agent required | Worker assertion alone is insufficient |
| Knowledge / Context | Retrieve current requirements, decisions, checkpoints and lessons with provenance | Atlas and existing GitHub/Markdown assets | Historical documents do not override current runtime and Git evidence |

An **LLM is a capability**, not a permanent organizational office. One role may use different LLMs; one supplier may fill multiple roles. Separate agents are justified by measured need, not job-title count.

## 3. Minimum externally supplied capabilities

| Capability contract | Current arrangement / candidates | Replacement requirement |
| --- | --- | --- |
| Reasoning / models | OpenAI/ChatGPT used for Atlas; other LLM suppliers are candidates | Portable instructions, context, decision records and structured outputs |
| Coding-agent execution | Cursor current worker; Codex candidate, NOT qualified as DORY worker | Common task, output, cancellation and evidence contract |
| Source control and CI | GitHub / Git-based repository and testing workflows | Exportable Git history, tests and artifacts |
| Compute and OS runtime | Local Windows host and Hyper-V; hosted compute is an option | Reproducible environment and controlled filesystem/process boundary |
| Identity and secret handling | Existing credential tools including Bitwarden; operating status must be verified | Least privilege, rotation/revocation, provider-scoped credentials |
| Backup and disaster recovery | Restic/Seagate and recovery procedure; independent restore/offsite assurance requires evidence | Portable snapshots, restoration drill and documented recovery ownership |

These are six **capabilities**, not six mandatory subscriptions or confirmed vendor contracts. Each provider entry should later record service owner, subscription/cost, credentials owner (never secrets), data exposure, limits, availability, exit procedure, tested fallback, and verification date.

Commercial operations (product hosting, domain/DNS, customer support, payments, legal/accounting and compliance) form an additional provider catalog **when the product and customer model require them**. No new agent or vendor purchase is authorized by this document.

## 4. Standard Engineering Worker Contract — target interface

The worker adapter receives: task ID and authorized envelope; project/repository and pinned baseline; allowed paths; capability requirements; environmental constraints; time/resource budget; test/acceptance predicates; stop and escalation conditions.

The worker returns: exact source diff and touched paths; test commands, exit codes and logs; provenance and artifact hashes; changed/untracked file status; completion or failure class; interruption/partial-work evidence.

The adapter must support: launch, observe liveness, cancel/terminate, time out, collect evidence, and fail closed on lost ownership. DORY remains responsible for publication, health gates, durable terminal acceptance and progression.

**Provider switch rule:** An alternative worker may be used only after its adapter passes the same task and failure-mode qualification in disposable isolation. A provider failure cannot silently cause a second worker to execute against partially modified work or repeat side effects. Reconcile first, then reauthorize.

**Isolation rule:** Prompt instructions and allowed-path checks are not OS-level isolation. Broader unattended write permission requires a demonstrated isolation boundary or a deliberately narrower approved risk model.

## 5. Durable architectural principles

1. Role contracts and DORY protocols are vendor-neutral; provider-specific commands belong in adapters.
2. One orchestration authority: existing DORY. No second scheduler, shadow mailbox, or autonomous policy engine.
3. Facts, decisions and proposals must remain distinguishable and traceable.
4. Founder authorizes consequential changes; DORY validates execution scope; Atlas independently reviews outcomes.
5. Portable IP, knowledge, tests, audit trails and recovery procedures remain organization-owned.
6. Prefer measured verified engineering throughput to token count or computer utilization.
7. Vendor redundancy is not proven merely by having two products from the same supplier.
8. Do not make production architecture changes to implement this document prematurely.

## 6. Incremental implementation path

| Stage | Next measurable proof | Scope now |
| --- | --- | --- |
| 0 — Record architecture | This document exists on Atlas planning branch | DOCUMENTATION ONLY |
| 1 — Restore one-task DORY loop | One Founder-approved read-only task is atomically published, executed, independently accepted and safely returned; no intervention between publication and acceptance | CURRENT CRITICAL PATH; requires separately qualified/authorized STOP transition and runner start |
| 2 — Baseline existing worker contract | Capture real input/output/process/error evidence from the one-task loop | Read-only specification and characterization |
| 3 — Compare alternative worker | Run same harmless scoped task with Codex or another agent in disposable environment; retain comparable result evidence | Separate approval; no production worker substitution |
| 4 — Vendor-neutral adapter + isolation | Qualify worker contract, termination, failure recovery, path/credential boundaries and reproducibility | Implement only against demonstrated gaps |
| 5 — Small bounded Focus | Demonstrate two distinct tasks, then 3–5, within one finite approved Focus, without relaxing STOP | Future, separately authorized |
| 6 — Resilient provider selection | Qualified provider selection/fallback without duplicate execution or authority expansion | Future |

**Immediate priority is still Stage 1: one end-to-end automated DORY task**, not building adapters, creating new organizational services, changing the master roadmap, or performing an uncontrolled multi-task run.

## 7. Decision status and next review

**Decided as architectural direction:** positions are separated from suppliers; DORY remains the control authority; workers are replaceable behind a qualified contract; isolation and evidence are required; the incremental path above is preferred.

**Not decided:** specific alternative vendor, contracts/pricing, automatic provider switching, implementation changes, production permission expansion, staffing as separate agents, and commercial-company procurement.

**Next review trigger:** after the first qualified one-task automated loop, examine the observed worker interface and decide whether a minimal vendor-neutral contract and Codex disposable pilot have enough measurable value to approve.

**Related existing records:** `docs/EFFICIENCY-LOOP-HANDSHAKE.md`, `docs/decisions/FOUNDER-DECISION-REGISTER.md`, `docs/CURRENT-OPERATING-ROADMAP.md`, `docs/engineering-inventory/ENVIRONMENT-AND-REPOSITORY-MAP.md`. Their existing execution and roadmap authority boundaries remain unchanged.

## 8. Provider adoption lifecycle and learning record (2026-11-24)

**Founder-directed documentation standard:** Record **every meaningful adoption step** for new AI/software providers—identity, installation, permissions, workspace, handshake, constraints, failures, qualifications, provider-switch tests, independent evidence and offboarding—so successive vendors can be evaluated under a common procedure.

- [AI Provider Adoption — Reusable Onboarding and Qualification Runbook V1](../provider-adoption/AI-PROVIDER-ONBOARDING-RUNBOOK-V1.md) — canonical repeatable gates and evidence/reporting requirements.
- [Codex Adoption Experience — 2026-11-24](../provider-adoption/CODEX-ADOPTION-EXPERIENCE-2026-11-24.md) — first living adoption case, installation and safety observations, lessons and outstanding work.

**Separation of states:** editor installed ≠ manual engineering qualification ≠ qualified DORY worker ≠ production activation. No newly recorded step changes STOP, publication authority, the current Cursor production worker or master roadmap status. All future provider adoption should create its own case record rather than overwriting prior experience.
