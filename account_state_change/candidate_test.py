"""Candidate behaviour only; reporting the selected State grants no execution or commit authority. Reuses the real e2e fixture (tests/test_account_state_change_e2e.py)."""
from candidate import propose
from test_account_state_change_e2e import fixture

SUBJECT = 'seed://app/accounting/reference/account/1001'
REQUIRED = 'node/state/accountstatus/suspendedaccountstate'


def test_candidate_reports_the_selected_state():
    store, config, reader, apply = fixture()
    assert propose(SUBJECT, read=reader(), demand={'instances_of': ['node/aggregate/account', REQUIRED], 'refinements_of': [REQUIRED]}) == {'state': REQUIRED}


def test_candidate_refuses_when_no_single_requirement_is_visible():
    store, config, reader, apply = fixture()
    try:
        propose(SUBJECT, read=reader(), demand={'instances_of': ['node/aggregate/account', 'node/state']})
    except Exception as error:
        assert 'requirement' in str(error)
    else:
        raise AssertionError('a worker without a visible requirement must refuse')
