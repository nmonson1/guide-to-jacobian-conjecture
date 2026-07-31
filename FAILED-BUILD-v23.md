# Failed build: docs v23

The first `docs-v23-20260730a` construction ran the graph renderer before
installing the static site scaffold. It therefore contains the 494 generated
graph-native pages but omits the top-level reader pages and assets required by
the public-site validator.

The partial tree is retained as a construction record and is not selected by
`site-state.json`. The corrected build uses the fresh versioned path
`docs-v23a-20260730a`, installs the static scaffold first, and only then runs
the deterministic graph renderer.
