# Efficiency Loop v1.0

Status: provisional specification. Advisory. Not execution authority.  
Canonical home: PENDING.  
Provisional placement: this knowledge repository, because it is an existing non-product store.  
This file is the single provisional copy. Do not copy it into a product or a control plane.

DORY, Donum, Cursor, a broker, a language, and this repository are not the definition of the loop. Examples at the end are labeled examples.

No prior document titled Efficiency Loop was found in the DORY or Donum architecture pages. Donum's DDEOS / DDEF material is a broader, branded engineering framework. It is related evidence. It is not this version.

---

## 1. Purpose

The Efficiency Loop is the smallest complete way to change a system without confusing intention, evidence, permission, and proof.

It applies to software, hardware, tests, automation, agent work, infrastructure, safety systems, documentation, research, debugging, deployment, and recovery. A domain may add rules. Those rules do not rewrite this loop.

## 2. Scope

Use it when a change, a repair, a release, a recovery, or a decision can affect a system or its record.

A read, a review, and a document-only task still enter the loop. Their execution step changes nothing in the target system.

This loop does not grant permission to act. A procedure that describes how to act is knowledge. Permission is a separate decision by the owner of the system.

## 3. Core principles

Verify the present before acting. Evidence outranks intention, memory, and a previous success. Choose the smallest objective that is complete, not the smallest phrase and not the largest design. Protect known-good state and unrelated work. Take only the authority the objective needs. Fail closed where an action is hard to undo or can cause harm. Understand the mechanism before changing it. Do not add complexity until the simpler mechanism is shown to be insufficient. Do not call an implementation proven. Do not turn UNKNOWN into PROVEN by tone. Knowledge does not grant authority. A significant change is unfinished while its implementation, proof, and governing description disagree. Return authority when the bounded work ends.

## 4. The loop

```text
VERIFY PRESENT TRUTH
→ DEFINE THE SMALLEST COMPLETE OBJECTIVE
→ PROTECT KNOWN-GOOD STATE AND UNRELATED WORK
→ BOUND THE AUTHORITY
→ EXECUTE ONLY INSIDE THAT BOUND
→ OBSERVE WHAT ACTUALLY HAPPENED
→ UNDERSTAND BEFORE CHANGING ANYTHING FURTHER
→ QUALIFY AT THE PROOF LEVEL THE RISK REQUIRES
→ CONFIRM NOTHING OUTSIDE THE OBJECTIVE CHANGED
→ PRESERVE THE RESULTING STATE
→ RETURN AUTHORITY
→ SELECT THE NEXT SMALLEST COMPLETE STEP, OR STOP
```

Learning, failure analysis, transition, and the change record are sub-loops. Invoke them when their entry condition is true. Do not run them as ceremony on every trivial edit.

## 5. Entry conditions

Enter when there is a proposed change, a failure, a recovery, or a need to decide. If the present state cannot be verified, stop. Do not formalize or repair from an uncertain foundation.

## 6. Stages

VERIFY PRESENT TRUTH. Purpose: know the system as it is. Input: the live or recorded state named by the objective. Action: read identity, health, scope, and protected work. Output: a statement of what is true, including unknowns. Exit: the statement is specific enough to detect a material change. Failure: acting on the intended state or on memory.

DEFINE THE SMALLEST COMPLETE OBJECTIVE. Purpose: bound the work. Input: the need and the verified state. Action: name the outcome that closes the need and name what will not be done. Output: one objective. Exit: a stranger can tell done from not done. Failure: a label that hides several changes, or a fragment that cannot stand alone.

PROTECT KNOWN-GOOD STATE AND UNRELATED WORK. Purpose: keep a return path and keep other work intact. Input: the known-good identity and any unrelated changes. Action: record them and do not clean, absorb, or overwrite them. Output: a protected boundary. Exit: the intended change can be told apart from protected work. Failure: a broad clean, stash, or reset.

BOUND THE AUTHORITY. Purpose: separate permission from the desire to act. Input: the objective and the owner's grant. Action: limit the grant to that objective. A read-only task's grant is permission to read. Output: an explicit bound. Exit: the actor can say what is allowed and what is refused. Failure: inferring permission from health, activity, a document, a skill, or a past success.

EXECUTE ONLY INSIDE THAT BOUND. Purpose: perform the change, or perform no system change when the task is observational. Input: the bound. Action: the permitted change and nothing adjacent. Output: the attempted result. Exit: the action stopped at the bound. Failure: a helpful extra change.

