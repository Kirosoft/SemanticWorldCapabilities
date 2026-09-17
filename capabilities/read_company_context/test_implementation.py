import unittest
from types import MappingProxyType
from implementation import read_company_context


def test_reads_bound_company_without_mutating_it():
    node = MappingProxyType({"ref": "seed://app/accounting/reference/company/acme", "node_type": "node/party/company"})
    before = dict(node)
    result = read_company_context(node)
    assert result == {"request": {"material": {"lexical": {"text": "node/party/company"}},
                                  "context": {"declaration": ("node/party/company",)}}}
    assert dict(node) == before
    assert read_company_context(node) == result


def load_tests(loader, tests, pattern):
    return unittest.TestSuite([unittest.FunctionTestCase(test_reads_bound_company_without_mutating_it)])
