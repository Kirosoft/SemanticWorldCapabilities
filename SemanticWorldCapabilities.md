# SemanticWorldCapabilities Specification

**Version:** 0.1-draft
**Status:** Normative candidate-supply specification
**Repository:** `SemanticWorldCapabilities`

**Authority-scope clarification:** HG's admission pipeline owns platform and
principal-genus authority admission. SWOS owns application-level type admission with
sufficient evidence and determines when a proposal must instead go through HG admission.
Candidate submission, evidence and PR approval support the applicable route; they do
not let SWOS bypass HG's scope. References below to SWOS admission apply within that
responsibility and to its applicable implementation/runtime admission boundary.
Actual instances and Effects belong to SemanticWorld, separately from type admission.

---

# 1. Purpose

SemanticWorldCapabilities is the governed source repository for proposed semantic executable software.

It provides:

```text
Capability semantic proposals
implementations
tests
fixtures
evidence
manifests
provenance
```

It provides **no semantic authority**.

The governing rule is:

> **A repository artifact is a Capability candidate, never a Capability, until SemanticWorld OS admits it.**

---

# 2. Repository Role

SemanticWorldCapabilities exists to provide a reliable, inspectable and reproducible route from software construction to SemanticWorld OS admission.

The lifecycle is:

```text
idea
  ↓
implementation
  ↓
Capability candidate
  ↓
repo review / CI
  ↓
evidence
  ↓
SemanticWorld OS admission
  ↓
admitted Capability
```

---

# 3. Relationship to HG

Every Capability candidate must be described entirely using vocabulary admitted by its declared HG/SemanticWorld OS basis.

The repository MUST NOT create private semantic vocabularies merely for implementation convenience.

Unknown required meaning must be proposed separately through the semantic admission route.

---

# 4. HG Does Not Define Capabilities

HG itself does not need to contain:

```text
EmitTelemetry
GenerateReport
ApproveInvoice
GNEP
```

A candidate package describes those concepts using HG vocabulary.

SemanticWorld OS determines whether that description becomes admitted semantics.

---

# 5. Repository Presence Has No Authority

None of the following confer runtime authority:

```text
git commit
merge
PR approval
CI pass
tag
release
package publication
signature
MCP registration
```

Only SemanticWorld OS admission does.

---

# 6. Candidate Structure

Recommended layout:

```text
capabilities/
  <capability-name>/
    semantic/
      definition.*

    implementation/
      ...

    tests/
      contract/
      invariants/
      negative/
      integration/
      fixtures/

    evidence/
      ...

    candidate-manifest.*
```

Formats are implementation choices.

Semantic contents are normative.

---

# 7. Candidate Manifest

The manifest MUST identify:

```text
candidate id
candidate revision

semantic description
implementation identity
implementation kind

HG basis
SemanticWorld OS basis

requested authority scope

test suite
evidence bundle

artifact digest
signatures
provenance
```

---

# 8. Semantic Description

A candidate MUST describe:

```text
semantic purpose
ingress
egress
port roles
cardinality
constraints
permitted Effects
Policies
Process participation
relevant Event participation
authority scope
```

A bare function signature is insufficient.

A Capability describes a general semantic transformation `C: X -> Y`. Ingress and
egress may express data, state, classification and Process position using HG.
These dimensions compose within one Strategy topology and one SWC execution model.
State refinements must specify their governing semantics and required evidence;
an output label cannot substitute for authoritative state or admission.

---

# 9. Process Participation

A candidate SHOULD state the semantic contexts in which it participates.

Process participation can include transforming Process position itself, rather than
only identifying a surrounding workflow. Such transformations use ordinary admitted
ports and composition. Any proposed World change still requires declared Effects
and the applicable authorisation/materialisation path. An admission-preparation
Capability may produce an authority proposal, but cannot perform the privileged
decision as an ordinary SWC edge. See the
[unified transformation model](../SemanticWorldComputer/SEMANTIC_TRANSFORMATIONS.md).

A useful Capability is not merely:

```text
A -> B
```

but an admitted semantic unit whose role can be understood in relation to the wider World.

For example:

```text
EmitSemanticEvent

participates in:
  EventEmission Process

accepts:
  SemanticEvent

produces:
  EventEmissionReceipt
```

where these terms are themselves HG-expressible semantics.

---

# 10. Implementation Forms

Candidate implementations MAY be:

```text
Python
native binary
WASM
container service
HTTP service
MCP
model endpoint
hardware endpoint
```

No form receives privileged admission status.

---

# 11. Local Python Example

A local Python function is initially only code:

```python
def emit_telemetry(event):
    ...
```

To become a Capability, the repository must additionally provide:

```text
semantic definition
implementation identity
tests
evidence
admission proposal
```

---

# 12. Artifact Identity

Locally controlled implementation artifacts SHOULD be content-addressed.

The manifest SHOULD bind:

```text
source/build provenance
artifact digest
publisher signature
```

Tests and evidence MUST refer to the exact artifact identity being proposed.

---

# 13. Changed Code

