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

Labels only. Values come from a fresh live read and are never stored in this contract:

- Active project and objective, or UNKNOWN
- Sequence, turn, and status
- STOP and READY
- SYNC_STOP
- Protected WIP and safe-point constraints
- Current approved next action, or AWAIT FOUNDER
- Evidence provenance and the read timestamp

## Fresh-session recovery procedure

**Founder may say:** `DORY handshake`, `Atlas Handshake`, or `Atlas, handshake`

**Atlas / Cursor then:**

1. Open this document and `handshake/efficiency-loop-handshake.json` from DonumDei-Atlas (GitHub or local clone).
2. Confirm stable roles: Founder / Atlas / DORY / Cursor — Atlas ≠ DORY.
3. Verify **live** control truth from `DORY_LOOP_CONTROL/v2/` (and runner process evidence as needed): `STATE.json`, `TASK.md` / absence, `RESULT.md`, `STOP`, worker presence, campaign publish flag — **do not trust baked PIDs or sequences**.
4. If mismatch with this document: report it; prefer live truth.
5. Reconstruct the operating model from STABLE PROTOCOL above.
6. Return a compact **ATLAS HANDSHAKE** summary (roles, transport, authority boundary, live mailbox snapshot, next safe step).
7. Do **not** mutate products, enable campaign publication, call brokers, issue READY, or invent the next sequence during recovery unless a separate authorized TASK says so.

### Compact ATLAS HANDSHAKE output shape

```text
ATLAS HANDSHAKE
roles: Founder / Atlas / DORY / Cursor (Atlas ≠ DORY)
control: dory-loop-control main · mailbox v2/{TASK,RESULT,STATE,STOP}
authority: Publish-DoryAtomicReadyMailbox only · request=DATA/non-authority
project: <active project or UNKNOWN> objective: <current objective or UNKNOWN>
live: <sequence> <turn>/<status> STOP=<CLEAR or asserted> READY=<present or absent> SYNC_STOP=<why or absent> (verified now)
constraints: protected WIP and safe points are named and not moved
provenance: <files read> at <read timestamp>
knowledge_vs_authority: knowledge may cross projects; authority may not
authority_grant: none — this handshake is not execution authority
next: <approved next action or AWAIT FOUNDER>
```

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

---

## Historical DORY Operational Capability — October–November 2026

This section records demonstrated history. It does not change roles, the atomic-publication invariant, STOP, campaign publication, or any safety restriction above. It is not execution authority. Live mailbox and process truth still win over this section.

### Counting evidence

Control repository `eejonathangomez/dory-loop-control`, branch `main`, tip used for the count: `824cf59cc63586374126d428fa3557c6b6b73836`.

Reproducible count, from that checkout:

```text
git log origin/main --format="%ad %s" --date=short --grep="COMPLETE return to DORY"
```

Count each matching subject whose date and `sequence N` parse. On the four days below, the raw subject count and the unique sequence count are the same.

| Date | Unique COMPLETE return subjects | Sequence span |
| --- | ---: | --- |
| 2026-10-26 | 39 | 318–359, not every number in the span |
| 2026-10-29 | 34 | 408–447, not every number in the span |
| 2026-10-30 | 78 | 448–525, contiguous |
| 2026-10-31 | 13 | 526–538, contiguous |

October 30 and 31 together are 91 COMPLETE return subjects. A subject is a published mailbox commit. It is not, by itself, proof of a distinct Cursor process, of automatic task selection, or of concurrent execution. The runner log for this era shows one `adapter=spawn` loop at a time.

### How to read the history

1. DORY demonstrated substantial historical task-completion throughput. The Founder remembers about 30 or more tasks around Sequence 500. The mailbox count is higher: 2026-10-30 alone accounts for sequences 448–525.
2. A stopped runner does not erase that capability. Current STOP and a runner count of zero are a runtime state.
3. Do not replace the current implementation with an older runner because an older period completed more tasks.
4. A later architecture review keeps the demonstrated loop: Atlas request data, one atomic READY publication, one Cursor execution, RESULT back to Git, and continuation only when it is separately enabled and the gates pass.

### Five facts that must stay distinct

| Fact | What it is | What it is not |
| --- | --- | --- |
| Historical demonstrated capability | Published COMPLETE subjects, and a spawn runner that accepted an Atlas request | Permission to run today |
| Last-known-good operational state | Sequence 630 at `a67cea92c66b14014ed601fc430e412def283db6` on 2026-11-10. See below | The current mailbox |
| Current implementation | Control `main` at `824cf59cc63586374126d428fa3557c6b6b73836`, including the later exact-STOP commits | A different product |
| Current runtime state | Dated runtime snapshot recorded 2026-11-20, not permanent current truth: sequence 632 COMPLETE, STOP asserted, runner not running. Verify live before acting | Permanent current truth, or proof the code path was removed |
| Safety authorization | STOP, `publish_enabled`, safe points, protected WIP, and a separate Founder decision | Implied by this history |

### Founder-confirmed context, not yet a runtime record

**DORY was fully functional immediately before the deliberate shutdown for the emergency backup and disaster-recovery campaign.**

That sentence is Founder-confirmed historical context. No control-repo commit subject names that backup or disaster-recovery campaign. The local runner log shows pid 16688 still polling at 2026-11-10 17:28 and does not contain a graceful-shutdown line for that process. Do not upgrade this statement into a logged shutdown until those records are found.

Sequence 630 remains the last recorded successful operating checkpoint before that pause: Atlas ingress published READY commit `62ff3901810f1c74665ad72b92d787f7c1eed497`, Cursor exited 0, and the COMPLETE commit is `a67cea92c66b14014ed601fc430e412def283db6`. Committed STOP in that commit is `CLEAR`. Campaign `publish_enabled` was already false, and continuation had already refused publication for product divergence. Those limits are part of the checkpoint, not a later failure.

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
