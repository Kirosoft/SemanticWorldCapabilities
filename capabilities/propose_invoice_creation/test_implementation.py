from implementation import propose_invoice_creation


def test_the_proposed_kind_is_the_selected_one():
    assert propose_invoice_creation("seed://witness/kind") == "seed://witness/kind"
