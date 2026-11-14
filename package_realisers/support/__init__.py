"""Execution functions of the support package, linked to the HG paths they realise. Fixture code for the
STRATEGY-001 transfer: nothing in swi/ knows this package exists."""
from decimal import Decimal

from semanticworld.swi.library import realiser

Q = "property/quantity"

# TriageTicket and ResolveTicket have no body here: a state transition is its admitted HG declaration's, realised by swi
# (INTRINSIC-REALISATION-001).


@realiser("node/capability/sumeffort")
def sum_effort(logged_effort: "property/quantity#logged_effort"):
    """Morphism: one or more logged efforts to their total. Declared over a collection of logged efforts."""
    return str(sum(Decimal(v) for v in logged_effort).normalize())