OBSERVE WHAT ACTUALLY HAPPENED. Purpose: replace the plan with evidence. Input: logs, tests, diffs, measurements, or inspected state. Action: record what changed and what did not. Output: evidence. Exit: the evidence can confirm or contradict the intent. Failure: treating the plan as the result.

UNDERSTAND BEFORE CHANGING ANYTHING FURTHER. Purpose: find the mechanism. Input: the evidence. Action: name cause, or name that the cause is unknown. Output: a mechanism account or an explicit unknown. Exit: the next change follows that account. Failure: a symptom patch or a redesign during diagnosis.

QUALIFY AT THE PROOF LEVEL THE RISK REQUIRES. Purpose: match proof to harm. Input: the risk class and the evidence. Action: run the checks that can falsify the claim, including the failure path when harm is hard to undo. Output: a proof label, not a vibe. Exit: the label matches section 11. Failure: calling code existence a proof, or skipping the adjacent failure on a safety-critical change.

CONFIRM NOTHING OUTSIDE THE OBJECTIVE CHANGED. Purpose: catch collateral mutation. Input: the objective boundary and the after-state. Action: compare. Output: a regression statement. Exit: collateral changes are none, or they are named and owned. Failure: declaring done from the happy path alone.

PRESERVE THE RESULTING STATE. Purpose: make the new known-good state recoverable. Input: the qualified result. Action: record the checkpoint level the risk requires. Output: an identity a later actor can find. Exit: the checkpoint does not silently replace a stronger qualified baseline. Failure: moving a qualified baseline just because a document or a telemetry note advanced.

RETURN AUTHORITY. Purpose: end the borrow. Input: the finished or stopped objective. Action: hand control back to the owner. Output: no lingering permission. Exit: the actor is not still authorized for the next idea. Failure: treating completion as permission for the following task.

SELECT THE NEXT SMALLEST COMPLETE STEP, OR STOP. Purpose: continue only by a new bound. Input: the remaining need. Action: pick one next objective, or stop for review. Output: the next entry, or a stop. Exit: the next step has its own verify. Failure: chaining unreviewed work because the loop feels productive.

## 7. Irreversible action model

```text
TRUTH → AUTHORITY → EXECUTION → OBSERVE → RECONCILE
```

TRUTH is the verified present state relevant to the action. AUTHORITY is explicit permission and a bound. EXECUTION is the permitted state change. A read-only task has an execution of no target mutation. OBSERVE is evidence of what occurred. RECONCILE is bringing the record and the control state back to that evidence.

This model sits inside BOUND, EXECUTE, OBSERVE, and PRESERVE. It is universal. Safety-critical work uses a durable authority record. Ordinary work may use the written objective as the bound, as long as the bound is explicit. Human-only work uses the same order. The person is the authority source. The loop does not require a particular tool to hold that authority.

Knowledge, health, activity, selection, and history do not skip to EXECUTION.

## 8. Change record

Use this for a significant change. A significant change alters authority, a safety boundary, persisted meaning, an external interface, or the governing description. A label rename is not significant.

Required: observation, problem, decision, invariants, evidence, new state, recovery point.  
Conditional: intent, when the problem does not already say it. Expected behavior, when it is not already the invariant. An implementation pointer.

```text
OBSERVATION
→ PROBLEM
→ DECISION
→ INVARIANTS
→ EVIDENCE
→ NEW STATE
→ RECOVERY POINT
```

Order the decision before the implementation so the record says why. Keep it short enough that a later reader can audit it. Do not open a second document system for a one-line fix.

## 9. Preservation contract

Before a significant change, answer: what must still work after this change?

Include the invariants, the user-visible behavior, the interfaces, the data, the compatibility promises, the recovery path, the authority boundaries, unrelated work, and the historical evidence that must remain findable.

For a trivial change, the non-goals in the objective are enough.

For a significant architectural decision, also answer: why not the simpler alternative? If the simpler alternative preserves the invariants, use it. Keep a repeated check when that repetition is the boundary before an irreversible action.

## 10. Known-good checkpoints

A checkpoint is an identity plus the claim it supports. Heavier claims need heavier checkpoints.

MINIMUM. Implementation identity, what was verified, and what remains unknown. Enough for a low-risk change.

