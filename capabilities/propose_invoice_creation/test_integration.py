"""Functional workspace verification, retained in the explicit local candidate."""
from test_invoice_creation_callable import test_candidate_returns_inert_request_and_refuses_occupied_subjects


def test_inert_creation_request():
    test_candidate_returns_inert_request_and_refuses_occupied_subjects()
