# EOS V2 — AI-Assisted Engineering Operating System

**Status:** Architectural Seed — preserved, dormant-ready, referenceable  
**Captured:** 2026-10-20  
**Implementation authority:** None. This document preserves the concept and proposed direction; it does not authorize runtime, production, trading, infrastructure, or security changes.  
**Relationship to Atlas:** This seed extends the Atlas vision from knowledge preservation toward a portable engineering operating-system concept. The current canonical Atlas architecture remains documentation/knowledge-only until a later architectural decision promotes this seed.

---

## 1. Vision

EOS is a portable AI-assisted engineering operating system that turns accumulated engineering experience into repeatable development and operational workflows.

The north star is a **system that builds systems**: an AI agent can understand a project, recover its context, plan work, retrieve institutional knowledge, inspect and change implementation, interact with authorized machines, test and commission results, monitor operation, diagnose failures, preserve evidence, and feed validated lessons back into the knowledge system.

The AI runtime is replaceable. Cursor is a strong first execution host, but Cursor itself is not EOS.

---

## 2. System-of-record contract

EOS deliberately separates authority:

| Concern | System of record | Purpose |
|---|---|---|
| Work / execution state | **Jira** | Epics, tasks, dependencies, blockers, acceptance criteria, progress, evidence links |
| Engineering knowledge | **Confluence** | Architecture, design decisions, procedures, commissioning results, lessons, incident reviews |
| Implementation truth | **Git / GitHub** | Code, configuration, tests, version history |
| Workflow / policy truth | **EOS** | Skills, methods, schemas, policies, orchestration, gates |
| Reasoning / orchestration | **AI Agent** | Context reconstruction, planning, tool selection, reasoning, execution coordination |
| Runtime / machine truth | **EOS Nodes** | Authorized machine health, files, logs, processes, services and controlled actions |

The AI is not the database. Skills are not the project database. Project state and knowledge remain durable outside any single AI conversation.

---

## 3. Core architecture

```text
                              USER
                               |
                               v
                         +-----------+
                         | EOS AGENT |
                         +-----+-----+
                               |
       +-----------------------+------------------------+
       |              |              |                 |
       v              v              v                 v
   EOS SKILLS       JIRA         CONFLUENCE        GIT/GITHUB
   procedures       work          knowledge       implementation
       |              |              |                 |
       +-----------------------+------------------------+
                               |
                               v
                         EOS NODE LAYER
                               |
                 +-------------+-------------+
                 |             |             |
                 v             v             v
             Home PC       Test/Lab PC    Cloud Host
             Donum         Hardware       Services
             Files         Logs           Jobs/Data
```

Cross-cutting controls:

```text
IDENTITY + POLICY + PERMISSIONS + AUDIT + SAFETY/RISK + HUMAN GATES
```

---

## 4. EOS core loop

The reusable engineering loop mined from the existing skill corpus is:

```text
Context + Experience + Policy
             |
             v
          Evidence
             |
             v
          Reasoning
             |
             v
          Decision
             |
             v
           Action
             |
             v
        Verification
             |
       +-----+-----+
       v           v
   Monitoring   Recording
       |           |
       +-----+-----+
             v
          Learning
             |
             +----> Experience
```

Operational lifecycle:

```text
Preflight -> Commission -> Operate -> Monitor
                ^                    |
                +-- Diagnose <- Recover
                       |
                       v
                      Learn
```

---

## 5. Skill-system direction

The existing engineering corpus contains approximately 105 accumulated skills. They are not discarded. They are mined for reusable engineering experience.

Each existing skill should eventually be classified into one or more of:

1. Universal principle
2. Reusable engineering method
3. Reusable capability
4. Orchestrated workflow
5. Domain-specific implementation
6. Historical lesson / failure pattern
7. Publisher / presentation layer
8. Alias / deprecated behavior

A mature EOS skill should be a **reusable procedure for accomplishing an engineering objective**, not a container for every fact about a system.

Proposed skill contract:

```text
Skill
  Intent
  Trigger / problem
  Preconditions
  Consumes
  Evidence required
  Procedure
  Decision rules
  Actions
  Verification
  Produces
  State changes
  Failure modes
  Recovery
  Human / risk gates
  Owns
  Calls
  Does Not Own
```

Project-specific addresses, credentials, paths, machine definitions and similar state should live in context/profile systems rather than being duplicated across skills.

---

## 6. First mined reusable patterns

The first mining pass condensed the skill corpus into a smaller reusable pattern set:

1. Context Reconstruction
2. System Preflight
3. Canonical System Profile / Context Registry
4. Heartbeat / Liveness
5. Layered Health Detection
6. Independent Protection
7. Controlled Recovery
8. Audit / Flight Recorder
9. Forensic Reconstruction / Timeline
10. Staged Commissioning
11. Baseline & Deviation Detection
12. Evidence Before Judgment
13. Structured Risk Analysis / FMEA-like reasoning
14. Persistent Engineering Lessons / Experience Store
15. Plan -> Dependencies -> Execute -> Observe -> Replan