Any executable change creates a new implementation identity.

A changed local `.py` file MUST NOT execute under the authority of an older admitted binding.

---

# 14. Remote/MCP Candidates

A remote implementation cannot normally provide exact code identity.

Its proposal MUST instead describe delegated implementation authority including:

```text
remote identity
endpoint
authentication
tool identity
contract
scope
trust conditions
```

MCP discovery never automatically creates a Capability.

---

# 15. Evidence Classes

Every normal candidate MUST supply evidence covering:

1. semantic closure;
2. ingress/egress contract;
3. implementation identity;
4. positive behaviour;
5. negative behaviour;
6. architectural invariants;
7. Effects;
8. failure behaviour;
9. provenance/security.

---

# 16. Semantic Closure Evidence

Evidence MUST prove:

```text
every semantic term resolves
all port semantics are admitted
all Effects are expressible
all Process/Policy relationships are lawful
no private semantic meaning exists only in code
```

---

# 17. Contract Tests

Contract tests MUST cover:

```text
lawful ingress
required ports
optional ports
cardinality
semantic roles
refinements
lawful egress
output principalisation
```

Binding MUST never rely solely on:

* parameter names;
* JSON shape;
* host-language type coincidence.

---

# 18. Behavioural Tests

Candidates SHOULD provide deterministic fixtures for expected normal behaviour where possible.

Tests SHOULD cover:

```text
representative valid case
boundary case
invalid case
failure case
```

Nondeterminism must be explicit and bounded.

---

# 19. Effect Tests

For a Capability that proposes mutation, tests MUST prove:

```text
declared Effects may be produced
undeclared Effects are rejected
Capability has no direct Authority-write route
failed invocation creates no authoritative truth
```

---

# 20. Leakage Guards

Tests MUST detect hidden SemanticWorld composition.

A candidate MUST normally fail admission if it:

```text
calls another semantic Capability implementation directly
performs GNEP/INEP internally for undeclared business inputs
contains hidden Process orchestration
directly mutates authoritative state
silently evaluates independent semantic workflow
```

Private implementation helpers remain valid.

---

# 21. Security Evidence

Platform/kernel candidate evidence SHOULD include as relevant:

```text
artifact signature
dependency provenance
SBOM
network requirements
filesystem requirements
secret requirements
sandbox assumptions
remote trust
privilege requirements
```

Customer-level evidence requirements MAY be scoped by Policy but cannot bypass mandatory invariants.

---

# 22. Negative Tests

Every platform/kernel Capability SHOULD include tests designed to prove that important forbidden paths cannot work.

Examples:

```text
attempt direct World mutation
attempt undeclared Effect
attempt direct second Capability invocation
attempt arbitrary semantic lookup
```

---

# 23. Evidence Immutability

Evidence is valid only for the candidate and implementation identity against which it was produced.

If:

```text
semantic definition changes
implementation changes
governing authority changes incompatibly
required validation Process changes
```

new evidence may be required.

---

# 24. CI

Repository CI SHOULD:

```text
validate candidate manifest
build artifact
compute digest
run local contract tests
run negative guards
construct preliminary evidence
```

CI success is evidence.

It is not admission.

---

# 25. PR Workflow

A recommended workflow is:

```text
candidate branch
   ↓
PR
   ↓
review
   ↓
CI / evidence
   ↓
merge
   ↓
candidate available for admission
```

Merge does not make the candidate recruitable.

---

# 26. SemanticWorld OS Pipeline

The normal route after candidate construction is:

```text
CandidatePackage
      ↓
SemanticWorld OS admitted validation Process
      ↓
EvidenceBundle
      ↓
AdmissionRecommendation
      ↓
ring-0 ADMIT
      ↓
admitted / rejected
```

---

# 27. Kernel/Bootstrap Candidates

This repository MAY contain the candidate source required to bootstrap SemanticWorld OS itself.

Examples:

```text
Capability semantic substrate
GNEP implementation
test execution
Capability validation
EmitTelemetry
evidence support
```

Bootstrap candidates MUST carry signed pre-generated evidence suitable for ring-0 verification.

---

# 28. Normal Restart

Capabilities are not re-admitted on every restart.

The repository is not a boot-time plugin scan.

The authoritative admitted surface lives in SemanticWorld OS.

---

# 29. Lazy Instantiation

An admitted Capability implementation MAY remain unloaded until recruited by SWC.

Therefore repository scale need not imply slow SemanticWorld startup.

---

# 30. Agent-Generated Capabilities

An agent MAY generate:

```text
semantic proposal
implementation
tests
fixtures
manifest
```

It enters exactly the same repository/admission pipeline.

Agent authorship confers no additional authority.

---

# 31. Customer Capability Sets

Customer-specific Capability repositories MAY adopt exactly the same candidate format.

For example:

```text
customer-a-capabilities
customer-b-capabilities
```

Their candidates may request only customer/application-level authority.

---

# 32. Promotion

Operational evidence may later support promotion:

```text
customer Capability
    ↓
platform candidate
    ↓
stronger tests/evidence
    ↓
SemanticWorld OS admission
```

