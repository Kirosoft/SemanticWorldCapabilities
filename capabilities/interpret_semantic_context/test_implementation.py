"""Lexical computation tests; HG ingress/egress coverage remains in test_integration."""
from copy import deepcopy
import unittest
from implementation import interpret_semantic_context


def test_exact_match_is_deterministic_and_does_not_mutate_input():
    request = {"material": {"lexical": {"text": "node/state"}},
               "context": {"declaration": ["node/state", "node/process"]}}
    before = deepcopy(request)
    result = interpret_semantic_context(request)
    hypothesis = result["interpretation"]["hypotheses"]["hypothesis"][0]
    assert hypothesis["candidate"] == "node/state" and hypothesis["confidence"] == "1"
    assert hypothesis["evidence"]
    assert request == before and result == interpret_semantic_context(request)


def test_no_match_outside_context():
    for text in ("invoice", "node/state", ""):
        result = interpret_semantic_context({"material": {"lexical": {"text": text}},
            "context": {"declaration": ["node/process"]}})
        assert result["interpretation"]["unresolved"]["reason"]


def test_explicit_references_are_ordered_unique_and_context_limited():
    request = {"material": {"lexical": {"text": "node/state node/document node/process node/state"}},
        "context": {"declaration": ["node/state", "node/process"]}}
    before = deepcopy(request)
    result = interpret_semantic_context(request)
    hypotheses = result["interpretation"]["hypotheses"]["hypothesis"]
    assert tuple(item["candidate"] for item in hypotheses) == ("node/process", "node/state")
    assert all(item["evidence"] and item["confidence"] == "1" for item in hypotheses)
    assert request == before and result == interpret_semantic_context(request)


def test_leaf_match_retains_lower_confidence():
    result = interpret_semantic_context({"material": {"lexical": {"text": " state "}},
        "context": {"declaration": ["node/state"]}})
    hypothesis = result["interpretation"]["hypotheses"]["hypothesis"][0]
    assert hypothesis["candidate"] == "node/state" and hypothesis["confidence"] == "0.5"


def test_unsupported_modifier_and_nonlexical_material_remain_unresolved():
    for request in (
        {"material": {"lexical": {"text": "node/state"}}, "context": {"modifier": ["test:modifier"]}},
        {"material": {"subject": "test:subject"}, "context": {}},
    ):
        assert interpret_semantic_context(request)["interpretation"]["unresolved"]["reason"]


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(unittest.FunctionTestCase(value) for name, value in
        sorted(globals().items()) if name.startswith("test_") and callable(value))
