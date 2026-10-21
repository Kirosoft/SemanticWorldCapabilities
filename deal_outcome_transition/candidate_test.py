"""Candidate behaviour only; selecting an occurrence of the required State grants no execution or commit authority. Reuses the real e2e fixture (tests/test_deal_outcome_transition_e2e.py).
The worker is handed the recruited subject and the narrowed view (`demand`) the host builds from the effective output requirement."""
from candidate import propose
from test_deal_outcome_transition_e2e import fixture

SUBJECT = 'seed://app/accounting/reference/deal/17'
REQUIRED = 'node/state/dealoutcomestate/wondealstate'


def test_candidate_selects_the_occurrence_of_the_required_state():
    store, config, reader, apply = fixture()
    read = reader()
    selected = propose(SUBJECT, read=read, demand={'instances_of': ['node/aggregate/deal', REQUIRED], 'refinements_of': [REQUIRED]})
    assert selected == 'seed://app/accounting/reference/deal/17-outcome/won'


def test_candidate_refuses_when_no_single_requirement_is_visible():
    store, config, reader, apply = fixture()
    try:
        propose(SUBJECT, read=reader(), demand={'instances_of': ['node/aggregate/deal', 'node/state']})
    except Exception as error:
        assert 'requirement' in str(error)
    else:
        raise AssertionError('a worker without a visible requirement must refuse')
