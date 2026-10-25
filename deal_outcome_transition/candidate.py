"""Report the commercial outcome State the recruited Strategy selected for a Deal (HG-STATE-VALUE-REPRESENTATION-L2-001). The worker is handed the
recruited subject occurrence and the step's issued requirement (`demand["refinements_of"]`). It reports that consequence as a State definition
result {"state": S}: it selects no occurrence, applies no occupancy rule, names no World node and creates nothing. The host checks that S is
exactly the issued consequence; the generic interpreter alone realises it as the World's canonical value of S, and the governed commit applies it."""
from hostio import fail


def propose(deal, *, read, demand):
    required = tuple(demand.get('refinements_of', ())) if isinstance(demand, dict) else ()
    if len(required) != 1:
        fail('INVALID_REQUEST', 'The recruited State requirement is not visible to the worker')
    return {'state': required[0]}
