# Codex Adoption Experience — 2026-11-24

**Purpose:** Preserve the complete observed onboarding experience so a future AI provider can be evaluated and added without losing what we learned.  
**Status:** Codex installed, manual read-only architecture handshake and one disposable read-only DORY source investigation **PASS / PASS WITH CONDITIONS (Codex-reported)**. Reporting preference was adopted in conversation and global `AGENTS.md` created/read-back **(Codex-reported)**. **Not qualified as DORY worker**.  
**Case owner:** Founder. **Architectural reviewer:** Atlas. **Target capability:** AI software engineering worker.  
**Companion reusable runbook:** [AI Provider Onboarding and Qualification V1](AI-PROVIDER-ONBOARDING-RUNBOOK-V1.md)  
**Architecture:** [AI Organization and Provider Contracts V1](../architecture/AI-ORGANIZATION-AND-PROVIDER-CONTRACTS-V1.md)  
**Evidence provenance:** Founder-visible setup screenshots and chat, Codex output relayed in conversation, and independently verified Atlas GitHub document/control reads where marked. No local Windows command results have been independently reproduced by Atlas. No credentials are stored here.

## 1. Why this adoption began

Founder reported hitting a Cursor usage allowance for the first time, with resets pending in multiple days. Rather than idle engineering development or immediately replace DORY, Founder and Atlas explored using OpenAI Codex as a manual coding agent while preserving the existing Cursor-based DORY workflow. This also became a real-world test of vendor-independent organizational positions.

**Intended short-term outcome:** safely onboard Codex in an editor, recover company procedures, then perform bounded independent engineering work.  
**Long-term hypothesis:** Codex or another provider could fill the Engineering Worker position through a **qualified** DORY adapter, without becoming the authority for publication, safety, or acceptance.  
**Important nuance:** ChatGPT and Codex are distinct products, but are not independent underlying AI vendors. Provider redundancy remains unproven.

## 2. Chronological onboarding log

All events below occurred in the 2026-11-24 adoption conversation; precise local timestamps were not recorded. Distinguish **Founder report / Codex report / Atlas verified GitHub** from direct runtime verification.

