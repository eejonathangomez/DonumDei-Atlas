# Atlas End Session — latest handoff pointer

**Status:** NO HANDOFF YET RECORDED BY THIS NEW WORKFLOW  
**Introduced:** 2026-11-22  
**Authority:** Read-only session evidence index, NOT live runtime state, a decision register, an active Focus or DORY execution permission.

The workflow `Atlas, End Session` is defined at `docs/skills/atlas-end-session/SKILL.md`. On the first explicitly requested run it will write a dated `reports/session-handoffs/YYYY-MM-DD/ATLAS-SESSION-<slug>.md` and replace this marker with a link to that report and verified commit. This initial marker is **not** a session closeout and must not be reported as one.

On every `Atlas, Handshake`, read this pointer if present; if no handoff exists, say so and continue from the current Founder plan, decision register and live GitHub evidence. A handoff may be stale and must not override fresh control GitHub, local STOP/runner evidence or approvals.
