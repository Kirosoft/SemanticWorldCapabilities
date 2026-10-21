# ProposeDealOutcomeTransition

Realises the commercial outcome State that a recruited Strategy requires for a Deal, replacing its current State on its admitted `"outcome"` relationship binding (`edge/in_state` to `node/state/dealoutcomestate`).

The worker is handed the recruited Deal occurrence (the Capability's single typed input) and a trusted view of the World narrowed by the host to the required State type and its refinements (`demand["refinements_of"]`). It returns the unattached occurrence of that State. It does not recruit, does not read a Projection, and does not choose the target: the required State is the consequence Recruitment selected for this step (`StateCandidate`), carried as the step's effective output requirement. The host independently types the returned reference by the occurrence's own type, validates it against the declared output (`node/state`) and the requirement, and the state overlay checks the transition law of the governing Process.

One general Capability serves every lawful target (Won, Lost, Withdrawn). The result grants no execution or commit authority; only the protected SWOS commit path can make a replacement authoritative. This is a local-bootstrap candidate (no formal admission).
