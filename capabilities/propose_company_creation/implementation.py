"""Functional Company creation candidate; no World writes or authority."""
from semanticworld.interpretation.capability import validate_capability_arguments
from hostio import fail
from semanticworld.company_creation import COMPANY_REFERENCE, INDUSTRY_TYPE, TAX_NUMBER, prepare
from semanticworld.inspection import resolve
from semanticworld.store import freeze

def propose_company_creation(company_reference: "property/identifier/proposedcompanyreference", industry: "node/class/industrytype", tax_number: "property/identifier/taxnumber", *, read, demand):
    selected, proposed = prepare(read, demand, company_reference, industry, tax_number)
    if not proposed.valid:
        fail("INVALID_REQUEST", "HG rejects the proposed Company World")
    definition = resolve(read.authority, "ProposeCompanyCreation")
    supplied = {COMPANY_REFERENCE: (company_reference,), INDUSTRY_TYPE: (industry,), TAX_NUMBER: (tax_number,)}
    inputs = validate_capability_arguments(definition.path, supplied, read.authority.declarations,
        instance_types={node.ref: node.node_type for node in selected.instances.nodes})
    if not inputs.valid:
        fail("INVALID_REQUEST", "HG rejects Company creation ingress")
    canonical = next(item.value for item in proposed.world.properties
        if item.subject_ref == company_reference and item.property_type == TAX_NUMBER)
    result = {key: values[0] for key, values in inputs.normalised_arguments.items()}
    result[TAX_NUMBER] = canonical
    return freeze(result)
