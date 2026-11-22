# Atlas / DORY / Donum — Founder-aligned engineering continuity and improvement plan

**Recorded:** 2026-11-22 (session review)  
**Status:** Founder-approved architectural direction and workflow priorities; **not** execution authority.  
**Location:** `eejonathangomez/DonumDei-Atlas`, branch `atlas/planning`.  
**Authority:** This is a continuity and decision record, not a READY envelope, runner command, approved product roadmap version, or permission to mutate control/product repositories.

## 1. Executive handoff — read this first

**Immediate blocker:** DORY production remains STOP asserted. Sequence **634 BLOCKED** has consistent committed STATE and RESULT, but sequence **635 was not published**. The latest activation campaign stopped correctly because the terminal-acknowledgement writer refuses acknowledging sequence 634 when `last_completed_sequence=632`, despite sequence 633 already being acknowledged and `closed_through=633`. This is an **acknowledgement/progression contract defect**, not a watchdog defect. **Do not clear STOP.**

**Exact next recommended engineering task:** qualify a minimal progression correction for terminal BLOCKED sequence 634 that preserves last completed 632 and the sequence 633 acknowledgement; reproduce the refusal and test gaps/duplicates/idempotence; prepare a safe, bounded publication proposal. **Separate explicit Founder authorization is required before production correction/publication.** After successful progression reconciliation, qualify STOP release and one supervised read-only sequence 635 under an appropriate new authorization; then verify accepted COMPLETE and checkpoint.

**Important distinction:** the earlier Founder approval of `DORY-SUPERVISED-ACTIVATION-EVIDENCE-CHECKPOINT-V1` was explicitly given in chat (Founder: “Yes I sent :)”), but the Cursor task text still contained `Authorization: PROPOSED — AWAIT FOUNDER APPROVAL`. Cursor interpreted that literal field as withholding STOP-release authority. The campaign also found a real independent progression defect. Future execution contracts must reflect actual approval unambiguously, while respecting technical gates; a reported approval must not be silently promoted to a mailbox authorization.

**Confirmed public repository evidence at documentation time:** control `main` `v2/STATE.json` is sequence 634, DORY/BLOCKED, last completed 632; `v2/RESULT.md` is sequence 634 BLOCKED, verdict `POST_EXECUTION_BLOCKED`; watchdog blob `d332945946ad76267b245b146238628e4a36f91c`. **Live STOP/runner/process status below is Cursor-reported, not independently inspected by Atlas.**

## 2. Non-negotiable architecture, roles and safety

Founder → **Atlas** (independent architect / partner in execution) → **DORY** (orchestrator) → **Cursor** (execution arm) → DORY → Atlas/Founder. Atlas is **not DORY**. Founder chooses outcomes and approves consequential authority boundaries; Atlas challenges assumptions, selects the simplest effective approach, prepares bounded tasks, verifies independent evidence and maintains continuity; DORY coordinates within authorized scope; Cursor performs implementation.

- STOP, SYNC_STOP, AUTO-READY NO, runner lock/ownership, atomic mailbox publication, explicit allowlisted paths, protected WIP and broker restrictions remain authoritative.
- Never treat worker RESULT COMPLETE, intermediate STATE COMPLETE, or an isolated test PASS as DORY-accepted COMPLETE. Acceptance requires the exact runner acceptance record, health/audit gates and confirmed published terminal state.
- No broker calls/orders or Donum/Family product mutations without explicit separate authority.
- Preserve existing dirty/untracked work. The three known telemetry modifications may be ignored by the sync classifier (`UNTRACKED_ONLY`); raw status labels are not the same as active SYNC_STOP.
- No force push, destructive reset/clean, improvised mailbox write, STOP release, runner restart or general AUTO-READY merely because this plan exists.
- Current planning roadmap's approved master version is `NONE`; this Founder-approved *operating direction* does not silently approve a master product roadmap.

## 3. Latest execution evidence and chronology

### Recovery and control plane

