"""Functional Company creation candidate; no World writes, identities or authority."""
from hostio import fail


def propose_company_creation(industry: "node/class/industrytype", tax_number: "property/identifier/taxnumber", *,
                             read, demand):
    """The recruited IndustryType of the new Company. SWC has already validated both inputs against HG and the selected
    World; generic protected creation derives the Company's identity and establishes its industry and tax number."""
    if read.world is None:
        fail("NOT_BOOTSTRAPPED", "Company creation requires a selected World basis")
    return industry
