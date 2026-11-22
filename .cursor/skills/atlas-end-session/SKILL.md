---
name: atlas-end-session
description: >-
  Preserve the Founder-Atlas engineering session in the Atlas planning repository.
  Use on "Atlas, End Session", "end-session", "close engineering session",
  or "save session handoff". Reconcile evidence, write one dated handoff and
  update reports/session-handoffs/LATEST.md, with GitHub read-back.
  Docs-only; not DORY production or broker authority.
---

# Atlas End Session — Cursor/Agent adapter

**Authoritative full procedure:** `docs/skills/atlas-end-session/SKILL.md` in `eejonathangomez/DonumDei-Atlas#atlas/planning`.

Read and follow that exact canonical file; do not copy or fork its rules. Verify current source availability and required GitHub permissions before attempting writes. A skill file does not grant READY, alter STOP, start a worker, or permit broker/product/control mutation.

**Output:** one dated Atlas session handoff under `reports/session-handoffs/YYYY-MM-DD/`, updated `reports/session-handoffs/LATEST.md`, optional minimal changes to existing canonical docs only for real new permanent facts or explicit Founder decisions, and actual commit/read-back proof. If unavailable, report `NOT SAVED` with a draft, rather than claiming persistence.

**Do not** create another handoff service, GitHub branch, automation or separate source of truth.
