---
title: "Proof and evidence ledger"
description: "Claim scope, primary proof locations, exact computation, independent checks, source form, and publication status for the guide's major-result pages."
---

# Proof and evidence ledger

The audit record belongs here, away from the result essays. Each entry states
what is proved, where the proof or certificate lives, what an independent
check verifies, and which claims remain announced pending a public full
proof.

The categories are deliberately separate:

- a **proof source** supplies the mathematical argument;
- an **exact computation** proves only the statement encoded by its inputs and
  certificate contract;
- a **formalization** checks the theorem represented in the formal statement;
- an **announcement** records a public claim whose full proof may still be in
  preparation;
- **peer review** and **editorial review** are publication processes, not
  substitutes for the items above.

The ledger is current to **7 August 2026**.

<a id="the-three-dimensional-counterexample"></a>
## The three-dimensional counterexample

| Field | Record |
| --- | --- |
| Reader essay | [The explicit counterexample](../start/counterexample.md) |
| Mathematical status | Exact theorem. The displayed map has determinant \(-2\) and an explicit three-point collision. |
| Primary source | [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf), containing the formula, construction, determinant, and collision. |
| Public announcement | [Levent Alpöge, 19 July 2026](https://x.com/__alpoge__/status/2079028340955197566). |
| Geometric reconstruction | [Terence Tao, “A digestion of the Jacobian conjecture counterexample”](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/). |
| Formal and independent checks | [Alejandro Radisic, Lean, pinned revision](https://github.com/alerad/alpoge-lean/tree/b39e3bf3493939db11b0f78c5b369dd028093f0f); [Paul Lezeau, Formal Conjectures PR 4474](https://github.com/google-deepmind/formal-conjectures/pull/4474); [Dean Cureton, all-characteristics Lean development](https://github.com/deancureton/jacobian/tree/0d4a9212d874226ad81ce5a926becddfa94e6a88); [Pablo Nogueira Grossi, independent Lean 4 verification](https://doi.org/10.5281/zenodo.21514514). |
| Credit recorded here | Akhil Mathew suggested the question to Alpöge; Alpöge asked Fable; Fable produced the work leading to the example; Alpöge announced the map. Later explanations and formal checks are separate contributions. |
| Scope | Refutes the characteristic-zero conjecture in dimensions \(n\ge3\) by stabilization. The characteristic-zero plane case remains open. |

<a id="every-generic-degree"></a>
## Every generic degree

| Field | Record |
| --- | --- |
| Reader essay | [Keller maps of every generic degree](every-generic-degree.md) |
| Mathematical status | Exact existence theorem: for every \(d\ge3\), a three-dimensional Keller map of generic degree \(d\) exists. |
| First public constructions | [Alexis Gallagher, explanatory article](https://alexisgallagher.com/posts/2026/jacobianfun/) with [pinned exact code](https://github.com/algal/jacobianfun/tree/0a73d4c75bed60660c6e91a56f1595be756cbd59); unbylined Ulam technical note, Theorem 5.2 and Corollary 5.3. |
| Later generalization | [Shuhong Gao, arXiv:2608.00222](https://arxiv.org/abs/2608.00222), using tangent sweeps and direction fields on hypersurfaces. |
| Chronology | Gallagher's article and the Ulam PDF have public metadata seventeen minutes apart. Those timestamps do not establish private discovery or circulation order; the guide records both constructions. |
| Scope | Existence and inequivalence across different generic degrees. No classification of maps of a fixed generic degree is claimed. |

<a id="the-24-variable-cubic-homogeneous-map"></a>
## The 24-variable cubic-homogeneous map

| Field | Record |
| --- | --- |
| Reader essay | [A cubic-homogeneous counterexample in 24 variables](cubic-homogeneous.md) |
| Mathematical status | Exact theorem: an explicit map \(G=I+H\) on \(\mathbf Q^{24}\), with \(H\) homogeneous cubic, has determinant one and a rational collision. |
| Proof and certificate | [William Thompson's repository, pinned revision](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9). |
| Archived release | [Zenodo record](https://doi.org/10.5281/zenodo.21466221). |
| Classical context | [Bass--Connell--Wright reduction](https://doi.org/10.1090/S0273-0979-1982-15032-7). |
| Verification scope | The supplied exact programs check the displayed determinant and collision for the explicit 24-variable map. |
| Scope | Establishes an explicit upper bound of 24 variables for this cubic-homogeneous construction. Minimal dimension remains open. |

<a id="characteristic-two-counterexamples"></a>
## Characteristic-two counterexamples

| Field | Record |
| --- | --- |
| Reader essay | [The separable conjecture fails in characteristic two](characteristic-two.md) |
| Mathematical status | Exact theorems. Separable generic-degree-three Keller counterexamples exist in dimension three over characteristic two and in the plane over \(\overline{\mathbf F}_2\). |
| Three-dimensional source | [Irit Huq-Kuruvilla, arXiv:2607.20968](https://arxiv.org/abs/2607.20968). |
| Plane source | [Romy Mondello, arXiv:2608.02634](https://arxiv.org/abs/2608.02634). |
| Key checked properties | Determinant one, explicit collision, function-field degree three, and separability. |
| Scope | Refutes the separable positive-characteristic repair, including a degree prime to the characteristic. It has no direct implication for the characteristic-zero plane case. |

<a id="the-announced-plane-degree-bound-125"></a>
## The announced plane degree bound 125

| Field | Record |
| --- | --- |
| Reader essay | [The announced plane degree bound 125](below-125.md) |
| Mathematical status | Announced computer-assisted theorem: a characteristic-zero plane counterexample must have maximum coordinate degree at least \(125\). |
| Published global reduction | [Guccione--Guccione--Horruitiner--Valqui, arXiv:2204.14178](https://arxiv.org/abs/2204.14178). It reduces every case below \(125\) to the exceptional pair \((72,108)\), up to order, and then to two explicit supports. |
| Terminal announcement | [ratto3423, MathOverflow answer](https://mathoverflow.net/a/513493), 23 July 2026. The answer states that a computer calculation eliminates both supports and that a full write-up is in preparation. |
| Public evidence boundary | As of 7 August 2026, the credited announcement does not expose the terminal equations or a complete certificate package. The published reduction and the announced terminal step should be cited separately. |
| Scope | Excludes degrees strictly below \(125\). Degree \(125\) is not excluded, and the plane conjecture remains open. |

<a id="a-modulus-at-infinity"></a>
## A modulus at infinity

| Field | Record |
| --- | --- |
| Reader essay | [A modulus at infinity survives stabilization](stable-cubic-frames.md) |
| Mathematical status | Project theorem with a complete working proof: stable left--right equivalence classes in the displayed quadratic cubic-frame family are indexed by \(\mathcal O_0\) and \(\mathcal O_q\). |
| Proof source | [Working manuscript source, pinned revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/04-stable-moduli/main.tex). |
| Reader manuscript | [Pinned working PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf). |
| Proof mechanism | Normalize the singular nonproperness component and recover \(q\) from a marked pair of boundary curves; the marked pair persists after adjoining affine-space factors. |
| Publication status | Public working manuscript; not presented as journal peer review. |
| Scope | Classifies the stated quadratic cubic-frame family under stable polynomial left--right equivalence. |

<a id="the-cubic-two-block-chart"></a>
## The cubic two-block chart

| Field | Record |
| --- | --- |
| Reader essay | [Why the cubic two-block chart is exceptional](two-block-uniqueness.md) |
| Mathematical status | Project theorem with a complete working proof: among the stated tangent nonosculating two-block opens, stable affineness occurs exactly for \(\{a,b\}=\{1,2\}\). |
| Proof source | [Working manuscript source, pinned revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/01-cubic-incidence/main.tex). |
| Reader manuscript | [Pinned working PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/01-cubic-marked-root-covers-2026-07-29-v13.pdf). |
| Proof mechanism | Divisor-class obstructions remove nonadjacent block sizes; Hodge--Deligne data remove the larger adjacent cases; an explicit coordinate isomorphism proves the \((1,2)\) case. |
| Publication status | Public working manuscript; not presented as journal peer review. |
| Scope | Tangent nonosculating hyperplanes in the two-block multiplication-incidence construction. |

<a id="five-degree-21-dessins"></a>
## Five degree-21 dessins

| Field | Record |
| --- | --- |
| Reader essay | [Five degree-21 dessins](degree-21-dessins.md) |
| Mathematical status | Exact computer-assisted project theorem: the passport \((2^{10}1),(3^7),(17\,1^4)\) has exactly five connected dessins, forming one arithmetic orbit with monodromy \(A_{21}\). |
| Certificate manuscript | [Pinned source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/appendices/degree-twenty-one-certificates.tex). |
| Reader manuscript | [Pinned working PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/06-plane-boundary-obstructions-2026-07-29-v13.pdf). |
| Exact supplement | [Pinned computational ZIP](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/docs-v56-converged-research-20260804j/assets/technical-materials/06-plane-boundary-computational-supplement.zip). |
| Verification scope | Enumerates the permutation triples, reconstructs exact coefficients, checks the orbit and monodromy, and supplies replay instructions. |
| Publication status | Public working manuscript and exact supplement; not presented as journal peer review. |
| Scope | Classifies the forced leading face. Globalization to a full plane Keller pair requires later compatibility equations. |

<a id="the-length-584-local-algebra"></a>
## The length-584 local algebra

| Field | Record |
| --- | --- |
| Reader essay | [A transverse local algebra of length 584](length-584.md) |
| Mathematical status | Exact computer-assisted project theorem for one normalized degree-at-most-seven transverse slice. |
| Proof source | [Working manuscript source, pinned revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/03-local-rigidity/main.tex). |
| Reader manuscript | [Pinned working PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/03-filtered-rigidity-2026-07-29-v13.pdf). |
| Exact supplement | [Pinned computational ZIP](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/docs-v56-converged-research-20260804j/assets/technical-materials/03-local-rigidity-computational-supplement.zip). |
| Verification mechanism | Exact Kuranishi equations, inverse-system computation through degree eight, proof of no degree-nine dual class, and an independent border-basis presentation with \(584\) standard monomials and commuting rational multiplication matrices. |
| Publication status | Public working manuscript and exact supplement; not presented as journal peer review. |
| Scope | Local, degree-bounded, and relative to a specified affine quotient and slice. |

## Chronological context

For a broader record of announcements, formalizations, independent checks,
new constructions, neighboring conjectures, and work on the plane problem,
see [Relevant external developments](../developments/index.md).