| Step | What was attempted | Actual evidence, observation and correction | Status / provenance |
| --- | --- | --- | --- |
| 01 — Define need | Find coding capacity while Cursor allowance resets | Founder wanted to continue DORY and Donum engineering with an alternative agent | DECIDED · Founder |
| 02 — Clarify the tool roles | Compare ChatGPT, Codex, DORY and Cursor | Founder adopted position/capability/provider separation: Atlas architect, DORY orchestrator, worker replaceable | DECIDED · Founder + Atlas |
| 03 — Preserve company architecture | Document minimum external capabilities and worker contracts | Atlas published `docs/architecture/AI-ORGANIZATION-AND-PROVIDER-CONTRACTS-V1.md` and linked Founder decision register on `atlas/planning`; GitHub read-back verified | VERIFIED · Atlas GitHub; architecture commit `70f80871fd6543329abdab4b1bab8c32003a228a`, index commit `c428d490e2571dcf5527ef71322180db56fc21e8` |
| 04 — Identify appropriate editor integration | Founder asked whether Codex extension was for Visual Studio or PyCharm | Clarified VS Code/Cursor integration versus Visual Studio 2026, a separate IDE. Avoid assuming VS Code extension works in full Visual Studio | RESOLVED · Founder conversation |
| 05 — Install coding assistant | Founder installed a plugin and clarified `Visual Studio 2026`, then proceeded to Visual Studio Code | Later screenshot showed Codex setup in VS Code; **exact installed extension version/publisher signature not independently audited** | REPORTED INSTALLED · Founder screenshot |
| 06 — GitHub authorization | Founder viewed GitHub authorization for Visual Studio Code and asked about `vscode.dev` link-opening permission | Founder chose to continue authentication; VS Code opened GitHub Copilot panel. Learned: GitHub editor authentication does **not** prove Codex is active or authorized, and Copilot is a separate tool | REPORTED · Founder screenshot/observation; permission grant details not independently reviewed |
| 07 — Open Codex specifically | Locate Codex extension, sign in with ChatGPT and enter Codex panel | Founder supplied Codex initial-screen screenshot; onboarding instructions recommended constrained approval. **Exact authentication state/scope, version and quota not independently checked** | REPORTED AVAILABLE · Founder |
| 08 — Initial unintended workspace | Codex appeared to be reading some prior code | Founder and Atlas requested **read-only environment discovery**, not edits | AUTHORIZED INSPECTION · Founder |
| 09 — Workspace discovery | Codex inspected open folder and Git | Codex reported `C:\Users\eejon\OneDrive\Desktop\Excel_GUI`, not DORY, no `.git`, six Python files and `DataExample.xlsx`, no file changes. Avoid conflating a familiar project with the intended repository | PASS (reported) · Codex |
| 10 — Clone organizational repo | VS Code `Git: Clone` of `https://github.com/eejonathangomez/DonumDei-Atlas.git`; chose new window | Dedicated workspace became `C:\Users\eejon\DonumDei-Atlas`, separating old Excel GUI work | PASS (reported) · Codex |
| 11 — First Atlas handshake | Codex asked to inspect repo on `atlas/planning`; stop if mismatched | Codex reported actual branch `main`, HEAD `f46de55a6cb074879c29ce0c2dfc3d4873f97b91`, clean worktree, only registered worktree, and **stopped before reading docs** | PASS (safe refusal) · Codex |
| 12 — Bounded Git correction | Founder authorized local branch alignment, no fetch/pull, then read-only documentation | Codex reported Git initially blocked by sandbox on `.git/index.lock`; after permission escalation, local `atlas/planning` tracked existing `origin/atlas/planning`. No other changes reported. This shows OS/sandbox approvals must be explicit and logged | PASS WITH OBSERVED ESCALATION · Codex |
| 13 — Architecture handshake V2 | Read five specified Atlas documents | Codex reported clean `C:\Users\eejon\DonumDei-Atlas`, HEAD `c428d490e2571dcf5527ef71322180db56fc21e8`; correctly described Founder, Atlas, DORY, worker, gates and provider contracts. GitHub Atlas files at this HEAD were independently read/verified by Atlas | PASS (worker-reported) · Codex; source documents independently read by Atlas |
| 14 — Catch stale operational guidance | Codex proposed rechecking seq634 based on older planning docs | Atlas independently checked DORY control GitHub: `main`=`9f4d63025fd32d82eee08ac04fa438a26c0e5c73`, sequence **636 COMPLETE**, STOP asserted, campaign publication disabled. Manual-results `LATEST.md` remained historical. **Do not act on stale seq634 recommendations** | VERIFIED CORRECTION · Atlas GitHub |
| 15 — Reporting preference | Founder required complete copy/paste-ready Codex task results by default | Codex adopted one fenced Markdown report with eight sections, checked for `AGENTS.md`, found none locally, reported no file changes; global/repo persistence was **not** performed | PASS (session-level only, worker-reported) · Codex |
| 16 — Global reporting persistence | Atlas authorized one scoped global instruction file and Codex returned an execution report: created `C:\Users\eejon\.codex\AGENTS.md`, read back, exit 0, SHA-256 `7F07560AD3C84A8C1B3C34FE0F32B93881E59A9EE15A84511626269BDF304204`; no fresh-session smoke test or Atlas-local verification | PASS (Codex-reported); fresh-session loading UNKNOWN |
| 17 — First real technical investigation | Codex completed `DORY-ONE-SHOT-COMMISSIONING-READINESS-REVIEW-V1` in a disposable cloned `dory-loop-control` checkout, at `9f4d63025...` | PASS WITH CONDITIONS: identified tip-sensitive 636 recovery and potential canonical unstaged local STOP/CLEAR route; recommended disposable qualification; **zero test suites**, no DORY scripts run; production-local runner and WIP UNKNOWN | PASS WITH CONDITIONS (Codex-reported), not production qualification |
| 18 — Generalize lessons | Founder directed recording every Codex adoption step as precedent for future providers | Reusable runbook plus this case report recorded in Atlas planning GitHub documentation; this act grants no worker execution authority | DOCUMENTED · Atlas |

## 2a. Additional evidence received (2026-11-24)

