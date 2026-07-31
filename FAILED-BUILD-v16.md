# Failed v16 render attempt

The additive `docs-v16-20260729a/` candidate was copied from v15c with its
generated pages already present. On 29 July 2026 the renderer correctly
refused to overwrite four pages whose expected content changed. No page was
modified by that attempt.

The active candidate moved to `docs-v16a-20260729a/`, populated with static
inputs only before the write-once generator ran. The failed directory is
retained as construction history and is not selected by `site-state.json`.
