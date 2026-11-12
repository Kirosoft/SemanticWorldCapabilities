"""Execution functions of the support package, linked to the HG paths they realise. Fixture code for the
STRATEGY-001 transfer: nothing in swi/ knows this package exists."""
from decimal import Decimal

from hg.relationships import SemanticNode
from semanticworld.swi.library import realiser, world_realiser
from semanticworld.swi.realisers import Produced, grounded

TICKET = "node/aggregate/ticket"
Q = "property/quantity"


def _state(result_type: str, identity: str) -> Produced:
    return Produced(SemanticNode(f"swi://{identity}/{result_type.rsplit('/', 1)[-1]}", result_type))


@world_realiser("node/capability/triageticket")
def triage_ticket(world, grounding, identity):
    grounded(grounding, TICKET)
    grounded(grounding, "node/state/ticketstate/openticketstate")
    return _state("node/state/ticketstate/triagedticketstate", identity)


@world_realiser("node/capability/resolveticket")
def resolve_ticket(world, grounding, identity):
    grounded(grounding, TICKET)
    grounded(grounding, "node/state/ticketstate/triagedticketstate")
    return _state("node/state/ticketstate/resolvedticketstate", identity)


@realiser("node/capability/sumeffort")
def sum_effort(logged_effort: "property/quantity#logged_effort"):
    """Morphism: one or more logged efforts to their total. Declared over a collection of logged efforts."""
    return str(sum(Decimal(v) for v in logged_effort).normalize())
