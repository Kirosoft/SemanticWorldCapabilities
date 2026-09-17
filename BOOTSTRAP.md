# Configured local candidate loading

The existing bootstrap.local.json is a proposed local configuration. Its TaxNumber
application description still uses excluded HG port structures. It is not currently
a working bootstrap configuration against the cleaned HG basis. Earlier admission
or NOT_BOOTSTRAPPED reports describe their recorded historical basis.

Configuration contains physical paths to application proposals and candidate
packages. It grants no authority. The protected SWOS host supplies the HG basis,
dependency roots and explicit local-bootstrap opt-in, validates proposals through HG,
packages exact artifacts, and selects the resulting eligible IDs.

SWOS startup accepts --bootstrap-config together with --local-bootstrap and --hg-root.
Configuration paths resolve relative to the configuration directory and must remain
inside the permitted candidate root. SWOS owns authority selection; SemanticWorld
provides catalogue/instance queries and Recruitment. SWC owns implementation
adaptation and invocation.

A compiled image, configuration entry or inbox receipt cannot install World facts.
An independently issued explicit sample grant may authorise its exact HG-validated
snapshot. The loader cannot manufacture that grant.

Capability and Process already imply execution. Use their direct HG paths.
Inputs/outputs are HG types resolved at registration; Python mapping and loading
are adapter concerns. Missing HG meaning cannot be inferred from files or host types.

Changed manifests and tests require fresh exact admission and selection. Retained
historical records are not automatically selected. Restore working admission only
after the proposal interfaces and runtime consumers follow current HG law.

See [local candidate admission](LOCAL_CANDIDATES.md) and [migration status](MIGRATION.md).
