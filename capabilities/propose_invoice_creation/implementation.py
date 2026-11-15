"""Propose an Invoice's transactional document kind; never allocate identities or numbers, or write facts
(ENGINE-3C-001: a value function)."""


def propose_invoice_creation(kind: "node/class/transactionaldocumentkind"):
    """The selected World kind the new Invoice is classified as. SemanticWorld has already validated the input against HG
    and the selected World; generic protected creation derives the Invoice's identity, generated bindings and initial state."""
    return kind