1. Sequence **633** previously produced worker COMPLETE but runner refused acceptance after watchdog STOP. It was reconciled as terminal BLOCKED; historical worker evidence retained, and acknowledgement of 633 recorded.
2. Sequence **634** supervised read-only smoke exposed watchdog false `DUPLICATE_WORKER`: one runner-owned `cursor-agent.ps1` launch and its children were counted as separate workers. STOP asserted; runner correctly refused COMPLETE. Worker evidence preserved. Local BLOCKED adapter commit was initially unpublished.
3. Isolated ownership correction reused the runner's single-spawn-root semantics; watchdog qualification **116 PASS**, spawn-adapter **86 PASS**; process-tree checks included live CIM observations and two independent launches.
4. Sequence 634 BLOCKED adapter commit `aae7f393c8d8997de15c0d0c8b2bfef5101e153b` published safely. Isolated RESULT-only repair commit `1bdd14d78ee54d2c9031361fb4a066b1df0ed13e` and watchdog candidate `c478e31950662698e7cf4bb61862c83246060933` qualified, then both non-force fast-forward published under Founder-approved bounded reconciliation. Committed STATE/RESULT now agree on sequence 634 BLOCKED; preserved worker COMPLETE remains historical.
5. `DORY-SUPERVISED-ACTIVATION-EVIDENCE-CHECKPOINT-V1` ended **BLOCKED** at Gate B; no STOP release, no watchdog arming, no READY publication, no sequence 635, no checkpoint publication, no context-engineering implementation.

### Exact most recent runtime report (Cursor-reported, not independently verified by Atlas)

- Control local, origin and GitHub main `c478e31950662698e7cf4bb61862c83246060933` (Cursor); control GitHub STATE/RESULT independently read as 634 BLOCKED.
- STOP canonical bytes `53-54-4F-50-0A`; runner PID **5924** alive and unique; latest log `NO-OP: STOP asserted` at 2026-11-22T07:25:49.565-08:00.
- No active worker/watchdog; corrected watchdog installed, inactive, SHA-256 `5DD1FB6DBF5EDF8056BA26FCF10937B9635D2AEBA6A060D52C50ED27DC797B43`.
- STATE 634 BLOCKED; RESULT 634 BLOCKED; `last_completed_sequence=632`; READY absent; TASK still 634.
- Worker COMPLETE preserved at `v2/audit/preserved/sequence-634-20261122T084911725Z.md`, SHA-256 `AA7C10798E834B4E65985D5E8B2AF122588027B71D97EEB5683D06F17E460EE0`. Audit SHA-256 `ECADA46F833CB3A6E02D08383EE6EBBD45FD17BFF1D0729663B71B7EF2C4E4C2`, verdict `POST_EXECUTION_BLOCKED`.
- `Get-DoryGitTreeSyncClass` reports `UNTRACKED_ONLY` despite three pre-existing modified telemetry files; not active SYNC_STOP.
- Donum protected WIP **12/12 unchanged**, HEAD `4dcf67d8cf2bd3fd498622a1e29173c8c027a968`; Family clean HEAD `63e2993661e5d45456c5e4af8c88d1a174c58da2`; broker actions 0.
- Previous watchdog and spawn-adapter qualifications 116/86 PASS, not rerun in latest activation campaign.

### Exact progression defect

`Get-DoryMailboxProgression` returned `ok=True idle=False acknowledged=False closed_through=633 reason=NONE`; acknowledgement records include 542, 554, 610, 633 but **not 634**. In a private fixture with STOP CLEAR, `Add-DoryTerminalAcknowledgement` returned `ok=False reason=ACK_SKIPS_SEQUENCE sequence=634`. Writer requires disk sequence = `last_completed_sequence + 1` (=633), ignoring `closed_through=633`. Terminal BLOCKED 634 must be acknowledged without changing the last **accepted COMPLETE** sequence 632. Publishing 635 before that is blocked by mailbox idle rules. This is the next root-cause/contract target.

### Manual results and Atlas planning freshness

- Independently inspect `eejonathangomez/dory-loop-control` branch `atlas/manual-results`, especially `atlas/manual-results/LATEST.md`, on every handoff. Last observed branch tip `f14a96c69f93ce8a8998fd6e0b23fccba55d0f23`, dated Nov 8, describing `DORY-MANUAL-RESULT-BYTE-INTEGRITY-CORRECTION-V1` and stamping old control HEAD `c900e103...`. It is **historical**, not the latest sequence 634/635 runtime.
- Existing Atlas `docs/CURRENT-CHECKPOINT.md` and `reports/engineering-continuity/LATEST.md` predate this campaign (Nov 15 and sequence 630). They are historical snapshots, not the live status. Read them for context; reconcile against GitHub and runtime.
- The current session record should be used as the *latest planning handoff*, but cannot replace a fresh read of runtime, GitHub, or manual-results evidence.

