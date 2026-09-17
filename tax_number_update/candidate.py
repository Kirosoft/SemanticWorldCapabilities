"""Return the canonical typed TaxNumber; the protected host handles the target."""


def propose(occurrence: 'node/component/propertyoccurrence',
            tax_number: 'property/identifier/taxnumber', *, read, demand):
    return tax_number
