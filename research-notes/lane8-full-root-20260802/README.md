# Lane 8 source-provenance harness

This directory contains the small CI utilities that recover the executable
sources embedded in the active public Lane 8 packets and fetch the published
Program 6 supplement. The theorem-bearing proof package is
[`contributions/JCG-C-0015/`](../../contributions/JCG-C-0015/).

The extractor verifies the pinned packet and member SHA-256 values before
writing any recovered source. The Program 6 fetcher verifies the published
archive digest before extraction. The entrypoint probe records, rather than
guesses, the command-line contracts of the recovered programs.

The canonical independent replay, proof-carrying queue, denominator ledger,
formal proof, and validation checker live in the contribution directory. The
CI workflow runs both that replay and the separately published reconstruction
and compares their invariant digests.

Two boundaries remain explicit:

- the layer-four square is retained scheme-theoretically and reduced only for
  geometric routing;
- the stored adjacent-chart terminal is exact but unattached, because the bare
  `k=4` shear starts at normal order seven. It is not used in the direct Lane 8
  closure.