## 4. Founder-approved target: Evidence-First Context Engineering

Founder approved adoption of **Evidence-First Retrieval, Context Engineering, and Production-Grade RAG Principles** as the target daily operating standard, **not** blanket authorization for implementation or production mutations. RAG = Retrieval-Augmented Generation, but the objective is broader than a vector-search product.

Cycle: **RETRIEVE → VALIDATE → PRIORITIZE → REASON → EXECUTE → VERIFY → DOCUMENT**.

- Pre-retrieval: task, repositories, current requirements, authoritative branches/commits, expected evidence.
- Retrieval: current docs, decisions, checkpoints, manual results, committed execution and live runtime evidence.
- Post-retrieval: remove irrelevant, superseded, contradictory and unverified claims; mark gaps.
- Ranking: source authority, task relevance, freshness, independent verification and safety; ranking never overrides authorization.
- Context composition: concise, traceable manifest of VERIFIED / REPORTED / HISTORICAL / CONFLICT / UNKNOWN facts, decisions, proposals, scope and next action.
- Orchestration: existing Atlas → DORY → Cursor; no second orchestrator.
- Verification: independently reconcile reports with commits, tests, runtime and safety.
- Continuity: update approved existing checkpoint, decision and report paths.

Explicitly distinguish **FACTS** (source-grounded), **DECISIONS** (Founder authorization with scope), and **PROPOSALS** (not authority). Source citation should include repo, branch, commit, path, observation time and verification class. Runtime observations govern runtime claims; GitHub commits govern published repo claims; historical docs cannot override newer verified facts; unknown stays unknown.

Do **not** automatically introduce embeddings, vector DBs, fine-tuning, new agent frameworks, parallel checkpoints or duplicate stores. Start with existing GitHub/Markdown/handshakes/skills and deterministic validators. Add technology only for measured deficits.

## 5. Founder-approved prompting and workflow standards

Aim for production-grade **verified engineering throughput**, not prompt length or computer utilization. Every meaningful task follows the **Atlas Task Contract**:

1. Objective and measurable outcome.
2. Starting evidence and provenance.
3. Explicit authorization / exact scope / allowed paths.
4. Constraints, safety and protected work.
5. Acceptance tests and independent completion evidence.
6. Worker autonomy within scope; no micromanagement.
7. Fail-closed stop/escalation conditions.
8. Evidence-rich handoff and documentation.

Use **Small / Standard / Campaign** prompt sizes proportional to complexity and risk. Prefer one bounded multi-gate campaign over repeated approval requests for routine decisions. Approval for an outcome does not authorize arbitrary means; approvals must be reflected accurately in the executable task, not left as contradictory `PROPOSED` labels. Avoid huge prompts when a short contract suffices.

Measure: verified tasks completed per engineering hour, authorization-to-acceptance elapsed time, Founder interventions, retries/failures, stale-context incidents, recovery time, prompt/context size and retrieval overhead. Reuse regression lessons from real failures. One worker launch and its children are one worker; never count child processes as duplicates.

## 6. Founder-approved improvement investment principle

**Optimize the productivity of the entire engineering system, not just individual task speed.** Significant infrastructure/process improvements may be prioritized **before** Donum product features when the **risk-adjusted expected gain** exceeds implementation, qualification, integration and opportunity costs. Do not categorically postpone all enhancements until product work.

Founder's illustrative example: improving workflow efficiency from 50% to 90% could justify substantial up-front work. These are **hypothetical figures**, not measured DORY efficiency. Example for 100 hours of productive work: 200 elapsed hours at 50%; ~111 at 90%; plus 20 hours improvement cost = ~131, potentially ~69 saved. Evaluate actual baseline, frequency of pain, plausible impact, confidence, cost, safety risk, payback and reversible rollout. Higher machine utilization alone is not success.

