---
name: reminder-handshake
description: >-
  Recover the Atlas/DORY/Cursor operating model from version-controlled
  handshake truth plus live verification. Use when the Founder says
  DORY handshake, recover DORY, reminder handshake, or when context loss
  is evident and the efficiency-loop operating model must be restored.
---

# reminder-handshake — DORY efficiency-loop recovery

**Goal:** Reconstruct the proven operating model for Atlas without Founder reteaching. Knowledge recovery only — **never** grant READY or invent authority from documentation.

**Founder phrase:** `DORY handshake`

## Required reads (every invocation)

1. `docs/EFFICIENCY-LOOP-HANDSHAKE.md` — authoritative protocol
2. `handshake/efficiency-loop-handshake.json` — machine manifest
3. Live control truth under the DORY control repo `v2/` (`STATE.json`, and as needed `TASK.md`, `RESULT.md`, `STOP`) — **mandatory**

If the control repo path is unknown, locate `eejonathangomez/dory-loop-control` / local `DORY_LOOP_CONTROL` and say so. Do not invent mailbox state.

## Hard rules

- Documentation and this skill are **not** execution authority.
- `v2/atlas-publication-request.json` is **DATA / non-authority**.
- Canonical publisher only: `Publish-DoryAtomicReadyMailbox`. Never recommend split `TASK.md` + `STATE.json` writes.
- Atlas ≠ DORY. Do not conflate roles.
- Knowledge may cross projects; authority may not.
- Do **not** silently mutate any project during recovery.
- Do **not** bake or trust stale PID / sequence / checkpoint values from chat or old docs — verify live.
- If live truth conflicts with the handshake doc, **live truth wins**; report the mismatch before action.

## Procedure

1. Read the authoritative document + manifest.
2. Verify live mailbox / runner facts now.
3. Emit a compact copy-ready block:

```text
ATLAS HANDSHAKE
roles: Founder / Atlas / DORY / Cursor (Atlas ≠ DORY)
control: dory-loop-control main · mailbox v2/{TASK,RESULT,STATE,STOP}
authority: Publish-DoryAtomicReadyMailbox only · request=DATA/non-authority
live: <sequence> <turn>/<status> STOP=<yes/no> worker=<n> publish_enabled=<bool> (verified now)
knowledge_vs_authority: knowledge may cross projects; authority may not
next: <smallest safe step or "await Founder/DORY">
```

4. Stop. Do not publish a new sequence, enable campaign publication, call brokers, or mutate Donum/Family unless a separate authorized TASK explicitly allows it.

## Out of scope

- Changing the canonical publisher
- Weakening authority gates
- Treating health/lifecycle/docs as READY
- Product mutation “because knowledge crossed”
