# Configured local capability loading

Current production-basis limit: loading `bootstrap.local.json` against the actual
HG PR checkout admits the TaxNumber candidate, but Recruitment returns
NOT_BOOTSTRAPPED because that basis contains no admitted Recruit description.
End-to-end runtime conformance uses the separately marked synthetic operation
fixture. It does not establish a working production admission path for Recruit.
The operational descriptions still require their proper admission and selection.

`bootstrap.local.json` is the initial boot-time candidate list. Its application
files contain ordinary HG declaration descriptions; package directories contain
the existing `callable.toml`, implementation and test artifacts. The config has
only physical paths, not a second type vocabulary or an authority registry.

SWOS startup accepts `--bootstrap-config PATH` together with `--local-bootstrap`
and `--hg-root PATH`. Paths inside the config resolve relative to its directory.
`--workspace-root PATH` supplies sibling source dependencies and defaults to this
workspace. The configuration replaces the individual `--local-application` and
`--local-candidate` flags; combining them is rejected. The existing listener and
client-authentication settings still apply. An optional `--local-accounting-world`
creates the separately authorised sample grant; config loading alone creates none.

The configured set is admitted before the server starts accepting requests. Its
authority-basis endpoint publishes that selected set using the existing SWOS
boundary. The loader is also callable directly by an integrated host as below.

The protected SWOS host calls:

```python
from swos.authority.bootstrap import admit_configured

selection = admit_configured(
    store, config_path, candidate_root, hg_root, dependency_roots,
    enabled=True, world_grant_id=existing_world_grant,
)
```

The host supplies its selected HG checkout, dependency roots and optional existing
World grant. Dependency roots have the same `(module, path)` format as ordinary
Python callable admission. Config paths resolve inside `candidate_root`; duplicate
or escaping artifact paths are rejected. No directory scanning is performed.

SWOS validates the entire application meaning through HG and prepares each package
before persisting admissions. It uses the existing temporary local admission path
and returns the exact application and implementation selection. Formal approval
remains false. Discovery does not execute candidates or run their test suites;
existing package admission retains exact implementation and test artifacts.

The host publishes that selection through its trusted `read_authority` function
when calling `semanticworld.read.capture`. Recruitment then sees selected HG
declarations, including their typed input/output ports, and selected implementation
bindings. Config presence, package presence and old admission records cannot add
an executable binding to an unselected read.

Recruitment can enumerate one HG genus, for example
`{'genus': ['node/capability/executablecapability']}`, using the selected HG lineage.
It returns the same typed projection as exact-definition recruitment. The genus
includes itself and its refinements; only explicitly selected implementations
appear as executable bindings. Remote SWC selection reconstructs the same verified composed result. A broad
genus does not establish a unique executable binding; a single-result selection
still requires the exact SWOS-selected implementation ID. Multiple-genus
combinations are currently refused.
Physical work/result bounds and remote constituent verification also apply.
This uses the existing Recruit candidate input description; it does not admit
that platform candidate or introduce a new foundational HG definition.

Rebooting with the same basis/artifacts is idempotent. Changed bytes require new
admission identities. A failure returns no selection; immutable records already
written before a later failure may remain, but are not automatically selected.
The loader does not create World grants or install facts. Hosts must not substitute
an arbitrary config file or a caller-provided selection for protected SWOS control.

The candidate repository can later provide a richer catalogue source using this
same admission boundary. Structured queries over executable ports and transient
accumulator values still need their HG-expressed projection/query mapping; loading
a typed catalogue does not by itself implement that advanced query surface.
The current runtime test harness uses unadmitted operational candidate fixtures
with explicitly synthetic support records in a disposable test directory. Revised
Projection ports cannot reuse historical approval evidence. This loader does not
discover that directory or promote fixtures to production platform authority.