Priority candidates to evaluate: stale-context prevention, fewer redundant Founder handoffs, reliable autonomous task completion, deterministic evidence reconciliation, recovery/progression contract hardening, compact prompts, context assembly. Vector DB is deferred absent demonstrated need.

**Sequencing decision:** finish the already authorized activation/progression safety path; establish a verified checkpoint; then assess and implement high-ROI workflow improvements before resuming full Donum feature development **if evidence supports it**. Avoid unbounded process projects. Maintain the right to reorder if new evidence shows a large near-term benefit.

## 7. Proposed phases and approval boundaries

### Phase 0 — current critical path: safe DORY activation

**Next:** bounded isolated progression correction for terminal 634 BLOCKED, preserving last completed 632, acknowledgements and STOP. Regression for 633→634, multiple consecutive BLOCKED/FAILED, idempotent ack, skips, duplicate ack, rollback/fail-closed, no false COMPLETE. Confirm writer/reader agreement on `closed_through`. Present exact minimal patch and test results. **No production mutation without separate Founder approval.**

Then under qualified separate authority: install/publish correction safely; acknowledge 634; arm corrected watchdog **before** READY; release STOP only through qualified procedure; publish one read-only 635 via atomic publisher; verify runner acceptance log + published terminal STATE/RESULT, health and audit; no automatic retry; no broker or product writes. Checkpoint after acceptance.

### Phase 1 — evidence-first context contract (read-only proposal first)

Inspect existing canonical handshake, skills, `docs/CURRENT-CHECKPOINT.md`, `reports/engineering-continuity/LATEST.md`, `docs/decisions/FOUNDER-DECISION-REGISTER.md`, `docs/CURRENT-OPERATING-ROADMAP.md`, and DORY operating model. Define minimal source authority, manifest schema, freshness/conflict handling, deterministic fixtures and precise edit plan. Avoid new service.

Acceptance: stale checkpoint cannot override fresh control; every critical claim has provenance; conflicts explicit; missing source UNKNOWN; manual-results inspected; session recovery repeatable; retrieved text cannot grant STOP release or READY; compare context/latency overhead against baseline.

### Phase 2 — prompt/workflow baseline and prioritized enhancements

Read-only audit representative past DORY campaigns. Identify top recurring inefficiencies; measure time, retries, interventions and errors. Rank improvements by risk-adjusted payoff. Propose smallest coherent batches with tests and rollback. Implement approved high-ROI batches **before** full Donum work if justified. Keep the existing Founder → Atlas → DORY → Cursor loop.

### Phase 3 — resume Donum with improved loop

Recover current Donum architecture/roadmap, reconcile protected WIP and authorized milestone. Resume product tasks with evidence-first task contract, bounded autonomy, independent acceptance and continuity updates. Family Kanban is already an online beta; preserve its deployment and separate product priorities. No broker action unless explicitly authorized.

## 8. Session-start and session-close protocol

**Startup:** (a) read this plan, Atlas checkpoint and continuity index; (b) inspect control main STATE/RESULT/READY, remote HEAD and safety constraints; (c) inspect `atlas/manual-results/LATEST.md` on the correct branch, validate provenance; (d) request live runtime observations for STOP, runner, SYNC_STOP, workers, telemetry classification and protected WIP; (e) reconcile contradictions; (f) list active Founder decisions, current authorization, blocker and exact next task. Never confuse historical reports with current state.

**Closeout:** record verified control/product HEADs, sequence and accepted status, tests, safety state, preserved WIP, provenance, new defects and lessons, approved decisions, proposed next task and outstanding unknowns. Update the **existing** canonical records through an authorized docs-only route; do not make a second authority system.

**Nightly engineering brief:** use same source hierarchy, not a parallel report truth. Report verified changes, STOP/runner state, risks, dependencies, stale evidence and smallest next authorized work. Avoid repeating an old checkpoint as fresh.

## 9. Decisions vs outstanding authorizations

**Approved direction:** evidence-first context engineering; production-grade prompting/task contracts; bounded worker autonomy; evidence-driven ROI prioritization; substantial workflow improvements before product work when justified; preserving safety/roles.

