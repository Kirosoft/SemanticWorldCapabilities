# Operational candidates relocated from HG

## CollectForward clarification

The latest user-agreed CollectForward contract is recorded in HG's
`proposals/collect-forward-navigation-v0.1/README.md`: exactly one Projection in
and one Projection out, with one-or-more input graph entry points and any relation
restriction carried by the Projection. It discovers eligible outgoing one-step
choices, including contextual Capabilities, without executing returned choices.
Materialisation means fetching during navigation, not committing semantic changes.
CollectForward is a Capability, not intrinsic machinery; other variants may coexist.

The older candidate YAML is retained as migration source, not a declaration that
its reachable-value wording or recursive port codec implements this clarified
contract. Missing Projection and type-based interface law remains an HG dependency.

## Retained source status

Status: **unadmitted review candidates**, relocated from HG PR #41 `d9b72cc`.

This directory preserves Recruit, Navigate, CollectForward/Backwards,
ExecuteCapability, and HandleProcess.
It preserves their meanings and test
inputs for review; it does not declare them foundational HG vocabulary or grant
execution authority. ExecuteCapability and HandleProcess describe SWC machinery
and their candidacy as separately admitted operations remains subject to review.

Original admission evidence is stored only under `.history/hg-admission.yaml`.
Those records describe the source snapshot; they are not current admission evidence.
`SemanticProjection` and its unused reference refinement are archived under
`experiments/previous_services/semantic_projection_candidates`. Current operation
inputs/results use HG's existing `node/projection`. This does not add mandatory
EXPOSES bindings to Projection; navigation remains a separately described operation.
No production loader or bootstrap selection has been modified to discover this
directory. These candidates require the applicable HG type-admission process and
protected SWOS admission/implementation selection before operational use.

Recruit's query member retains the historical recursive value structure rather
than the withdrawn foundational `query` kind. That recursive port representation
is not accepted by current HG. SemanticWorld owns operational interpretation;
neither repository presence nor this retained source grants current admission.
Other declaration content is preserved for review.

The isolated SemanticWorld interpretation test runner attempts to stage these candidates as
test fixtures. It generates explicitly synthetic support records using HG's own
support calculation, only inside its disposable marked test directory; historical
approval records cannot cover revised declarations. The selected HG base and its
evidence are copied unchanged, and candidates cannot overwrite its declarations.
These fixtures exercise runtime law, not a successful platform admission process.
Test success does not admit them. Existing capability packages and
previous local bootstrap selections are not automatically migrated.

Current-HG fixture construction is blocked before test execution by rejected port
cardinality fields; recursive value contracts need semantic migration too. HG's
remaining name/type port codec is itself transitional, not the agreed target.
[Current HG migration](CURRENT_HG_MIGRATION.md) records the constraint-preserving
work required. Do not remove cardinality or replace typed demand meaning with
opaque payloads just to make fixture construction succeed.
