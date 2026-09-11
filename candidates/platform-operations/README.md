# Operational candidates relocated from HG

Status: **unadmitted review candidates**, relocated from HG PR #41 `d9b72cc`.

This directory preserves Recruit, Navigate, CollectForward/Backwards,
ExecuteCapability, HandleProcess, ApplySemanticEffect, SemanticTelemetry,
SemanticProjection and its reference type. It preserves their meanings and test
inputs for review; it does not declare them foundational HG vocabulary or grant
execution authority. ExecuteCapability and HandleProcess describe SWC machinery
and their candidacy as separately admitted operations remains subject to review.

Original admission evidence is stored only under `.history/hg-admission.yaml`.
Those records describe the source snapshot; they are not current admission evidence.
No production loader or bootstrap selection has been modified to discover this
directory. These candidates require the applicable HG type-admission process and
protected SWOS admission/implementation selection before operational use.

Recruit's query member is now expressed through the existing HG recursive value
structure, not the withdrawn foundational `query` kind. SemanticWorld owns its
operational interpretation. Other declaration content is preserved for review.

The isolated SemanticWorld interpretation test runner stages these candidates as
test fixtures. Test success does not admit them. Existing capability packages and
previous local bootstrap selections are not automatically migrated.
