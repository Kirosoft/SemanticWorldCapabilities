# Company creation proposal

`company_creation.json` describes the proposed application Capability
`ProposeCompanyCreation`. It refines HG's existing Capability and uses
existing Company, IndustryType, TaxNumber and Effect meaning. It introduces no
platform genus, operation enum, schema registry or execution authority.

The new Company is represented by HG's `subject` value, carrying proposed identity
and type. An `instance` reference would require evidence that the Company already
exists and is therefore unsuitable for this ingress. Industry is an instance
reference and must already be recruited from the selected World. The Effect has
a structured payload containing those values; it does not falsely identify the
not-yet-created Company as an existing Effect subject.

Two current-HG interface tests pass, using explicit temporary SWOS application
admission in an isolated test store. They verify valid framing, unchanged base HG,
no invented instance-type evidence for the new Company, and rejection of unknown
Company types, fabricated Industry references and an `admitted` flag in a subject.
Repository presence and these tests do not admit an implementation or create facts.

Implemented path:

1. `semanticworld.company_creation.prepare` resolves the actual Company bindings and recruited Industry instance.
   Company requires its HG Industry relationship; it is not a duplicate property
   field. Use HG create availability and TaxNumber normalisation, including whole
   proposed-World validation. Refuse an identity occupied by any existing node or
   property occurrence.
2. `capabilities/propose_company_creation` supplies the functional Python candidate and exact local admission evidence. Its output
   is an inert HG Effect. It must retain the original query/World basis and must not
   receive a writable store or authority key.
3. `semanticworld.operations` interprets the exact admitted application meaning,
   preserving implementation provenance, currentness, atomic succession, receipts
   and replay. Revalidate the proposed payload; candidate validity flags are not
   authority. Do not turn this into a generic untyped dictionary update API.
4. All 12 creation tests pass (133.619 seconds), including four HTTP/actual Python
   child E2E cases: committed creation,
   duplicate identity and invalid scope/value refusal, unchanged catalogue authority,
   restart/query, lost-response replay and revocation before commit. Restricted
   Docker/Arango and telemetry recovery also pass, checked by
   `python -m tools.run tools.operational_check creation` from SemanticWorldOS.
   Exact source/admission fingerprints and results are retained in
   `../../semanticworld/company-creation-operational-evidence.json`; logs are
   `../../experiments/history/company-creation-focused.log` and
   `../../experiments/history/company-creation-operational-live.log`.

This application participates in the original speculative-fork mapping. Ordinary
Invoice creation and duplicate Invoice identity now have separate direct Invoice
tests and mappings. This application supplies no Invoice-generation semantics or
UKVATInvoicePolicy evaluator; the remaining Invoice Policy and derived-state
obligations are tracked separately.
