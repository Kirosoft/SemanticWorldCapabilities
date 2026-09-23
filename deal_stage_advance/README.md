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

Requires exactly one existing stage fact on the subject Deal and exactly
one lawful alternative State recruited into the Projection; ambiguous
alternatives, incomplete context, and an unchanged State are refused. The
result grants no execution or commit authority — only the protected SWOS
commit path can make a proposed replacement authoritative.
