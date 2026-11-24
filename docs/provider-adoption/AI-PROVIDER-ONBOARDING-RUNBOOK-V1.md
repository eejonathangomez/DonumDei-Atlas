# AI Provider Adoption — Reusable Onboarding and Qualification Runbook V1

**Created:** 2026-11-24  
**Status:** Founder-directed documented process; **not authorization to install software, grant account permissions, execute code, onboard a provider into DORY, or change production**.  
**Owner:** Founder; architecture and acceptance steward: Atlas; DORY authority owner: DORY.  
**First application:** [Codex adoption experience, 2026-11-24](CODEX-ADOPTION-EXPERIENCE-2026-11-24.md)  
**Parent architecture:** [AI Organization and Provider Contracts V1](../architecture/AI-ORGANIZATION-AND-PROVIDER-CONTRACTS-V1.md)

## A. Governing idea

We contract **capabilities**, not vendor identities, and fill **organizational positions**, not brand-specific job titles. A provider may supply an LLM, coding agent, test environment, source service or other capability. Keep company-owned role contracts, DORY authority, knowledge, repositories, IP, evidence and recovery portable.

**Adoption has three distinct meanings:** (1) a user has installed and signed in to a tool; (2) the tool has qualified to perform a bounded manual engineering task; (3) the tool has qualified as a DORY-supervised worker. **Never collapse these into one PASS.**

**Source of truth:** product/runner facts require fresh verified evidence; a past session report is historical. A planning document is not DORY publication authority.

## B. Standard evidence labels

- **INDEPENDENTLY VERIFIED:** Atlas or deterministic evidence directly read from GitHub/command outputs (cite origin/time/commit).
- **WORKER-REPORTED:** Codex/Cursor result provided by Founder but not independently executed or verified; capture exact claim and tests.
- **FOUNDER-REPORTED:** Founder-observed UI/auth behavior; not independent verification of security privileges.
- **HISTORICAL:** Previously correct, no longer necessarily current.
- **UNKNOWN:** Evidence unavailable. Do not infer success.
- **PROPOSED / AUTHORIZED / EXECUTED / VERIFIED:** Separate action lifecycle states. Authorization must have bounded scope.

No credentials, OAuth tokens, private environment variables, or secrets in evidence documents.

## C. Minimum onboarding gates (reuse for each provider)

| Gate | Required operation and artifact | Pass condition | Disallowed shortcut |
| --- | --- | --- | --- |
| 0. Need and role | Name role, capabilities, reason to adopt, incumbents, expected benefit and relevant usage/cost limits | Distinct organization role and provider recorded | Calling a new brand a new DORY role |
| 1. Trust and installation | Verify publisher, correct IDE/integration, official documentation/extension identity; record version when obtainable | Tool identity and environment established | Assuming a similarly named extension is official |
| 2. Identity and permissions | Inspect consent scope, authentication method, account/workspace privileges and data exposure; approve least privilege | Founder understands and authorizes scope; no secret copying | Treating GitHub sign-in as blanket Codex/DORY authority |
| 3. Workspace isolation | Choose a disposable or dedicated checkout; ensure it is not production; protect existing WIP and backups | Canonical absolute path, isolation class and target repo known | Opening live DORY/Donum and issuing unrestricted tasks |
| 4. Git/environment preflight | Inspect repo remote, branch, HEAD, upstream, staged/unstaged/untracked status and OS constraints | Exact baseline verified; mismatch stops pending explicit permission | Implicit branch switches, resets, fetches, forced sync |
| 5. Role/authority handshake | Read canonical Atlas/DORY role, handshake, decisions and provider contracts; distinguish stale from current | Provider accurately reports who approves, who orchestrates, what worker may do | Worker claiming DORY acceptance authority |
| 6. Reporting portability | Require one complete copy-ready Markdown report, tests and provenance; choose session/global/repo persistence | Report can be independently reviewed; persistence verified separately | Claiming a conversation preference exists in AGENTS.md |
| 7. Read-only technical qualification | Assigned bounded investigation in approved disposable workspace; compare with authoritative control evidence | Accurate, cited findings with correct stop and uncertainty behavior | Treating dated planning records as current runtime |
| 8. Bounded edit qualification | Separate Founder approval for allowed paths, target and tests; run controlled regression, inspect diff and WIP | Reproducible evidence and exact allowed mutation | Treating read-only pass as implementation permission |
| 9. DORY adapter qualification | Disposable task contract, lifecycle, launch, supervision, cancellation, timeout, evidence and fail-closed tests, including interrupted work | Same harmless test as incumbent; independent accept/reject | Assuming interactive IDE operation proves unattended suitability |
| 10. Security/isolation review | Prove OS/process/workspace and credential boundaries, failure containment and no duplicate side effects | Verified controls or explicit narrower approved risk scope | Equating prompt path restrictions with OS isolation |
| 11. Production commissioning | Separately approved task publication, STOP transition, runner and worker activation following DORY protocols | One independently accepted end-to-end DORY task, complete audit trail | Installation or adapter PASS releasing STOP or AUTO-READY |
| 12. Operate, review, exit | Cost, rate limits, accepted throughput, retries, human intervention, incidents; backup/export/revoke plan | Measured ongoing benefit, reversible provider dependency | Relying on one vendor or silently switching failed work |

