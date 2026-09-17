# ProposeInvoiceCreation

Functional candidate for the [HG-based application proposal](../../applications/INVOICE_CREATION.md).
It returns an ordinary typed Invoice subject; it neither assigns an InvoiceNumber nor commits
an instance. SWOS must explicitly admit and select the exact bundle before SWC
invocation. The local test shortcut is not formal PR approval.

The previous 11-test Invoice suite covered the withdrawn Effect protocol. Its
restart, replay, conflict and lost-response expectations still need migration;
that historical evidence does not verify this changed candidate. Fresh exact
admission is required. Live verification is separate. The callable's
test artifact uses workspace test helpers, as supported by the temporary local
admission route; this is not a claim of a hermetic formal-admission test package.

The isolated SemanticWorld interpretation suite now verifies actual local admission,
SWC subprocess execution, typed-result validation, HG-generated numbering and
protected commit, followed by next-number preparation from retained allocation.
Its World/operation basis is a fixture and it substitutes subprocess transport for
Docker; production admission and OS isolation remain separate requirements.

Seven original interface/preparation/callable tests now run on the selected HG
basis with an explicitly granted sample World. Their candidate verification entries
use typed outputs; allocator conflict, rollback, reconstruction and unselected
record refusal are retained. Protected commit recovery/replay tests remain pending.

The remaining four recovery tests are now migrated too: all 11 focused Invoice
tests pass with typed outputs and physical request IDs. They verify HTTP replay,
fresh-store reconstruction, lost-response recovery, conflict without allocation
consumption and retention across a TaxNumber update. The run took 361.846 seconds;
this is correctness evidence, not acceptable performance or production admission.
