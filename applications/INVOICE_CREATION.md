# Invoice creation proposal

`invoice_creation.json` proposes the application Capability `ProposeInvoiceCreation`
using existing HG Invoice and subject meaning. It admits no foundational
vocabulary. Explicit temporary SWOS application and implementation admission are
exercised in isolated tests; repository presence and test success grant no authority.

The caller supplies the proposed Invoice identity and HG type. The interface has
no invoice-number input. The typed output requests creation and contains that subject;
it does not pretend that an instance exists or that an index was already allocated.
HG's required InvoiceNumber binding is generated and not caller assignable.

The candidate in `../capabilities/propose_invoice_creation` validates the HG ingress,
refuses occupied node/property identities and unsupported required bindings, and
returns the validated typed Invoice subject. A selected SWC Python child executes the
exact bundle without writable storage or protected host keys. There are no existing
instance ingress ports; the adapter uses the real Capability Recruitment query
instead of inventing an unrelated existing-instance dependency.

The initial five focused prerequisite tests passed in 26.418 seconds, recorded in
`../../experiments/history/invoice-creation-prerequisites.log`. HG rejects supplied generated values;
its allocator demonstrates staged allocation, concurrent conflict, rollback reuse
and reconstruction from saved state. That in-memory API check does not prove
durable allocation or authorise the test seed as a real World's allocation basis.
The missing-lowering check has since been replaced by missing-protected-binding
refusal now that Invoice lowering exists. Successful SWC computation alone still
supplies no commit authority.

Protected integration is implemented in `semanticworld.invoice_creation` and
`semanticworld.operations`: reconcile the selected World's initial index state,
resolve HG-generated bindings, validate the proposed whole World and atomically
retain allocation, World, evidence, receipt and selected succession. Historically, all 11 Invoice
tests passed in 192.810 seconds (`../../experiments/history/invoice-creation-protected.log`).
These include conflict, lost response, restart/query, replay, duplicate identity,
unselected counter records and retention through an unrelated TaxNumber update.

That historical log covers the withdrawn Effect protocol. Current typed-result
verification is recorded in `semanticworld/interpretation/README.md`. Commit receipts
now use physical request IDs, and non-generating commits retain no new allocation
snapshot; the preceding selected snapshot remains the basis for further allocation.
Live Arango/restricted-Docker verification also passed, including generated number
`2`, retained next counter `3`, restart/query, replay with Docker unavailable and
independent telemetry recovery. Exact current source/admission fingerprints are in
`../../semanticworld/invoice-creation-operational-evidence.json`; the transcript is
`../../experiments/history/invoice-creation-operational-live.log`.

The ordinary Invoice creation case now has explicit current-HG adaptations for
generated numbering, native instance representation and removal of parallel claim
and validator hooks. The separate amount/Policy and derived-overdue cases remain unmapped.
See `../../SemanticWorldComputer/evidence/invoice-creation-migration-audit.md`.
