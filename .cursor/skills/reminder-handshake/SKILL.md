---
name: reminder-handshake
description: >-
  Recover the Atlas/DORY/Cursor operating model from version-controlled
  handshake truth plus live verification. Use when the Founder says
  "DORY handshake", "Atlas Handshake", "Atlas, handshake",
  "recover DORY", or "reminder handshake", or when context loss
  is evident and the
  efficiency-loop operating model must be restored.
---

# reminder-handshake — DORY efficiency-loop recovery

**Goal:** Reconstruct the proven operating model for Atlas without Founder reteaching. Knowledge recovery only — **never** grant READY or invent authority from documentation.

**Founder phrases:** `DORY handshake`, `Atlas Handshake`, and `Atlas, handshake`. All three resolve to `docs/EFFICIENCY-LOOP-HANDSHAKE.md`. Do not duplicate that contract here. `DORY handshake` remains the primary manifest phrase.

## Required reads (every invocation)

1. `docs/EFFICIENCY-LOOP-HANDSHAKE.md` — authoritative protocol
2. `handshake/efficiency-loop-handshake.json` — machine manifest
3. Live control truth under the DORY control repo `v2/` (`STATE.json`, and as needed `TASK.md`, `RESULT.md`, `STOP`, `SYNC_STOP`, `AUTO-READY`) — **mandatory**
4. `docs/CURRENT-OPERATING-ROADMAP.md` — operating roadmap record. Approved version `NONE` is not an approved plan
5. `docs/decisions/FOUNDER-DECISION-REGISTER.md` — decision index
6. `planning/` on branch `atlas/planning` — proposals only, separate from approved work
7. `reports/engineering-continuity/LATEST.md` and the historical report it names — evidence only. If missing, report `UNKNOWN`. Do not run a FULL continuity audit on every handshake.

If the control repo path is unknown, locate `eejonathangomez/dory-loop-control` / local `DORY_LOOP_CONTROL` and say so. Do not invent mailbox state.

## Hard rules

- Documentation and this skill are **not** execution authority. They do not grant READY, clear STOP, select a project, or publish.
- `v2/atlas-publication-request.json` is **DATA / non-authority**.
- Canonical publisher only: `Publish-DoryAtomicReadyMailbox`. Never recommend split `TASK.md` + `STATE.json` writes.
- Atlas ≠ DORY. Do not conflate roles.
- Knowledge may cross projects; authority may not.
- Do **not** silently mutate any project during recovery.
- Do **not** bake or trust stale PID / sequence / checkpoint values from chat or old docs — verify live.
- If live truth conflicts with the handshake doc, **live truth wins**; report the mismatch before action.
- The operating roadmap and a planning proposal cannot authorize READY. A proposal cannot become an approved task automatically.
- If a retrieval file is missing, report `UNKNOWN` and name the missing source. Never substitute chat memory for a missing authoritative file.

## Procedure

1. Read the authoritative document + manifest.
2. Verify live mailbox / runner facts now.
3. Emit a compact copy-ready block:

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

4. Stop. Do not publish a new sequence, enable campaign publication, call brokers, or mutate Donum/Family unless a separate authorized TASK explicitly allows it.

## Out of scope

- Changing the canonical publisher
- Weakening authority gates
- Treating health/lifecycle/docs as READY
- Product mutation “because knowledge crossed”
