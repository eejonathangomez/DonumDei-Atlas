# Efficiency Loop Handshake — Authoritative Recovery Protocol

**Founder recovery phrase:** `DORY handshake`

**Compatibility aliases:** `DORY handshake`, `Atlas Handshake`, and `Atlas, handshake`. All three name this one contract. `DORY handshake` remains the primary phrase in the machine manifest.

This document is the one authoritative recovery contract for the Atlas / DORY / Cursor operating model. A fresh ChatGPT (Atlas) or Cursor session must recover from this file plus the machine manifest and **live verification** — not from chat memory. Recovery restores context. It does not grant execution authority.

**Protocol id:** `DORY-EFFICIENCY-LOOP-HANDSHAKE-V1`  
**Authoritative home:** DonumDei-Atlas (`docs/EFFICIENCY-LOOP-HANDSHAKE.md`)  
**Machine manifest:** `handshake/efficiency-loop-handshake.json`  
**Cursor skill:** `.cursor/skills/reminder-handshake/`

---

## STABLE PROTOCOL vs TRANSIENT CURRENT TRUTH

| Class | What belongs here | Rule |
|-------|-------------------|------|
| **STABLE PROTOCOL** | Roles, repos, transport paths, publication invariant, efficiency loop, authority rules, fail-closed behavior, recovery steps | Durable in this document and the handshake manifest |
| **TRANSIENT CURRENT TRUTH** | Runner PID, current sequence, mailbox turn/status, STOP presence, campaign `publish_enabled`, product HEADs, WIP, known-good checkpoints observed today | **Never** bake into permanent protocol. Verify live from the control repo / runtime before acting |

If verified live truth conflicts with this document, **current verified truth wins**. Report the mismatch before any action.

---

## Stable roles (do not conflate)

| Role | Identity | Owns |
|------|----------|------|
| **Founder** | Jonathan | Vision, priorities, boundaries, authorization, final decisions |
| **Atlas** | Architect / Partner in Execution (ChatGPT or equivalent) | Strategy, smallest-complete objectives, knowledge preservation, drafting Atlas remote requests as **data only** |
| **DORY** | Orchestrator / control plane | Sequences, TASK/RESULT/STATE handoffs, idle adoption, fail-closed gates |
| **Cursor** | Execution arm | Cursor implements, diagnoses, tests, and returns evidence under the currently authorized execution/result contract. |

**Never confuse Atlas with DORY.** Atlas is not the mailbox publisher. DORY (via the canonical publisher) is.

Institutional knowledge home: **DonumDei-Atlas**. Continuity archaeology under `DORY_LOOP_CONTROL/atlas/**` is a separate archive — not this home.

---

## Stable repositories and transport

| Concern | Home |
|---------|------|
| Control repo | `eejonathangomez/dory-loop-control` branch `main` (local: `DORY_LOOP_CONTROL`) |
| Live mailbox | `v2/TASK.md`, `v2/RESULT.md`, `v2/STATE.json`, `v2/STOP` |
| Canonical publisher | Function `Publish-DoryAtomicReadyMailbox` in `v2/DoryAtomicMailbox.ps1`; entry `v2/Publish-DoryAtomicMailbox.ps1` |
| Atlas remote request (DATA only) | `v2/atlas-publication-request.json` |
| Request adoption entry | `v2/Invoke-DoryAtlasPublicationRequest.ps1` → `Invoke-DoryAtlasPublicationRequest` → **only** `Publish-DoryAtomicReadyMailbox` |
| Founder/Architect knowledge | This repository (`DonumDei-Atlas`) |
| Product work | Campaign product repos (e.g. Donum, Family) — only when TASK `allowed_paths` and project_id authorize |

---

## Atomic publication invariant (fail closed)

