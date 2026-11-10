"""Propose an Invoice's transactional document kind; never allocate identities or numbers, or write facts."""
from hostio import fail


def propose_invoice_creation(kind: "node/class/transactionaldocumentkind", *, read, demand):
    """The selected World kind the new Invoice is classified as. SWC has already validated the input against HG and the
    selected World; generic protected creation derives the Invoice's identity, generated bindings and initial state."""
    if read.world is None:
        fail("NOT_BOOTSTRAPPED", "Invoice proposal requires a selected World basis")
    return kind
