# Engineering continuity archive

This directory is the Git-versioned history of engineering continuity reports. It is evidence. It is not execution authority, and it cannot grant READY or AUTO-READY.

## Purpose

A later session reads `LATEST.md`, then the historical report that index names, then fresh Git, DORY, and runtime evidence. Chat memory does not replace a missing file. If this archive is absent, report `UNKNOWN` and name `reports/engineering-continuity/LATEST.md`.

## Evidence precedence

1. A fresh live read of Git, `v2/STATE.json`, STOP, and runtime evidence.
2. The dated report named by `LATEST.md`.
3. Older dated reports in this directory.
4. Stale runbooks and checkpoints. They remain historical when a later report disagrees.
5. Chat memory. Never use it to fill a missing authoritative file.

## Naming

Store an immutable report at `YYYY-MM-DD/<report-id>.md`. The date is the session date recorded in that report's provenance note in `LATEST.md` or in an amendment file. Do not take the date from an attachment filename.

## Retention

Do not overwrite a historical report. A correction is a new dated report or an explicit amendment file that names the report it corrects. `LATEST.md` may move its pointer to a newer report. That pointer change does not edit the older report.

## Qualification

`LATEST.md` records the qualification stated by the archived report. Archiving a report does not re-run its tests and does not approve a roadmap.
