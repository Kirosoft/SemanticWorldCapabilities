# Operational candidates against current HG

Status: blocked semantic-interface migration, not completed conversion or admission.

## Observed blocker

The focused SemanticWorld Property-read and admission-capture test groups fail during
disposable fixture construction against the HG implementation containing PR #49:

```text
ValueError: Capability port does not allow field: cardinality
```

No test cases execute. This is not evidence of a Property read/replacement regression,
nor evidence that those updated consumer paths work. The runner stages all operational
candidates before discovering the requested tests, so the failure is not scoped to
the particular operation a test would exercise.

## Do not convert to another superseded contract

The candidates retain recursive `value`, `members`, reference-target and cardinality
descriptions in their ports. Current HG's retained codec accepts a different
name/type/required_guarantees representation, but HG's Capability meaning and
registration specification explicitly identifies that codec as transitional too.
Its acceptance is not a warrant to replace these candidates with named-port wrappers.

The agreed target is inputs and outputs defined entirely by admitted HG types,
resolved at registration. Physical argument names and return dictionaries belong
to SWC adaptation. Multiplicity, optionality, structured content and relationships
must remain governed by HG meaning, not disappear during a syntax rewrite.

## Concrete first migration requirements

| Candidate | Preserved requirement | Required treatment |
| --- | --- | --- |
| CollectForward | Exactly one input/output Projection; standard Recruitment of eligible one-step forward relations and context-matching Capabilities; genus-based interpretation, retained context/provenance, no automatic following, invocation or commit. | Candidate semantics updated; legacy port multiplicity retained pending the agreed HG interface. No separate choice schema. See [CollectForward migration](COLLECT_FORWARD_MIGRATION.md); implementation and registration remain outstanding. |
| CollectBackwards | One input Projection, one output Projection; backward reachability with the same scope/provenance protections. | Same type reuse, retaining the direction-dependent interpretation and existing test assertions. |
| Recruit | Its demand currently contains structured query variables, typed references, optional members and collections. | Identify reusable admitted HG demand meaning and its binding/cardinality law before replacing the recursive source structure. Do not substitute an opaque Structured payload or host query schema. |
| Navigate | Its selection currently distinguishes Property and relationship selections within a retained Projection. | Preserve endpoint/binding identity and directional constraints through HG-expressed selection meaning before changing the consumer contract. |
| ExecuteCapability | SWC invocation machinery. | Do not make it a founding HG validator or automatically migrate it as an ordinary admitted Capability merely because a test fixture contains it. |
| HandleProcess | SWC Process transduction machinery. | Keep runtime ownership with SWC; separate reusable admitted Process meaning from host execution framing. |

These are migration requirements, not an exhaustive reconstruction of every nested
source constraint. The candidate declarations remain the retained source contracts.
Their existing historical evidence is not rewritten and grants no current admission.

## Work sequence and evidence boundary

1. Resolve the agreed HG input/output type contract beyond the retained transitional
   named-port codec. Preserve meaningful multiplicity through HG law.
2. Identify and propose missing reusable demand/selection meaning, with actual
   semantic distinctions, rather than automatically promoting every nested field
   into a new Property type. Contextual primitive-valued Properties can use the
   binding-local representation introduced by HG #49 where that law fits.
3. Migrate candidate descriptions and SemanticWorld/SWC consumers together, retaining
   source-to-target assertions and explicit reasons for changed expectations.
4. Adapt the test fixtures to that contract without importing removed HG runtime
   models, manufacturing compatibility aliases or silently skipping candidates.
5. Run isolated consumer tests against the exact intended HG implementation and
   authority basis. Fixture construction and passing tests do not grant admission.

HG owns the definition and shared binding law. SemanticWorld owns Recruitment and
interpretation; SWC owns binding/invocation/Process transduction; SWOS owns protected
selection and admission. No host enum, permissive fallback or automatic capability
admission is introduced by this migration note.

## Current outcome

Candidate declarations are deliberately unchanged. Neither cardinality nor other
rejected fields have been stripped. The immediate migration is a dependency on the
agreed HG semantic interface and missing input-type meaning, not a request to weaken
the loader. No additional test run is claimed by this documentation update.
