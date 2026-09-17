from implementation import propose


def test_proposal_returns_only_the_typed_replacement_state():
    result = propose({'ref': 'order:7'}, 'binding:state', {'ref': 'draft'}, {'ref': 'sale'})
    assert result == {'next_state': 'sale'}
