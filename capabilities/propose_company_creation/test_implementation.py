from implementation import propose_company_creation


def test_the_proposed_industry_is_the_recruited_one():
    assert propose_company_creation("seed://witness/industry", "GB123456789") == "seed://witness/industry"