**Previously approved and executed:** two-commit sequence 634 reconciliation; the activation campaign was sent with Founder agreement, but failed closed before STOP release.

**NOT approved by this document:** production acknowledgement writer change, STOP release, new 635 publication, general AUTO-READY, broker activity, product edits, new RAG infrastructure, automatic implementation of context engineering, or changing master roadmap version from NONE.

**Outstanding:** qualify sequence 634 terminal acknowledgement correction; separately approve production correction; then re-authorize qualified 635 supervised activation; verify checkpoint; plan/approve evidence-first integration; benchmark workflow; prioritize improvements; resume Donum.

## 10. Next-session handoff phrase

“Atlas, handshake. Read `eejonathangomez/DonumDei-Atlas` branch `atlas/planning`, file `planning/ATLAS-DORY-EVIDENCE-FIRST-ENGINEERING-CONTINUITY-2026-11-22.md`. Reconcile fresh `eejonathangomez/dory-loop-control` main STATE/RESULT, `atlas/manual-results/LATEST.md` on `atlas/manual-results`, and live runtime evidence. Sequence 634 is BLOCKED; last completed 632; STOP was asserted in the latest report; sequence 635 not published. The next proposed task is an isolated terminal-acknowledgement progression correction. Preserve all safety controls and the approved evidence-first/prompting/ROI plan. Do not execute without separate authority.”

## 11. Founder-approved architecture review: PLAN → FOCUS → EXECUTE → REVIEW (2026-11-22)

**Decision:** Founder agreed with Atlas's independent AI-systems architectural review. Adopt **PLAN → FOCUS → EXECUTE → REVIEW** as the *target operating model*, while **reusing and qualifying DORY's existing machinery**, rather than building another orchestration engine or granting broader permissions now. This is approved strategy and documentation, **not** permission to activate a campaign.

### North star and focus guardrail

The engineering platform exists to accelerate **verified product delivery**, not to become an endless infrastructure project. Allow substantial workflow investment when expected, risk-adjusted return exceeds implementation and qualification cost. Keep a single active Focus with bounded tasks, permissions, budgets, success criteria and explicit return to Donum product work. A discovered unrelated enhancement is backlog, not automatically the next task.

- **PLAN (Founder + Atlas):** evidence-first review; define product/engineering outcome, dependencies, expected ROI, constraints and candidate tasks.
- **FOCUS (Founder approval):** approve a **versioned, finite campaign contract**—specific project/branch, task permissions and exact allowed paths, dependencies, task/attempt limits, acceptance predicates, stop/escalation conditions, return condition. Focus is a logical contract *represented within existing Atlas and DORY policy*; not a new queue, agent, approval server or publisher.
- **EXECUTE (DORY + Cursor):** DORY selects and publishes each eligible task via the existing canonical atomic publisher; Cursor implements and tests within approved limits; DORY verifies terminal acceptance, checkpoints progress, learns and can select the next authorized task only after predecessor gates pass.
- **REVIEW (Atlas + Founder):** independently reconcile control GitHub, runtime, preserved evidence, manual-results, safety and product WIP; declare COMPLETE / BLOCKED / BUDGET_EXHAUSTED / SUPERSEDED, and decide whether to authorize another Focus.

**Autonomy rule:** One Founder approval can bound multiple tasks; it is not unlimited delegated authority. Routine AGREE/IMPROVE choices within the unchanged scope do not require repeated Founder approval. Material authority, scope, financial exposure, safety or mission changes always require escalation. No campaign may spawn another campaign by itself.

### As-built architecture findings (control main observed at `c478e31950662698e7cf4bb61862c83246060933`)

