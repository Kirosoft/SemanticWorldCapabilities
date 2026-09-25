"""Candidate behavior only; recruiting/proposing an alternative State grants
no execution or commit authority. Reuses the real e2e fixture
(tests/test_account_state_change_e2e.py) rather than a parallel synthetic
one -- admission only requires this file to exist with a real
test_-prefixed function; it is never executed by admission itself."""
from candidate import propose
from semanticworld.interpretation.projection_value import lower
from test_account_state_change_e2e import fixture

ACCOUNT = 'node/aggregate/account'
ACCOUNT_STATUS = 'node/state/accountstatus'
ACCOUNT_1001 = 'seed://app/accounting/reference/account/1001'


def subject_pinning_demand():
    # Account has more than one real seeded instance (unlike Deal), so a
    # multi-type "definition" demand would recruit every Account and make
    # prepare()'s default subject resolution ambiguous. A general_query
    # pinning "account" to one real instance recruits exactly that Account
    # (plus its real current status), keeping the subject unambiguous.
    return {'query': {
        'variables': [
            {'name': 'account', 'type': ACCOUNT, 'instance': ACCOUNT_1001},
            {'name': 'status', 'type': ACCOUNT_STATUS},
        ],
        'relationships': [{'source': 'account', 'relationship': 'edge/in_state', 'target': 'status'}],
        'project': ['account']}}


def test_candidate_returns_the_unique_lawful_alternative_status():
    # candidate.py discovers alternative States itself (CANDIDATE_STATUS_TYPES),
    # not from `demand` -- the real selected-callable dispatch always sets
    # `demand` equal to `projection.request`, so it cannot carry a separately
    # chosen value; `demand` is passed here only to match that real signature.
    store, config, reader, apply = fixture()
    read = reader()
    projection = lower(read, subject_pinning_demand())
    alternative = propose(projection, read=read, demand={})
    assert alternative == 'seed://app/accounting/reference/account/1001-status/suspended'
