"""Compute one typed TaxNumber; repository presence grants no authority (ENGINE-3C-001: a value function).

SemanticWorld validates the recruited occurrence and the canonical TaxNumber against HG and prepares the protected update
(`semanticworld.tax_number_result.prepare`); this function only proposes the value."""


def propose_company_tax_number_update(occurrence: "node/component/propertyoccurrence",
                                      tax_number: "property/identifier/taxnumber"):
    return tax_number
