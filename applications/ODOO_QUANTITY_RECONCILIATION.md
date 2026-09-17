# Odoo quantity reconciliation candidate

`odoo_quantity_reconciliation.json` proposes one application Capability and two
State refinements under HG. Their zero/nonzero difference guarantees distinguish
the outcomes; they are not globally admitted reconciliation enums. The definitions
require explicit SWOS admission. Repository presence grants no authority.

The computation uses exact decimal sum(invoices) minus sum(refunds), then source
minus computed. Input collections have HG multiset semantics so repeated equal
quantities remain distinct contributions. The caller must establish eligible,
non-cancelled invoice/refund lines with identical evidenced source units. No unit
conversion, tolerance or source eligibility is inferred by this calculation.

The returned State-valued outcome is a semantic value, not a materialised World
observation. The Capability has no Effect ports. HG validates the interface and
admitted output types; bound implementation tests verify the declared arithmetic.
The implementation uses the existing Python callable adapter with exact local
artifact admission and an explicitly selected HG/application basis.

`tests/test_odoo_quantity_capability.py` covers exact fractional arithmetic,
refund subtraction, discrepancy, repeated contributions and actual isolated SWC
worker invocation. Its execution test checks that World/store contents remain
unchanged. V2 source eligibility and the full compiler are separate pending work.
