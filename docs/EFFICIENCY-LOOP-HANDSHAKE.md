# Efficiency Loop Handshake — Authoritative Recovery Protocol

**Founder recovery phrase:** `DORY handshake`

This document is the durable, version-controlled recovery protocol for the proven Atlas / DORY / Cursor operating model. A fresh ChatGPT (Atlas) or Cursor session must recover from this file plus the machine manifest and **live verification** — not from chat memory.

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
| **Cursor** | Execution arm | Executes only when TASK permissions + READY gates authorize; writes RESULT; returns turn to DORY |

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

## Fresh-session recovery procedure

**Founder says only:** `DORY handshake`

**Atlas / Cursor then:**

1. Open this document and `handshake/efficiency-loop-handshake.json` from DonumDei-Atlas (GitHub or local clone).
2. Open `docs/engineering-continuity/README.md` and `reports/engineering-continuity/LATEST.md`. Use them for DORY architecture, Donum engineering state, and cross-project decisions. Treat dated checkpoints as observations.
3. Confirm stable roles: Founder / Atlas / DORY / Cursor — Atlas ≠ DORY.
4. Verify **live** control truth from `DORY_LOOP_CONTROL/v2/` (and runner process evidence as needed): `STATE.json`, `TASK.md` / absence, `RESULT.md`, `STOP`, worker presence, campaign publish flag — **do not trust baked PIDs or sequences**.
5. If mismatch with this document or a dated checkpoint: report it; prefer live truth.
6. Reconstruct the operating model from STABLE PROTOCOL above and the continuity architecture reference.
7. Return a compact **ATLAS HANDSHAKE** summary (roles, transport, authority boundary, live mailbox snapshot, next safe step).
8. Do **not** mutate products, enable campaign publication, call brokers, issue READY, or invent the next sequence during recovery unless a separate authorized TASK says so.

### Compact ATLAS HANDSHAKE output shape

```text
ATLAS HANDSHAKE
roles: Founder / Atlas / DORY / Cursor (Atlas ≠ DORY)
control: dory-loop-control main · mailbox v2/{TASK,RESULT,STATE,STOP}
authority: Publish-DoryAtomicReadyMailbox only · request=DATA/non-authority
live: <sequence> <turn>/<status> STOP=<yes/no> worker=<n> publish_enabled=<bool> (verified now)
knowledge_vs_authority: knowledge may cross projects; authority may not
next: <smallest safe step or "await Founder/DORY">
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
| Recover from docs without live verification | Recovery procedure live-verification step is mandatory |

---

## Engineering continuity records

Stable architecture and changing operational status are separate records. This handshake does not store runner liveness, sequence numbers, or product HEAD values.

| Need | Record |
|------|--------|
| Continuity index | `docs/engineering-continuity/README.md` |
| DORY architecture and capability | `docs/engineering-continuity/DORY-ARCHITECTURE.md` and `DORY-CAPABILITY-REGISTRY.md` |
| Latest DORY and Donum observations | `reports/engineering-continuity/LATEST.md` |
| Pointer that does not duplicate those observations | `docs/CURRENT-CHECKPOINT.md` |
| 2026-11-20 observed decisions | `docs/engineering-continuity/FOUNDER-DECISION-REGISTER.md` |
| 2026-11-15 decisions | `docs/decisions/FOUNDER-DECISION-REGISTER.md` on branch `atlas/planning`. Not in this branch |

A fresh session reads the index and `LATEST.md`, then verifies live `DORY_LOOP_CONTROL/v2/` before acting. If the dated checkpoint and the live read disagree, the live read wins. Historical capability counts published on `docs/historical-dory-capability-2026-11` stay on that branch.

These records are knowledge. They do not grant READY, clear STOP, arm campaign publication, or install a runner candidate.

## Related pointers (reference only)

- Founder/Architect bootstrap: `docs/founder-architect/START-HERE.md`
- DORY simple architecture (control repo): `DORY_LOOP_CONTROL/docs/DORY_V2_SIMPLE_ARCHITECTURE.md`
- Dual-Atlas clarification (control repo): `DORY_LOOP_CONTROL/docs/ATLAS_WHAT_IS_AND_IS_NOT.md`

*Knowledge and recovery protocol only. Not execution authority. Ad Majorem Dei Gloriam.*
