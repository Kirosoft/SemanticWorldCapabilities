# ProposeCompanyCreation

Functional Python lowering of the application meaning in
`../../applications/company_creation.json`. It takes an HG Company subject with a
proposed identity, a recruited existing IndustryType reference and a TaxNumber.
It resolves HG's required Industry relationship and TaxNumber binding, checks
create availability, normalises the value and validates the whole proposed World.
The result contains typed Company, Industry and normalised TaxNumber values;
no candidate code writes facts or admits authority.

`callable.toml` pins the semantic entry, dependencies and functional test artifacts
through SWOS's explicit local-bootstrap Python admission. The host separately
selects that exact admission for SWC invocation. The worker receives read-only
context and has no store credentials or protected host key. Test success and
repository presence confer no admission; this is not the formal PR approval path.

The protected host revalidates those values against its original ingress and current
World before committing. Existing node/property identities, mismatched payloads,
unrecruited Industry references and invalid HG values are refused. Replaying the
same host request returns its original receipt; a different request cannot create
the same Company again. Generated Invoice identifiers and future Policy evaluation
are outside this application's meaning.

The typed-output revision requires fresh explicit admission. The isolated
SemanticWorld interpretation suite exercises actual local application/callable
admission, fresh-process SWC execution and protected commit. The six original
interface, preparation and candidate cases now use typed outputs and an explicitly
granted sample World on the selected HG basis. `test_implementation.py` references
the migrated callable cases. Historical admission evidence does not verify these
changed bytes. Production operation admission and
Docker isolation are not established by the subprocess integration fixture.
