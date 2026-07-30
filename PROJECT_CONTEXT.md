# PROJECT_CONTEXT.md

| Field | Value |
|-------|-------|
| **Standard** | [DDES-001](../DonumDei-TradingPlatform/docs/ENGINEERING-STANDARDS/DDES-001-project-context-standard.md) |
| **Purpose** | Official Engineering Boot Document — repository truth without chat history |
| **Last Updated** | 2026-07-08 |
| **Living document** | Update on stage, milestones, architecture, or mission changes |

> **Read this file first** when joining the repository.  
> Then complete §15 AI Boot Sequence before any work.

---

## 1. Project Identity

| Field | Value |
|-------|-------|
| **Project Name** | Donum Dei Atlas |
| **Repository Name** | DonumDei-Atlas — Repository 1 (first inheriting repository) |
| **Current Version** | Foundation — ATLAS-001 / ATLAS-EM-001 |
| **Current Branch** | `main` (initial) |
| **Repository Purpose** | Knowledge Preservation Repository — preserve, connect, and make discoverable institutional engineering wisdom across the Donum Dei Engineering Ecosystem. Atlas is not a product. |

**Parent:** [Repository 0 — Donum Dei Engineering Bridge](../DonumDei-TradingPlatform) (constitutional authority)

---

## 2. Mission

> Preserve knowledge.  
> Connect knowledge.  
> Make knowledge discoverable.  
> Preserve engineering wisdom for future generations.

Atlas exists so knowledge becomes **institutional** rather than **personal**.

**Mission heartbeat:** [MISSION.md](./MISSION.md)  
**Full operational truth:** [ENGINEERING_CONTEXT.md](./ENGINEERING_CONTEXT.md)

---

## 3. Current Engineering Stage

| Field | Value |
|-------|-------|
| **Current Stage** | Foundation — Repository 1 established |
| **Current Phase** | ATLAS-001 complete · Domain scaffolding initialized |
| **Current Objective** | Verify inheritance · publish ATLAS-EM-001 · establish knowledge domain structure |
| **Certification Status** | N/A — documentation-only repository |
| **Active Investigation** | None at foundation |

**Inheritance gate:** [EM-007](../DonumDei-TradingPlatform/docs/engineering-milestones/EM-007-repository-0-approved-for-inheritance.md) — satisfied

---

## 4. Engineering Philosophy

**Primary (inherited — read at source):** [The Donum Dei Way](../DonumDei-TradingPlatform/docs/THE-DONUM-DEI-WAY.md) — Faith · Character · Engineering · Service

**Atlas philosophy (owned):** [PHILOSOPHY.md](./PHILOSOPHY.md)

Governing principles (documented):

- Truth before convenience · Evidence before opinion · Humility before certainty
- Knowledge traceable to source · Relationships preserved as carefully as facts
- Repository 0 defines engineering · Atlas preserves knowledge
- Documentation-first · Search-oriented · Relationship-aware · Truth-centered

**Constitutional references (not duplicated):**

- [DDEF-PRINCIPLES.md](../DonumDei-TradingPlatform/docs/engineering-framework/DDEF-PRINCIPLES.md)
- [DDEOS-FOUNDATION-v1.0.md](../DonumDei-TradingPlatform/docs/engineering-framework/DDEOS-FOUNDATION-v1.0.md)
- [DDEOS-ENGINEERING-DNA.md](../DonumDei-TradingPlatform/docs/engineering-framework/DDEOS-ENGINEERING-DNA.md)

---

## 5. Current Architecture

Atlas has **no application runtime**. Knowledge architecture only.

```text
Boot layer (PROJECT_CONTEXT, ENGINEERING_CONTEXT, MISSION)
        ↓
Philosophy + Architecture (PHILOSOPHY, ARCHITECTURE)
        ↓
Knowledge domains (docs/knowledge-domains/)
        ↓
Evidence (reports/)
        ↓
Constitutional reference → Repository 0 (../DonumDei-TradingPlatform)
```

**Do not duplicate detail here.** Canonical reference: [ARCHITECTURE.md](./ARCHITECTURE.md)

---

## 6. Major Components

| Component | Role |
|-----------|------|
| **Boot documents** | Session initialization — PROJECT_CONTEXT, ENGINEERING_CONTEXT, MISSION |
| **Philosophy** | Atlas knowledge philosophy — PHILOSOPHY.md |
| **Architecture** | Knowledge structure — ARCHITECTURE.md |
| **Knowledge domains** | Subject-area organization — `docs/knowledge-domains/` |
| **Reports** | Milestones and curation evidence — `reports/` |
| **Roadmap** | Planned knowledge work — ROADMAP.md |
| **Constitutional reference** | Inherited standards from Repository 0 — `../DonumDei-TradingPlatform/docs/` |

No services, frontend, or production code exist in this repository by design.

---

## 7. Repository Structure

```text
DonumDei-Atlas/
├── PROJECT_CONTEXT.md       ← this file (AI / engineer boot)
├── MISSION.md               ← mission heartbeat
├── ENGINEERING_CONTEXT.md   ← living operational truth
├── PHILOSOPHY.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── README.md
├── docs/
│   ├── README.md
│   └── knowledge-domains/   ← domain knowledge organization
└── reports/                 ← milestone and evidence
```

