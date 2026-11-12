# Package realisers

The Python implementations of the Capabilities declared in the HG packages `accounting`, `manuscript` and `support`.
They moved here from `HG/packages/<name>/realisers` in step 1 of the engine consolidation (2026-11-12), because
implementation code does not belong in HG.

- `semanticworld.swi.library.load` imports `package_realisers.<name>` for each package the authority was loaded with.
- Each realiser is admitted only by its evidence in HG (`.evidence/realiser.yaml` and, for read-safe value morphisms,
  `.evidence/readsafe.yaml`). That evidence names `package_realisers.<name>.<function>` and pins the function's source
  digest. Being present in this repository does not admit a realiser.
- Regenerate evidence after a reviewed change with `python -m semanticworld.swi.build.write_realiser_evidence`
  (and `write_readsafe_evidence` for read-safe ones), from a root with HG, this repository and `semanticworld` on the path.
