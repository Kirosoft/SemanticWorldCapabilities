"""Candidate behavior only; recruiting/proposing an alternative State grants
no execution or commit authority. Reuses the real e2e fixture
(tests/test_deal_outcome_transition_e2e.py) rather than a parallel
synthetic one -- admission only requires this file to exist with a real
test_-prefixed function; it is never executed by admission itself."""
from candidate import propose
from semanticworld.interpretation.projection_value import lower
from test_deal_outcome_transition_e2e import fixture

DEAL = 'node/aggregate/deal'
OPEN = 'node/state/dealoutcomestate/opendealstate'
WON = 'node/state/dealoutcomestate/wondealstate'


def test_candidate_returns_the_unique_lawful_alternative_outcome_state():
    # A multi-type "definition" demand recruits exact-type instances per
    # listed path, not refinements -- the abstract node/state recruits
    # nothing; the concrete substates must be named explicitly.
    store, config, reader, apply = fixture()
    read = reader()
    projection = lower(read, {'definition': [DEAL, OPEN, WON]})
    alternative = propose(projection, read=read, demand={})
    assert alternative == 'seed://app/accounting/reference/deal/17-outcome/won'