**Where artifacts live:** philosophy & architecture → root · domains → `docs/knowledge-domains/` · evidence → `reports/` · constitutional authority → `../DonumDei-TradingPlatform`

---

## 8. Current Priorities

Ordered (highest first):

1. **Foundation complete** — ATLAS-EM-001 published
2. **Inheritance verified** — constitutional references resolve; no duplication
3. **Domain scaffolding** — initial knowledge domain files established
4. **Phase 2 planning** — experience intake and curation protocol (see [ROADMAP.md](./ROADMAP.md))

---

## 9. Recent Engineering Milestones

| Date | ID | Title |
|------|-----|-------|
| 2026-07-08 | **ATLAS-EM-001** | Atlas Foundation Repository Established |
| 2026-07-08 | ATLAS-001 | First inheriting repository charter executed |

**Parent milestone:** [EM-007](../DonumDei-TradingPlatform/docs/engineering-milestones/EM-007-repository-0-approved-for-inheritance.md)

---

## 10. Known Open Investigations

| Item | Status |
|------|--------|
| Domain content curation | Planned — Phase 2 |
| Experience intake from DDTP | Planned — protocol not yet authored |
| Discovery conventions | Planned — Phase 3 |

No active investigations at foundation. Use [DDES-002](../DonumDei-TradingPlatform/docs/ENGINEERING-STANDARDS/DDES-002-investigation-discipline-standard.md) when investigations begin.

---

## 11. Important Engineering Documents

| Document | Purpose |
|----------|---------|
| [README.md](./README.md) | Repository entry point |
| [MISSION.md](./MISSION.md) | Mission heartbeat |
| [ENGINEERING_CONTEXT.md](./ENGINEERING_CONTEXT.md) | Living operational truth |
| [PHILOSOPHY.md](./PHILOSOPHY.md) | Atlas knowledge philosophy |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | Knowledge architecture |
| [ROADMAP.md](./ROADMAP.md) | Planned work |
| [docs/README.md](./docs/README.md) | Documentation index |
| [docs/knowledge-domains/](./docs/knowledge-domains/) | Domain organization |
| [ATLAS-INHERITANCE-GUIDE](../DonumDei-TradingPlatform/docs/ENGINEERING-STANDARDS/ATLAS-INHERITANCE-GUIDE.md) | Inheritance protocol |
| [ATLAS-EM-001](./reports/ATLAS-EM-001-atlas-foundation-repository-established.md) | Foundation milestone |

---

## 12. AI Engineering Instructions

AI assistants working in Atlas shall:

- Read **PROJECT_CONTEXT.md** first
- Read **ARCHITECTURE.md** before structural changes
- **Reference** Repository 0 constitutional documents — never duplicate or redefine them
- Follow [The Donum Dei Way](../DonumDei-TradingPlatform/docs/THE-DONUM-DEI-WAY.md) and Atlas [PHILOSOPHY.md](./PHILOSOPHY.md)
- Preserve **provenance** — knowledge must trace to source
- Treat **relationships** as first-class knowledge
- **Not** add production code, dependencies, or automation unless explicitly authorized
- **Not** conflate DDTP product state with Atlas knowledge scope
- Update living docs (MISSION, ENGINEERING_CONTEXT, this file) when state materially changes
- Truth before prediction · Architecture before implementation

---

## 13. Next Engineering Session

Begin with:

1. Review [ROADMAP.md](./ROADMAP.md) Phase 2 objectives
2. Select first domain for content curation ([engineering.md](./docs/knowledge-domains/engineering.md) recommended)
3. Define experience intake protocol for DDTP investigations

---

## 14. Repository Health Summary

| Area | Status |
|------|--------|
| Foundation structure | ✅ Complete |
| Constitutional inheritance | ✅ Verified |
| Knowledge domains | 🟡 Scaffolded |
| Milestone evidence | ✅ ATLAS-EM-001 |
| Production code | ✅ None (by design) |
| Dependencies | ✅ None |
| Automation | ✅ None |

---

## 15. AI Boot Sequence

Every AI assistant shall initialize in this order before work:

1. Read **PROJECT_CONTEXT.md** (this file)
2. Read [ARCHITECTURE.md](./ARCHITECTURE.md)
3. Read [ENGINEERING_CONTEXT.md](./ENGINEERING_CONTEXT.md)
4. Read [MISSION.md](./MISSION.md) + latest [reports/](./reports/) evidence
5. Acknowledge Repository 0 constitutional references (no substitute for Atlas living context)
6. Read git status and active branch
7. Review current priorities (§8) and open work (§10)
8. Begin knowledge work

No structural or curation work shall begin before the boot sequence completes.

If documentation conflicts with practice, documentation governs until an investigation determines truth.

**Truth before prediction. Architecture before implementation.**

---

*DDES-001 boot instance · Donum Dei Atlas · Ad Majorem Dei Gloriam.*
