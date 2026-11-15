"""Return the canonical typed TaxNumber; the protected host handles the target (ENGINE-3C-001: a value function)."""


def propose(occurrence: 'node/component/propertyoccurrence', tax_number: 'property/identifier/taxnumber'):
    return tax_number