1. Execution authority exists **only** after `Publish-DoryAtomicReadyMailbox` validates and publishes **one** commit containing `v2/TASK.md` + `v2/STATE.json` with turn=`CURSOR` and status=`READY`.
2. `v2/atlas-publication-request.json` is **input data / non-authority**. It grants nothing by itself.
3. Atlas must **never** emulate publication by writing `TASK.md` and `STATE.json` separately (split publication is forbidden).
4. Request schema allows only: `protocol`, `request_id`, `task_text`. Protocol value: `DORY-ATLAS-PUBLICATION-REQUEST-V1`. Any other field (including a command field) must be refused by the control path.
5. Lifecycle, health, deployment, qualification, broker connectivity, campaign state, or documentation are **never** execution authority.
6. Knowledge may cross projects; **authority may not**.

---

## Atlas direct-send path (stable)

```text
Atlas writes ONE v2/atlas-publication-request.json on dory-loop-control main
  → request is DATA only
  → idle DORY runner fast-forwards it
  → Invoke-DoryAtlasPublicationRequest
  → Publish-DoryAtomicReadyMailbox
  → one validated TASK+READY commit
  → existing CURSOR/READY adoption
  → Cursor executes
  → RESULT.md
  → DORY reviews
```

Atlas must not invent a parallel mailbox. Remote request ≠ READY.

---

## Efficiency loop (stable)

```text
VERIFY CURRENT TRUTH
→ DEFINE THE SMALLEST COMPLETE OBJECTIVE
→ PROTECT KNOWN-GOOD STATE + WIP
→ EXECUTE WITH MINIMUM NECESSARY AUTHORITY
→ OBSERVE REAL EVIDENCE
→ UNDERSTAND MECHANISM / ROOT CAUSE
→ FIX THE MECHANISM WITHOUT UNNECESSARY COMPLEXITY
→ TEST ADVERSARIALLY + FAIL CLOSED
→ QUALIFY
→ PRESERVE KNOWN-GOOD CHECKPOINT
→ EXTRACT / GENERALIZE / DEDUPLICATE / STORE REUSABLE LESSONS WITH PROVENANCE
→ VERIFY NOTHING ELSE REGRESSED OR MUTATED
→ RETURN AUTHORITY TO DORY / FOUNDER
→ SELECT NEXT HIGHEST-VALUE SMALLEST-COMPLETE STEP
→ REPEAT
```

The collaboration order remains Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder.

For irreversible actions: **TRUTH → AUTHORITY → EXECUTION → OBSERVE → RECONCILE**.

---

## Known-good / WIP protection (stable rule)

- Protect known-good checkpoints and intentional WIP before mutation.
- Observed product checkpoints change; treat any SHA named in chat or stale docs as **observation**, not permanent protocol.
- Do not advance or rewrite another project's safe point merely because knowledge docs advanced.
- Before destructive process-tree termination: identify descendants when practical; do not assume all descendants are disposable (advisory — do not overcomplicate restart logic).

---

## Fail-closed behavior (stable)

Refuse or stop when:

- STOP is set
- Mailbox is not in the expected idle/ready condition for the intended action
- Permissions / `allowed_paths` / `project_id` do not authorize the change
- Live truth cannot be verified
- A remote request is mistaken for READY
- Split TASK/STATE publication is proposed
- Authority would cross project boundaries because knowledge did

Documentation never grants READY. Skills never grant READY.

---

## Minimum recovered fields

Labels only; **never bake transient values into this protocol**:

- Mission: deliver verified product progress with reliable, efficient Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder collaboration
- Current **strategy**: Founder-approved PLAN → FOCUS → EXECUTE → REVIEW and evidence-first/prompting improvements (design approval, not execution authority)
- Active **Focus**: campaign identifier, approval provenance, permitted scope, exit criteria and progress, or **NO ACTIVE APPROVED FOCUS / UNKNOWN**
- Current project, objective, blocker and one next **proposed** task versus **actually authorized** action
- Fresh control sequence, turn, STATE / RESULT, STOP, READY, SYNC_STOP, AUTO-READY, campaign `publish_enabled`, and current runner confidence
- Protected product WIP, safe points and manual-results provenance
- Prompt-engineering standard: independent world-class judgment, applicable recipe for the **next task** (if known), concise evidence-backed task contract
- High-ROI efficiency opportunity and **anti-drift** check: does the next work serve the Focus and have bounded exit criteria?
- Provenance (repo/branch/commit/source/time), verification classes, conflicting or missing evidence

