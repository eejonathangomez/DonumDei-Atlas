#!/usr/bin/env python3
"""Checks for the engineering continuity skill and report archive."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".cursor" / "skills" / "engineering-continuity-audit" / "SKILL.md"
LATEST = ROOT / "reports" / "engineering-continuity" / "LATEST.md"
README = ROOT / "reports" / "engineering-continuity" / "README.md"
REPORT = (
    ROOT
    / "reports"
    / "engineering-continuity"
    / "2026-11-15"
    / "ATLAS-FULL-PROJECT-CONTINUITY-AND-ENGINEERING-STATE-RECONCILIATION-V1.md"
)
DOC = ROOT / "docs" / "EFFICIENCY-LOOP-HANDSHAKE.md"
MANIFEST = ROOT / "handshake" / "efficiency-loop-handshake.json"
PLANNING = ROOT / "planning" / "README.md"


class EngineeringContinuityArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.latest = LATEST.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")
        cls.report = REPORT.read_text(encoding="utf-8")
        cls.doc = DOC.read_text(encoding="utf-8")
        cls.planning = PLANNING.read_text(encoding="utf-8")
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.manifest = json.load(handle)

    def test_quick_and_full_modes_exist(self) -> None:
        self.assertIn("## QUICK", self.skill)
        self.assertIn("## FULL", self.skill)
        self.assertIn("Use FULL only when", self.skill)
        self.assertIn("Do not run FULL on every handshake", self.skill)

    def test_latest_points_at_imported_report(self) -> None:
        self.assertIn("Qualified report imported", self.latest)
        self.assertIn(REPORT.relative_to(ROOT).as_posix(), self.latest)
        self.assertIn("6bedcd5923279cebbc6b3298ccb303a5e54fbb0a", self.latest)
        self.assertTrue(REPORT.is_file())
        self.assertTrue(self.report.startswith("# ATLAS FULL PROJECT CONTINUITY"))
        self.assertIn("line 1260", self.latest)

    def test_historical_report_keeps_provenance_and_is_not_authority(self) -> None:
        self.assertIn("verbatim", self.latest.lower())
        self.assertIn("not from an attachment filename", self.latest)
        self.assertIn("Do not overwrite a historical report", self.readme)
        self.assertIn("cannot authorize READY or AUTO-READY", self.latest)
        self.assertIn("cannot grant READY or AUTO-READY", self.skill)
        self.assertIn("UNKNOWN", self.skill)

    def test_proposals_stay_unapproved_and_handshake_stays_one_contract(self) -> None:
        self.assertIn("not approved work", self.skill)
        self.assertIn("does not become an approved task automatically", self.planning)
        self.assertIn("Publish-DoryAtomicReadyMailbox", self.doc)
        self.assertIn("DORY handshake", self.doc)
        self.assertIn("Atlas Handshake", self.doc)
        self.assertIn("Atlas, handshake", self.doc)
        self.assertIn("one authoritative recovery contract", self.doc.lower())
        archive = self.manifest["continuity_archive"]
        self.assertFalse(archive["authority"])
        self.assertFalse(archive["full_audit_on_every_handshake"])
        self.assertEqual(archive["missing_value"], "UNKNOWN")
        self.assertEqual(archive["index"], "reports/engineering-continuity/LATEST.md")
        self.assertIn(
            "An engineering-continuity report is evidence, not READY",
            self.manifest["explicit_non_authority_facts"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
