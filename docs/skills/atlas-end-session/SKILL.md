# Skill — Atlas End Session (durable engineering closeout)

**Skill ID:** `atlas-end-session`  
**Triggers:** `Atlas, End Session`, `end-session`, `close engineering session`, `save session handoff`.  
**Audience:** ChatGPT / Atlas. The optional .cursor skill adapter references this canonical document.  
**Authority:** The Founder's explicit End Session instruction authorizes **bounded Atlas planning/documentation preservation** on `DonumDei-Atlas#atlas/planning` through currently available GitHub write actions. It **does not** authorize control/product repository mutation, mailbox/READY, STOP, runner/broker actions, secrets export, or changing a separate approved master roadmap. If GitHub write access is missing, prepare a clearly labeled uncommitted draft and report non-persistence.

## Objective

Preserve the useful context, decisions, evidence, and unresolved work of the *current session* in GitHub so a fresh `Atlas, Handshake` can recover continuity from canonical sources with minimal re-explanation. This is a **bounded documentation task**, not a full project archaeology campaign. Source files and canonical decision registers remain authoritative; session summaries are handoff pointers, not alternate live truth.

## Exact workflow — End Session

1. **Capture this session:** summarize verified work, Founder-approved decisions, tasks sent or received, results with exact provenance, open questions, next Focus, and new tools/branches/skills. Explicitly distinguish agreed decisions from discussed ideas, proposed tasks and unverified reports. Do not hallucinate conversations the current session cannot access.
2. **Reconcile minimum fresh evidence:** when connected, inspect `dory-loop-control#main` STATE, RESULT, TASK, STOP and relevant campaign/README evidence; separately `dory-loop-control#atlas/manual-results` LATEST; source and intended current Atlas plan; product WIP if available. Label `VERIFIED GITHUB`, `FOUNDER REPORTED`, `CURSOR REPORTED`, `HISTORICAL`, `UNKNOWN`, `CONFLICT`. No claim of live Windows runner verification from GitHub alone.
3. **Check existing records:** `docs/EFFICIENCY-LOOP-HANDSHAKE.md`, `docs/decisions/FOUNDER-DECISION-REGISTER.md`, `planning/ATLAS-DORY-EVIDENCE-FIRST-ENGINEERING-CONTINUITY-2026-11-22.md` or verified successor, `docs/engineering-inventory/ENVIRONMENT-AND-REPOSITORY-MAP.md`, `docs/engineering-inventory/CURSOR-SKILLS-CATALOG.md`, and `reports/session-handoffs/LATEST.md`. Avoid duplicating complete long-lived documents.
4. **Write ONE dated handoff** under `reports/session-handoffs/YYYY-MM-DD/ATLAS-SESSION-<slug>.md`. If an exact path exists, choose a unique explicit suffix; never overwrite a different session. Include:
   - Mission / active Focus versus approved strategy;
   - Verified and reported work since last handoff;
   - Exact repo, branch, commit, test and report references, with timestamps where known;
   - DORY STATE, STOP, READY, runner confidence and authorization **at read time**;
   - Decisions (**APPROVED / PROPOSED / DEFERRED / REJECTED**) with Founder provenance;
   - Candidate changes, uncommitted or protected WIP and safe-point warning;
   - Newly found branches, tools, credentials-handling patterns and skills **without secrets**;
   - Unresolved blockers / safety / risk and the smallest next proposed action versus actually authorized action;
   - What changed in reference docs, sources accessed and what could not be verified.
5. **Update only canonical records that actually changed:** a newly approved enduring decision goes to the Founder decision register; genuinely reusable procedures go to existing corresponding docs; new verified capabilities to the inventory and skill catalog. Do **not** turn a temporary PID/branch tip/state into a permanent handshake fact; these belong in the dated handoff. Do not create another master roadmap or a second authority layer.
6. **Update `reports/session-handoffs/LATEST.md`** to point to the exact new handoff, its commit and date/verification class, with a warning that it is not current runtime truth. Ensure the **existing handshake** already retrieves the pointer; update its stable retrieval instructions only if missing—not on every End Session.
7. **Verify GitHub publication:** use connected GitHub write operations on the exact approved Atlas planning branch, confirm each resulting commit and read back handoff, LATEST pointer and changed canonical records. Do not claim saved until commit/readback success. Prefer minimal diff and reuse existing files. Do not modify DORY or product repos while closing the session.
8. **Return compact closeout:** handoff link, saved commits, preserved decisions, unverified evidence, next Focus/task, approvals needed, any failures. Stop. Do not execute the next task just because it was documented.

## Authority / safety guardrails

- No `READY`, `AUTO-READY`, STOP/SYNC_STOP change, runner/worktree operation, Git force, GitHub production branch mutation, product/broker order or credential read as part of End Session.
- No vault entries or tokens in session handoff. Say `Bitwarden vault — Founder-reported`, not a credential.
- An approval to *document* a decision is distinct from approval to *execute* it.
- If a task result is pasted but the candidate commit exists only on the Founder's host, record `CURSOR REPORTED / NOT VERIFIED REMOTELY`.
- If conflicting evidence exists, preserve both with source and raise `CONFLICT`; do not edit history silently.
- If evidence/tools are unavailable, produce partial provenance and report the missing source. **Never invent success.**

## Reusable skill creation (related, distinct request)

When the Founder says **`Atlas, Create Skill: <workflow>`**, first search the actual Atlas/DORY/Donum skill catalogs and relevant skill files for existing procedure. Prefer extending an existing source. If new, define exact triggers, inputs, expected output, authorized repo/paths, non-authority limits, evaluation/acceptance tests and retrieval map. Create the **canonical Atlas skill** under `docs/skills/<slug>/SKILL.md`; add a short optional `.cursor/skills/<slug>/SKILL.md` adapter only if Cursor will use it; update the skills catalog and handshake pointers if needed. Version and verify commit/readback. **Do not invoke the newly created skill unless the Founder explicitly requests its run.**

## Completion / qualification

**PASS** = new dated session report and LATEST pointer committed/read-back, source classification and approved decisions correct, no unauthorized changes.  
**PASS WITH CONDITIONS** = bounded record saved but a relevant runtime source is unavailable and properly marked.  
**FAIL / NOT SAVED** = GitHub write/readback failed or essential source/approval is ambiguous.  
**NO-OP** = no meaningful session changes; explicitly say so instead of manufacturing new content.

**Fresh-session test:** In a separate conversation, say only `Atlas, Handshake`; Atlas should discover `reports/session-handoffs/LATEST.md`, read the linked handoff, compare with current GitHub control/manual results and state the next safe task without the Founder pasting the old session.
