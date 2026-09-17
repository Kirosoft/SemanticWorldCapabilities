# Company TaxNumber update candidate

## Current typed-result migration

The implementation now returns only `{"tax_number": <HG TaxNumber>}`. Its reviewed
application description is `applications/company_tax_number_update.json`, relative
to this repository. SemanticWorld prepares the replacement against the recruited
ingress occurrence; no Effect envelope or extra Effect identity is produced.
These changed bytes and interface require fresh explicit admission. The protected
operational caller still uses the old occurrence protocol and has not been migrated.
The earlier integration claims below are historical, not validation of this version.

Candidate verification entry points now use
`semanticworld/interpretation/tests/test_typed_property_result.py`; run the workspace
interpretation runner against `.hg-functional-changes`. The old Effect expectations
are superseded by typed-output, unchanged-World and binding-target assertions. The
original workspace tests remain retained for migration accounting. This verification
does not establish current bundle admission, isolated invocation or protected commit.

## Historical implementation evidence

Status: functional implementation with explicit local bundle admission and SWC
invocation. Atomic World application remains incomplete. The HG application interface draft is
`HG/proposals/operational-property-update-v0.1/company-tax-number-update.json`
(workspace relative).

Semantic inputs are an exact PropertyOccurrence reference and replacement TaxNumber.
The callable adapter supplies a trusted SemanticWorld read and HG query as scoped
execution context. The function recruits the target, resolves Company binding
meaning directly from HG, validates and normalises the proposed World, and produces
an HG-validated immutable Effect. It performs no mutation or receipt creation.

This implementation requires HG and SemanticWorld helpers. `callable.toml` describes
its semantic entry point and the physical context parameters supplied by the host.
`swos.authority.python_callable.admit` can now admit its exact source/dependency
bundle under explicit local-bootstrap mode. `swc.world.evaluate` dispatches this
format to `swc.python_callable`, which binds scoped context and executes those
exact bytes. The legacy dependency-free worker rejects this format.

`swos.authority.python_dependencies.capture` now packages explicitly host-selected
Python roots as exact source bytes without importing them. Its currentness check
rejects changed, added, removed or substituted files. Seven tests cover the format,
including this candidate and the actual HG/SemanticWorld/helper roots. This is
physical packaging. The callable-admission record includes that complete snapshot,
its digest, entry signature, HG basis and test artifacts. Preparation checks the
entry's static import closure and excludes detected dynamic loading. It executes
neither the candidate nor its tests, and does not claim formal approval. The test
entry points use workspace verification fixtures; a hermetic verification bundle
and bound execution evidence are still needed for formal admission.

The static import inventory reaches 43 modules from this candidate with no missing
module or detected dynamic loader. Seven packaging/import tests pass, including
loading the captured bytes in a fresh `python -I -S -B` process and checking that
the candidate and helper module origins are inside the staged snapshot. This
proves loading without ambient workspace/site packages for the exercised imports.
It does not prove arbitrary dynamic behaviour safe, execute the update, or provide
an operating-system security boundary.

Offline verification is in `tests/test_property_update_callable.py`. These tests
exercise candidate code before admission, using the explicit local application
meaning shortcut and existing accounting snapshot. They do not invoke it through
the production SWC evaluator or authorise World updates.

The read-context codec in `semanticworld.call_context` now transports selected
authority identifiers and a fully scoped World view without backing-store bytes
or credentials. Reconstruction uses HG's original YAML loader and the selected
application declarations, then HG whole-World validation. Callable admission now
retains the exact HG declaration/primitive YAML files; tests reconstruct the same
base and application revisions from staged admitted files. The reconstructed
context refuses store reads/writes. Views requiring hidden facts are explicitly
unsupported rather than widening scope. The parent checks exact admission and
selected authority/context before and after execution, then validates HG egress.

`tests/test_python_callable_invocation.py` exercises the connected SWC path with
the actual staged bundle in a fresh Python process. It verifies the canonical
Effect, retained input provenance, unchanged store, invalid ingress/egress refusal,
and rejection when the World basis or implementation selection changes during
execution. Production transport uses a restricted Docker container; these tests
substitute local subprocess transport and do not establish Docker isolation.
The current adapter supports the explicit `read`/`demand` context. Synchronous
bundles also run inside an HG Process when a deferral hook is configured; HG's
`external_io: false` keeps that hook unused. External-I/O bundle deferral and
Policy evaluation remain unsupported. General callable lowering and atomic
application remain work.
