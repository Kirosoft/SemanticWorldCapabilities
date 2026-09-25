# ProposeAccountStateChange

Proposes changing an Account's lifecycle status (its admitted `"status"`
relationship binding, `edge/in_state` → `node/state/accountstatus`) to a
lawful alternative — Active, Suspended, Closed. Same generic transition
law the Deal Capabilities already use
(`semanticworld/document_state.py::prepare`), targeting Account's
`"status"` binding instead.

Requires exactly one existing status fact on the subject Account and
exactly one lawful alternative State recruited into the Projection;
ambiguous alternatives, incomplete context, and an unchanged State are
refused. The result grants no execution or commit authority — only the
protected SWOS commit path can make a proposed replacement authoritative.
