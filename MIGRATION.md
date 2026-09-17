# Candidate registration alignment, 2026-09-14

## Changes

Candidate manifests now use direct node/capability paths. The old manifests are
retained under .history/registration-alignment-2026-09-14. Names, artifacts and test
lists changed, so previous admission IDs and evidence cannot cover the new packages.

Standalone tests no longer import workspace integration suites. Original verification
entry points remain in test_integration.py and are still listed in candidate manifests.
The default runner executes both kinds and reports failure when integration fails.

The interpretation integration test now imports runtime checks from SemanticWorld
and resolves its HG root from the imported package. No HG compatibility alias is added.

## Coverage retained

| Candidate | Standalone coverage | Retained integration obligation |
| --- | --- | --- |
| InterpretSemanticContext | Determinism, immutability, lexical matching, confidence, context bounds, ordering and unresolved cases | HG ingress/egress validity and invalid-ingress rejection |
| Odoo reconciliation | Exact decimal arithmetic, duplicate quantities, unit and subject retention, HG-validated State lookup, finite-value refusal and missing-meaning refusal | Full application admission and runtime fixtures |
| Company creation | Existing tests remain integration tests | Canonical typed result, immutable output, occupied identity and invalid-value refusal |
| TaxNumber update | Existing tests remain integration tests | Exact Property target, canonical result, invalid values/envelopes and retargeting refusal |
| Invoice creation | Existing tests remain integration tests | Inert creation, occupied node/Property identity, numbering refusal and no commit |
| Other seven candidates | Existing eight computation cases preserved | Passing standalone cases do not confer admission |

The replacement reconciliation unit fixture uses only the two existing State
proposals, validated through HG under the explicit test-local application path.
It does not invent outcome enums or admit the full Capability interface.

## Run and evidence

From the workspace:

    python SemanticWorldCapabilities/run_tests.py --hg-root .hg-clean-pr

Supply the selected HG checkout explicitly. The runner isolates every test artifact
in a separate process, preserves full failures and rejects zero-test artifacts.
Add --unit only for an explicitly limited standalone run.

The full run reports nine passing standalone suites (16 cases) and five failing
integration suites. The failures remain a visible runtime dependency, not skipped
tests or evidence of successful current-basis admission.

## Unresolved dependencies

SemanticWorld's interpretation runtime still imports the removed CapabilityMember
and CapabilityValue model. The application proposals retain excluded recursive port
and Process structures. The replacement HG registration interface remains pending.

Completing Company creation, TaxNumber update, Invoice creation and the retained
integration scenarios requires that meaning and consumer migration. Restoring
removed HG schemas, discarding valid Property/relationship cardinality, or adding a
host semantic registry is not an authorised solution.

The legacy Company proposal generator now refuses explicitly before emitting
withdrawn schemas. Bootstrap configuration remains blocked until its descriptions
and consumers are lawfully aligned. Post-commit trigger meaning and formal admission
are not established by this cleanup.
