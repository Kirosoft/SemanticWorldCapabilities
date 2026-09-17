# Candidate delivery and approval

Candidate source, HG descriptions and tests support a proposed admission.
Repository presence, a merged PR or successful execution alone cannot authorise it.

## Describe and package

Resolve all semantic vocabulary, types, Properties, relationships and constraints
through HG. Property and relationship cardinality remain HG law. Inputs and outputs
are HG types discovered and validated at registration. Do not invent another
Capability port schema or HG layer for Python mappings.

Use pure functions with explicit inputs/outputs and isolate physical I/O.
Retain exact source, dependency and test artifacts, the governing HG basis and
implementation provenance. Capability names are ordinary HG Properties; callable
locations and argument/result mapping are implementation-adapter details.

Candidate output is a typed result. Only the authorised constrained-commit path can
make typed changes authoritative. Effect and SemanticTelemetry wrappers are withdrawn.

## Review and admission

1. Submit the candidate, HG description and meaningful tests for formal review.
2. Run algorithm, contract, negative and integration checks against exact artifacts.
   Record failures and missing HG dependencies, not just the passing subset.
3. Obtain the applicable independent approval and trusted evidence for those bytes.
   Reviewer and Policy requirements must follow admitted governance.
4. SWOS assesses the route. Platform/principal-genus changes require HG admission;
   eligible application refinements require sufficient evidence and SWOS admission.
5. Admitted validation may prepare a proposal through SWC. The protected authority
   boundary makes the admission decision and selects eligible implementation IDs.

Changed artifacts invalidate reuse of earlier exact admission evidence. Generated
attestations must not modify the source commit whose identity they attest to.
Candidate execution cannot hold authority credentials or approve itself.

## Temporary local path and current status

The explicit local-bootstrap exception is implemented with temporary provenance.
It packages tests without running them and cannot promote itself to formal approval.
Formal founding, trusted evidence collection and normal admission remain incomplete.

Current application descriptions and integration consumers still need HG alignment.
The default test runner includes integration failures and exits unsuccessfully while
they remain. An explicit unit-only run establishes only algorithm coverage.

Use [migration status](MIGRATION.md), [local packaging](LOCAL_CANDIDATES.md) and
[SWOS formal admission](../SemanticWorldOS/docs/FIRST_CAPABILITY_ADMISSION.md).