These patterns are candidates for EOS primitives and methods. They should be extracted only when a real project needs them, avoiding premature abstraction.

---

## 7. Jira operating model

Jira is the authoritative execution ledger.

EOS should be able to:

```text
work.search()
work.create()
work.update()
work.transition()
```

A well-formed engineering work item should be capable of carrying:

- objective
- parent initiative / epic
- dependencies
- blockers
- risk level
- acceptance criteria
- implementation evidence
- verification evidence
- design/knowledge references
- current state

The existing project-planning experience already supports the pattern:

```text
Plan -> Ticket creation -> Dependency map -> Schedule -> Timeline -> Refresh from actual state
```

EOS should query Jira at startup to reconstruct active work rather than depending on conversational memory.

---

## 8. Confluence operating model

Confluence is institutional engineering memory.

Candidate information architecture:

```text
EOS Knowledge
|
+-- Architecture
|   +-- EOS Architecture
|   +-- AI Architecture
|   +-- Design Principles
|
+-- Skills
|   +-- Skill Catalog
|   +-- Skill Standards
|   +-- Skill Dependencies
|
+-- Engineering Knowledge
|   +-- Lessons Learned
|   +-- Patterns
|   +-- Failure Modes
|   +-- Troubleshooting
|
+-- Projects
|   +-- Donum Dei
|   +-- Test Systems
|   +-- Future Projects
|
+-- Operations
|   +-- Commissioning
|   +-- Monitoring
|   +-- Recovery
|   +-- Incident Reviews
|
+-- Standards
    +-- Safety / Risk
    +-- Documentation
    +-- Testing
    +-- Release
```

Validated reusable lessons should become first-class knowledge with provenance rather than disappearing in chat history.

Proposed lesson model:

```text
Lesson
  Context
  Failure / problem
  Root cause
  Resolution
  Evidence
  Applicability
  Confidence
  Supersedes
```

---

## 9. AI agent

EOS should have an AI agent capable of directly using EOS skills and authorized adapters for Jira, Confluence, Git/GitHub and EOS Nodes.

Cursor is the proposed first host because it is already part of the engineering workflow and can act as the implementation worker. The architecture must keep the AI runtime replaceable.

Example project-start behavior:

```text
1. Identify project
2. Load EOS context and applicable policies
3. Query Jira for active work, blockers and priorities
4. Query Confluence for architecture, decisions and lessons
5. Inspect Git state
6. Inspect relevant EOS Node/runtime state when authorized
7. Reconstruct current project state
8. Recommend / select next permitted action
9. Execute through the applicable skill/workflow
10. Verify result
11. Preserve evidence
12. Update Jira
13. Update Confluence when durable knowledge changed
14. Propose/store a reusable lesson when earned
```

---

## 10. EOS Node system — remote computers

Authorized computers become **EOS Nodes**. Examples include the home desktop, engineering/test laptops and future cloud hosts.

The goal is structured remote-machine capability, not dependence on GUI remote desktop.

Conceptual interface:

```text
nodes.list()
node.status(node)
node.health(node)
node.files.list(node, path)
node.files.read(node, path)
node.logs.tail(node, source)
node.processes.list(node)
node.service.status(node, service)
node.command.run(node, approved_action)
```

Capability levels:

| Level | Examples | Default control |
|---|---|---|
| Observe | health, files, logs, process/service state, Git status | autonomous where authorized |
| Diagnose / Test | diagnostics, approved safe tests | autonomous/policy-controlled |
| Operate / Recover | restart approved service, approved recovery workflow | policy-controlled and audited |
| Modify | configuration/software/file mutations | permission-controlled |
| Critical | security changes, privileged arbitrary commands, risk-policy changes, live trading enablement | explicit human gate |

Remote access should use authenticated encrypted private connectivity/gateways. Public exposure of RDP/SMB is not part of the design.

The node layer should support heartbeat, health and event reporting so EOS can observe machine state consistently.

---

## 11. Autonomy model

EOS should operate inside a protected envelope.

Typical policy:

- Read/search knowledge: autonomous
- Inspect code and machine status: autonomous when authorized
- Run safe tests: autonomous within defined scope
- Create draft documentation: autonomous
- Add evidence/status updates: autonomous or low-friction
- Create development subtasks: semi-autonomous
- Significant architecture changes: review gate
- Production merges/deployments: policy gate
- Risk/safety policy changes: explicit human approval
- Disable watchdog/protection: explicit human approval
- Enable live trading or change capital/risk limits: explicit human approval

Independent deterministic safeguards remain authoritative for safety/risk-critical controls. The AI does not become the sole safety or financial-risk authority.

---

## 12. Agent roles

Initially these may be roles/workflows of one agent rather than separate models:

```text
                     EOS AGENT
                         |
       +-----------------+-----------------+
       |                 |                 |
    ARCHITECT          BUILDER          OPERATOR
       |                 |                 |
 requirements           code             monitor
 architecture           test             diagnose
 risk analysis          verify           recover
       |                 |                 |
       +-----------------+-----------------+
                         |
                      AUDITOR
                         |
                      evidence
                      validation
                         |
                       SCRIBE
                         |
                  Jira / Confluence
                  lessons / reports
```

