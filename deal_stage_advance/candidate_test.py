"""Candidate behavior only; recruiting/proposing an alternative State grants
no execution or commit authority. Reuses the real e2e fixture
(tests/test_deal_stage_advance_e2e.py) rather than a parallel synthetic
one -- admission only requires this file to exist with a real
test_-prefixed function; it is never executed by admission itself."""
from candidate import propose
from semanticworld.interpretation.projection_value import lower
from test_deal_stage_advance_e2e import fixture

DEAL = 'node/aggregate/deal'
NEW = 'node/state/dealworkflowstate/newdealstate'
QUALIFIED = 'node/state/dealworkflowstate/qualifieddealstate'


def test_candidate_returns_the_unique_lawful_alternative_stage():
    # A multi-type "definition" demand recruits exact-type instances per
    # listed path, not refinements -- both real stage instances are named
    # explicitly, so exactly one lawful alternative (Qualified) is recruited.
    store, config, reader, apply = fixture()
    read = reader()
    projection = lower(read, {'definition': [DEAL, NEW, QUALIFIED]})
    alternative = propose(projection, read=read, demand={})
    assert alternative == 'seed://app/accounting/reference/deal/17-stage/qualified'
