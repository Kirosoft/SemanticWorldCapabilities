"""Pure function behavior only; admission and HG checks belong to the host."""
from candidate import propose


def test_canonical_value_is_returned_without_a_named_output_envelope():
    assert propose('tax-1', 'GB999', read=None, demand=None) == 'GB999'