| Capability | Evidence / existing home | Assessment |
| --- | --- | --- |
| Canonical atomic TASK+READY publication | `v2/DoryAtomicMailbox.ps1`; `Publish-DoryAtomicReadyMailbox` | Existing; retain |
| Campaign selection and bounded continuation | `v2/DoryCampaignContinuation.ps1` | Existing; inspect and qualify for new use case |
| Campaign policy | `v2/campaign-continuation.json`: `COMMISSIONED`, `publish_enabled=false`, `bounded_campaign=true`, `max_complete_tasks=15` | Existing, disarmed; **not** authority or proof of ready deployment |
| Durable progress | `v2/campaign-progress.json` logic and publication function | Existing; test crash/restart/idempotence |
| Candidate permissions and allowlist | bounded policy, publisher, allowed-path checks | Existing application controls; retain |
| Runner health/audit/supervised acceptance | runner, post-exec health/audit and corrected watchdog | Implemented; accepted new smoke not yet established |
| Multi-task distinct dependencies and unattended completion | selected/candidate continuation mechanism | **Not yet independently qualified** for proposed general engineering Focus |
| Evidence-first knowledge and prompt recovery | Atlas plan, handshake, Cursor skill | Target direction documented; runtime integration/overhead not qualified |
| OS-level isolation of real Cursor worker | `docs/DORY-OPERATING-MODEL.md` explicitly says not proven | **Security qualification gap** before broad unattended mutations |

**Important implementation fact:** At this revision `Test-DoryBoundedCampaignContract` requires `max_complete_tasks` to equal **15**, not an arbitrary Founder-selected bound; the current policy has **one** chart-cancellation candidate and prohibits broker activity. Do not mistake a one-candidate disarmed policy for a proven general multi-task workflow. Historical sequences **455–502** reportedly exercised 48 continuation cycles for **one task shape**, which supports the existence of continuation, **not** 48 independent software deliverables. Verify historical evidence before using it as a fresh operational qualification.

**Defect finding:** DORY's `Add-DoryTerminalAcknowledgement` and `Get-DoryMailboxProgression` both contain sequencing assumptions tied to `last_completed_sequence`; fixing only the writer could leave reader/writer inconsistency. Correct a **single terminal closure invariant** while preserving the distinction between last successfully accepted COMPLETE and last terminally acknowledged BLOCKED. Test consecutive terminal failures, idempotence, corrupt/missing audit, gaps, published parent sequencing and proper refusal. This remains the next critical-path work, not an excuse to redesign all of DORY.

### Agreed architectural decisions

**GO:** Adopt PLAN → FOCUS → EXECUTE → REVIEW as the target; integrate evidence-first retrieval and Atlas Task Contract; measure verified throughput rather than runner utilization or prompt size.

**MODIFY/REUSE:** Reuse DORY's campaign policy, selector, ledger, publisher, runner, STOP and learning systems. Qualify normal software-engineering tasks and *then* make minimal compatible improvements if needed (including configurable task-budget validation when justified).

**NO-GO now:** General unattended mutating campaigns, automatic STOP release, permissive credentials, any broker/LIVE authority, a second orchestrator, new agent network, vector database/fine-tuning without proven need, or unbounded self-improvement loops. `allowed_paths` is an application authorization check, not an OS security sandbox. Broader unattended worker execution requires evidence for isolation/scoped credentials/mutation controls and a qualified rollout.

### Updated implementation stages and exit contracts

**Stage 0 — restore supervised execution (critical path).** Qualify the existing isolated `DORY-TERMINAL-ACK-PROGRESSION-CORRECTION-V1` task and its full progression invariant; separately authorize production correction, acknowledge 634, qualify STOP release, arm watchdog, publish one supervised read-only 635, verify accepted COMPLETE. **No permission implied here.** Exit: accepted, independently corroborated terminal sequence and safe checkpoint.

**Stage 1 — focused as-built gap audit.** Inspect selector, ledger, policy schema, task publication, auth, terminal recovery, restart/replay, tests and realistic worker isolation. Produce reuse / modify / defer and minimal gap list. Avoid a broad redesign. Exit: prioritized validated gaps and proposed bounded changes.

**Stage 2 — small synthetic multi-task Focus.** Qualify at least two **distinct** dependent engineering tasks in isolated non-broker fixtures, with exact approval envelope, normal completion, retry ceiling, duplicate/reconnect/restart safety, partial completion, out-of-scope refusal, budget-exhausted stop and authoritative evidence. Exit: repeatable verified campaign completion with no unauthorized publication/mutation.

**Stage 3 — evidence-first context and prompt quality.** Minimal source manifest (repo/path/branch/commit/time/verification class), fresh versus stale comparison, manual-results and checkpoint retrieval, conflict UNKNOWN behavior, compact Atlas Task Contract, session handoff, nightly report. Measure context retrieval overhead and errors; do not add technology by default. Exit: repeatable fresh recovery and measurable quality/efficiency improvement.