FULL OPERATING. Implementation truth, runtime or system truth, operational intent, and a recovery contract. Add protected unrelated work and unresolved risks when they exist.

SAFETY-CRITICAL. The full checkpoint, plus the proof level, the authority boundary, and the identity of external dependencies that can change the outcome.

A later note, document, or heartbeat does not replace a safety-critical checkpoint. Name both identities when they differ.

## 11. Proof model

Do not promote a claim past its evidence.

```text
UNKNOWN
IMPLEMENTED
UNIT-PROVEN
INTEGRATION-PROVEN
SYSTEM-PROVEN
HISTORICALLY PROVEN
CURRENTLY PROVEN
BLOCKED
HISTORICAL
```

IMPLEMENTED means the mechanism exists. UNIT-PROVEN means a isolated check passed. INTEGRATION-PROVEN means the parts were exercised together. SYSTEM-PROVEN means the deployed or end-to-end path was exercised. HISTORICALLY PROVEN means an earlier run passed and is not permission for the next run. CURRENTLY PROVEN means the present deployment or present evidence still supports the claim. BLOCKED means a gate refuses the action. HISTORICAL means the artifact remains and does not govern.

UNKNOWN becomes a proof label only when evidence of that class exists. A document that asserts the label is not the evidence.

## 12. Uncertainty

UNKNOWN stays UNKNOWN until evidence changes it.

Missing evidence stays unknown. Contradictory evidence stays unresolved until the contradiction is shown. Stale evidence is labeled with its time. Historical evidence proves the past run. Inferred behavior is a hypothesis. Intended behavior is a design. Observed behavior is what the evidence shows. When they differ, say so. Do not let the smoothest story win.

## 13. Knowledge and authority

```text
KNOWLEDGE DOES NOT GRANT EXECUTION AUTHORITY
```

Documentation, lessons, skills, reports, prior successes, old checkpoints, recommendations, plans, and model memory are knowledge. They may describe how to act. They do not permit the act. Permission comes from the owner of the system, in the bound for this objective. A future agent uses the same rule. Reading this file is not permission to change a system.

## 14. Documentation closure

A significant architectural change is complete only when the governing description, the implementation, and the proof agree, and the recovery implication is recorded.

```text
THE GOVERNING DESCRIPTION STATES THE CONTRACT.
THE IMPLEMENTATION DOES THE CONTRACT.
THE PROOF TESTS THE CONTRACT.
HISTORY EXPLAINS WHY THE CONTRACT EXISTS.
```

If they disagree, the change is not complete. What the system does is settled by the implementation and the observed evidence. The governing description is then corrected or marked historical. A stale document does not outrank a failing check. A new intention does not outrank an unfixed implementation. Trivial edits do not need this ceremony.

## 15. Failure sub-loop

Enter when evidence shows a failure or a contradicted intent.

```text
OBSERVE THE FAILURE
→ PRESERVE THE EVIDENCE
→ CONTAIN THE RISK
→ REPRODUCE OR CHARACTERIZE IT
→ NAME THE ROOT CAUSE OR LEAVE IT UNKNOWN
→ NAME THE INVARIANT THAT FAILED
→ CHANGE THE MECHANISM
→ RE-TEST THE ORIGINAL FAILURE
→ TEST THE ADJACENT FAILURE PATH
→ CHECK FOR REGRESSION
→ RECORD THE LESSON IF IT GENERALIZES
→ PRESERVE THE NEW KNOWN-GOOD STATE
```

This is a sub-loop of UNDERSTAND and QUALIFY. A difficult failure should leave the system easier to understand, not only harder to break. Do not redesign the surrounding system while containing the failure.

## 16. Transition sub-loop

Use this when changing project, environment, deployment, machine, agent, or recovery context.

```text
CLOSE
→ PROTECT
→ SELECT
→ RESTORE
→ VERIFY
→ RESUME
```

Close finishes or explicitly stops the current work. Protect the known-good state and unrelated work. Select the next context. Restore only what that context claims. Verify the restored identity. Resume only inside a new authority bound. The transition itself does not create permission to execute.

## 17. Simplicity

Make it work. Make it correct. Understand why it works. Then make it simple.

Prefer the smallest complete mechanism, the fewest moving parts, and one canonical statement where a second statement would become a second truth. Keep duplication when the two copies protect a real boundary, such as a repeated check immediately before an irreversible action. Do not add an abstraction, a framework, or a parallel store because it might be useful later. Do not remove a check because it looks redundant until the race it covers is disproven.

