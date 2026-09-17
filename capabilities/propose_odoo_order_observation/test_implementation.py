from implementation import propose


def test_proposal_preserves_all_proposed_subjects():
    order = {'identity': 'test:order', 'type': 'node/document/transactionaldocument/odoov2order'}
    current = {'identity': 'test:draft', 'type': 'node/state'}
    following = {'identity': 'test:sale', 'type': 'node/state'}
    assert propose(order, current, following) == {'order': order,
        'current_state': current, 'next_state': following}
