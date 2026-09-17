# SemanticWorldCapabilities

Current registration alignment and test limits are recorded in [MIGRATION.md](MIGRATION.md).
Candidate manifests use direct Capability paths. Application interface proposals
and five integration suites still require HG/runtime migration; standalone test
success does not establish current admission. [Application status](applications/README.md)
records the outstanding semantic dependencies.

This repository supplies proposed semantic software for SWOS admission.
[The specification](SemanticWorldCapabilities.md) governs every candidate.

The initial [candidate workflow](CANDIDATE_WORKFLOW.md) defines packaging, review and
approval evidence. The user-authorised temporary local-bootstrap path can admit
exact Python packages and eligible HG-described application refinements; it does
not establish formal approval. See [local admission](LOCAL_CANDIDATES.md).
Do not add runtime plugin registration or treat merged code as invokable authority.

All semantic descriptions and constraints must use HG. The former SWOS-local schema
registry was removed; it must not be reproduced here. SWOS owns protected admission
and authorisation. SemanticWorld queries its selected catalogue and instances;
SWC binds and invokes selected implementations. Approval contributes evidence to
the wider authority model.

Implement candidate computation as pure functions with explicit inputs/outputs and
immutable data. Keep physical effects in explicit adapter functions. Functional style
supports future promotion but does not itself make a function a Capability.

Boot-time candidate discovery now supports an explicit [local configuration](BOOTSTRAP.md).
It feeds existing SWOS admission and selection; it does not register executable
authority directly from the repository.
