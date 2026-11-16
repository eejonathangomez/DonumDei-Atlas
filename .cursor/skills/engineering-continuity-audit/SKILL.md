---
name: engineering-continuity-audit
description: >-
  Read-only reconstruction of Donum Dei engineering continuity from
  authoritative files. Use when the Founder says engineering-continuity-audit,
  continuity audit, where are we, or what is verified. QUICK is the default.
  CHECKPOINT records a work stop or handoff. FULL is only on request or
  when significant evidence conflicts.
---

# engineering-continuity-audit

**Goal:** Restore an accurate checkpoint from files. Auditing grants no execution authorization and cannot grant READY or AUTO-READY.

**Default mode:** QUICK. Use CHECKPOINT at a meaningful work stop, a completed milestone, or a handoff. Use FULL only when the request says FULL or when two authoritative files materially conflict.

The collaboration order remains Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder.

## Required behavior

- Read authoritative files. Do not rely on chat memory.
- Prefer a fresh read over a stale summary.
- Distinguish local Git state, cached `refs/remotes`, and live `git ls-remote`. Do not fetch unless a separate authorization says so.
- Preserve Founder decisions. Do not turn a recommendation into approval.
- Mark a missing file or unread remote `UNKNOWN` or `NOT VERIFIED`.
- Do not invent a completed task, milestone, approval, or Git state.
- Do not repeat a completed recovery compare without a documented reason.
- Do not start or stop DORY, publish, push, or modify STOP, SYNC_STOP, READY, or AUTO-READY.

## Reads

1. `docs/EFFICIENCY-LOOP-HANDSHAKE.md` and `handshake/efficiency-loop-handshake.json`.
2. `docs/CURRENT-OPERATING-ROADMAP.md` and `docs/decisions/FOUNDER-DECISION-REGISTER.md`. An approved version of `NONE` is not an approved roadmap.
3. `docs/CURRENT-CHECKPOINT.md`. If it is missing, report `UNKNOWN`.
4. `reports/engineering-continuity/LATEST.md` and the historical report it names. If the archive is missing, report `UNKNOWN`.
5. Fresh Git state for Atlas, DORY control, Donum, and Family, plus live `v2/STATE.json`, `v2/STOP`, and the presence or absence of READY, SYNC_STOP, and AUTO-READY.

`planning/` proposals are not approved work.

## QUICK

Return a short checkpoint:

- Founder priority order as recorded in a file, or `UNKNOWN` if no file records it
- Latest verified milestones named by the archive and still supported by a fresh read
- Current evidence paths
- Local, cached, and live Git state
- DORY safety snapshot
- Blockers
- Next authorized action, or `AWAIT FOUNDER`

## CHECKPOINT

Use this mode at a meaningful work stop, a completed milestone, or a handoff.

- Update `docs/CURRENT-CHECKPOINT.md` only when a labeled field changed. If the new body would be identical, do not write a file and do not commit.
- Label each statement `VERIFIED`, `REPORTED`, `UNKNOWN`, or `HISTORICAL`.
- When the engineering state materially changes, add a new dated file under `reports/engineering-continuity/YYYY-MM-DD/`. Do not overwrite an older report and do not copy an unchanged report.
- The checkpoint cannot authorize READY, AUTO-READY, publication, or product execution.

## FULL

Cover chronology, backups, Git inventory, DORY, Donum, Atlas, Family, approved plans, confirmed defects, unverified risks, continuity RCA, critical path, and an evidence index. Do not run FULL on every handshake.
