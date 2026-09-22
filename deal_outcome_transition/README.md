# ProposeDealOutcomeTransition

Proposes replacing a Deal's current commercial outcome State (its admitted
`"outcome"` relationship binding, `edge/in_state` → `node/state/dealoutcomestate`)
with a lawful recruited alternative. Same generic transition law
`ProposeDocumentStateTransition` already uses (`semanticworld/document_state.py::prepare`),
targeting Deal's `"outcome"` binding instead of a TransactionalDocument's
implicit one — the first Capability to exercise Deal's `"outcome"` binding
at all; zero new HG declarations were needed to support it.

Requires exactly one existing outcome fact on the subject Deal and exactly
one lawful alternative State recruited into the Projection; ambiguous
alternatives, incomplete context, and an unchanged State are refused. The
result grants no execution or commit authority — only the protected SWOS
commit path can make a proposed replacement authoritative.
