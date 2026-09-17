"""Candidate verification entry points; the workspace fixtures are test-only."""
from test_typed_property_result import (
    test_typed_tax_result_preserves_target_and_does_not_mutate_world,
    test_typed_tax_result_rejects_envelopes_invalid_values_and_changed_output,
    test_typed_tax_candidate_cannot_retarget_a_different_property_binding,
)


def test_canonical_typed_result():
    test_typed_tax_result_preserves_target_and_does_not_mutate_world()


def test_invalid_inputs():
    test_typed_tax_result_rejects_envelopes_invalid_values_and_changed_output()


def test_binding_identity():
    test_typed_tax_candidate_cannot_retarget_a_different_property_binding()
