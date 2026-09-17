"""Return typed Company/TaxNumber values; invocation grants no update authority."""


def propose_company_tax_number(subject, tax_number):
    return {'subject': subject['ref'], 'tax_number': tax_number}
