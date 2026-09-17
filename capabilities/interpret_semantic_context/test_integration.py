"""Run with HG on PYTHONPATH: python -m unittest discover -s <this folder>."""
import copy
from pathlib import Path
import unittest

from hg.authority import load_verified_authority
import hg
from semanticworld.interpretation.execution import validate_capability_arguments, validate_capability_outputs
from implementation import interpret_semantic_context

HG_ROOT = Path(hg.__file__).resolve().parent.parent
CAPABILITY = "node/capability/interpretsemanticcontext"


def test_hg_validated_proposal_and_immutable_input():
    authority = load_verified_authority(HG_ROOT)
    request = {"material": {"lexical": {"text": "node/state"}},
               "context": {"declaration": ["node/state", "node/process"]}}
    original = copy.deepcopy(request)
    inputs = validate_capability_arguments(CAPABILITY, {"request": request}, authority.declarations)
    assert inputs.valid, inputs.observations
    result = interpret_semantic_context(inputs.normalised_arguments["request"])
    output = validate_capability_outputs(CAPABILITY, result, authority.declarations)
    assert output.valid, output.observations
    assert result["interpretation"]["hypotheses"]["hypothesis"][0]["candidate"] == "node/state"
    assert request == original
    assert result == interpret_semantic_context(inputs.normalised_arguments["request"])


def test_unresolved_and_no_match_outside_context():
    authority = load_verified_authority(HG_ROOT)
    for text in ("invoice", "node/state", ""):
        result = interpret_semantic_context({"material": {"lexical": {"text": text}},
                                             "context": {"declaration": ["node/process"]}})
        assert "unresolved" in result["interpretation"]
        assert validate_capability_outputs(CAPABILITY, result, authority.declarations).valid


def test_invalid_ingress_rejected_by_hg():
    authority = load_verified_authority(HG_ROOT)
    for request in ({}, {"material": {"lexical": {"text": ""}}, "context": {}},
                    {"material": {"lexical": {"text": "thing"}},
                     "context": {"declaration": ["node/unknown"]}}):
        assert not validate_capability_arguments(CAPABILITY, {"request": request}, authority.declarations).valid


def test_explicit_reference_mentions_are_ordered_unique_and_context_limited():
    authority = load_verified_authority(HG_ROOT)
    request = {'material': {'lexical': {'text': 'node/state node/document node/process node/state'}},
        'context': {'declaration': ['node/state', 'node/process']}}
    original = copy.deepcopy(request)
    inputs = validate_capability_arguments(CAPABILITY, {'request': request}, authority.declarations)
    assert inputs.valid, inputs.observations
    result = interpret_semantic_context(inputs.normalised_arguments['request'])
    assert validate_capability_outputs(CAPABILITY, result, authority.declarations,
        validated_inputs=inputs).valid
    hypotheses = result['interpretation']['hypotheses']['hypothesis']
    assert tuple(item['candidate'] for item in hypotheses) == ('node/process', 'node/state')
    assert all(item['evidence'] and item['confidence'] == '1' for item in hypotheses)
    assert request == original
    assert result == interpret_semantic_context(inputs.normalised_arguments['request'])


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(unittest.FunctionTestCase(value) for name, value in
                              sorted(globals().items()) if name.startswith("test_"))
