# Projection-based document-state candidate

This is a prospective replacement for the historical four-argument package, not
an admitted implementation. It has one HG Projection input and one HG State output.
Python context keywords and reference serialization are physical lowering details.

The input recruits one transactional document and candidate State instances.
Existing IN_STATE relationships determine current state and binding. This candidate
chooses only a unique alternative accepted by HG whole-World validation. It does
not impose an ordering on states or invoke other capabilities. Ambiguity is refused.

The explicit bootstrap configuration selects this package alone. Do not combine its
declaration with the historical declaration of the same path. No existing admission
or operational evidence authorises these new artifacts.

The SWC Projection adapter now has an explicit typed-output transport. Its parent
validates returned references against the current scoped World. The protected
coordinator restores the Projection and uses the existing atomic commit and replay
path. Tests for that wiring use explicit worker doubles, not Docker execution.

Pending: run the candidate and coordinator tests; admit the exact artifacts and
test evidence through SWOS; verify real worker execution, commit, conflict and replay.
The existing commit implementation and its authority checks must be reused, not
replaced by a separate persistence path. Tests use repository fixture helpers and
do not constitute worker execution or admission evidence.
