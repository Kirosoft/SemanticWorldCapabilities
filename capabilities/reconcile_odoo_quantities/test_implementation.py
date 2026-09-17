"""Exact candidate arithmetic over HG-validated test outcome meaning.

Only the two existing State proposals are locally admitted for these unit tests.
Capability interface and SWC admission/invocation remain integration coverage.
"""
import json
from pathlib import Path
from types import SimpleNamespace
import unittest

import hg
from hg.authority import load_verified_authority
from swos.authority.application import extend
from implementation import reconcile


def context():
    root = Path(__file__).resolve().parents[2]
    proposals = json.loads((root / "applications/odoo_quantity_reconciliation.json").read_text())
    states = tuple(item for item in proposals if item["id"] in
                   ("OdooQuantityEquivalent", "OdooQuantityDiscrepant"))
    assert len(states) == 2
    base = load_verified_authority(Path(hg.__file__).resolve().parent.parent)
    return SimpleNamespace(authority=extend(base, states))


def test_exact_arithmetic_preserves_unit_identity_and_hg_outcomes():
    read = context()
    for invoices, refunds, source, computed, difference, state in (
        (("0.1", "0.2"), (), "0.3", "0.3", "0.0", "odooquantityequivalent"),
        (("3",), ("1",), "4", "2", "2", "odooquantitydiscrepant"),
        (("1", "1"), (), "2", "2", "0", "odooquantityequivalent"),
        (("10000000000000000000000000000", "0.1"), (),
         "10000000000000000000000000000.1", "10000000000000000000000000000.1", "0.0", "odooquantityequivalent"),
    ):
        result = reconcile(invoices, refunds, source, "unit:1", "comparison:1", read=read, demand=None)
        assert result == {"computed": computed, "difference": difference, "unit": "unit:1",
            "outcome": {"identity": "comparison:1", "type": "node/state/" + state}}
        assert result == reconcile(invoices, refunds, source, "unit:1", "comparison:1", read=read, demand=None)


def test_nonfinite_values_are_rejected():
    read = context()
    for value in ("NaN", "Infinity", "-Infinity"):
        for invoices, refunds, source in (((value,), (), "0"), ((), (value,), "0"), ((), (), value)):
            with unittest.TestCase().assertRaises(ValueError):
                reconcile(invoices, refunds, source, "unit:1", "comparison:1", read=read, demand=None)


def test_missing_outcome_meaning_is_not_synthesised():
    base = load_verified_authority(Path(hg.__file__).resolve().parent.parent)
    with unittest.TestCase().assertRaises(KeyError):
        reconcile(("1",), (), "1", "unit:1", "comparison:1",
            read=SimpleNamespace(authority=base), demand=None)


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(unittest.FunctionTestCase(value) for name, value in
        sorted(globals().items()) if name.startswith("test_") and callable(value))
