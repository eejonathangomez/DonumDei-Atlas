#!/usr/bin/env python3
"""Qualification tests for DORY efficiency-loop handshake artifacts.

Fail closed on drift between document, manifest, and skill.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "EFFICIENCY-LOOP-HANDSHAKE.md"
MANIFEST = ROOT / "handshake" / "efficiency-loop-handshake.json"
SKILL = ROOT / ".cursor" / "skills" / "reminder-handshake" / "SKILL.md"
LESSONS = ROOT / "docs" / "lessons" / "efficiency-loop-handshake-lessons.json"
ROADMAP = ROOT / "docs" / "CURRENT-OPERATING-ROADMAP.md"
REGISTER = ROOT / "docs" / "decisions" / "FOUNDER-DECISION-REGISTER.md"
PLANNING = ROOT / "planning" / "README.md"
PROPOSAL = ROOT / "planning" / "proposals" / "P-001-persistent-planning-foundation.md"

CANONICAL_PUBLISHER = "Publish-DoryAtomicReadyMailbox"
REQUEST_PATH = "v2/atlas-publication-request.json"


class EfficiencyLoopHandshakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.doc = DOC.read_text(encoding="utf-8")
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.roadmap = ROADMAP.read_text(encoding="utf-8")
        cls.register = REGISTER.read_text(encoding="utf-8")
        cls.planning = PLANNING.read_text(encoding="utf-8")
        cls.proposal = PROPOSAL.read_text(encoding="utf-8")
        with MANIFEST.open(encoding="utf-8") as fh:
            cls.manifest = json.load(fh)
        with LESSONS.open(encoding="utf-8") as fh:
            cls.lessons = json.load(fh)

    def test_required_artifacts_exist(self) -> None:
        for path in (DOC, MANIFEST, SKILL, LESSONS):
            self.assertTrue(path.is_file(), f"missing required artifact: {path}")

    def test_document_manifest_skill_agree_on_canonical_publisher(self) -> None:
        self.assertIn(CANONICAL_PUBLISHER, self.doc)
        self.assertIn(CANONICAL_PUBLISHER, self.skill)
        self.assertEqual(
            self.manifest["canonical_publisher"]["function"],
            CANONICAL_PUBLISHER,
        )
        self.assertEqual(
            self.manifest["atlas_remote_request"]["publishes_via"],
            CANONICAL_PUBLISHER,
        )

    def test_document_manifest_skill_agree_on_request_path(self) -> None:
        self.assertIn(REQUEST_PATH, self.doc)
        self.assertIn(REQUEST_PATH, self.skill)
        self.assertEqual(self.manifest["atlas_remote_request"]["path"], REQUEST_PATH)

    def test_no_split_task_state_publication_recommended(self) -> None:
        for text in (self.doc, self.skill):
            self.assertRegex(
                text,
                re.compile(r"never.*split|split.*forbidden|Never recommend split", re.I),
            )
        forbidden = " ".join(self.manifest["atlas_remote_request"]["forbidden"]).lower()
        self.assertIn("split", forbidden)

    def test_request_explicitly_data_non_authority(self) -> None:
        self.assertFalse(self.manifest["atlas_remote_request"]["authority"])
        classification = self.manifest["atlas_remote_request"]["classification"].lower()
        self.assertIn("data", classification)
        self.assertIn("non-authority", classification)
        for text in (self.doc, self.skill):
            self.assertRegex(text, re.compile(r"DATA.*non-authority|non-authority", re.I))

    def test_stable_protocol_has_no_required_hardcoded_pid_or_sequence(self) -> None:
        # Stable sections must not require a concrete PID or "current sequence is N".
        stable_chunk = self.doc.split("## Fresh-session recovery procedure")[0]
        self.assertNotRegex(stable_chunk, re.compile(r"\bPID\s+\d+\b"))
        self.assertNotRegex(
            stable_chunk,
            re.compile(r"current (production )?DORY runner.*PID", re.I),
        )
        self.assertNotRegex(
            stable_chunk,
            re.compile(r"current sequence\s*(is|=|:)\s*\d+", re.I),
        )
        transient = self.manifest["transient_current_truth"]["examples"]
        self.assertIn("runner PID", transient)
        self.assertIn("current sequence number", transient)
        secrets = self.manifest["secrets_policy"].lower()
        self.assertIn("pid", secrets)
        self.assertIn("sequence", secrets)

    def test_recovery_requires_live_truth_verification(self) -> None:
        self.assertRegex(self.doc, re.compile(r"Verify\s+\*\*live\*\*|verify live", re.I))
        steps = " ".join(self.manifest["recovery_steps"]).lower()
        self.assertIn("verify live", steps)
        self.assertRegex(self.skill, re.compile(r"Live control truth|verify live", re.I))
        self.assertIn("mandatory", self.skill.lower())

    def test_roles_remain_founder_atlas_dory_cursor(self) -> None:
        for role in ("Founder", "Atlas", "DORY", "Cursor"):
            self.assertIn(role, self.doc)
            self.assertIn(role, self.manifest["roles"])
            self.assertIn(role, self.skill)
        self.assertRegex(self.doc, re.compile(r"Never confuse Atlas with DORY", re.I))
        self.assertIn("Atlas is not DORY", self.manifest["role_invariants"])

    def test_knowledge_crosses_authority_does_not(self) -> None:
        pattern = re.compile(
            r"Knowledge may cross projects;\s*\*?\*?authority may not",
            re.I,
        )
        self.assertRegex(self.doc, pattern)
        self.assertIn(
            "Knowledge may cross projects; authority may not",
            self.manifest["role_invariants"],
        )
        self.assertIn(
            "Knowledge may cross projects; authority may not",
            self.skill,
        )

    def test_fresh_session_can_locate_required_artifacts(self) -> None:
        self.assertEqual(
            self.manifest["authoritative_document"],
            "docs/EFFICIENCY-LOOP-HANDSHAKE.md",
        )
        self.assertEqual(
            self.manifest["cursor_skill"],
            ".cursor/skills/reminder-handshake/SKILL.md",
        )
        self.assertIn("DORY handshake", self.doc)
        self.assertEqual(self.manifest["founder_recovery_phrase"], "DORY handshake")
        self.assertIn("DORY handshake", self.skill)

    def test_three_phrases_alias_one_contract(self) -> None:
        aliases = ["DORY handshake", "Atlas Handshake", "Atlas, handshake"]
        self.assertEqual(self.manifest["recovery_phrase_aliases"], aliases)
        self.assertEqual(
            self.manifest["authoritative_document"],
            "docs/EFFICIENCY-LOOP-HANDSHAKE.md",
        )
        for phrase in aliases:
            self.assertIn(phrase, self.doc)
            self.assertIn(phrase, self.skill)
        self.assertIn("one authoritative recovery contract", self.doc.lower())
        self.assertIn("one contract", self.doc.lower())
        self.assertNotIn("writes RESULT", self.doc)
        self.assertIn(
            "returns evidence under the currently authorized execution/result contract",
            self.doc,
        )
        self.assertIn(
            "Founder → Atlas → DORY → Cursor → DORY → Atlas/Founder",
            self.doc,
        )
        for label in (
            "SYNC_STOP",
            "AWAIT FOUNDER",
            "Protected WIP",
            "safe-point",
        ):
            self.assertIn(label, self.doc)
        self.assertEqual(
            self.manifest["recovered_field_labels"][0],
            "active project or UNKNOWN",
        )
        self.assertIn("SYNC_STOP", self.manifest["recovered_field_labels"])

    def test_skill_never_grants_ready(self) -> None:
        self.assertRegex(
            self.skill,
            re.compile(r"never.*grant READY|not.*execution authority", re.I),
        )
        for fact in self.manifest["explicit_non_authority_facts"]:
            self.assertRegex(fact, re.compile(r"not READY|no execution authority|DATA only", re.I))

    def test_lessons_capture_durable_memory_and_process_tree_rules(self) -> None:
        ids = {item["lesson_id"] for item in self.lessons["lessons"]}
        self.assertIn(
            "DURABLE-OPERATING-MEMORY-REQUIRES-VC-TRUTH-PLUS-LIVE-VERIFY",
            ids,
        )
        self.assertIn(
            "IDENTIFY-PROCESS-DESCENDANTS-BEFORE-TREE-TERMINATION",
            ids,
        )
        # Deduplicate: reference existing control-repo lesson, do not re-author as new QUALIFIED body.
        ref = next(
            x
            for x in self.lessons["lessons"]
            if x["lesson_id"] == "ATLAS-REMOTE-REQUEST-IS-NOT-EXECUTION-AUTHORITY"
        )
        self.assertEqual(ref["status"], "DEDUPLICATED-REFERENCE")

    def test_roadmap_reference_cannot_authorize_ready(self) -> None:
        planning = self.manifest["persistent_planning"]
        self.assertFalse(planning["authority"])
        self.assertIn("treating the roadmap as READY", planning["forbidden"])
        self.assertIn("The operating roadmap is knowledge, not READY", self.manifest["explicit_non_authority_facts"])
        self.assertIn("cannot authorize READY", self.doc)
        self.assertIn("NOT AUTHORIZED", self.roadmap)
        self.assertIn("not execution authority", self.roadmap.lower())
        self.assertIn("cannot authorize READY", self.skill)

    def test_planning_proposal_cannot_become_approved_task(self) -> None:
        self.assertIn(
            "promoting a planning proposal to an approved task without a Founder decision",
            self.manifest["persistent_planning"]["forbidden"],
        )
        self.assertIn("cannot become an approved task automatically", self.doc)
        self.assertIn("does not become an approved task automatically", self.planning)
        self.assertIn("not an approved task", self.proposal.lower())
        self.assertEqual(self.manifest["persistent_planning"]["planning_branch"], "atlas/planning")

    def test_approved_roadmap_has_version_and_source(self) -> None:
        self.assertIn("OPERATING-ROADMAP-RECORD-2026-11-15", self.roadmap)
        self.assertIn("Approved roadmap version", self.roadmap)
        self.assertIn("`NONE`", self.roadmap)
        self.assertIn("ATLAS PERSISTENT PLANNING AND HANDSHAKE IMPLEMENTATION — PHASE 1", self.roadmap)
        self.assertEqual(
            self.manifest["persistent_planning"]["approved_operating_roadmap"],
            "docs/CURRENT-OPERATING-ROADMAP.md",
        )

    def test_missing_evidence_is_unknown(self) -> None:
        self.assertEqual(self.manifest["persistent_planning"]["missing_value"], "UNKNOWN")
        self.assertIn("substituting chat memory for a missing file", self.manifest["persistent_planning"]["forbidden"])
        self.assertIn("Never substitute chat memory", self.doc)
        self.assertIn("UNKNOWN", self.skill)
        self.assertIn("missing authoritative file", self.skill)

    def test_retrieval_preserves_roles_and_one_contract(self) -> None:
        order = self.manifest["persistent_planning"]["retrieval_order"]
        self.assertEqual(
            order,
            [
                "stable operating contract",
                "approved operating roadmap",
                "founder decision record",
                "current milestone and acceptance checklist",
                "latest verified execution evidence",
                "STOP, SYNC_STOP, AUTO-READY, and protected-work status",
                "backlog and proposed enhancements",
                "pending decisions and next authorized action",
            ],
        )
        self.assertIn("creating a second handshake", self.manifest["persistent_planning"]["forbidden"])
        self.assertIn("do not replace this contract", self.doc.lower())
        self.assertIn("FD-2026-11-15-02", self.register)
        self.assertIn("Publish-DoryAtomicReadyMailbox", self.doc)

    def test_required_planning_files_exist(self) -> None:
        for path in (ROADMAP, REGISTER, PLANNING, PROPOSAL):
            self.assertTrue(path.is_file(), f"missing required artifact: {path}")


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(EfficiencyLoopHandshakeTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1
    print(
        f"QUALIFIED: {result.testsRun} tests passed "
        f"(failures={len(result.failures)} errors={len(result.errors)})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
