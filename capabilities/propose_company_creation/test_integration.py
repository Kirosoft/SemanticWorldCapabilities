"""Candidate verification entry points; workspace helpers are test-only."""
from test_company_creation_callable import (
    test_candidate_produces_canonical_typed_result,
    test_candidate_rejects_existing_company_and_invalid_tax_number,
)


def test_canonical_result():
    test_candidate_produces_canonical_typed_result()


def test_invalid_creation():
    test_candidate_rejects_existing_company_and_invalid_tax_number()
