# Recruit operational admission proposal

Status: **unresolved; no approval or admission record**.

See [the complete demand-member audit](DEMAND_COVERAGE.md) and its source-pinned
`demand-surface-probe.json`. Five representative demands passed HG validation but
failed dispatch at the recorded revision; exact occurrence reads are now supported.
The remaining gaps mean the held proposal therefore remains
held despite the now-working ownership-query callable path.

`source-review.json` records a held coding-agent source review through HG's
`review_proposal(Failure, ...)` path. The original proposal, source and observed
failure digests were verified against the current HG semantic basis. HG refuses
to stage this held result. This is neither human approval nor production admission.

The concrete integration gap is the general `query` member: it is declared by
Recruit, but `semanticworld.read.recruit` dispatches specific genus, definition,
traversal and property forms before falling back to a single exact definition.
Standalone query interpretation is not the public integrated implementation.
Integrate the full declared form and its provenance/authority checks; do not
silently reduce the interface to the subset that currently passes. The review
pins inspected source files so later fixes can be reviewed against the exact code.

Implementation follow-up: local `read.recruit` now dispatches the general `query`
member to `semanticworld/general_query.py`. It validates HG ingress/egress, retains
selected basis and ownership witnesses, filters invisible owners, rejects unresolved
Policy eligibility and refuses exhausted work/result bounds without claiming a
complete result. Three local integration cases and the original query interpreter
suite pass. The held review is historical and unchanged; it is not admission of
this new implementation. Remote evidence verification/transport and reusable INEP
binding evidence remain incomplete, and HTTP explicitly refuses this query form
until its verification path is implemented. Full declared-surface conformance and
SWOS external catalogue selection still remain admission gates.

Remote follow-up: the HTTP server and client now support the general-query path.
The verifier reconstructs the returned HG nodes/occurrences and ownership edges,
replays the query over those witnesses, checks typed Projection output and exact
requested basis/bounds, and rejects rehashed row/owner/witness tampering. It does
not infer truth or completeness from the digest: the authenticated selected host
remains responsible for completeness and visibility. Four remote checks (including
real HTTP authentication, partition and stale-basis refusals), three local query
checks, nine interpreter cases and two existing read-service cases pass.
The earlier HTTP refusal is superseded. Reusable SWC ingress evidence and full
declared-surface conformance remain unfinished. The held review remains unchanged;
no completed HG admission or external-catalogue SWOS selection is claimed.

Ingress follow-up: local and remotely verified general-query WorldRead values now
retain the entire query projection as physical `QueryEvidence`. SWC's existing
input re-read/equality and continuation fingerprint code consumes it without a new
execution mechanism. Three integration checks prove local/remote equality and
refusal of changed evidence, occurrence values and authority selection; the four
remote and three local query cases remain green. This is retained read provenance,
not new HG vocabulary or an implementation grant. Full admitted callable execution
using a general query still needs end-to-end evidence, and full Recruit conformance
and external-catalogue admission/selection remain open.

Callable follow-up: the configured TaxNumber Python candidate now executes with
general-query ingress through the real isolated Python subprocess transport.
The exact SWOS local admission is selected, the worker returns HG-normalised
TaxNumber output, and the result retains the query's owner/binding evidence.
Storage and World remain unchanged. This is one passing end-to-end callable case,
using the disposable operational catalogue fixture; it proves neither production
Recruit admission nor Docker/OS sandbox isolation.

The real snapshot exposed two integration gaps now corrected: unrelated Policy
associations no longer block a query after its required ownership joins exclude
those subjects, and native owned PropertyOccurrences project their intrinsic
ownership witnesses using HG's `property_occurrence_edge`. Relevant unresolved
Policy still refuses the query; HG still validates each occurrence. No physical
duplicate edge or new World mutation is introduced. The original interpreter's
requirement for supplied witnesses remains unchanged below this World lowering.

Exact-identity follow-up: the existing HG `occurrence` member now recruits one or
multiple identities using the same query/witness path. The required occurrence
type is resolved from the admitted input port. The response retains the original
demand rather than replacing it with an internal query. Equal values do not merge
distinct identities; invisible owners expose no occurrences. Rehashed responses
containing an unrequested occurrence are rejected. Combined demand members remain
unfinished and this implementation does not confer admission.

The configured TaxNumber Python candidate admits against the actual HG checkout,
but `semanticworld.read.recruit` rejects its exact-definition query because Recruit
has no admitted description. The observed failure is recorded in
`observed-failure.json`; its digest is retained in the HG Failure.

`proposal.json` contains HG's canonical Declaration and RefinementProposal fields,
the full proposal digest, source-file digest and selected HG base revision. HG
structural validation succeeds without an evidence override. This does not claim
admission: no synthetic support record, reviewer report or admitted disposition is
included, and the selected HG base remains unchanged.

The proposal describes an operational executable interface over HG-defined query
members and the existing Projection type. It belongs with the capability catalogue,
not as a new foundational search/selection/coverage concept. It introduces no
SemanticProjection wrapper or mandatory Projection EXPOSES links. Its implementation
eligibility must be separately selected by SWOS after the applicable admission.

Outstanding review and implementation gates:

1. Review the complete declared query surface against the actual implementation.
   Passing exact/genus/property/traversal tests does not prove complete conformance
   for every query shape the description permits.
2. Obtain actual review of this failure and its retained artifacts. HG intake now
   accepts its existing Failure directly, preserving provenance and producing only
   a prospective delta with no seed replay. This enables review staging without
   fabricating an import; it supplies neither a review recommendation for this
   proposal nor an external operational-catalogue activation path.
3. A prospective delta or proposal digest is not completed admission. Preserve
   actual review, scope, provenance and implementation trust; approval is one
   contributor. A matching AdmissionRecord alone does not authenticate its issuer.
4. SWOS needs to select an exact completed HG admission for this external catalogue
   before SemanticWorld reconstructs it. Current selection supports one HG base and
   application admissions; local application mode must not promote a platform type.
5. Verify boot and Recruitment against that selected admission with no synthetic
   test overlay. This proposal is deliberately absent from `bootstrap.local.json`.

The canonical proposal digest can be reconstructed with HG's RefinementProposal;
source and evidence digests bind the checked artifacts. No files under the selected
HG checkout, admission evidence, implementation selection or World were changed by
preparing this review artifact. The boot probe used a disposable in-memory store.
