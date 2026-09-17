from types import MappingProxyType
import unittest

from implementation import propose_company_tax_number


def test_proposal_preserves_exact_subject_and_normalised_value_without_mutation():
    subject = MappingProxyType({'ref': 'company:1', 'node_type': 'node/party/company'})
    before = dict(subject)
    expected = {'subject': 'company:1', 'tax_number': 'GB123'}
    assert propose_company_tax_number(subject, 'GB123') == expected
    assert propose_company_tax_number(subject, 'GB123') == expected
    assert dict(subject) == before


def test_distinct_subject_and_value_produce_distinct_inert_proposals():
    first = propose_company_tax_number({'ref': 'company:1'}, 'GB123')
    second = propose_company_tax_number({'ref': 'company:2'}, 'FR456')
    assert first != second
    assert second['subject'] == 'company:2'
    assert second['tax_number'] == 'FR456'
    assert set(second) == {'subject', 'tax_number'}


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(unittest.FunctionTestCase(value) for name, value in
        sorted(globals().items()) if name.startswith('test_') and callable(value))
