# ProposeAccountStateChange

Realises the lifecycle status State that a recruited Strategy requires for an Account, replacing its current State on its admitted `"status"` relationship binding.

The worker is handed the recruited Account occurrence (the Capability's single typed input) and a trusted view of the World narrowed by the host to the required State type and its refinements (`demand["refinements_of"]`). It returns the unattached occurrence of that State, which no other subject occupies. It does not recruit, does not read a Projection, and does not choose the target: the required State is the consequence Recruitment selected for this step. The host independently types the returned reference by the occurrence's own type and validates it against the declared output (`node/state`) and the requirement; the state overlay checks the transition law of the governing Process.

A target State with no occurrence in the World (for example `Closed` in the current fixtures) cannot be realised and the invocation is refused; that is a data question, not a worker defect. This is a local-bootstrap candidate (no formal admission).
