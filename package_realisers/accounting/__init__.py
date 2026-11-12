"""Execution functions for the accounting package, linked to the HG paths they realise.

Each function is the physical computation of one admitted Capability. It is
handed a World view and a grounding (input type -> occurrence ref) and returns
the single occurrence it produces. It reads nothing else and writes nothing:
where the result lands is the business of the Capability's effect law and the
Edge realiser, both declared in HG.
"""
from hg.relationships import SemanticNode
from semanticworld.swi.library import realiser, world_realiser
from semanticworld.swi.realisers import Produced, grounded


def _state(result_type: str, identity: str) -> Produced:
    """A State occurrence of the declared result type, named by the issuing witness (replay-stable)."""
    return Produced(SemanticNode(f"swi://{identity}/{result_type.rsplit('/', 1)[-1]}", result_type))


@world_realiser("node/capability/qualifydeal")
def qualify_deal(world, grounding, identity):
    grounded(grounding, "node/aggregate/deal")
    grounded(grounding, "node/state/dealworkflowstate/newdealstate")
    return _state("node/state/dealworkflowstate/qualifieddealstate", identity)


@world_realiser("node/capability/windeal")
def win_deal(world, grounding, identity):
    grounded(grounding, "node/aggregate/deal")
    grounded(grounding, "node/state/dealworkflowstate/qualifieddealstate")
    return _state("node/state/dealoutcomestate/wondealstate", identity)


@world_realiser("node/capability/withdrawdeal")
def withdraw_deal(world, grounding, identity):
    grounded(grounding, "node/aggregate/deal")
    grounded(grounding, "node/event/dealsignal/withdrawalsignal")
    return _state("node/state/dealoutcomestate/withdrawndealstate", identity)


@world_realiser("node/capability/linkdeal")
def link_deal(world, grounding, identity):
    """The result is the Deal occurrence itself: relating two existing occurrences mints nothing."""
    grounded(grounding, "node/party/company")
    deal = grounded(grounding, "node/aggregate/deal")
    return Produced(world.node(deal))


@world_realiser("node/capability/registertaxinvoice")
def register_tax_invoice(world, grounding, identity):
    """The result is the input occurrence under the refined type; identity is preserved by construction."""
    invoice = grounded(grounding, "node/document/transactionaldocument/invoice")
    return Produced(SemanticNode(invoice, "node/document/transactionaldocument/invoice/taxinvoice"))


# ---- value realisers: a library. Each function realises an admitted Capability; its meaning is
# the reviewed HG declaration (swi.library: the contract is the admitted one; annotations only map parameters). The body sees typed values only.
from decimal import Decimal
from decimal import Context, Inexact, MAX_EMAX, MAX_PREC, MIN_EMIN, localcontext

Q, FLAG = "property/quantity", "property/flag"


@realiser("node/capability/doublequantity")
def double_quantity(quantity: "property/quantity"):
    """Morphism: a Quantity to twice that Quantity. Commits nothing on its own; a combinator applies it to each member of a source."""
    return str(Decimal(quantity) * 2)


@realiser("node/capability/ispositivequantity")
def is_positive_quantity(quantity: "property/quantity"):
    """Predicate: whether a Quantity is strictly greater than zero. Commits nothing on its own; a selection combinator applies it to each member of a source."""
    return Decimal(quantity) > 0


@realiser("node/capability/addquantities")
def add_quantities(accumulator: "property/quantity#accumulator", member: "property/quantity#member"):
    """Morphism: the sum of an accumulator Quantity and a member Quantity; the two same-typed inputs are told apart by their semantic roles. Commits nothing on its own; a reduction combinator folds it over a source."""
    return str(Decimal(accumulator) + Decimal(member))


@realiser("node/capability/subtractquantities")
def subtract_quantities(accumulator: "property/quantity#accumulator", member: "property/quantity#member"):
    """Morphism: the accumulator Quantity less the member Quantity; the two same-typed inputs are told apart by their semantic roles, so application order is HG data, never a parameter order."""
    return str(Decimal(accumulator) - Decimal(member))


@realiser("node/capability/settlequantity")
def settle_quantity(quantity: "property/quantity"):
    """Morphism: one settlement step, a Quantity reduced by one settlement unit of 250 and floored at zero. Endomorphic on Quantity, with zero as its fixed point. Commits nothing on its own; an iteration combinator drives it to closure."""
    return str(max(Decimal(quantity) - 250, Decimal(0)))


# ---- the authorisation diamond: three state morphisms, no Python beyond naming the result ----
@world_realiser("node/capability/assessrisk")
def assess_risk(world, grounding, identity):
    grounded(grounding, "node/aggregate/deal")
    grounded(grounding, "node/state/dealworkflowstate/qualifieddealstate")
    grounded(grounding, "node/state/dealriskstate/riskpendingstate")
    return _state("node/state/dealriskstate/riskacceptedstate", identity)


@world_realiser("node/capability/verifycontract")
def verify_contract(world, grounding, identity):
    grounded(grounding, "node/aggregate/deal")
    grounded(grounding, "node/state/dealworkflowstate/qualifieddealstate")
    grounded(grounding, "node/state/dealcontractstate/contractunverifiedstate")
    return _state("node/state/dealcontractstate/contractverifiedstate", identity)


