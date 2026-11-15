"""Functional Company creation candidate; no World writes, identities or authority (ENGINE-3C-001: a value function)."""


def propose_company_creation(industry: "node/class/industrytype", tax_number: "property/identifier/taxnumber"):
    """The recruited IndustryType of the new Company. SemanticWorld has already validated both inputs against HG and the
    selected World; generic protected creation derives the Company's identity and establishes its industry and tax number."""
    return industry
