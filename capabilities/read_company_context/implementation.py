"""Read an HG Company node supplied by SWC's explicit instance-reference lowering."""


def read_company_context(subject):
    return {"request": {"material": {"lexical": {"text": subject["node_type"]}},
                        "context": {"declaration": (subject["node_type"],)}}}
