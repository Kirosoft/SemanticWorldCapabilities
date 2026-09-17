"""Exact arithmetic with HG-resolved output meaning; no persistence or I/O."""
from decimal import Decimal, localcontext
from semanticworld.inspection import resolve


def reconcile(invoices, refunds, source, unit, comparison_id, *, read, demand):
    positive, negative = tuple(Decimal(str(value)) for value in invoices), tuple(Decimal(str(value)) for value in refunds)
    observed = Decimal(str(source))
    values = positive + negative + (observed,)
    if not all(value.is_finite() for value in values):
        raise ValueError('Quantity calculation requires finite values')
    # Enough digits for exact alignment, addition and subtraction; no tolerance.
    precision = sum(len(value.as_tuple().digits) + abs(value.as_tuple().exponent) for value in values) + len(values) + 8
    with localcontext() as context:
        context.prec = precision
        computed = sum(positive, Decimal(0)) - sum(negative, Decimal(0))
        difference = observed - computed
    outcome = resolve(read.authority, 'OdooQuantityEquivalent' if difference == 0 else 'OdooQuantityDiscrepant')
    return {'computed': format(computed, 'f'), 'difference': format(difference, 'f'),
        'unit': unit, 'outcome': {'identity': comparison_id, 'type': outcome.path}}
