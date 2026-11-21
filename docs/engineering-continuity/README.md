# Engineering continuity index

**Protocol:** `DORY-DONUM-ENGINEERING-CONTINUITY-V1`  
**Home:** DonumDei-Atlas  
**Authority:** none. These records are knowledge. They do not publish READY, clear STOP, or authorize execution.

This index is the continuity entry for both DORY and Donum Dei. A new Atlas session starts here after the efficiency-loop handshake, then re-verifies live control truth before any action.

## Evidence classes

| Class | Meaning |
|-------|---------|
| VERIFIED | Directly observed during the named observation |
| REPORTED | Supported by a named document or result, not independently rechecked in that observation |
| HISTORICAL | Previously true. Not current operational truth |
| UNKNOWN | Not established by the available evidence |

If a dated checkpoint conflicts with a fresh live read, the live read wins. Report the mismatch.

## Stable records

Stable records describe purpose, architecture, and capability. They do not store runner PIDs or the current sequence as protocol constants.

| Record | Path |
|--------|------|
| Efficiency-loop handshake | [docs/EFFICIENCY-LOOP-HANDSHAKE.md](../EFFICIENCY-LOOP-HANDSHAKE.md) |
| Handshake manifest | [handshake/efficiency-loop-handshake.json](../../handshake/efficiency-loop-handshake.json) |
| DORY architecture reference | [DORY-ARCHITECTURE.md](./DORY-ARCHITECTURE.md) |
| DORY capability registry | [DORY-CAPABILITY-REGISTRY.md](./DORY-CAPABILITY-REGISTRY.md) |
| Founder decision register | [FOUNDER-DECISION-REGISTER.md](./FOUNDER-DECISION-REGISTER.md) |
| Control-repo operating contract | `eejonathangomez/dory-loop-control` `docs/DORY_CURRENT_ARCHITECTURE.md` |

## Changing operational records

| Record | Path |
|--------|------|
| Latest pointer | [reports/engineering-continuity/LATEST.md](../../reports/engineering-continuity/LATEST.md) |
| Current-checkpoint pointer | [docs/CURRENT-CHECKPOINT.md](../CURRENT-CHECKPOINT.md) |

`LATEST.md` names the newest operational observations, the latest documentation publication event, and the latest recovery qualification. A publication event is not a runtime observation. Do not overwrite a dated checkpoint. Replace the pointer when a newer record is accepted.

## What this index does not replace

| Existing record | Treatment |
|-----------------|-----------|
| `docs/historical-dory-capability-2026-11` at `feb9b53090a4a77d9b376b653b0eee89e7c20e68` | Published historical capability section in that branch's handshake. Parent is unpublished-on-main `0a4a825`. Not merged |
| `atlas/planning` at GitHub `f792d76ba66e6e69469021de9f798f65d8da0b83` | 2026-11-15 continuity archive, `docs/CURRENT-CHECKPOINT.md`, `docs/decisions/FOUNDER-DECISION-REGISTER.md`, and `reports/engineering-continuity/LATEST.md`. Not merged. Its checkpoint still reports sequence 630 as not re-read |
| `reports/EOS-V2-2026-10-20-CONTINUITY-CHECKPOINT.md` | Historical Atlas continuity note |
| `ROADMAP.md` | Atlas knowledge roadmap, last marked 2026-07-08. Not the DORY or Donum engineering status |
| `DORY_LOOP_CONTROL/atlas/**` | Continuity archaeology. Not this knowledge home |
| `dory-loop-control` branch `atlas/manual-results` | Manual-result evidence archive. Not mailbox authority and not current `main` |

## Recovery order

1. Read the handshake and confirm Atlas is not DORY.
2. Read this index.
3. Read the architecture reference and capability registry.
4. Read `reports/engineering-continuity/LATEST.md` and the dated checkpoints it names.
5. Verify live `DORY_LOOP_CONTROL/v2/` mailbox, STOP, campaign flag, and runner process evidence.
6. Verify the Donum worktree without cleaning it.
7. Emit the handshake summary. Do not grant READY.