**A gate can be NOT STARTED, IN PROGRESS, PASS, PASS WITH CONDITIONS, FAIL, or BLOCKED.** Do not present proposed steps as accomplished. A later gate never retroactively proves an earlier safety gate.

## D. Repeatable adoption record template

For each new vendor/service, create one dated case record:

```markdown
# <Provider> Adoption Experience — <date>
Capability/position:
Provider/product/extension/host:
Purpose and founder approval:
Onboarding owner and operating context:
Current status: Installed | Manual-read-only-qualified | Manual-edit-qualified | DORY-worker-qualified
Scope of current authority:
Costs/quotas/data/secret exposure: VERIFIED | REPORTED | UNKNOWN
Evidence timeline (step | date | action | expected | actual | evidence provenance | status):
Gate table (0–12 with statuses):
Git and runtime baseline(s), time-bound, not hardcoded as protocol:
Stop conditions, safety incidents, escalation and corrective actions:
Outputs and artifacts (commit SHA, file paths, hashes, test logs if available):
Provider-specific adapter differences:
Measured benefit, usage and alternatives:
Open risks and next smallest authorized step:
Rollback/offboarding: revocation, access removal, export, credential rotation, reconciliation
Lessons to apply to the next provider:
```

Link the case record from the architecture and the Founder decision register; do not create a separate master roadmap or duplicate the canonical handshake.

## E. Standard reporting convention for all worker vendors

At task completion return **one fenced, copy-ready Markdown block** with Task ID, RESULT, MODE, AUTHORIZATION and eight sections:

1. Executive Summary
2. Environment
3. Actions Performed
4. Evidence and Test Results
5. Findings
6. Safety and Integrity
7. Recommendation
8. Founder / Atlas Decision Required

Record commands, exit codes, counts, baseline/commit, diff and touched paths, hashes and named evidence locations when relevant. Use VERIFIED / WORKER-REPORTED / HISTORICAL / UNKNOWN accurately. Human-friendly formatting is not an evidence substitute. Report blocked and failed steps honestly. No report-format instruction grants execution permission.

## F. Organizational handoff and stop rules

Founder sets mandate and approves scope → Atlas prepares role/contract and independently reviews → DORY enforces publication and terminal acceptance when a worker is actually integrated → qualified worker executes → independent review. For a manual pilot, Codex is **outside DORY** and Atlas/Founder review the reported result; never call a manual report DORY-accepted COMPLETE.

Safety invariants: existing atomic TASK+STATE publisher, STOP/READY, SYNC_STOP, parent and progression gates, runtime ownership, allowed paths, protected WIP, secrets, product/broker restrictions and independently checked terminal evidence. No provider adoption may bypass them.

If an agent sees unexpected repo/branch, dirty worktree, uncertain permissions, failed qualification, unknown runtime authority or stale contradictory control evidence: **STOP**, preserve bytes, and report. Exception handling requires narrow separate authorization.

## G. Success metrics and review triggers

Measure independently accepted tasks per engineering hour, task turnaround, Founder interventions, retries, unreconciled partial work, cost/usage consumption, unavailable-provider time, security incidents and successful disposable recovery. A second tool from the same underlying vendor is not necessarily independent supplier redundancy.

**Current organization priority:** qualify **one complete supervised read-only DORY task** through the current Cursor path; only then use observed real worker behavior to justify a Codex adapter. The standard operating roadmap remains unratified (`NONE`). This runbook is documentation, not production change authorization.


## H. Provider-neutral continuity and initiative (2026-11-24)

Compare local institutional knowledge against fresh authoritative remote evidence before decisions. A clean fast-forward requires explicit scope and verification; stale local knowledge may instead be read remotely. Recover existing mechanisms before proposing new ones. Specify task-wide mandatory stops and independent workstream gates; only continue independently authorized work, never bypass ambiguous mandatory stops. Distinguish reproduced defects, source-supported hypotheses, environmental blockers and unknowns. Record meaningful results with exact refs, artifact hashes and evidence provenance. A provider-specific instruction or reporting preference must not overwrite another provider's established skills or runtime contract. Existing Cursor usage and production DORY/Cursor integration remain unchanged. No execution authority is granted here.
