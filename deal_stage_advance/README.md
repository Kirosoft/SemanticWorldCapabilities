# ProposeDealStageAdvance

Proposes advancing a Deal's workflow/pipeline stage (its admitted
`"state"` relationship binding, `edge/in_state` →
`node/state/dealworkflowstate`) to a lawful alternative — Odoo CRM's
`stage_id` pipeline (New → Qualified → Proposition → Negotiation), an
independent dimension from the Deal's commercial outcome (`"outcome"`
binding, `ProposeDealOutcomeTransition`/`ProposeDealWithdrawal`). Same
generic transition law those Capabilities already use
(`semanticworld/document_state.py::prepare`), targeting Deal's `"state"`
binding instead.

Takes the recruited subject Deal as its single typed input and a trusted view
narrowed by the host to the State the recruited Strategy requires
(`demand["refinements_of"]`), exactly as the outcome worker does
(TYPED-WORKER-SEMANTIC-INPUT-001; DEAL-WORKFLOW-TYPED-INPUT-001). It selects that
State's single eligible occurrence, whether or not other Deals occupy it; it does not recruit, read a Projection or
choose the target. A requirement with no such occurrence is refused. The
result grants no execution or commit authority — only the protected SWOS
commit path can make a proposed replacement authoritative.
