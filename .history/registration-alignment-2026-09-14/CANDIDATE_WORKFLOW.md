# Candidate delivery and approval

Status: delivery workflow; repository protection, trusted collection/signing and normal
admission execution remain to be installed. This document does not grant approval.

The first delivery gate is [one valid Capability admission](../SemanticWorldOS/docs/FIRST_CAPABILITY_ADMISSION.md),
including durable authority and resolution of the exact admitted implementation.
Proposal submission and review alone do not satisfy that gate.

## Package

```text
capabilities/<name>/
  semantic/definition.json
  implementation/...
  tests/contract/...
  tests/invariants/...
  tests/negative/...
  tests/integration/...
  tests/fixtures/...
  evidence/...
  candidate-manifest.json
```

Use HG for all semantic definitions, relationships, ports and constraints. Do not create
a local Candidate/Scope/Effect/Decision schema. Identify the exact HG and SWOS basis and
the applicable admitted governance. Repository commits, artifact digests and build manifests
are physical provenance until interpreted into HG-expressible evidence. Describe ingress,
egress, roles, cardinality, Effects, Policies and Process participation using HG. Report
missing semantic structure rather than defining it in code; a function signature is insufficient.

Write computation as pure functions over explicit immutable inputs/outputs, with I/O in
small adapter functions. No stateful domain classes or hidden inter-Capability composition.
Approval is one contributor to authority; semantic closure, law, implementation trust,
scope, Policy and evidence remain independently governed requirements.

Do not put generated attestations into the source commit whose identity they attest to.
Build candidate/evidence bundles as immutable CI outputs with source provenance; changing
source or artifacts requires new candidate identity and applicable approval/checks.

## PR gate

1. Submit source, semantic description and tests in a candidate PR.
2. Run contract, negative, effect, failure and architectural-leakage tests against the
   exact build; produce evidence binding source and artifact digests.
3. Require at least one authorised reviewer other than the author and required checks.
4. New candidate content invalidates its old approval; account for integration/merge
   changes before producing the final attestation.
5. A trusted collector verifies the repository/PR/reviews/checks and signs an approval
   statement tied to the exact candidate digest, policy revision and validity interval.

Repository protection should prevent ordinary bypass and dismiss stale reviews. The
reviewer allowlist and approval-policy revision must be governed outside candidate code.
Never run untrusted PR code in a privileged collector or expose signing secrets to it.
Use unprivileged CI for candidate tests; keep trusted approval collection separate.

## Admission gate

SWOS first determines the required authority route. Platform/principal-genus authority
definitions require HG admission; sufficiently evidenced application-type definitions
can be admitted by SWOS. Required HG dependencies must be resolved before dependent
application admission. Repository location and PR approval do not determine that route.
Actual instances and Effects belong to SemanticWorld and are not created by type admission.

Submit the immutable package and approval/evidence to SWOS. The admitted validation
Process runs in a restricted SWC worker and returns evidence/recommendation. SWOS
rechecks identity, approval, freshness, scope, authority basis and required evidence.
Only ring-0 ADMIT can commit admission. The validator cannot approve itself or acquire
authority write credentials.

The SWOS prototype can currently persist only uninterpreted input in its physical inbox. It has
no active bootstrap/normal admission route, so a PR approval cannot accidentally enable
execution before the remaining authority machinery is built.

## Bootstrap candidates

Use the [founding inventory](../SemanticWorldOS/docs/FOUNDING_BUNDLE.md) to establish
the minimum candidate closure and external evidence. The intrinsic SWOS verifier
establishes founding admission under independently provisioned HG-governed trust;
these candidates do not validate themselves into initial authority. The next gate is
admitting an additional candidate through the installed normal admission Process.

First audit the HG closure and dependencies for recruitment, invocation support,
evidence construction and the validation Process. Supply signed pre-generated bootstrap
evidence and approved artifacts for the minimum set. Ring 0 verifies the bundle without
arbitrarily executing it. Thereafter validator changes use the currently admitted Process.

## Release/change gate

Each executable change, semantic change or scope promotion is a new candidate. Retain
the original evidence and admitted identity. Exact approved bytes must be the bytes
resolved for invocation; an edited local file never inherits an older binding.