**Stage 4 — measured engineering Focus.** Establish baseline (successful tasks per hour, Founder interventions, retry/recovery time, context incidents, wasted calls); test a real authorized low-risk campaign and compare under equivalent safety requirements. Exit: improvement demonstrated or explicitly deferred with lessons.

**Stage 5 — Donum product delivery.** Reconcile product architecture/WIP and approved product milestone. Use bounded Focus campaigns; avoid further infrastructure work unless a new substantial expected return is justified. Exit: repeated independently verified product outcomes.

Stages are an **architectural roadmap**, not automatically authorized execution tasks; sequence may be reordered when credible evidence shows a higher-return, equally safe investment. Prioritize correcting 634 right now.

### Focus drift and completion contract

For each Focus define: problem/baseline, outcome and acceptance, budget/attempt limit, allowed repos/paths/actions, required predecessor gates, exact stop conditions, rollback/safe point, and return-to-product condition. Execution ends on **COMPLETE**, **BLOCKED**, **BUDGET_EXHAUSTED**, or **SUPERSEDED**. A task failing acceptance triggers bounded diagnosis or escalation, **not** permission for unlimited additional tasks. Related safety prerequisites must be resolved before advancing; unrelated discoveries go to the existing backlog. Only the Founder can approve a materially new campaign.

**Atlas handshake retrieval:** `Atlas, Handshake` already auto-loads this existing plan, decision register and evidence index. Because this update is incorporated **in place** at the same path, no additional handshake, reminder phrase, branch, or file is required. Always re-read current evidence: this section's code observations are dated, not live runtime proof.

**Decision provenance:** Founder explicitly accepted the prior PLAN → FOCUS → EXECUTE → REVIEW proposal, then requested an independent architecture review, then approved updating that reviewed plan in this repo. This record is documentation-only; no control-plane or product changes are authorized.

## 12. Founder-approved living prompt-engineering knowledge base and Atlas leadership (2026-11-22)

**Decision:** Integrate a living, versioned Prompt Engineering Knowledge Base into **existing Atlas architecture**; let Atlas compose effective, task-specific Cursor requests from concise reusable recipes, fresh evidence and the approved Atlas Task Contract. [Canonical knowledge base](../docs/prompt-engineering/ATLAS-PROMPT-ENGINEERING-KNOWLEDGE-BASE.md) provides a small initial catalog (RCA, IMPLEMENT, REVIEW, QUALIFY, RECOVER, CAMPAIGN, DOC), evaluation and promotion rules, permission checks and a standing expert-leadership reminder. It is retrieved through the **existing Atlas handshake / manifest / Cursor reminder skill**, not through a new phrase or separate service.

**Leadership interpretation:** Founder asks Atlas to behave as a world-class AI systems architect with co-founder-level ownership, decisiveness, independent challenge, creativity and full-trust stewardship; Atlas should strive for excellent outcomes and make efficient use of ChatGPT, Cursor and DORY. This is **not** a literal claim of unrivaled expertise, Founder impersonation, unlimited clearance, all-green-light execution authorization, or permission to bypass STOP, READY, broker restrictions, allowed paths or task limits. The Founder remains ultimate authority. High trust authorizes confident *judgment within actual scope*, not blanket operations.

**First proposed implementation Focus (not yet authorized):** inspect existing skills/rules/tasks; evaluate concise recipe selection versus baseline on representative historical cases; verify objective/evidence/authority/paths/tests/stop/handoff completeness; measure token/context cost, task acceptance rate and Founder interruptions; adopt only proven improvements. Start with GitHub Markdown and existing skills; no vector database, new agent, prompt server or automated repo mutation without separate approval. After current sequence 634 progression and supervised activation, prioritize based on measurable expected ROI and anti-drift exit criteria.


---
**Document provenance:** synthesized from the current Founder–Atlas session and the latest Cursor reports; GitHub control STATE/RESULT and manual-results content were separately retrieved. Local runtime details are explicitly Cursor-reported. This record may become stale and must be revalidated before action.
