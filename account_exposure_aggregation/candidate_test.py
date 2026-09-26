"""Candidate behavior only; this Capability is read-only and grants no
execution or commit authority regardless. Reuses the real e2e fixture
(tests/test_account_exposure_aggregation_e2e.py) rather than a parallel
synthetic one -- admission only requires this file to exist with a real
test_-prefixed function; it is never executed by admission itself."""
import json

from candidate import propose
from semanticworld.interpretation.projection_value import lower
from test_account_exposure_aggregation_e2e import fixture

QUERY = {'query': {
    'variables': [
        {'name': 'holder', 'type': 'node/party'},
        {'name': 'account', 'type': 'node/aggregate/account'},
        {'name': 'status', 'type': 'node/state/accountstatus'},
    ],
    'relationships': [
        {'source': 'account', 'relationship': 'edge/refers_to', 'target': 'holder'},
        {'source': 'account', 'relationship': 'edge/in_state', 'target': 'status'},
    ],
    'project': ['holder']}}

COMPANY_ACME = 'seed://app/accounting/reference/company/acme'
PERSON_JANE = 'seed://app/accounting/reference/person/jane-doe'
PERSON_JOHN = 'seed://app/accounting/reference/person/john-smith'
ACTIVE = 'node/state/accountstatus/activeaccountstate'
UNDER_REVIEW = 'node/state/accountstatus/activeaccountstate/underreviewaccountstate'


def test_candidate_computes_a_real_two_dimensional_exposure_report():
    store, read_world = fixture()
    read = read_world()
    projection = lower(read, QUERY)
    report = json.loads(propose(projection, read=read, demand={}))
    assert report == {
        COMPANY_ACME: {UNDER_REVIEW: 1},
        PERSON_JANE: {UNDER_REVIEW: 1},
        PERSON_JOHN: {ACTIVE: 1},
    }, report
