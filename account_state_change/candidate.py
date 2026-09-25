"""Choose one lawful recruited alternative Account lifecycle State, without
invocation or commit. Structurally close to deal_outcome_transition/candidate.py,
deal_withdrawal/candidate.py and deal_stage_advance/candidate.py, with one
real difference: Deal has exactly one seeded instance, so a single
multi-type "definition" demand unambiguously supplies both the subject and
its candidate alternative States via `demand`/`projection.request`. Account
has more than one real seeded instance, so the same multi-type demand would
recruit every Account and `document_state.py::prepare`'s default subject
resolution (which requires exactly one recruited node refining the subject
type) would see more than one and refuse.

`projection` here is instead built from a `general_query` demand that pins
"account" to one specific instance (Phase 3's own proven composition
grammar), keeping the subject unambiguous. `demand` (the `propose(...,
demand=...)` parameter) is *not* a separate, caller-chosen value -- the real
selected-callable dispatch (`SemanticWorldComputer/swc/projection_callable.py`)
always sets it to `plain(projection.request)`, the same demand used for
subject pinning; it is unused here, same as every other candidate.py in this
family. Candidate alternative States (including the deliberately unlinked
one Phase 0 planted) are discovered via this module's own internal exact-type
recruit instead, over the AccountStatus hierarchy -- domain knowledge this
capability already needs to declare.

Account's "status" binding, like Deal's own `edge/in_state` bindings,
declares an unbounded `sources_per_target` -- `prepare()` faithfully
allows any admitted, differently-typed State as a replacement, trusting
the caller to supply sensible candidates; it does not itself check
whether a candidate State already belongs to a *different* subject. With
only one real Deal this never mattered. With two real Accounts, a
type-only candidate recruit can surface another Account's own current
State (e.g. account/1002's Active State) as a spurious "lawful
alternative" for account/1001. This module excludes any candidate
already the target of an existing IN_STATE fact from a different
subject before trying it.
"""
from hostio import HostError, error_code, fail
from semanticworld.document_state import prepare
from semanticworld.inspection import is_refinement_of, resolve
from semanticworld.interpretation.projection_value import validate
from semanticworld.read import recruit
from semanticworld.reference import plain

CANDIDATE_STATUS_TYPES = (
    'node/state/accountstatus/activeaccountstate',
    'node/state/accountstatus/suspendedaccountstate',
    'node/state/accountstatus/closedaccountstate',
    'node/state/accountstatus/activeaccountstate/underreviewaccountstate',
)


def propose(projection, *, read, demand):
    projection = validate(read, projection)
    selected = recruit(read, plain(projection.request), result_bound=projection.result_bound,
        work_bound=projection.work_bound)
    if not selected.complete:
        fail('INVALID_REQUEST', 'State choice requires complete recruited context')
    account_type = resolve(read.authority, 'Account').path
    subjects = tuple(node.ref for node in selected.instances.nodes
        if is_refinement_of(read.authority, node.node_type, account_type))
    if len(subjects) != 1:
        fail('INVALID_REQUEST', 'Recruited context must identify exactly one subject Account')
    subject, = subjects
    candidates = recruit(read, {'definition': list(CANDIDATE_STATUS_TYPES)},
        result_bound=projection.result_bound, work_bound=projection.work_bound)
    if not candidates.complete:
        fail('INVALID_REQUEST', 'State choice requires complete candidate recruitment')
    state_type = resolve(read.authority, 'node/state').path
    in_state = resolve(read.authority, 'IN_STATE').path
    attached_elsewhere = {edge.target_ref for edge in read.world.world.edges
        if edge.source_ref != subject and is_refinement_of(read.authority, edge.relationship_type, in_state)}
    alternatives = []
    for node in candidates.instances.nodes:
        if not is_refinement_of(read.authority, node.node_type, state_type) or node.ref in attached_elsewhere:
            continue
        try:
            prepare(read, projection, {state_type: (node.ref,)}, definition_id='ProposeAccountStateChange',
                subject_type='Account', binding_handle='status')
        except HostError as error:
            if error_code(error) != 'INVALID_REQUEST':
                raise
        else:
            alternatives.append(node.ref)
    if len(alternatives) != 1:
        fail('INVALID_REQUEST', 'Recruited context must contain exactly one lawful alternative State')
    return alternatives[0]
