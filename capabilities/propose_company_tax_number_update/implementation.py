"""Compute one typed TaxNumber; repository presence grants no authority."""
from semanticworld.interpretation.capability import validate_capability_arguments
from hostio import fail
from semanticworld.inspection import resolve
from semanticworld.read import recruit
from semanticworld.tax_number_result import prepare

OCCURRENCE = "node/component/propertyoccurrence"
TAX_NUMBER = "property/identifier/taxnumber"

def propose_company_tax_number_update(
        occurrence: "node/component/propertyoccurrence",
        tax_number: "property/identifier/taxnumber", *, read, demand):
    definition = resolve(read.authority, "ProposeCompanyTaxNumberUpdate")
    selected = recruit(read, demand)
    supplied = {OCCURRENCE: (occurrence,), TAX_NUMBER: (tax_number,)}
    inputs = validate_capability_arguments(definition.path, supplied, read.authority.declarations,
        instance_types={node.ref: node.node_type for node in selected.instances.nodes})
    if not inputs.valid:
        fail("INVALID_REQUEST", "HG rejects property update ingress")
    value, = inputs.normalised_arguments[TAX_NUMBER]
    prepare(read, demand, inputs.normalised_arguments, {TAX_NUMBER: (value,)})
    return value