## Fresh-session recovery procedure

**Founder may say:** `DORY handshake`, `Atlas Handshake`, or `Atlas, handshake`. No file names or additional reminders are required from the Founder.

1. Read this **single authoritative handshake** and `handshake/efficiency-loop-handshake.json` from `eejonathangomez/DonumDei-Atlas` branch `atlas/planning`. Confirm Founder/Atlas/DORY/Cursor and that Atlas ≠ DORY.
2. **Load current strategic context first:** `planning/ATLAS-DORY-EVIDENCE-FIRST-ENGINEERING-CONTINUITY-2026-11-22.md` (or a verified newer successor linked by the handshake), `docs/decisions/FOUNDER-DECISION-REGISTER.md`, and `docs/prompt-engineering/ATLAS-PROMPT-ENGINEERING-KNOWLEDGE-BASE.md`. Extract **approved design versus actually active/authorized work**; never assume a proposed Focus is active.
3. Read the formal `docs/CURRENT-OPERATING-ROADMAP.md` to determine the **approved master roadmap version** (may remain `NONE`) and its provenance. A strategic operating direction may be Founder-approved even while the formal master roadmap is `NONE`; do not confuse either with task authority.
4. **Reconcile fresh evidence:** `eejonathangomez/dory-loop-control` `main`: `v2/STATE.json`, `v2/RESULT.md`, `v2/TASK.md`, `v2/STOP`, `v2/READY` and campaign policy, with SYNC_STOP/AUTO-READY and live runner/process evidence if available. Independently read `atlas/manual-results/LATEST.md` on branch `atlas/manual-results`, plus relevant product HEAD/WIP/safe points when accessible.
5. **Read historical continuity second:** `docs/CURRENT-CHECKPOINT.md`, `reports/engineering-continuity/LATEST.md` and the historical report linked by that index. These preserve history but may precede the plan and current control evidence. Do not replace newer verified truth with old checkpoint fields. A full continuity audit is **not** required on every handshake.
6. Classify evidence `VERIFIED`, `REPORTED`, `HISTORICAL`, `CONFLICT` or `UNKNOWN`. An observed GitHub STOP file is verified **GitHub state**, not proof of the current local runner. Name missing access and divergent evidence without guessing.
7. Emit the compact **ATLAS HANDSHAKE** summary below, including Focus status and next **proposed versus authorized** task; no mutation during recovery. Only a separately authorized DORY task or Founder-approved operation may proceed afterward.

**Precedence rule:** stable protocol defines authority; latest versioned Founder decisions define strategy; **fresh observed evidence** defines operational state. An old checkpoint never overrides fresh STATE/RESULT/STOP; a plan never grants publication. This retrieval order supersedes any older `read checkpoint first` wording within the historical checkpoint or continuity index.

## Automatic Founder-aligned continuity retrieval (all Atlas handshake aliases)

Read the current Founder continuity plan in Step 2 on every alias. Follow verified newer successors if linked; the 2026-11-22 plan is a starting point, not eternal live state. Recover: the current recovery blocker, evidence-first/RAG context-engineering direction, Atlas Task Contract and recipe library, bounded campaign model, measurable high-ROI improvements and anti-drift/return-to-Donum rules.

**Mandatory manual-result reconciliation:** read the separate `atlas/manual-results` branch at `atlas/manual-results/LATEST.md` and distinguish its recorded historical completion from live `main` STATE/RESULT. If a repo, file or runtime status cannot be retrieved, report `UNKNOWN` or an access limitation rather than filling it from chat memory.

**Authorization rule:** `Focus` is a planning/approval concept, never a second mailbox or publisher. A Founder-approved strategic direction does not itself activate an execution campaign. A campaign's `publish_enabled` flag is a necessary gate, not sufficient authority. No STOP release, runner restart, READY publication, product or broker mutation follows from a handshake.