---

## 13. Donum Dei as first proving ground

Donum Dei should be the first new product/project to deliberately consume EOS patterns rather than receiving a large EOS rewrite.

Initial candidate implementation order:

1. Flight Recorder / structured event evidence
2. Unified Health & State model
3. Heartbeat / independent watchdog
4. System preflight
5. Commissioning / promotion gates
6. Recovery policy
7. Trading-system risk audit
8. Experience Store / reusable lessons

Proposed Donum commissioning lifecycle:

```text
Unit / Integration
      -> Backtest
      -> Historical Replay
      -> Paper
      -> Unattended Paper
      -> Shadow Live
      -> Limited-Capital Live
      -> Controlled Scale-Up
      -> Production
```

Each promotion must have explicit acceptance criteria and evidence. Software correctness and strategy validity are separate concerns.

---

## 14. Portability

EOS should remain domain-independent:

```text
EOS + Donum Context + Trading Skills      -> Trading Platform
EOS + Test Context + Test/HW Skills       -> Reliability/Test System
EOS + Robotics Context + Robotics Skills  -> Robotic System
EOS + Manufacturing Context               -> Manufacturing Automation
EOS + Future Project Context              -> Future system
```

The domain changes. The engineering operating system remains.

---

## 15. Relationship to DORY

DORY remains the governed architect-to-worker execution machinery already proven in the ecosystem. It can later become one execution adapter/control-plane mechanism used by EOS rather than being conflated with EOS itself.

Conceptually:

```text
User / Architect
      |
      v
     EOS
 planning / policy / knowledge / skills
      |
      v
    DORY
 governed execution handoff
      |
      v
   Cursor
 implementation worker
```

No DORY runtime change is required to preserve this seed.

---

## 16. Proposed EOS V2 repository shape

This is a target model, not yet an implementation commitment:

```text
EOS/
+-- core/
|   +-- context/
|   +-- state/
|   +-- evidence/
|   +-- policy/
|   +-- execution/
|   +-- verification/
|
+-- skills/
+-- methods/
+-- workflows/
+-- schemas/
+-- policies/
+-- experience/
+-- adapters/
|   +-- jira/
|   +-- confluence/
|   +-- git/
|   +-- nodes/
|
+-- agents/
+-- project-packs/
+-- docs/
```

Do not migrate or delete the existing skill corpus merely to match this shape. Extraction should preserve provenance and be validated incrementally.

---

## 17. Migration strategy

### Phase 0 — Preserve
- Keep the existing 105-skill corpus intact.
- Preserve this architectural seed.
- Do not destructively refactor working systems.

### Phase 1 — Mine
- Inventory all skills.
- Extract principles, methods, capabilities, workflows, domain instances and lessons.
- Identify duplication, hidden state and policy coupling.

### Phase 2 — Define contracts
- Define skill contract.
- Define context/profile schemas.
- Define evidence/event schema.
- Define policy and human-gate model.
- Define adapter interfaces.

### Phase 3 — Connect work and knowledge
- Establish Jira project/work model.
- Establish Confluence EOS space/hierarchy.
- Connect AI agent to both with least privilege.

### Phase 4 — Establish node capability
- Define EOS Node protocol/profile.
- Start with read-only health/files/logs/process visibility on one authorized machine.
- Add controlled actions only after audit/policy boundaries are proven.

### Phase 5 — Prove with Donum
- Extract only the EOS primitives Donum actually needs.
- Implement and validate them in real work.
- Promote reusable lessons back into EOS.

### Phase 6 — Cross-domain proof
- Apply EOS to a materially different engineering project.
- Refine abstractions based on evidence.

---

## 18. Next decision / resume point

When this seed is resumed, do **not** begin by rewriting skills or changing Donum production behavior.

Start with:

1. Review this seed against the current Atlas/DDEF/DORY architecture.
2. Finish systematic mining of the 105-skill corpus into a canonical taxonomy/matrix.
3. Decide the durable home and boundaries of EOS V2 relative to Atlas and DDEF.
4. Design the Jira project hierarchy and Confluence information architecture.
5. Define the EOS Agent contract and permissions.
6. Define the EOS Node read-only MVP.
7. Select the first Donum proving-ground capability (recommended: Flight Recorder).

**Dormant-ready state:** the concept is preserved here with enough context to resume without relying on chat memory.

---

## 19. Guiding principles

- Preserve experience before refactoring it.
- Evidence before interpretation.
- Context before action.
- Observe before automate.
- Verification after action.
- Autonomy inside a protected envelope.
- Independent safeguards for safety/risk-critical behavior.
- Durable systems of record over conversational memory.
- Reusable methods over project-specific hardcoding.
- Let real projects pull abstractions out of EOS; do not over-abstract in advance.
- Keep AI runtimes, work trackers, knowledge stores and remote-access implementations replaceable behind EOS contracts.

---

*Architectural Seed — EOS V2 AI-Assisted Engineering Operating System*  
*Preserved for future architectural review and promotion.*
