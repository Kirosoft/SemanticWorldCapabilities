# standard_sil

Canonical standard SIL core declarations: Map, Filter, Fold. Declarations only: each refines its HG `semanticalgebra` combinator class (MemberwiseCombinator, SelectionCombinator, ReductionCombinator) and inherits the effective law from it. Ports use type variables (`?A`, `?B`); Filter carries `?A` on its projection input and output. No implementation id, no application type, no predicate. Realisation is derived generically by SemanticWorldComputer from the admitted declaration.

Admission uses the existing application/HG authority route (see STANDARD-SIL-CAPABILITIES-001); the files confer no authority by being present.
