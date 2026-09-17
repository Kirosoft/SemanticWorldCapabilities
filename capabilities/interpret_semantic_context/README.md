# Conservative semantic interpretation

This functional implementation uses the existing HG InterpretSemanticContext
interface. It proposes only declarations supplied in its HG-validated context.

Lexical material may contain whitespace-separated full declaration references;
matching references are returned once each in deterministic reference order.
An entire lexical value equal to a declaration's leaf name is also supported.
Substrings, hints mapped through a private type registry, and declarations outside
the supplied context do not become candidates. Unsupported material/modifiers and
unmatched input return HG's unresolved result with a reason.

Hypotheses retain evidence and confidence as required by HG. They neither admit
meaning nor select executable implementations, and produce no Effects. Context
membership and lexical matching do not confer execution authority.

The source and bound tests are included in exact local-bootstrap admission.
Changing either produces a different candidate identity; an earlier admission is
not rewritten or silently promoted. Formal PR approval remains separate work.
