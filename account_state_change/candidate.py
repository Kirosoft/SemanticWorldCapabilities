"""Realise the State the recruited Strategy requires for an Account: the worker is handed the recruited subject occurrence (its single typed input) and a trusted view of the World narrowed by the host to the
required State type and its refinements (`demand["refinements_of"]`). It selects the occurrence of that State; it does not recruit, does not read a Projection, and does not choose the target: the requirement is the
consequence Recruitment selected for this step. The host independently types and validates the returned reference (by the occurrence's own type) and the state overlay checks the transition law."""
from hostio import fail
from semanticworld.inspection import is_refinement_of


def propose(account, *, read, demand):
    required = tuple(demand.get('refinements_of', ())) if isinstance(demand, dict) else ()
    if len(required) != 1:
        fail('INVALID_REQUEST', 'The recruited State requirement is not visible to the worker')
    edges = tuple(edge for edge in read.world.world.edges if edge.relationship_type == 'edge/in_state')
    unavailable = {edge.target_ref for edge in edges}  # every State already occupied by some subject
    candidates = tuple(node.ref for node in read.world.world.nodes
        if node.ref in read.eligible_refs and node.ref not in unavailable and is_refinement_of(read.authority, node.node_type, required[0]))
    if len(candidates) != 1:
        fail('INVALID_REQUEST', 'The required State has no single unattached occurrence: ' + required[0])
    return candidates[0]
