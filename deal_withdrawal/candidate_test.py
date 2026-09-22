"""Candidate behavior only; recruiting/proposing an alternative State grants
no execution or commit authority. Reuses the real e2e fixture
(tests/test_deal_withdrawal_e2e.py) rather than a parallel synthetic one --
admission only requires this file to exist with a real test_-prefixed
function; it is never executed by admission itself."""
from candidate import propose
from semanticworld.interpretation.projection_value import lower
from test_deal_withdrawal_e2e import fixture

DEAL = 'node/aggregate/deal'
OPEN = 'node/state/dealoutcomestate/opendealstate'
WITHDRAWN = 'node/state/dealoutcomestate/withdrawndealstate'


def test_candidate_returns_the_unique_lawful_alternative_outcome_state():
    # A multi-type "definition" demand recruits exact-type instances per
    # listed path, not refinements -- deliberately excludes WonDealState
    # (also present in the shared seed) so exactly one lawful alternative
    # (Withdrawn) is recruited.
    store, config, reader, apply = fixture()
    read = reader()
    projection = lower(read, {'definition': [DEAL, OPEN, WITHDRAWN]})
    alternative = propose(projection, read=read, demand={})
    assert alternative == 'seed://app/accounting/reference/deal/17-outcome/withdrawn'
