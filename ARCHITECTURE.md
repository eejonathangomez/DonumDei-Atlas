# ARCHITECTURE.md

## Atlas Knowledge Architecture

| Field | Value |
|-------|-------|
| **Repository** | Donum Dei Atlas — Repository 1 |
| **Type** | Documentation architecture (no runtime stack) |
| **Last Updated** | 2026-07-08 |
| **Production impact** | None |

---

## Purpose

Define how Atlas organizes, preserves, connects, and makes discoverable institutional knowledge across the Donum Dei Engineering Ecosystem.

Atlas has no application runtime. Its architecture is **knowledge architecture**.

---

## System context

```text
┌─────────────────────────────────────────────────────────────┐
│                  Donum Dei Engineering Ecosystem             │
├─────────────────────────────────────────────────────────────┤
│  Repository 0 (Engineering Bridge)                           │
│    Constitutional authority · standards · methodology        │
│                         │ references                         │
│                         ▼                                    │
│  Atlas (Repository 1)                                      │
│    Knowledge preservation · relationships · discovery        │
│                         ▲                                    │
│                         │ curates experience                 │
│  Trading Platform (DDTP) · future repositories               │
│    Engineering experience · investigations · case studies    │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer model

| Layer | Role | Atlas artifacts |
|-------|------|-----------------|
| **Boot** | Session initialization | `PROJECT_CONTEXT.md`, `ENGINEERING_CONTEXT.md`, `MISSION.md` |
| **Constitutional reference** | Inherited authority (not duplicated) | Links to Repository 0 paths |
| **Philosophy** | Why Atlas exists | `PHILOSOPHY.md` |
| **Architecture** | How knowledge is structured | This document |
| **Domains** | Subject-area organization | `docs/knowledge-domains/` |
| **Evidence** | Milestones, investigations, curation records | `reports/` |
| **Planning** | Future knowledge work | `ROADMAP.md` |

Dependencies flow **downward**: boot documents reference philosophy and architecture; domains reference constitutional standards; evidence references sources.

---

## Knowledge flow

```text
Experience (DDTP, future repos)
        ↓
Investigation / case study (DDES-002, DDES-003 patterns)
        ↓
Curation decision (Atlas)
        ↓
Domain placement + relationship links
        ↓
Institutional knowledge (discoverable, traceable)
```

Atlas does not automatically ingest product code or runtime state. Knowledge enters Atlas through **documented curation** with provenance.

---

## Domain architecture

Knowledge domains live in [docs/knowledge-domains/](./docs/knowledge-domains/).

| Domain | Scope |
|--------|-------|
| [engineering](./docs/knowledge-domains/engineering.md) | Donum Dei engineering practice, standards application |
| [artificial-intelligence](./docs/knowledge-domains/artificial-intelligence.md) | AI engineering partners, boot protocols, AI-friendly knowledge |
| [software](./docs/knowledge-domains/software.md) | Software design, architecture, implementation wisdom |
| [markets](./docs/knowledge-domains/markets.md) | Market understanding, trading context (curated, not live data) |
| [science](./docs/knowledge-domains/science.md) | Scientific reasoning applicable to engineering |
| [mathematics](./docs/knowledge-domains/mathematics.md) | Quantitative foundations |
| [philosophy](./docs/knowledge-domains/philosophy.md) | Reasoning, ethics, epistemology in engineering context |
| [theology](./docs/knowledge-domains/theology.md) | Faith integration per The Donum Dei Way |

Each domain file defines scope, relationship to other domains, and curation rules. Content grows over time; structure is established at foundation.

---

## Relationship model

Atlas treats relationships as first-class knowledge:

| Relationship type | Example |
|-------------------|---------|
| **Constitutional** | Atlas standard → Repository 0 DDES spec |
| **Experiential** | Atlas domain entry → DDTP DECS investigation |
| **Cross-domain** | markets ↔ mathematics ↔ software |
| **Temporal** | Milestone → prior investigation → outcome |
| **Inheritance** | Future repo → Atlas domain → Repository 0 standard |

Every curated entry should declare: **source repository**, **source artifact**, **curation date**, **relationships**.

---

## Inheritance architecture

Per [ATLAS-INHERITANCE-GUIDE](../DonumDei-TradingPlatform/docs/ENGINEERING-STANDARDS/ATLAS-INHERITANCE-GUIDE.md):

| Class | Atlas behavior |
|-------|----------------|
| **Inherit** | Reference Repository 0 constitutional documents unchanged |
| **Extend** | Author Atlas instances using Repository 0 patterns (boot docs, reports, DECS when earned) |
| **Own** | Atlas knowledge domains, curation, relationships, milestones |

Physical DDEB repository split is **deferred**. Atlas references `../DonumDei-TradingPlatform` paths until a future split is earned.

---

## Non-goals

| Excluded | Reason |
|----------|--------|
| Production code | Atlas is knowledge layer only |
| Runtime services | No servers, databases, or automation at foundation |
| Constitutional duplication | Single source of TRUTH in Repository 0 |
| Product truth | DDTP certification and Gateway state remain in DDTP |

---

## Expansion path

Future architecture may add (when earned):

- Search index conventions
- Cross-repository link registry
- DECS library in Atlas (`docs/engineering-case-studies/`)
- Submodule or pin strategy for constitutional references
- Physical DDEB split with updated reference paths

Foundation phase establishes structure only.

---

*Atlas Knowledge Architecture · Ad Majorem Dei Gloriam.*