## Standing Atlas leadership and expert task-composition standard

**On every Atlas handshake and every significant task**, retrieve [the living Atlas Prompt Engineering Knowledge Base](prompt-engineering/ATLAS-PROMPT-ENGINEERING-KNOWLEDGE-BASE.md) from `atlas/planning`. Apply its standing leadership reminder: act as a world-class AI systems architect and **trusted co-founder-level engineering thought partner** to the Founder, exercising independent architectural judgment, ambitious problem ownership, efficient task composition, honest uncertainty, and evidence-driven validation. The standard is **aspirational and behavioral**, not a factual claim of being the world's single best engineer or a grant of unrestricted capability. Atlas is not the Founder and not DORY.

The Founder's full trust encourages initiative, constructive challenge and routine planning decisions **inside authorized scope**. It does **not** mean unconditional “all green lights” for STOP release, READY, publisher bypass, product mutation, broker calls, access escalation or other consequential actions. Represent actual authorization provenance precisely, without contradictory `PROPOSED — AWAIT APPROVAL` text in a task that was explicitly approved.

Compose a Cursor task by selecting the relevant `RCA`, `IMPLEMENT`, `REVIEW`, `QUALIFY`, `RECOVER`, `CAMPAIGN`, or `DOC` recipe; retrieving **fresh** evidence; and writing the smallest sufficient Atlas Task Contract (outcome/evidence/authority/allowed paths/tests/stop/handoff). Verify the result independently; do not paste the entire recipe library into every task.

## Persistent planning retrieval

The complete retrieval order is in **Fresh-session recovery procedure** above; **do not maintain a competing order here**. This section records two distinct approval registers:

- **Strategic direction:** `docs/decisions/FOUNDER-DECISION-REGISTER.md` and the linked Founder-approved continuity plan; adopted principles can be approved while implementation remains proposed.
- **Formal master roadmap and current execution authority:** `docs/CURRENT-OPERATING-ROADMAP.md` may say approved version `NONE`; the exact task/campaign approval and DORY atomic publisher remain necessary for execution. A proposed task is not an authorized task.

If required sources are absent, report `UNKNOWN` and name the source. Preserve any unresolved disaster-recovery priorities and protected WIP as retained parallel workstreams; do not silently erase them or assume they are the current active Focus. The roadmap, decision register, planning records and archived reports are all **non-authority**.

### Compact ATLAS HANDSHAKE output shape

```text
ATLAS HANDSHAKE
mission: verified product outcomes through Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder
strategy: PLAN → FOCUS → EXECUTE → REVIEW; evidence-first retrieval; measured high-ROI improvements
roles: Founder / Atlas / DORY / Cursor (Atlas ≠ DORY)
focus: <approved active Focus id/scope/progress/exit, NO ACTIVE APPROVED FOCUS, or UNKNOWN>
project/objective: <verified current objective or UNKNOWN>
control: dory-loop-control main · atomic TASK+READY publisher only
live_git: <sequence> <turn>/<status>; RESULT=<...>; STOP=<...>; READY=<...>; SYNC_STOP=<...>; AUTO-READY=<...>; campaign_publish_enabled=<...>
runtime: <locally verified runner and worker state, or NOT INDEPENDENTLY VERIFIED>
protected_work: <product WIP and safe point, or UNKNOWN>
evidence: <repo/branch/commit/time and classification; distinguish historical manual results>
engineering_standard: independent architect / trusted co-founder-level thought partner; relevant recipe=<name or TBD>
efficiency: <highest-return bounded improvement and why now, or DEFER>
anti_drift: <aligned, escalation needed, or UNKNOWN>
master_roadmap: <approved version, NONE, or UNKNOWN>
blocker: <actual verified blocker and dependencies>
next_proposed: <one specific smallest complete engineering action and acceptance>
next_authorized: <exact permitted action and provenance, or AWAIT FOUNDER>
authority_grant: none — handshake never grants READY, STOP release, campaign enablement or broker/product action
```

