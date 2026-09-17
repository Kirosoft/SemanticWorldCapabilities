"""Propose an Invoice reference; never allocate numbers or write facts."""
from semanticworld.interpretation.capability import validate_capability_arguments
from hostio import fail
from semanticworld.company_creation import occupied_identities
from semanticworld.inspection import resolve
from semanticworld.invoice_creation import INVOICE_REFERENCE
from semanticworld.store import freeze

def propose_invoice_creation(invoice_reference: "property/identifier/proposedinvoicereference", *, read, demand):
    if read.world is None:
        fail("NOT_BOOTSTRAPPED", "Invoice proposal requires a selected World basis")
    definition = resolve(read.authority, "ProposeInvoiceCreation")
    supplied = {INVOICE_REFERENCE: (invoice_reference,)}
    inputs = validate_capability_arguments(definition.path, supplied, read.authority.declarations)
    if not inputs.valid:
        fail("INVALID_REQUEST", "HG rejects the proposed Invoice reference")
    reference, = inputs.normalised_arguments[INVOICE_REFERENCE]
    if reference in occupied_identities(read.world.world):
        fail("INVALID_REQUEST", "Proposed Invoice identity already exists")
    return reference
