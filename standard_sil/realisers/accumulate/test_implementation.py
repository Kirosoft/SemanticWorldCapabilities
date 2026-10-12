from implementation import realise


def test_the_declaration_is_never_a_computation():
    assert realise(None, None, None) is None
