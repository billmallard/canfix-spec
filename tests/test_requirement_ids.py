"""
Stable-identifier checks for src/requirements.rst.

Every requirement in the General Requirements chapter carries an identifier
(``_`CFX-<section>-<number>``` as an inline target, list items add ``.<item>``).
Other documents -- hazard analyses, test plans -- cite these identifiers, so
they must never be renumbered, reused or silently dropped.

Run from the repo root:
    python -m pytest tests/ -v
"""
import os
import re

import pytest

REQ_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "requirements.rst")

ID_RE = re.compile(r"_`(CFX-[A-Z]{3}-\d{3}(?:\.\d+)?)`")
WELL_FORMED_RE = re.compile(r"^CFX-(GEN|COM|PHY|ELE)-\d{3}(\.\d+)?$")
NORMATIVE_RE = re.compile(r"\b(must|should|required|mandatory|recommend\w*|cannot)\b", re.I)

# Every identifier ever issued, in document order. Append new ones; never edit
# or remove an entry. A withdrawn requirement keeps its identifier in the text.
ISSUED = [
    "CFX-GEN-001",
    "CFX-COM-001",
    "CFX-COM-001.1", "CFX-COM-001.2", "CFX-COM-001.3",
    "CFX-COM-001.4", "CFX-COM-001.5", "CFX-COM-001.6",
    "CFX-COM-002", "CFX-COM-003", "CFX-COM-004", "CFX-COM-005",
    "CFX-COM-006", "CFX-COM-007", "CFX-COM-008", "CFX-COM-009",
    "CFX-COM-010",
    "CFX-PHY-001",
    "CFX-PHY-002",
    "CFX-PHY-002.1", "CFX-PHY-002.2", "CFX-PHY-002.3",
    "CFX-PHY-002.4", "CFX-PHY-002.5",
    "CFX-ELE-001", "CFX-ELE-002", "CFX-ELE-003",
    "CFX-ELE-004",
    "CFX-ELE-004.1", "CFX-ELE-004.2", "CFX-ELE-004.3", "CFX-ELE-004.4",
]

# Normative-sounding text that describes the chapter rather than requiring
# anything of a device, matched by its opening words.
INFORMATIVE = (
    "This section describes the minimum functionality",
)


@pytest.fixture(scope="module")
def text():
    with open(REQ_PATH, encoding="utf-8") as f:
        return f.read()


def blocks(text):
    """Paragraphs and list items, each joined onto one line."""
    out = []
    for para in re.split(r"\n\s*\n", text):
        lines = para.strip().splitlines()
        if not lines or set(lines[-1].strip()) <= set("=-"):
            continue  # heading or empty
        if lines[0].startswith(".."):
            continue  # directive / label
        item = []
        for line in lines:
            if line.lstrip().startswith("* ") and item:
                out.append(" ".join(item))
                item = []
            item.append(line.strip())
        out.append(" ".join(item))
    return out


def test_ids_well_formed(text):
    for rid in ID_RE.findall(text):
        assert WELL_FORMED_RE.match(rid), rid


def test_ids_unique(text):
    ids = ID_RE.findall(text)
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    assert not dupes, f"duplicate requirement IDs: {dupes}"


def test_issued_ids_still_present_in_order(text):
    ids = ID_RE.findall(text)
    assert ids[:len(ISSUED)] == ISSUED, (
        "an issued requirement ID was removed, renumbered or reordered; "
        "IDs are permanent -- mark a withdrawn requirement instead")


def test_new_ids_are_registered(text):
    ids = ID_RE.findall(text)
    assert ids == ISSUED, f"register new IDs in ISSUED: {ids[len(ISSUED):]}"


def test_every_normative_statement_has_an_id(text):
    missing = [
        b for b in blocks(text)
        if NORMATIVE_RE.search(b)
        and not ID_RE.search(b)
        and not b.startswith(INFORMATIVE)
    ]
    assert not missing, "requirements without an ID:\n" + "\n".join(
        m[:80] for m in missing)