@world_realiser("node/capability/authorisedeal")
def authorise_deal(world, grounding, identity):
    for port in ("node/aggregate/deal", "node/state/dealworkflowstate/qualifieddealstate",
                 "node/state/dealriskstate/riskacceptedstate", "node/state/dealcontractstate/contractverifiedstate"):
        grounded(grounding, port)
    return _state("node/state/dealoutcomestate/authoriseddealstate", identity)


@world_realiser("node/capability/markinvoicepaid")
def mark_invoice_paid(world, grounding, identity):
    grounded(grounding, "node/document/transactionaldocument/invoice")
    grounded(grounding, "node/state/invoicepaymentstate/awaitingpaymentstate")
    grounded(grounding, "node/event/paymentreceived")
    return _state("node/state/invoicepaymentstate/paidstate", identity)


# ---- LIFT-001 fixtures: two morphisms that were never designed to work together ----
R = "property/ratio"


@realiser("node/capability/normaliseinstallment")
def normalise_installment(installment: "property/quantity#installment"):
    """Morphism: one Quantity expressed as a Ratio of the standard unit (1000). Declared over one value; it knows nothing of sequences."""
    return str((Decimal(installment) / 1000).normalize())


@realiser("node/capability/sumratios")
def sum_ratios(ratio: "property/ratio"):
    """Morphism: the sum of one or more Ratios. Declared over a collection; it knows nothing of how the collection was made."""
    return str(sum(Decimal(v) for v in ratio).normalize())


# ---- QUALIFIED-PROPERTY-001: a money morphism; the currency is governed by HG, never by this body ----
M = "property/monetary"


@realiser("node/capability/summonetary")
def sum_monetary(monetary: "property/monetary"):
    """Morphism: the sum of one or more monetary amounts. It is handed magnitudes only; the amounts' shared currency is carried to the result by the admitted QualifiersPreserved law."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(sum(Decimal(v) for v in monetary))  # non-exponent decimal text; no rescaling


# ---- INVOICE-VAT-001: the two invoice computations beside SumMonetary. Each states, by its roled ports, which
# of the subject's values it reads; the rate is an HG value on the subject, never a constant here. ----
@realiser("node/capability/addvat")
def add_vat(subtotal: "property/monetary#subtotal", vat: "property/monetary#vat"):
    """Morphism: an invoice total from its subtotal and its VAT: subtotal + VAT. It is handed magnitudes only; the shared currency is carried by the admitted QualifiersPreserved law, and differing currencies have no total."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(Decimal(subtotal) + Decimal(vat))


# ---- S4 (X2, V1): line amounts and their fold over the lines an invoice owns. Roled ports say which values each reads;
# `over` (HG) says a port is filled from the lines the subject owns. Exact: never rounds. ----
@realiser("node/capability/multiplyquantity")
def multiply_quantity(line_quantity: "property/quantity#line_quantity", unit_price: "property/monetary#unit_price"):
    """Morphism: the amount of a line: its quantity multiplied by its unit price. It is handed magnitudes only; the price's currency is carried to the result by the admitted QualifiersPreserved law (a quantity carries none)."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(Decimal(line_quantity) * Decimal(unit_price))


@realiser("node/capability/vatonlineamount")
def vat_on_line_amount(line_amount: "property/monetary#line_amount", line_vat_rate: "property/ratio#line_vat_rate"):
    """Morphism: the VAT due on a line: its amount multiplied by its VAT rate. It is handed magnitudes only; the amount's currency is carried to the result by the admitted QualifiersPreserved law (a rate carries none)."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(Decimal(line_amount) * Decimal(line_vat_rate))


@realiser("node/capability/sumlineamounts")
def sum_line_amounts(line_amount: "property/monetary#line_amount"):
    """Morphism: the sum of the line amounts held by the lines a whole owns (a fold over its parts). It is handed magnitudes only; the amounts' shared currency is carried to the result by the admitted QualifiersPreserved law."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(sum(Decimal(v) for v in line_amount))


@realiser("node/capability/sumlinevats")
def sum_line_vats(line_vat: "property/monetary#line_vat"):
    """Morphism: the sum of the line VAT amounts held by the lines a whole owns (a fold over its parts). It is handed magnitudes only; the amounts' shared currency is carried to the result by the admitted QualifiersPreserved law."""
    with localcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN, traps=[Inexact])):    # exact: never rounds
        return "{:f}".format(sum(Decimal(v) for v in line_vat))


@realiser("node/capability/takeproductname")
def take_product_name(product_name: "property/label/name#product_name"):
    """Morphism: the name of the product a line refers to, as the line's description (a snapshot default, read across the reference)."""
    return product_name


@realiser("node/capability/takelistprice")
def take_list_price(list_price: "property/monetary#list_price"):
    """Morphism: the list price of the product a line refers to, as the line's unit price (a snapshot default, read across the reference). It is handed a magnitude only; the currency is carried by the admitted QualifiersPreserved law."""
    return list_price


@realiser("node/capability/takecategoryrate")
def take_category_rate(vat_rate: "property/ratio#vat_rate"):
    """Morphism: the VAT rate of the category of the product a line refers to, as the line's own rate (a snapshot default, read across the reference and the category)."""
    return vat_rate
