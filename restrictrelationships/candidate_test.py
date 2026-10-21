"""Admission package smoke test; semantic execution is intentionally deferred."""
from candidate import restrict_relationships


def test_restrict_relationships_candidate_is_callable():
    assert callable(restrict_relationships)
