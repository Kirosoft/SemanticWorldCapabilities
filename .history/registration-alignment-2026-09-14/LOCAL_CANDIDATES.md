# Temporary local Python admission

The user has authorised a temporary opt-in SWOS admission path that bypasses formal
PR review and normal admission execution. It does not claim those checks passed.
Candidate packaging is retained for later review and formal admission.

Each package supplies `candidate.toml`, implementation files and test files:

```toml
hg_path = "node/capability/executablecapability/navigate"
entry_file = "implementation.py"
function = "navigate_projection"
files = ["implementation.py"]
tests = ["test_implementation.py"]
rationale = "Explain how the implementation satisfies every HG guarantee and its limits."
```

This is a packaging example, not an implementation of Navigate. Do not substitute
a stub or identity function and claim it satisfies that meaning. New semantic descriptions
still need HG expression and the applicable admission route; the shortcut does not
create a parallel type system or edit HG's existing implementation references.

The initial supported Python subset has no implementation imports, classes, module
initialisation, decorators or default argument expressions. Functions use explicit inputs
and outputs. AST checks are structural checks, not a purity proof or sandbox. Dependencies
and richer execution forms require extending package verification before use.

SWOS verifies the HG tree, resolves the Capability description, checks source structure
and retains exact source/test bytes and hashes, the entry point, HG revision, HG Python
source hashes and original HG implementation reference in a content-addressed snapshot.
The local entry point is an explicit temporary binding overlay, not a rewrite of HG.
The package manifest is physical provenance, not a semantic authority schema.

From SemanticWorldOS, using its existing development client configuration:

```powershell
python -m tools.run swos.server --clients .runtime/clients.json --local-bootstrap --hg-root ../HG --local-candidate ../SemanticWorldCapabilities/capabilities/your-candidate
```

Each startup candidate produces its local admission id. Multiple candidate paths can
be supplied. Identical content is idempotent; changed content creates another immutable
identity. Selection must name an exact id, never silently use the newest source file.
The authenticated `/v1/local-admissions?id=...` endpoint resolves stored packages without
reading the candidate repository. This is exact local resolution, not a general GNEP
implementation. SemanticWorld now owns catalogue and instance queries and Recruitment
against the exact authority selected by SWOS. The former SWOS GNEP/INEP routes do not
serve those queries. SWC supplies scoped accumulator context, binds inputs and invokes
the selected implementation. General authorised World mutation remains unfinished.

SWOS does not import or execute candidate code or tests while admitting. Test files
are retained, but this path does not claim they passed or that semantic guarantees have
been proved. Run tests in a separate unprivileged worker and retain bound results for
formal review. The eventual formal process should consume the same source/test artifacts,
HG basis and rationale, with independently verified evidence and a formal binding.

Without `--local-bootstrap`, stored temporary admissions cannot be resolved through this
endpoint. Formal admission never inherits the temporary approval mode. ArangoDB retains
packages across restarts; InMemory is process-local. The
[InterpretSemanticContext candidate](capabilities/interpret_semantic_context/implementation.py)
provides conservative lexical interpretation against explicit HG declaration context.
See [SWC usage](../SemanticWorldComputer/README.md) for isolated evaluation and retained
test/execution evidence. It is a temporary local admission, not a formally reviewed release.
