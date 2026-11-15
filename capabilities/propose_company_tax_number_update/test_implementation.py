from implementation import propose_company_tax_number_update


def test_the_proposed_tax_number_is_the_canonical_input():
    assert propose_company_tax_number_update("seed://witness/occurrence", "GB123456789") == "GB123456789"
