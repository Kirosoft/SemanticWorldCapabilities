"""Choose one lawful recruited alternative Deal workflow State, without
invocation or commit. Identical structure to
deal_outcome_transition/candidate.py and deal_withdrawal/candidate.py --
this operates on Deal's "state" (workflow/pipeline) binding instead of
its "outcome" (commercial result) binding, an independent dimension."""
from hostio import HostError, error_code, fail
from semanticworld.document_state import prepare
from semanticworld.inspection import is_refinement_of, resolve
from semanticworld.interpretation.projection_value import validate
from semanticworld.read import recruit
from semanticworld.reference import plain


def propose(projection, *, read, demand):
    projection = validate(read, projection)
    selected = recruit(read, plain(projection.request), result_bound=projection.result_bound,
        work_bound=projection.work_bound)
    if not selected.complete:
        fail('INVALID_REQUEST', 'State choice requires complete recruited context')
    state_type = resolve(read.authority, 'node/state').path
    alternatives = []
    for node in selected.instances.nodes:
        if not is_refinement_of(read.authority, node.node_type, state_type):
            continue
        try:
            prepare(read, projection, {state_type: (node.ref,)}, definition_id='ProposeDealStageAdvance',
                subject_type='Deal', binding_handle='state')
        except HostError as error:
            if error_code(error) != 'INVALID_REQUEST':
                raise
        else:
            alternatives.append(node.ref)
    if len(alternatives) != 1:
        fail('INVALID_REQUEST', 'Recruited context must contain exactly one lawful alternative State')
    return alternatives[0]