Promotion does not happen merely because the implementation is useful.

---

# 33. Process Candidates

Processes and Strategies MAY use the same evidence-supply model.

A candidate Process SHOULD include evidence for:

```text
semantic closure
port closure
topology validity
Effect boundaries
branching
iteration
expected completion
failure behaviour
```

---

# 34. Platform Capability Examples

Potential platform candidates include:

```text
EmitSemanticEvent
EmitTelemetry
SemanticInterpretation
DocumentProjection
ExternalRequestDispatch
EvidenceCollection
```

Their exact admission is an Authority decision, not a consequence of being listed here.

---

# 35. Candidate Repository Independence

SemanticWorldCapabilities MUST NOT depend on operational SemanticWorld state.

Candidates should be constructible/testable from:

```text
HG basis
declared SemanticWorld OS authority basis
fixtures
test environment
```

without requiring uncontrolled production-state access.

---

# 36. No Runtime Registration

The repository MUST NOT expose a mechanism equivalent to:

```python
register_capability(fn)
```

that makes a candidate operational.

Runtime registration without SemanticWorld OS admission is forbidden.

---

# 37. No Filesystem Authority

SWC MUST NOT treat:

```text
capabilities/
plugins/
tools/
```

or any filesystem path as executable authority.

The admitted implementation identity from SemanticWorld OS controls invocation.

---

# 38. No MCP Auto-Authority

MCP discovery may identify implementation candidates.

It MUST NOT create authoritative Capability bindings automatically.

---

# 39. Conformance Tests

### `SWCAP-001`

A newly committed candidate is not GNEP-recruitable.

### `SWCAP-002`

A merged candidate is not GNEP-recruitable.

### `SWCAP-003`

A CI-passing candidate is not GNEP-recruitable.

### `SWCAP-004`

An admitted candidate becomes recruitable only after SemanticWorld OS admission commit.

### `SWCAP-005`

Changing implementation content invalidates old implementation identity.

### `SWCAP-006`

Evidence for artifact A cannot admit artifact B.

### `SWCAP-007`

A candidate using unknown semantic vocabulary fails closure validation.

### `SWCAP-008`

Implementation parameter names cannot establish semantic ports.

### `SWCAP-009`

Undeclared Effects fail candidate validation.

### `SWCAP-010`

Direct authoritative mutation fails architectural validation.

### `SWCAP-011`

Hidden direct inter-Capability invocation fails architectural validation.

### `SWCAP-012`

Private helper functions remain permissible.

### `SWCAP-013`

An unadmitted MCP tool cannot be selected by SWC.

### `SWCAP-014`

Agent-generated code receives no special admission path.

### `SWCAP-015`

Customer-level admission cannot silently promote to platform scope.

---

# 40. Bootstrap Acceptance Scenario

Given a fresh SemanticWorld OS Authority and foundational HG, the repository supplies signed bootstrap candidates.

Required behaviour:

```text
candidate package
    ↓
ring-0 verifies immutable evidence
    ↓
minimal platform semantics admitted
    ↓
GNEP admitted
    ↓
testing/admission Process admitted
    ↓
remaining candidates use normal validation
```

At no point does repository presence create Authority.

---

# 41. Agent Acceptance Scenario

An agent generates:

```text
GenerateReconciliationReport
```

with implementation/tests.

Required path:

```text
agent output
    ↓
candidate repository
    ↓
CI/evidence
    ↓
normal SemanticWorld OS validation Process
    ↓
ring-0 ADMIT
    ↓
GNEP recruitable
    ↓
SWC invokable
```

Skipping any Authority step MUST leave the implementation non-authoritative.

---

# 42. Core Invariants

1. The repository contains candidates, not Capabilities.
2. Every candidate is described using admitted HG vocabulary.
3. Code existence never creates semantic meaning.
4. Repository presence never creates runtime authority.
5. PR merge never creates runtime authority.
6. CI produces evidence, not admission.
7. Implementation identity is immutable/content-bound where controllable.
8. Tests bind to the exact candidate artifact.
9. Capability semantics are independent of implementation parameter names.
10. Hidden semantic composition is prohibited.
11. Effects are explicit.
12. Direct Authority mutation is prohibited.
13. Remote implementations require explicit delegated trust admission.
14. Agent-generated candidates use the same route.
15. Customer candidates use the same route.
16. Promotion is a new admission event.
17. Bootstrap candidates are exceptional only in evidence source, not in final Authority status.
18. Only SemanticWorld OS can turn a candidate into an admitted Capability.

---

# 43. Compact Definition

> **SemanticWorldCapabilities is the non-authoritative semantic software supply repository for SemanticWorld. It contains Capability and Process candidates described entirely using admitted HG vocabulary, together with implementation artifacts, tests, evidence and provenance. Repository, CI, signature or package status never confers semantic authority. The repository exists to make candidates reproducible and reviewable so that SemanticWorld OS can validate and admit them through one Authority pipeline. Human-, platform-, customer- and agent-generated software all use the same route.**
