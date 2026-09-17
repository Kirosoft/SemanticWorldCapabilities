# CollectForward migration

Status: candidate semantic declaration updated; not an admitted or runnable
implementation. No runtime, traversal or test changes are part of this increment.

## Current contract

CollectForward takes exactly one Projection and returns exactly one Projection.
It uses standard Recruitment for eligible one-step forward relations and
Capabilities whose HG input requirements match the context. Relation relevance
comes from HG edge genus meaning and context, not a selected binding identifier.
Actual relationships remain subject to applicable HG binding constraints.

The result contains existing HG meaning, not separately modelled choices. It
retains originating entry points, matching context, provenance and applicable
scope/completeness. Nothing eligible to follow does not erase the input context.
Recruitment may fetch supporting content; it does not automatically follow every
result, invoke returned Capabilities, admit meaning or commit changes.

The previous candidate description of reachable values through selected bindings
is superseded. Historical evidence is not evidence for this revised contract.

## Retained interface dependency

The declaration still contains the legacy input_ports/output_ports representation,
including its exactly-one cardinalities and reference/subject encodings. These are
retained migration constraints, not an endorsement of that codec as current HG law.
The existing failures/external_io/policies fields are also legacy metadata, not
proof of a current implementation's behaviour or authority.

The known harness failure on the legacy cardinality field is not resolved by this
semantic update. Do not strip constraints, substitute the other transitional port
codec or invent a host signature to make registration appear successful. The
agreed HG type-based Capability interface must express the Projection input/output
contract before current-interface registration can be claimed.

## Remaining implementation work

No CollectForward implementation was located by name in SemanticWorldCapabilities
during this increment. Implement or explicitly identify the candidate adapter to
standard Recruitment after resolving the registration interface. Do not put an
intrinsic CollectForward evaluator into HG or change traversal, Process sequencing,
transducers or accumulator mechanics to supply that adapter.

Required behavioural evidence includes multiple entry points, restricted and
unrestricted one-step relations, empty and bounded results, matching and ineligible
Capabilities, inferred applicability without a stored edge, preserved provenance,
and absence of automatic following, returned-Capability invocation or commits.
These are outstanding cases, not passing tests. Formal approval and SWOS admission
remain separate from this local declaration update.
