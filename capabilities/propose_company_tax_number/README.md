# Company TaxNumber proposal candidate

`../../applications/company_tax_number.json` describes an eligible application
Capability over HG's Company, TaxNumber and Effect meanings. `candidate.toml` pins
the entry point and source/test files for explicit SWOS local admission. Repository
presence alone never makes it executable.

The pure function returns an inert Effect for the bound Company. Its text payload
retains the exact lexical input: current HG Capability text validation does not
apply the TaxNumber Property's minimum length or trim/uppercase normalisation.
This candidate therefore does not claim to produce a valid property update. Its
Effect has no admitted update-operation interpretation, and neither its port role
nor the absence of Capability policies provides principal/scope authorisation.

Run the package's two pure-function tests from this directory:

```powershell
python -m unittest discover -s . -p test_implementation.py -v
```

From `SemanticWorldOS`, six integration tests exercise application and exact local
implementation admission, Company binding, subprocess invocation, inert results,
and refusal of unselected code or invented operation/commit fields:

```powershell
python -m tools.run unittest discover -s ../tests -p test_company_tax_number_proposal.py -v
```

These tests grant no formal admission and perform no operational mutation. See
`../../../semanticworld/COMMIT_PLAN.md` for the missing HG interpretation and
protected commit steps. The test transport uses a Python subprocess; it is not
evidence of production Docker isolation.