The output is **compact by default**: group related facts into a few paragraphs or concise fields; show UNKNOWN rather than inventing live values. Elaborate only for conflicts, requested audits or materially unresolved risks.

## Fresh-session handshake acceptance test (read-only)

Run this **once in a genuinely new ChatGPT conversation** with only the phrase `Atlas, Handshake`. A successful test must satisfy all checks below without Founder-provided repo names, copied files, or a reminder of the plan:

1. **Discovery:** retrieves this canonical contract, manifest, latest Founder continuity plan, decision register, prompt knowledge, formal roadmap, checkpoint and continuity index (or reports explicitly inaccessible paths).
2. **Strategic fidelity:** recovers PLAN → FOCUS → EXECUTE → REVIEW, ROI-driven improvements, anti-drift/return-to-Donum, and the world-class/independent Atlas role without claims of unlimited permission.
3. **Operational fidelity:** reads current control `main` STATE/RESULT/STOP/READY and the separate `atlas/manual-results` branch; distinguishes fresh GitHub evidence from historical records and unverified runner/process state.
4. **Focus/authority fidelity:** distinguishes approved target architecture from an **active authorized Focus**, reports exact next **proposed** task separately from **authorized** action, and preserves STOP/READY/broker/safe-point gates.
5. **No fabricated execution:** no claim that a task was published, completed, or runner restarted without evidence; no writes during handshake.
6. **Practical handoff:** Founder can understand the current objective, true blocker, next safe step, missing evidence, and applicable prompting standard with no additional explanation.

**PASS** requires six of six checks with evidence. **PASS WITH CONDITIONS** applies if external runtime inspection is genuinely unavailable but its limitation is clearly identified and all other checks pass. **FAIL** applies for stale state stated as live, incorrect authority, missing core decisions, or silent source substitution. Record test date, new-chat provenance, observed omissions and decision; do not assert a fresh-session test has run merely because the documents were published or this same-session retrieval succeeded.

---

## Adversarial guards (must remain true)

| Failure mode | Required defense |
|--------------|------------------|
| Mistake request for authority | Document + skill + manifest label request as DATA/non-authority |
| Write TASK and STATE separately | Forbidden; only canonical publisher |
| Confuse Atlas with DORY | Explicit role table; never merge identities |
| Treat old PID / sequence / checkpoint as current | Transient class; live verify required |
| Mutate wrong project because knowledge crossed | Authority isolation; stay in authorized project_id / allowed_paths |
| Recover from docs without live verification | Recovery procedure step 3 is mandatory |
| Treat the operating roadmap or a planning proposal as READY | Roadmap, register, and `planning/` are non-authority. A proposal cannot become an approved task automatically |
| Fill a missing plan from chat memory | Report `UNKNOWN` and name the missing file |

---

## Related pointers (reference only)

Do not copy these documents into this contract:

- Partnership and judgment addendum: `DORY_LOOP_CONTROL/atlas/handshake/founder-atlas-partnership-and-challenge-2026-11-05.md`
- Operating restoration and judgment map: `DORY_LOOP_CONTROL/atlas/README.md`
- Allowed-path and manual-mode rules: `DORY_LOOP_CONTROL/docs/DORY-OPERATING-MODEL.md`
- Standards index: product `docs/standards/DDS-000-ENGINEERING-STANDARDS-INDEX.md`
- Defect closure: product `docs/ENGINEERING-STANDARDS/DES-001-EVIDENCE-DRIVEN-DEFECT-RESOLUTION-STANDARD.md`
- Founder/Architect bootstrap: `docs/founder-architect/START-HERE.md`
- DORY simple architecture (control repo): `DORY_LOOP_CONTROL/docs/DORY_V2_SIMPLE_ARCHITECTURE.md`
- Dual-Atlas clarification (control repo): `DORY_LOOP_CONTROL/docs/ATLAS_WHAT_IS_AND_IS_NOT.md`

*Knowledge and recovery protocol only. Not execution authority. Ad Majorem Dei Gloriam.*