## 18. Learning sub-loop

Enter when an observation might help a later task.

```text
OBSERVATION
→ LOCAL LESSON
→ GENERALIZE ONLY WITH A STATED BASIS
→ DEDUPLICATE
→ ATTACH PROVENANCE
→ STORE AS ADVISORY
→ MAKE IT DISCOVERABLE
→ REVALIDATE WHEN THE WORLD CHANGES
```

A local lesson may be stored immediately as local and advisory. Promotion to a universal rule needs either a second independent case or an explicit qualification that names the boundary of the claim. Do not generalize from one incident by adjective. Do not store a second copy of an existing lesson. A stale lesson is marked stale. It is not deleted just because it is old, and it is not authority while it is current.

## 19. Safety-critical extension

Use this when the action can cause harm that is hard to undo, including safety interlocks, live control, irreversible external mutation, or authority itself.

Add a durable authority bound, the safety-critical checkpoint, adversarial checks of the refusal path, the preservation contract, the change record, and a named recovery point. A second check immediately before the irreversible action stays unless a proof shows the window cannot change the decision. UNKNOWN on a safety claim blocks the action. Historical proof does not authorize the next action. Recovery restores a safe state and does not silently re-arm the action.

Low-risk work does not carry this pack. Section 21 shows the difference.

## 20. Examples

EXAMPLE, DORY. Verified mailbox identity is truth. A validated ready publication is authority. A worker run is execution. A result and an audit are observation. Return to the idle owner is reconcile. Health, an active project, a selected candidate, a lesson, and a stored request are not authority. Those nouns are DORY's. The loop does not require them.

EXAMPLE, DONUM. Broker position and account state are part of truth before an order. A pre-issued mutation authorization plus the gates is authority. The broker place call is execution. Callbacks are observation. The local record is reconciled to those callbacks. A status display, a chart reconstruction, a report, and an older fill are not authority. Those nouns are Donum's. The loop does not require them.

EXAMPLE, a document-only task. Truth is the current text and the system it describes. Authority is permission to edit that text. Execution changes the document and not the system. Observation is the diff. Qualification is an adversarial read. No safety interlock is moved.

## 21. Anti-patterns

Acting before verify. Fixing a symptom before the mechanism is known. Taking broad authority for a narrow task. Cleaning unrelated work. Inferring authority from health, activity, or selection. Inferring permission from history. Calling an implementation proven. Resolving UNKNOWN by narrative. Adding complexity before the simpler mechanism fails. Keeping two governing truths. Changing the architecture during recovery. Letting the governing description drift. Letting a lesson or a skill become hidden permission. Declaring completion before the outside-the-objective check.

## 22. Versioning

PATCH clarifies wording and does not change a stage, a proof label, or the authority rule.  
MINOR adds an optional sub-loop, a proof label, or an example. Existing stages keep their meaning.  
MAJOR changes stage order, what authority means, or what completion requires.

This document is v1.0. It does not version DDEOS, DORY, or Donum.

## 23. Practical scale

SMALL, LOW RISK. Example: rename a label. Verify the string and its callers. Bound the edit. Change the label. Observe the diff. Qualify by inspection or the existing check that covers the label. Confirm no other behavior changed. Preserve by the change itself. Return. No change record. No lesson. No safety checkpoint.

NORMAL. Example: add a read-only endpoint. Verify the current route table. Define the response and the non-goals. Bound the edit to that route. Execute. Observe tests and the route list. Understand any failure before expanding scope. Qualify with the unit or integration check that fits. Confirm no write path was added. Record a minimum checkpoint. Return.

SAFETY-CRITICAL. Example: change an interlock or an irreversible external mutation boundary. Use section 19. Name the first irreversible action. Prove the refusal path. Keep the immediate pre-action recheck unless the race is disproven. Historical success does not authorize the new path. UNKNOWN blocks the change.

## 24. Placement

Canonical home remains PENDING until a repository exists whose only role is vendor-neutral engineering method, or until the owner designates one.

This provisional copy lives here so it is versioned, discoverable, and outside the trading product and the live control plane. Atlas branding on the surrounding repository does not make this loop a Donum rule or an Atlas grant of authority. Project documents may later link here. They should not paste a second full copy.