### Codex global reporting instructions
Codex returned `CODEX-GLOBAL-ENGINEERING-REPORTING-STANDARD-V1` PASS, maintenance-mode. It reported confirming effective `CODEX_HOME=C:\\Users\\eejon\\.codex`, no existing `AGENTS.md` or override, an exclusive-create UTF-8 write of `C:\\Users\\eejon\\.codex\\AGENTS.md`, read-back exit `0`, and SHA-256 `7F07560AD3C84A8C1B3C34FE0F32B93881E59A9EE15A84511626269BDF304204`. It reported no repository or DORY mutations. **Founder-provided Codex report; not an Atlas-direct Windows readback; fresh-session loading was not smoke-tested.**

### Codex commissioning source review
Codex returned `DORY-ONE-SHOT-COMMISSIONING-READINESS-REVIEW-V1` **PASS WITH CONDITIONS**, read-only, using disposable clone `C:\\Users\\eejon\\AppData\\Local\\Temp\\DORY-Commissioning-Review-f4397ebaa4a442be8213b59e0a8470db`. It reported `origin/main`=`main`=`9f4d63025fd32d82eee08ac04fa438a26c0e5c73`; sequence 636 `DORY/COMPLETE`; STOP asserted; campaign disabled. It traced the acceptance predicate in `v2/DoryAtomicMailbox.ps1`, STOP handling in `v2/dory_v2_runner.ps1`, the Atlas publisher/request routes and watchdog. **Finding:** unrelated synced commits or a committed STOP release can displace the special acceptance-at-HEAD boundary, while a canonical **unstaged local CLEAR** may preserve the tip; the latter still needs strict disposable publisher/sync/runner qualification. A preceding committed Atlas publication-request would be unsuitable for this acceptance boundary. No test suites were run, no DORY scripts executed; runtime UNKNOWN. **Verdict:** disposable rehearsal GO WITH CONDITIONS, production 637 NO-GO until distinct qualification and Founder approval. Full report was supplied in the Founder conversation, not published to this repository as a verified local artifact.

**Priority interpretation:** Codex is now a viable **manual read-only investigation agent**, not a demonstrated autonomous engineering worker. Continue current DORY/Cursor one-shot milestone. Correct future instructions that still describe this Codex review or global AGENTS write as not yet performed.

## 3. Concrete environment evidence and boundaries

- **Codex project checkout (worker-reported):** `C:\Users\eejon\DonumDei-Atlas`, `atlas/planning`, HEAD `c428d490e2571dcf5527ef71322180db56fc21e8`, clean after switch.
- **Atlas documentation home (independently verified):** `eejonathangomez/DonumDei-Atlas` branch `atlas/planning`. The HEAD above was a specific historical observation; documentation may have newer commits.
- **DORY control GitHub checkpoint (independently verified 2026-11-24):** `eejonathangomez/dory-loop-control` `main`=`9f4d63025fd32d82eee08ac04fa438a26c0e5c73`; `STATE.json` sequence 636 `turn=DORY`, `status=COMPLETE`, `last_completed_sequence=636`; `STOP` content `STOP\n`; campaign `publish_enabled=false`.
- **Local runner state:** UNKNOWN to Atlas; no DORY runner, broker or OS process state independently observed in this onboarding.
- **manual-results latest:** indexed result on `atlas/manual-results` was historical and must not override newer evidence. A task report transferred via chat is not equivalent to DORY acceptance.
- **Safety:** onboarding inspections and a bounded branch switch only (worker-reported); no DORY production STOP/READY actions, DORY worker activation, commits or product/broker activity reported. This is **not** independent proof of OS isolation.
- **Auth data:** Sign-in flow occurred (Founder-reported). Actual OAuth grants, provider/extension version, data routing, quota, secrets and revocation state not independently examined. Do not treat VS Code GitHub sign-in as a DORY worker credential.

## 4. Reusable lessons from this first provider adoption

