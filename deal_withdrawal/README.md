# ProposeDealWithdrawal

Proposes withdrawing a Deal by replacing its current commercial outcome
State (its admitted `"outcome"` relationship binding, `edge/in_state` →
`node/state/dealoutcomestate`) with the terminal `WithdrawnDealState`
alternative. Same generic transition law `ProposeDocumentStateTransition`/
`ProposeDealOutcomeTransition` already use
(`semanticworld/document_state.py::prepare`), exposed as its own named
Capability for a clear delete/withdraw journey narrative — SemanticWorld's
append-only, World-succession model has no physical-deletion mechanism, so
"delete a Deal" is represented as a real terminal state transition, not a
removal.

Requires exactly one existing outcome fact on the subject Deal and exactly
one lawful alternative State recruited into the Projection; ambiguous
alternatives, incomplete context, and an unchanged State are refused. The
result grants no execution or commit authority — only the protected SWOS
commit path can make a proposed replacement authoritative.