1. **Distinguish editor products.** Visual Studio, Visual Studio Code, Cursor and PyCharm are not interchangeable installation targets.
2. **Authenticate each product intentionally.** An authorized GitHub editor can open Copilot while Codex is a separate extension and login.
3. **Never infer workspace identity from recent code.** Codex first inspected Excel_GUI; explicit `pwd`/Git preflight prevented applying DORY instructions to it.
4. **Environment mismatch must fail closed.** Codex stopped on `main` rather than silently checking out the expected branch.
5. **Explicitly approve the smallest corrective action.** Branch switch permission was separately granted; sandbox needed an elevation request for Git lock creation.
6. **Historical docs are not current DORY state.** The seq634 next-step advice was outdated; Atlas cross-checked actual seq636 GitHub state.
7. **Reporting style and persistence differ.** Codex accepted the format in conversation, but global `AGENTS.md` persistence remained unverified.
8. **Manual onboarding is not DORY integration.** Correct chat answers do not demonstrate supervised process ownership, timeout, cancellation, allowed-path containment or independent acceptance.
9. **Use evidence-ranked gate decisions.** Distinguish Founder observation, worker report, GitHub verification and local-runtime UNKNOWN.
10. **Protect future portability.** Preserve organization-wide roles, generic worker contracts, and provider-specific adoption notes separately. Do not make DORY dependent on one IDE.

## 5. Gate ledger as of documentation

| Gate | Outcome | Basis / remaining requirement |
| --- | --- | --- |
| 0 Need and role | PASS | Founder need and target engineering worker role explicit |
| 1 Installation/trust | PASS WITH CONDITIONS | Codex UI shown, but version and publisher trust metadata not independently audited |
| 2 Identity/permissions | PASS WITH CONDITIONS | Sign-in flow reported; actual scopes/data exposure not independently verified |
| 3 Workspace | PASS WITH CONDITIONS | Separate Atlas checkout reported; OS-level isolation not proven |
| 4 Git preflight | PASS | Wrong branch detected, stopped, bounded correction, clean state reported |
| 5 Organizational handshake | PASS | Five docs reviewed, roles and safety accurately described |
| 6 Copy-ready reporting | PASS WITH CONDITIONS | Global `AGENTS.md` created and hashed (Codex report); no independent readback or fresh-session smoke test |
| 7 Read-only source investigation | PASS WITH CONDITIONS | Codex-reported disposable DORY clone, source inspection and bounded report; no scripts/tests executed, no independent local observation |
| 8 Bounded source edits | NOT STARTED | No implementation authority or test evidence |
| 9 DORY adapter | NOT STARTED | No supervised Codex lifecycle qualification |
| 10 Isolation/security | NOT STARTED | No OS/process/credential-boundary tests |
| 11 Production commissioning | NOT STARTED | No Codex DORY execution, STOP release or accepted run |
| 12 Operate/offboard | NOT STARTED | No quantitative usage or fallback/exit drill |

**Current classification: manually onboarded for read-only exploration; not approved for production DORY execution.**

## 6. Next steps and stop criteria

**Immediate, smallest step:** Verify the Codex global `AGENTS.md` configuration on a fresh Codex session when useful (creation/read-back is Codex-reported). Qualify the proposed **disposable 636 → 637 transition and STOP/acceptance progression** before asking for any production sequence 637 commissioning. Atlas independently reviews source, test fixtures and evidence.

**Do not divert the critical path:** First prove one actual automated read-only DORY task via the **existing qualified Cursor path**, with separately authorized, fully qualified STOP transition and worker/runner activation. Only then compare Codex on the same harmless task and decide whether a DORY adapter is worth building.

**Explicit new authorization needed for:** creating/changing production control files; clearing STOP, publishing READY, launching runner, touching product WIP, broker calls, changing credential grants; modifying worker adapters; unattended Codex or another provider activation.

## 7. Security/exit considerations to complete later

Record provider account owner, integration version, permission scopes and actual data-handling terms; whether Codex sees repository source automatically; how to revoke IDE and GitHub access; how to remove an untrusted extension; whether credentials need rotation; how to inspect/preserve local worktrees, global/repo instruction files and execution logs before uninstall. Do not publish tokens or personal secrets in this case log.

## 8. Follow-up evidence rules

Append date/time and source to **this case record** for each returned Codex result, test/CI run, permission change, implementation and DORY integration decision. Link commits/hashes rather than replacing reports with a narrative of success. Keep the current GitHub/runtime checkpoint time-bound. A future provider gets its **own** case record following the shared runbook; do not overwrite the Codex history.

**This case log records installation and manual handshakes. It is not a claim of production Codex integration or live DORY execution.**
