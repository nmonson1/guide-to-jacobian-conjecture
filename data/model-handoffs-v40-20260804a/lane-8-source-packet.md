# Lane 8 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`manuscripts/06-plane-boundary/appendices/f2-terminal-boundary.tex`](#source-c26059902ddde738) — `856fb0644f5bcacf23d0b441e4c93053f8dd518fd6020cb13bd9316360fa413d`
- [`manuscripts/06-plane-boundary/appendices/six-sheet-monodromy.tex`](#source-b484876061566931) — `33c3368317818e619918f3d4d4d56f069b435f3343436e7d0c9461d3cbabe774`
- [`manuscripts/06-plane-boundary/computational-supplement/degree-296-compact/THEOREM_AND_DEPENDENCIES.md`](#source-598ed8b6db67151f) — `8646e627fe186cf13d39e6d60a646b696cb947ebabecd182ca6f15f5ef7ed9cc`
- [`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`](#source-ee3b672b4c13351c) — `63fb30b6de06df86c9c87e968d4d72e58b9218134a9eaa8cbce978b78901eb5e`
- [`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_boundary_gluing_program.md`](#source-3b11d78922960385) — `d1ca56b6fa4ea8494513e1f60a0ef9b0f3fcf5bf029df8185ea833377283a09e`
- [`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py`](#source-b6bb7682cc550398) — `dcb23b88c89bb3588d48e98826abe3289ce040a469ca610666b17baae8acaa1f`
- [`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py`](#source-07b7b4b6dfbd8330) — `eab0a34c3f4565999fbcd09389fb059e1f4d5bf63df366cd89541549761b8fc6`
- [`manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py`](#source-2cdc0acae76d0682) — `6f8ad5aea64d82ef73037260721fc5a5280058ee64cea599442a1bfda2e982a8`
- [`research-notes/lane8-f2-root-divisibility-20260804-v1/README.md`](#source-e1384a8451d58dd7) — `f29531bf3b894a0e644e9f318fa9c028f7cdcc374653f20ae3a40d0cb28fadca`
- [`research-notes/lane8-f2-root-divisibility-20260804-v1/block_manifest.json`](#source-ecdf70748a34b462) — `da3ddc8933fd91c67d0acdc45fbc1eb85f455ea21974e204055a2bf2c6c4601e`
- [`research-notes/lane8-f2-root-divisibility-20260804-v1/verify_f2_root_divisibility.py`](#source-3d84642c02b15a3c) — `342218e53f62c4be2f2dd16baea395ce12706a7d7bfe856de6ae2e72d0977c3f`
- [`research-notes/lane8-f2-support-determinacy-audit-20260803-v1/README.md`](#source-c897ba0ee0d3d561) — `38c3c52d8deeed6036f0739da5837b98e6eac29b22f82c33f34931ca9c60da84`
- [`research-notes/lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md`](#source-08d38befa366c56b) — `2eeb8b32471a6d0cc46bbdb35adb3e58a9aaa055c44fb3399970f53e9eb1e670`
- [`research-notes/lane8-full-root-closure-20260803-v1/README.md`](#source-7637370c469b9202) — `f778eb819886a64aba4080fcbc8aafd60978534191a32fffb6261cdabceac7f0`
- [`research-notes/lane8-full-root-closure-20260803-v1/fixtures/belyi_exact_field_relations.json`](#source-9accc1d6c5d4c9d7) — `5f20a89c3b832fea512f16a9452762d461f0fd783266ad91cbe72972ed38e7b8`
- [`research-notes/lane8-full-root-closure-20260803-v1/fixtures/quintic_field_fast.py`](#source-17e90f7c7cfb3106) — `028cac6094ae01d090c4cefecc62bd77261d8e5218c013e7af4457e864610600`
- [`research-notes/lane8-full-root-closure-20260803-v1/independent_raw_support_replay.py`](#source-d48d3823ed65bdc1) — `5e84c9b9a3ef77c1de5f28555a28d2f207212b774bc96df3f91b1f37799aab4d`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/__init__.py`](#source-57b89af6ad61a7ba) — `6e3ae27694039dcde9afa57b47fdf2cfd6342b9a7b9e974be6e2d11617e8e743`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/algebra.py`](#source-f9a58ccf95e56275) — `c58a83f670c9923ce869238cf05c6606fc82a246839e5e1fa280d932dd0b866d`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/certificates.py`](#source-5af7c6845d045cd4) — `283712dc265bc84610447a5cf82dd89fe8961b7f607de63c4b325552c5c41e35`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/model.py`](#source-0f27a7fc3768a4bf) — `1a889d955b8b418aeb1057aca28b650a57cd75a9677a5ec12607655990a32925`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/__init__.py`](#source-25fe326b81beaecf) — `4ac68f5246a7355d04b56e49ed0c64991faac404c0e0778ba3986021ddfcce05`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/common.py`](#source-ad118b41f1258c2a) — `92cdc645684c0ab8a19564662582a4359966e5b41a9ab09d8851f41faf86fb45`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/main.py`](#source-047a2847b42f12df) — `fdc4a3702ce0af6518015982781fa60548d9ac0f30041e47e6bd6a5ba758477a`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/manifest.py`](#source-348ac607606cf592) — `96aeb1cba0f3def1c093cb6fc3afd463acba0baceb7c44ac0f8ec51ace0bbda1`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/queue.py`](#source-7bfbfcd699f91d45) — `bee8d52836d66ae32fab49d1649588d5b1ce3834d7a92c92a8d255d8e65930ff`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/replay.py`](#source-55805a9e3aea256f) — `11e1b0d3c1c911d6fc8a8cc8fddfd884372883abc888a6d5e5b85af2c762ee89`
- [`research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/sources.py`](#source-d1f052461df06a78) — `7ea4610feae292d43075f3bef50c4efafa8ea2fc57ecb98d8d652cd5b817d849`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/checklist.json`](#source-c23f1c6df4346e40) — `2312b467dec0fff15b908897e968b2a34ba1d3e81fa03830befec622962728bf`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/field.json`](#source-593fe9efb431bec7) — `3c6a00f6bcdd09ac265c16d1eb4904b0514840a80e5f8f957dcbd1c1eadb5a1f`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/queue.json`](#source-88bb00bdcf4735d7) — `f9b33f5cb5e6f2e377f2fb0612ee677533ae2f21c4dc2cf4a17a8d24a6642df1`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/replay-full-stages.json`](#source-0422289841495ac7) — `3eeb2c0a05a13da832725c50bde31b9ae73e60c6c2181ef0569cc96e1804ab69`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/replay-truncated-stages.json`](#source-ee3fb966b7e4afcb) — `fb2eda00f7dae9c88097a8483a662a2bb8d0b6c5d09d47956f66e964c04eba38`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/replay.json`](#source-546e947b1ca05fc3) — `3e7097a74558459ce015d2d981a12da799c2e5d13f55d3559d04323a3e068797`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/sources.json`](#source-872badec8715a0c5) — `868b7e17b46833237b8af60b1ff1a3e14eb45fdd0d547c1776aca9fd867d9143`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s0-face.json`](#source-68539ea3cb17d0c9) — `b990c851803ca3e6eaa9fb96369e0fdd4d61c8207ffe6604479f77951f4d5fa8`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s1-truncated-layers.json`](#source-6f17b4887d709bb1) — `fea1e27b5bf454086ed54c22769cf0a8630597f9c57271d05a88d994986acb2d`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s2-full-layers-1-4.json`](#source-3a7b99d8233b2143) — `8373c5d01f9f0169546fa765013e9be4a8f606d64985ff2d01e687e88bcf3b9e`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s3-full-square-routing.json`](#source-c0d6bbf214c90a82) — `c0cf6fda83dfcdedcc9ef7542bc60b74c28a83a2e9951cca4b6b6700f0b3df49`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s4-full-normalization.json`](#source-dbc1ad9159b2251f) — `36a3527486717f3783ee397cb2f1550a268870e74f06079eeae3e7d810eb52b1`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s5-full-layers-5-8.json`](#source-c1b0583cf38dfd28) — `571411d3d5a4de71474dfb3cebf74acd2d6d6f932b723e40b5a49f76d8f2b942`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s6-toric-projection.json`](#source-cddc42b218cb9b0f) — `3c2dfac77827825813c81f6498f392f250208e607ee100c046e70e005e2da744`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s7-toric-terminal.json`](#source-4157d50990ad2a23) — `fdcd3abc9161325c98fa86f60be3b54116472fe0907a2eeb9e71f1efeea5bb84`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s8-adjacent-stored.json`](#source-641b3ee74f85e4a3) — `4a06becb7c2e0658d689a51348394066998da04f6ae813c82d3d89f5466ad9a6`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s9-lane9-order-obstruction.json`](#source-6f0975d7fc918e96) — `92724d87d97a1178dce887a07dae3d979b3fc705e4eb7c3311c620711eb281fd`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/terminal-certificates.json`](#source-77da4c6680fab5f7) — `73c42edbafc6716a1a9bff0a6b87c9c38225362dc3ae72b969c64f59386f8191`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/theorem-scope.json`](#source-8ba456338695e7f2) — `6f68bfa513ad7b5a512784fde54dfb0ab58aadefe257837bbc6287e12b1d1910`
- [`research-notes/lane8-full-root-closure-20260803-v1/manifest/variable-systems.json`](#source-b98b1e3b33c17163) — `e8c52d635bb504082f7e3b98201798cb683efed6ae58c0e60907388537616275`
- [`research-notes/lane8-full-root-closure-20260803-v1/stage-manifest.json`](#source-f2a5a9b855b4c6e5) — `8b725f4751785075a3a3f61ebba9921588d547d4a026f213bf7c473ec10d7c73`
- [`research-notes/lane8-full-root-closure-20260803-v1/verify_lane8_packet.py`](#source-1aeef542ed770f29) — `35a40633f1e229adadf42150b2f370a75403fc2232bcb8214011bae1a39013a1`
- [`research-notes/lane8-proof-queue-20260802-v1/check_queue.py`](#source-c4b71016901540c7) — `e1b6556645ff74e18ce04600f1d1e5ff7bcbe30e4dfeaa9ec53cadbe7b32320e`
- [`research-notes/lane8-proof-queue-20260802-v1/full_early_layer_reduction.py`](#source-825cbf7a3e2c79ec) — `ed4a150374eb969e19bf8601f8f4529edae57fb457f9aae9211997fb6f83bd95`
- [`research-notes/lane8-proof-queue-20260802-v1/hurwitz_degree21.py`](#source-86a7146cd6277db5) — `926383532c456f92d812e104c9409009a840d26cd2cdf367ce738082af05eda1`
- [`research-notes/lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md`](#source-417fb9530af82c25) — `bdbe6c5557e93c3dbafac75ffbf3c833eb22d5988af9e3f7bfcbdd4b040b94f0`
- [`research-notes/lane8-proof-queue-20260802-v1/queue.schema.json`](#source-048b1950297f5eb0) — `82c7cd8f7a1dba56a7605575f7a71a19c5ac9d6557cb4f47569ffb2e03e13bff`
- [`research-notes/lane8-proof-queue-20260802-v1/queue.seed.json`](#source-963267c8285aa781) — `a55e0c1aaf49d834ec0004c14f64e0ba04d8d969d1af9cde5eef01da4ea28743`
- [`research-notes/lane8-proof-queue-20260802-v1/quintic_face_coefficients.json`](#source-68d42e1275446a86) — `3222b8ef063eb2490b37847e74dc638f90d767e24f39bf7d8902c55923147cac`
- [`research-notes/lane8-proof-queue-20260802-v1/quintic_face_reconstruction.py`](#source-de3965d83ed72274) — `e48869fb09d7afcc3c1ae08a604c7656efadf0c3588c0fca82a42817dfaf8c1f`
- [`research-notes/lane8-proof-queue-20260802-v1/root_face_check.py`](#source-0362c0ea7e22f043) — `b1f8175c8c74264df4bda78e60f300b2cea0feef139951e7f649830ad37c5547`
- [`research-notes/lane8-proof-queue-20260802-v1/truncated_support_certificate.json`](#source-640bafff64cc649e) — `f086c7eca67d51f3c48fd6311c55e8fe5012a8b1373ff6eae4746fd4c3fec6ac`
- [`research-notes/lane8-proof-queue-20260802-v1/truncated_support_certificate.py`](#source-aebcda934fbbb291) — `40daac940f6c82e76a3679495e14cd0fcadfe5a926b3053eeff2cab879401da5`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/README.md`](#source-38ab8bd19d25aff4) — `d91dea30f97b84627a5f470a62042d7b08113e1099e8a2ceb917d9fe0b3b04ab`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/evidence.json`](#source-ab81932dfb3d4762) — `85f9d954c411ae8c712a5fe3b750438b404395f8783cda56806c966549b24042`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py`](#source-151645a0e17f5aa6) — `9ddebd48cf42375304756cd116248ab0be41d42282018f72d425bc9dc580ee11`
- [`research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py`](#source-de9fde3d3aea4139) — `97fb0634bccd4ecd863bda23e018156205431ae5e1ebe87d2adb7a75bd6be177`
- [`research-notes/planar-descent-no-go-20260802-v1/README.md`](#source-e5ed63a9f4cbb255) — `6e483b4273025c64f004a512b3de80296ff6e7479dfec51e8a484af8c5d06d60`
- [`research-notes/planar-descent-no-go-20260802-v1/affine_plane_linear_projection_no_go.py`](#source-78e62daae2246c31) — `8ea6300b370186911f8109a2aada13679b1612428bae9d045d9c9720aaa1ab02`
- [`research-notes/planar-descent-no-go-20260802-v1/hc4_linear_descent_no_go.py`](#source-f7cb2b829210956c) — `8644beef8041ae41578ed84fa58697b6f0aae9726eb37086f4b040c9f2925ce4`
- [`research-notes/planar-descent-no-go-20260802-v1/hc4_square_correction_no_go.py`](#source-9e967fdeb2921c93) — `41d933337f35705eb1031e82d54f666853206bda0ec97315e8a4f7aa0ed43b57`
- [`research-notes/planar-descent-no-go-20260802-v1/linear_target_coordinate_fibres.py`](#source-6f882ea3f01158fb) — `3428ddee84b549dcb1f247d41d8abe9dde62c62e7dfae97820ab9d427604de3e`
- [`research-notes/planar-descent-no-go-20260802-v1/three_dimensional_descent_no_go.py`](#source-e5a22357febe952a) — `e5d51dd28d34f7586539f854a2f40b97591ec0a7d7728bff5acc6ef18ce829a6`
- [`research-notes/planar-descent-no-go-20260802-v1/y_graph_descent_no_go.py`](#source-3b8a058f37f1b009) — `e157ae481c1e47d234ae5a048e388955d24aebe05b102baf4e7cccb9871be09e`

<a id="source-c26059902ddde738"></a>

## `manuscripts/06-plane-boundary/appendices/f2-terminal-boundary.tex`

<pre><code class="language-tex">
\section{The terminal boundary of the parametric
\texorpdfstring{\(F_2\)}{F2} family}
\label{app:f2-terminal-boundary}

The complete-chain \(F_2\) family has
\&#91;
A_0=(5,20),\qquad A_0'=(1,0),\qquad
A_1=\left(\frac75,2\right),
\&#93;
\&#91;
n=2m-1,\qquad m\ge2,
\&#93;
and coordinate-degree pair
\&#91;
\bigl(25m,25(2m-1)\bigr).
\&#93;
This appendix classifies the final face for every \(m\), shows that its
local defect equations are integrable, and gives a global no-go theorem for
the natural five-band lift.  It does not eliminate the full \(F_2\) family.

\subsection{The final regular corner}

If \((\rho,\sigma)\) is the direction at \(A_1\), the type-I corner identity
gives
\&#91;
(7m-4)\rho+(10m-5)\sigma=0.
\&#93;
With
\&#91;
d_m=\gcd(10m-5,7m-4)\in\{1,5\},
\&#93;
the primitive direction is
\&#91;
(\rho_m,\sigma_m)=
\left(\frac{10m-5}{d_m},-\frac{7m-4}{d_m}\right).
\&#93;
The type-I.a start formula would require the positive integer
\&#91;
a'=\frac1{2m-1},
\&#93;
and is therefore impossible.  Type I.b has \(k=1\) and starts
\&#91;
\operatorname{st}P_E=\left(\frac45,1\right),\qquad
\operatorname{st}Q_E=\left(\frac15,0\right).
\&#93;

Set
\&#91;
Z=x^{(7m-4)/5}y^{2m-1}.
\&#93;
After source and target scaling, the final leading forms are
\&#91;
P_E=x^{4/5}y\,p(Z),\qquad p(Z)=Z-1,
\&#93;
\&#91;
Q_E=x^{1/5}q(Z),\qquad\deg q=2.
\&#93;
Their bracket equation is
\begin{equation}
\label{eq:f2-final-face}
-pq+mZpq'-(2m-1)Zp'q=\lambda.
\end{equation}

\begin{theorem}&#91;Final-face classification&#93;
\label{thm:f2-final-face}
Equation \eqref{eq:f2-final-face} has the unique normalized solution
\&#91;
q_m(Z)=
Z^2-\frac{2m-1}{m}Z+
\frac{(2m-1)(m-1)}{2m^2},
\&#93;
\&#91;
\lambda_m=\frac{(2m-1)(m-1)}{2m^2}.
\&#93;
The discriminant is
\&#91;
\Disc(q_m)=\frac{2m-1}{m^2}\ne0.
\&#93;
\end{theorem}

\begin{proof}
Substitute \(p=Z-1\) and a monic quadratic
\(q=Z^2+\alpha Z+\beta\) into \eqref{eq:f2-final-face}.  Vanishing of the
coefficients of \(Z^2\) and \(Z\) gives
\&#91;
\alpha=-\frac{2m-1}{m},\qquad
\beta=\frac{(2m-1)(m-1)}{2m^2}.
\&#93;
The constant term is \(\lambda_m=\beta\), and direct substitution gives the
discriminant.
\end{proof}

\subsection{The alternating boundary dessin}

Define
\&#91;
\beta_m(Z)=\frac{q_m(Z)^m}{Z(Z-1)^{2m-1}}.
\&#93;
Logarithmic differentiation using \eqref{eq:f2-final-face} gives
\&#91;
\beta_m'(Z)=
\lambda_m\frac{q_m(Z)^{m-1}}{Z^2(Z-1)^{2m}}.
\&#93;

\begin{theorem}&#91;Unique alternating dessin&#93;
\label{thm:f2-alternating-dessin}
The map \(\beta_m\) is a degree-\(2m\) Belyi map with passport
\&#91;
(m,m),\qquad(2m-1,1),\qquad(3,1^{2m-3}).
\&#93;
It is the unique normalized map of this form, and its monodromy group is
\&#91;
\operatorname{Mon}(\beta_m)=A_{2m}.
\&#93;
\end{theorem}

\begin{proof}
The derivative shows that the roots of \(q_m\) lie over \(0\), each with
ramification \(m\); \(Z=1\) is a pole of order \(2m-1\); \(Z=0\) is a
simple pole; and \(Z=\infty\) has ramification index \(3\).  The total
ramification is \(4m-2=2\deg\beta_m-2\), so there is no further
ramification.

On \(2m\) letters, take
\&#91;
\sigma_\infty=(1\,2\,\cdots\,2m-1),\qquad
\sigma_1=(1\,m\,2m),
\&#93;
and \(\sigma_0=(\sigma_\infty\sigma_1)^{-1}\).  Then \(\sigma_0\) is the
product of two \(m\)-cycles.  The group is primitive because a block
containing the fixed point of \(\sigma_\infty\) is either a singleton or
the whole set.  For \(m\ge3\), Jordan's theorem and the contained
three-cycle give \(A_{2m}\); all generators are even.  The case \(m=2\)
is checked directly and gives \(A_4\).

Finally, the unique pole of order \(2m-1\), the simple pole, and the
index-three point normalize the source points to \(1,0,\infty\);
\cref{thm:f2-final-face} then gives uniqueness.
\end{proof}

\begin{corollary}&#91;Complete final-face package&#93;
\label{cor:f2-final-face-package}
For every \(m\ge2\), the \(F_2\) terminal corner has the unique normalized
face polynomial \(q_m\) of \cref{thm:f2-final-face}.  Its unique normalized
degree-\(2m\) Belyi map has passport
\&#91;
(m,m),\qquad(2m-1,1),\qquad(3,1^{2m-3})
\&#93;
and monodromy group \(A_{2m}\).
\end{corollary}

\begin{proposition}&#91;The \(m=3\) self-similarity&#93;
\label{prop:f2-m3-self-similarity}
For \(m=3\),
\&#91;
q_3(Z)=Z^2-\frac53Z+\frac59,
\&#93;
and the change \(Z=\frac53t\) gives
\&#91;
\beta_3\left(\frac53t\right)
=\frac{(t^2-t+1/5)^3}{t(t-3/5)^5}.
\&#93;
The right side is exactly the degree-six \(A_6\) Type-II first-face dessin.
This is a genuine self-similarity of the two boundary maps, but it does not
identify their ambient boundary components and is not a gluing theorem.
\end{proposition}

\subsection{Unimodular defect coordinates}

Pass to \(X=x^{1/5}\), translate the selected double root to \(u=0\), and
put
\&#91;
Z=X^{5m-3}u^{2m-1},\qquad
\epsilon=X^{-5}u^{-2}.
\&#93;
The exponent matrix has determinant
\&#91;
\det\begin{pmatrix}-5&amp;-2\\5m-3&amp;2m-1\end{pmatrix}=-1,
\&#93;
so
\&#91;
X=\epsilon^{-(2m-1)}Z^{-2},\qquad
u=\epsilon^{5m-3}Z^5.
\&#93;
Write
\&#91;
P=\epsilon^{-m}Z^{-1}A(\epsilon,Z),\qquad
Q=\epsilon^{-(2m-1)}Z^{-2}B(\epsilon,Z).
\&#93;
Then
\&#91;
&#91;P,Q&#93;_{x,y}=\frac15\mathcal K_m(A,B),
\&#93;
where
\begin{align}
\mathcal K_m(A,B)={}&amp;-AB+mZA B_Z-(2m-1)ZA_ZB\notag\\
&amp;+\epsilon\bigl&#91;(ZA_Z-A)B_\epsilon
                 +(2B-ZB_Z)A_\epsilon\bigr&#93;.
\label{eq:f2-defect-operator}
\end{align}

\begin{theorem}&#91;Local defect integrability&#93;
\label{thm:f2-local-integrability}
For every \(m\ge2\), the local equation
\&#91;
\mathcal K_m(A,B)=\lambda_m
\&#93;
has a nontrivial exact finite-support one-parameter family satisfying the
Newton support conditions.  Consequently no obstruction based only on
finite-order local lifting at the final face can eliminate the \(F_2\)
family.
\end{theorem}

\begin{proof}
Use
\&#91;
A=Z-1+Za(\epsilon),\qquad
B=q_m(Z)+Zb(\epsilon)+Z^2c(\epsilon).
\&#93;
Equation \eqref{eq:f2-defect-operator} reduces to two ordinary differential
equations.  With free parameter \(\tau\), an exact solution is
\&#91;
a(\epsilon)=
\frac{2m(m-2)}{(2m-3)(2m-1)}\tau\epsilon,
\&#93;
\&#91;
b(\epsilon)=
-\frac{2(m-1)^2}{m(2m-3)}\tau\epsilon,
\&#93;
\&#91;
c(\epsilon)=
\tau\epsilon+
\frac{4(m-2)(m-1)^3}{(2m-3)^3(2m-1)}
\tau^2\epsilon^2.
\&#93;
Direct substitution yields \(\mathcal K_m(A,B)=\lambda_m\).
\end{proof}

\subsection{A global five-band no-go theorem}

Before translating the root, put \(v=Xy\).  Polynomial descent is the
invariant-ring condition for
\&#91;
(X,v)\longmapsto(\zeta X,\zeta v),\qquad\zeta^5=1.
\&#93;
The natural lift using only the bands forced directly by the first and
final faces is
\&#91;
P=X^{5m}R(v)^m+X^3U(v),
\&#93;
\&#91;
Q=X^{5(2m-1)}R(v)^{2m-1}
  +X^{5m-2}V(v)+XW(v).
\&#93;
Cyclic descent forces
\&#91;
U=v^2A(v^5),\qquad
V=v^2B(v^5),\qquad
W=v^4C(v^5).
\&#93;

\begin{theorem}&#91;Five-band descent no-go&#93;
\label{thm:f2-five-band-no-go}
No pair of the displayed five-band form descends to a plane polynomial map
with nonzero constant Jacobian.
\end{theorem}

\begin{proof}
Since
\&#91;
\det\frac{\partial(x,y)}{\partial(X,v)}=5X^3,
\&#93;
a nonzero constant original Jacobian requires a nonzero constant coefficient
at \(X^3\) in the bracket
\&#91;
&#91;P,Q&#93;_{X,v}.
\&#93;
The only contribution from the five bands is
\&#91;
3UW'-U'W.
\&#93;
Writing \(s=v^5\) and using the character forms gives
\&#91;
\begin{aligned}
3UW'-U'W
  &amp;=5v^5\bigl(2AC+3sAC'-sA'C\bigr),
\end{aligned}
\&#93;
which is divisible by \(v^5\).  It cannot be the required nonzero
constant.
\end{proof}

\subsection{The global attachment problem}

For a general descended pair
\&#91;
P=\sum_\alpha X^\alpha P_\alpha(v),\qquad
Q=\sum_\beta X^\beta Q_\beta(v),
\&#93;
the exact band equation is
\&#91;
\sum_{\alpha+\beta=r+1}
\left(\alpha P_\alpha Q_\beta'
-\beta P_\alpha'Q_\beta\right)
=5\kappa\,\delta_{r,3}.
\&#93;
A constant \(v^0\)-term at \(X^3\) can arise only from the band pairs
\&#91;
(\alpha,\beta)=(5,-1)\quad\text{or}\quad(-1,5),
\&#93;
corresponding to crossed affine-linear \(x\)- and \(y\)-terms.

\begin{question}&#91;Two-sided \(F_2\) attachment&#93;
\label{q:f2-global-attachment}
Does any finite two-sided band system simultaneously realize the rigid
first face, the final \(A_{2m}\) face, the cyclic character conditions, and
the affine bands \(5,-1\)?  Equivalently, can the locally integrable
terminal model be attached to a global plane polynomial Keller pair?
\end{question}

The local theorem and the five-band theorem show why this question cannot
be replaced by either a higher-order one-sided Puiseux calculation or the
most economical global ansatz.
</code></pre>

<a id="source-b484876061566931"></a>

## `manuscripts/06-plane-boundary/appendices/six-sheet-monodromy.tex`

<pre><code class="language-tex">
\section{A six-sheet monodromy problem}
\label{app:six-sheet-monodromy}

The boundary calculations above suggest a separate problem at generic
degree six.

\begin{question}&#91;Six-sheet monodromy&#93;
\label{q:six-sheet-monodromy}
Must every hypothetical six-sheet counterexample to the plane Jacobian
conjecture have monodromy group \(A_6\) or \(S_6\)?
\end{question}

\begin{remark}&#91;Present evidence&#93;
\label{rem:six-sheet-provisional}
A dated synthesis reported the corresponding necessary-condition statement
and eliminations of several conditional compactification strata.  The
available archive does not contain the underlying proof or computational
artifacts.  We therefore record the monodromy statement as an open problem
and do not claim the reported stratum eliminations as theorems.
\end{remark}
</code></pre>

<a id="source-598ed8b6db67151f"></a>

## `manuscripts/06-plane-boundary/computational-supplement/degree-296-compact/THEOREM_AND_DEPENDENCIES.md`

<pre><code class="language-markdown">
# Exact theorem and dependency boundary

## Unconditional theorem for the six displayed polynomials

Let

\&#91;
K=\mathbf Q(u),\qquad u^5-u^4+3u^3+3u^2+26=0,
\&#93;

and let

\&#91;
\rho=F_4,\qquad (g_1,g_2,g_3,g_4,g_5)=(F_6,F_8,F_9,F_{10},F_{11})
\&#93;

be the six exact polynomials in `inputs/handoff-lite/layer-calculation/full_exact_fivevar_w8.json`.
At the prime `p=2053`, with `u=216`, the five equations `g_1,...,g_5` are
BKK-nondegenerate: every one of the 344 proper faces of the Minkowski sum
has root-free initial system in the algebraic torus.  The mixed volume is 296.
The resulting special algebra is reduced of dimension 296, every coordinate
is invertible, and multiplication by `rho` has determinant 682.

Localizing the coefficient ring at `(2053,u-216)` therefore gives a finite
etale scheme of rank 296, and `rho` is a unit on it.  Consequently

\&#91;
V(\rho,g_1,g_2,g_3,g_4,g_5)(\overline K)=\varnothing.
\&#93;

This characteristic-zero conclusion does not depend on a heuristic modular
lift: the projective toric compactification is proper, the full special fiber
is the reduced 296-point torus scheme, all boundary initial systems are
root-free, and the etale locus containing the special fiber must be the entire
finite scheme over the local DVR.

## Raw-support bridge for the Keller interpretation

The companion program
`../degree-twenty-one/raw-support-reconstruction/rebuild_lower_face_reduction.py`
now audits the bridge that was previously imported. Starting from the two
displayed normalized Newton polygons, it:

1. generates every lattice point and deficiency layer directly from the
   polygon vertices;
2. reconstructs the exact degree-\(21\) lower face and verifies its Jacobian
   equation coefficientwise;
3. performs the complete truncated recursion and verifies the rank-\(14\)
   Macaulay contradiction after vertex saturation;
4. performs the full recursion through order \(8\), verifies the weight-four
   square, and proves that vertex saturation justifies the nonzero parameter
   normalization;
5. regenerates the fifteen normalized compatibility equations, including the
   six used here, and matches the recovered equation list coefficientwise.

Thus the exact six-polynomial theorem above is connected by a reproducible
exact calculation to the two normalized raw `(8,28)` supports. The original
`lower_face_layers.py` file remains unrecovered but is no longer used.

The remaining imported dependency is earlier: the package does not reprove
the published reduction from an arbitrary below-\(125\) Keller pair to these
two normalized support alternatives. It also relies on the separate
degree-\(21\) dessin count to show that the generic quintic orbit exhausts the
normalized lower faces. No conclusion about the full plane Jacobian
conjecture follows from the degree bound alone.
</code></pre>

<a id="source-ee3b672b4c13351c"></a>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`

<pre><code class="language-markdown">
# Boundary seed for the first post-125 complete-chain case

## Source data

The first family at maximum degree 125 in the complete-chain table is

\&#91;
F_2:\qquad A_0=(5,20),\quad A_0'=(1,0),\quad A_1=(7/5,2),
\qquad (m,n)=(3,5).
\&#93;

This note extracts the exact terminal-edge information that is available before a full Newton-support normalization.

## 1. Starting direction and fractional coordinate

The edge difference is

\&#91;
A_0-A_0'=(4,20),
\&#93;

so its primitive normal direction is

\&#91;
(\rho,\sigma)=(5,-1).
\&#93;

The standard fractional edge coordinate is therefore

\&#91;
z=x^{-\sigma/\rho}y=x^{1/5}y.
\&#93;

For the \(P\)-coordinate, the edge runs from

\&#91;
mA_0'=(3,0)
\quad\text{to}\quad
mA_0=(15,60),
\&#93;

so

\&#91;
\ell_{5,-1}(P)=x^3p(z),\qquad \deg p=60,\qquad p(0)\ne0.
\&#93;

For \(Q\), the corresponding edge runs from \((5,0)\) to \((25,100)\), hence

\&#91;
\ell_{5,-1}(Q)=x^5q(z),\qquad \deg q=100.
\&#93;

Because the original pair is polynomial in \(x,y\), only powers \(z^{5j}\) occur. Equivalently, with

\&#91;
w=z^5=xy^5,
\&#93;

one may write

\&#91;
\ell_{5,-1}(P)=x^3\widetilde p(w),\quad \deg\widetilde p=12,
\&#93;

\&#91;
\ell_{5,-1}(Q)=x^5\widetilde q(w),\quad \deg\widetilde q=20.
\&#93;

## 2. Common-power and double-root constraint

The standard leading-form theorem for an \((m,n)=(3,5)\) pair gives, up to nonzero scalars,

\&#91;
p(z)=R(z)^3,\qquad q(z)=R(z)^5,
\qquad \deg R=20.
\&#93;

In the integral coordinate \(w=z^5\), this becomes

\&#91;
\widetilde p(w)=S(w)^3,\qquad
\widetilde q(w)=S(w)^5,
\qquad \deg S=4.
\&#93;

The child-corner formula is

\&#91;
A_1=A_0'+\frac{m_\lambda}{m}
\left(-\frac\sigma\rho,1\right).
\&#93;

Substituting the table data gives

\&#91;
(7/5,2)=(1,0)+\frac{m_\lambda}{3}(1/5,1),
\&#93;

and therefore

\&#91;
\boxed{m_\lambda=6.}
\&#93;

Thus the chosen root has multiplicity six in \(p=R^3\), hence multiplicity two in \(R\). Since \(p(0)\ne0\), the root is nonzero. After the fractional shear

\&#91;
y\longmapsto y+\lambda x^{-1/5},
\qquad z\longmapsto z+\lambda,
\&#93;

we have

\&#91;
R(z+\lambda)=z^2T(z),\qquad T(0)\ne0,
\&#93;

and the new leading monomial of \(P\) is

\&#91;
x^3z^6=x^{21/5}y^6.
\&#93;

Dividing its exponent pair by \(m=3\) gives

\&#91;
(7/5,2)=A_1,
\&#93;

which independently verifies the chain transition.

## 3. What this fixes, and what it does not

The complete-chain data already force:

- the fractional scale \(l_1=5\);
- a quartic integral common-root polynomial \(S(w)\);
- a distinguished nonzero double root of \(S\);
- the first approximate-root shear;
- the child corner \((7/5,2)\).

They do **not** yet determine:

- the complete normalized Newton polygons after the shear;
- the monomial bracket exponent \(\kappa\) in the final toric chart;
- the adjacent-component pole scale \(a\);
- the higher normal-neighborhood line-bundle windows (the reduced primary Hurwitz problem is determined in Section 5);
- the secondary contact degree \(e\).

Once \((a,\kappa)\) are obtained, with common powers \((3,5)\), the universal contact formula gives

\&#91;
\boxed{e=8a-\kappa-1.}
\&#93;

If \(e&gt;a^2\), the secondary cover is then forced by the universal transport theorem and has passport

\&#91;
(a^a\,(e-a^2)),\qquad(e),\qquad(a+1\,1^{e-a-1}).
\&#93;

## 4. Remaining support-normalization task

The reduced primary face can be determined without the entire support (Section 5). Full support propagation is still needed for the gluing problem:

1. propagate the fractional shear through the full standard rectangle;
2. use the terminal-corner inequalities and the gap-five congruence to discard forbidden lattice points;
3. choose the adjacent toric ray and return to the quotient coordinate \(u=z^5\);
4. enumerate the finite normal-layer windows;
5. compute \(a\), \(\kappa\), the secondary contact data, and the two-point line-bundle spaces.

This is the first meaningful test of whether the degree-21 gluing mechanism is a terminal-chain mechanism rather than a special feature of the \((8,28)\) support.

## 5. Subsequent terminal-face determination and lattice quotient

The type-I.b final-corner formulas give

\&#91;
A_1=(7/5,2),\quad k=1,\quad(m,n)=(3,5),
\&#93;

\&#91;
(\rho,\sigma)=(25,-17),\qquad z=x^{17/25}y,
\&#93;

\&#91;
P_E=x^{4/5}y\,p(z),\quad\deg p=5,
\qquad
Q_E=x^{1/5}q(z),\quad\deg q=10,
\&#93;

and

\&#91;
5pq-3zpq'+5zp'q=1.
\tag{5.1}
\&#93;

The fractional uniformizing cover has degree 30 and passport

\&#91;
(5^6),(3^{10}),(15,1^{15}).
\&#93;

That ambient passport has eleven connected dessin classes.  However, the complete-chain lattice gap is

\&#91;
g=\operatorname{gap}(25,5)=5.
\&#93;

Polynomial support therefore forces

\&#91;
p(z)=\bar p(z^5),\qquad q(z)=\bar q(z^5).
\&#93;

With \(u=z^5\), equation (5.1) becomes

\&#91;
\bar p\bar q-3u\bar p\bar q'+5u\bar p'\bar q=\frac15,
\&#93;

with

\&#91;
\deg\bar p=1,\qquad\deg\bar q=2.
\&#93;

The lattice-compatible quotient passport is

\&#91;
\boxed{(5,1),(3^2),(3,1^3),}
\&#93;

of degree six.  Its connected Hurwitz count is one, and its deck group is trivial.  A normalized representative is

\&#91;
\bar p=1-u,
\qquad
\bar q=\frac15-\frac35u+\frac9{25}u^2,
\&#93;

so, up to target scaling,

\&#91;
\boxed{
\phi_6(u)=\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
}
\&#93;

The degree-30 ambient face is the cyclic pullback \(\phi_6(z^5)\).  Thus only the unique \(C_5\)-symmetric one among the eleven ambient dessins is compatible with the polynomial lattice.

## 6. Revised next exact computation

The reduced terminal map is now completely fixed.  The next calculation is not an eleven-case degree-30 search.  It is one \(C_5\)-equivariant normal-neighborhood computation around the explicit degree-six map above:

1. propagate the full Newton support through the complete chain into the quotient coordinate \(u=z^5\);
2. determine the allowed two-point line-bundle windows for the normal coefficients;
3. form the intrinsic determinant layer operators and their pole-filtered residue adjoints;
4. compute the boundary Kuranishi section;
5. prove either no gluing or a strict complete-chain descent.

See `terminal_primary_belyi_reduction.md` and `verify_post125_terminal_examples.py`.
</code></pre>

<a id="source-3b11d78922960385"></a>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_boundary_gluing_program.md`

<pre><code class="language-markdown">
# From the degree-21 boundary obstruction to a terminal gluing–descent program

**Status:** The layer, adjoint, index, resonance, hypergeometric, derivative, passport, and filtered-descent statements below are proved. The terminal gluing–descent dichotomy is conjectural. This is not a proof of the plane Jacobian conjecture.

## 1. Universal determinant complex

For

\&#91;
\alpha A B_z-\beta A_zB+s(A_zB_s-A_sB_z)=\Psi(z),
\&#93;

with \(A=A_0+\sum_{r\ge1}s^ra_r\) and \(B=B_0+\sum_{r\ge1}s^rb_r\), the new order-\(r\) coefficients enter through

\&#91;
\mathscr D_r^{\alpha,\beta}(a,b)
=(\alpha-r)a\,dB_0-\beta B_0\,da
+\alpha A_0\,db+(r-\beta)b\,dA_0.
\&#93;

Its residue adjoint is

\&#91;
(\mathscr D_r^{\alpha,\beta})^\vee(\lambda)=
\left(
\beta B_0d\lambda+(\alpha+\beta-r)\lambda dB_0,
-\alpha A_0d\lambda+(r-\alpha-\beta)\lambda dA_0
\right).
\&#93;

For a map

\&#91;
H^0\mathcal O(d_A)\oplus H^0\mathcal O(d_B)\to H^0\mathcal O(d_W)
\&#93;

on \(\mathbf P^1\), the virtual target-minus-domain dimension is

\&#91;
\epsilon=d_W-d_A-d_B-1.
\&#93;

For the certified full \((8,28)\) support, \(d_A=10-r\), \(d_B=15-r\), and \(d_W=25-r\), hence

\&#91;
\epsilon_r=r-1.
\&#93;

## 2. Contact-degree formula and universal secondary Belyi transport

Suppose the common-power exponents are coprime integers \(m,n\), with

\&#91;
v_E(P)=-m,\quad v_E(Q)=-n,\qquad
v_D(P)=-ma,\quad v_D(Q)=-na.
\&#93;

Choose \(c,d\) with \(dn-cm=1\), put \(\pi=P^c/Q^d\), \(\tau=Q^m/P^n\), and suppose the normalized bracket is \(&#91;P,Q&#93;=x^\kappa\) in a toric chart with \(x=t^{-1}\) up to an \(s\)-unit. Comparing the \(t\)-orders in \(d\pi\wedge d\tau\) gives

\&#91;
\boxed{e=a(m+n)-\kappa-1}.
\&#93;

For the certified case, \((m,n,a,\kappa)=(2,3,4,2)\), hence \(e=17\).

Now let \(a,e\in\mathbf N\) with \(e&gt;a^2\), and put \(\delta=e-a^2\). After removing all resonant target shears, assume

\&#91;
\pi=t^a\frac{s}{s-1}+O(t^{a+1})
\&#93;

and the first nonzero boundary-volume term forces

\&#91;
e c'h-a c h'=-(s-1)^{-a-2},\qquad c=\frac{s}{s-1}.
\&#93;

Then

\&#91;
h=\frac{H_{a,e}(s)}{(s-1)^a},
\&#93;

where

\&#91;
H_{a,e}(s)=\sum_{k=0}^a
\frac{a^k a!}{(a-k)!\prod_{j=0}^k(e-aj)}s^k
=\frac1e\,{}_2F_1\left(-a,1;1-\frac ea;s\right).
\&#93;

It obeys

\&#91;
a s(s-1)H'+(e-a^2s)H=1,
\&#93;

is squarefree, and satisfies \(H(0)=1/e\), \(H(1)=1/\delta\).

The exceptional ratio

\&#91;
W_{a,e}(s)=\frac{(s-1)^\delta H_{a,e}(s)^a}{s^e}
\&#93;

is a degree-\(e\) Belyi map with

\&#91;
W_{a,e}'(s)=\frac{(s-1)^{\delta-1}H_{a,e}(s)^{a-1}}{s^{e+1}}
\&#93;

and passport

\&#91;
(a^a\,\delta),\qquad(e),\qquad(a+1\,1^{e-a-1}).
\&#93;

For \((a,e)=(4,17)\),

\&#91;
H_{4,17}=\frac{195+240s+320s^2+512s^3+2048s^4}{3315},
\&#93;

recovering the degree-17 secondary map in the current boundary package.

## 3. Exact one-layer descent lemma

Let \(D:U\to V\) and let \(V_{\le m}\subset V\) be a smaller Newton/pole window. For \(\Phi\in V\), the following are equivalent:

1. there is \(u\in U\) with \(\Phi-Du\in V_{\le m}\);
2. every \(\lambda\in(\operatorname{im}D)^\perp\cap(V_{\le m})^\perp\) satisfies \(\lambda(\Phi)=0\).

In the boundary complex, these \(\lambda\)'s are precisely the high-pole adjoint residue classes. Therefore vanishing high-pole residues *does* lower a single Newton window. The missing step is to make the reductions compatible across all normal layers and integrate them to one allowable approximate-root transformation.

## 4. Conditional full-proof theorem

A sufficient global statement is:

&gt; For every terminal complete-chain model, either its Newton-bounded boundary Kuranishi zero scheme is empty, or every zero produces a standard Keller pair of strictly smaller complete-chain complexity.

Together with completeness of the boundary Kuranishi functor, this would prove the plane Jacobian conjecture by minimal counterexample descent.

## 5. Next test queue

| Priority | Complete-chain data | \((m,n)\) | maximum degree |
|---:|---|---:|---:|
| 1 | \(F_2: (5,20)\to(7/5,2)\) | \((3,5)\) | 125 |
| 2 | \((7,35)\to(19/7,5)\) | \((2,3)\) | 126 |
| 3 | \((12,30)\to(16/3,10)\to(11/6,3)\) | \((3,2)\) | 126 |
| 4 | \(F_{24}: (8,24)\to(14/4,6)\to(19/8,3)\) | \((3,4)\) | 128 |
| 5 | \((11,33)\to(19/4,8)\) | \((2,3)\) | 132 |

The first meaningful universality test is \(F_2\): it is the first candidate at 125, has a one-step complete chain, and changes the degree ratio from the current \((2,3)\)-type geometry.

## 6. Lattice-gap terminal-primary reduction

For every type-I.b final corner in the orientation of equation (3.17), the fractional terminal faces satisfy

\&#91;
npq-mzpq'+nzp'q=1.
\&#93;

The ambient uniformizing map

\&#91;
\tau=z^n p^n/q^m
\&#93;

has degree \(mnb\).  However, if

\&#91;
g=\operatorname{gap}(\rho,\ell),
\&#93;

then polynomial lattice support forces

\&#91;
p(z)=\bar p(z^g),\qquad q(z)=\bar q(z^g).
\&#93;

Writing \(u=z^g\) and \(N=n/g\), the actual quotient equation is

\&#91;
N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q=\frac1g,
\&#93;

and

\&#91;
\bar\tau=u^N\bar p^n/\bar q^m
\&#93;

has degree \(mnb/g\) and passport

\&#91;
\left(n^{(mb-1)/g},N\right),\qquad
\left(m^{nb/g}\right),\qquad
\left(\frac{(m+n)b-1}{g},1^{\frac{mnb-(m+n)b+1}{g}}\right).
\&#93;

This is the finite Hurwitz problem relevant to the complete-chain corner; the ambient degree-\(mnb\) cover is its cyclic \(g\)-pullback.

For the first cases in the queue:

| Case | \(g\) | quotient degree | quotient passport | classes |
|---|---:|---:|---|---:|
| \(F_2\), max 125 | 5 | 6 | \((5,1),(3^2),(3,1^3)\) | 1 |
| one-step max 126 | 3 | 10 | \((3^3,1),(2^5),(8,1^2)\) | 1 |
| two-step max 126 | 2 | 9 | \((2^4,1),(3^3),(7,1^2)\) | 1 |
| \(F_{24}\), max 128 | 4 | 9 | \((4^2,1),(3^3),(5,1^4)\) | 2 |
| one-step max 132 | 3 | 16 | \((3^5,1),(2^8),(13,1^3)\) | 2 |

The important correction is the first row.  The ambient \(F_2\) degree-30 passport has eleven dessin classes, but the gap-five lattice condition selects only its unique \(C_5\)-symmetric pullback.  The actual reduced boundary map is the unique degree-six map

\&#91;
\bar\tau(u)\doteq
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
\&#93;

Thus the next universality test is a single \(C_5\)-equivariant normal-neighborhood computation, not eleven unrelated degree-30 calculations.  Exact maps for the two degree-126 rows and the two conjugate \(F_{24}\) rows are given in `terminal_primary_belyi_reduction.md`.


## 7. Reduced terminal covers are rigid in the first explicit cases

For the quotient equation

\&#91;
N\bar p\bar q-mu\bar p\bar q'+nu\bar p'\bar q=\frac1g,
\&#93;

the fixed-constant linearization is

\&#91;
\mathscr L(\alpha,\beta)
=N(\alpha\bar q+\bar p\beta)
-mu(\alpha\bar q'+\bar p\beta')
+nu(\alpha'\bar q+\bar p'\beta).
\&#93;

Exact matrices for the degree-6, degree-10, degree-9, and the two conjugate degree-9 quotient maps have full target rank and one-dimensional kernel

\&#91;
\ker\mathscr L=\operatorname{Span}\{(u\bar p',u\bar q')\}.
\&#93;

Thus the reduced-cover coefficient scheme is smooth only along source rescaling; after quotienting by that rescaling, each map is a reduced isolated point.  This removes one potential source of hidden moduli from the next boundary calculations.  The first post-125 test can therefore be organized as a normal-jet Kuranishi problem over a rigid reduced degree-six cover.

The result does not yet identify the full boundary deformation functor with a product of the reduced Hurwitz point and the normal-jet complex.  The next structural theorem should prove this etale splitting, or explicitly identify the cross-terms that obstruct it.
</code></pre>

<a id="source-b6bb7682cc550398"></a>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact infinitesimal rigidity of the first lattice-quotient boundary maps.

For the quotient equation

    N p q - m u p q' + n u p' q = 1/g,

the constants p(0),q(0) are fixed and u-scaling remains.  This script forms
the exact linearization on the full coefficient windows, proves surjectivity,
and verifies that its kernel is exactly the scaling vector (u p',u q').
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp

u = sp.symbols("u")


def linearization_record(
    *, label: str, p: sp.Expr, q: sp.Expr, m: int, n: int, g: int, extension: Any = None
) -&gt; dict&#91;str, Any&#93;:
    A, B = int(sp.degree(p, u)), int(sp.degree(q, u))
    N = n // g
    avec = sp.symbols(f"a1:{A+1}")
    bvec = sp.symbols(f"b1:{B+1}")
    alpha = sum(avec&#91;i - 1&#93; * u**i for i in range(1, A + 1))
    beta = sum(bvec&#91;j - 1&#93; * u**j for j in range(1, B + 1))
    Dexpr = sp.expand(
        N * (alpha * q + p * beta)
        - m * u * (alpha * sp.diff(q, u) + p * sp.diff(beta, u))
        + n * u * (sp.diff(alpha, u) * q + sp.diff(p, u) * beta)
    )
    variables = list(avec) + list(bvec)
    rows = A + B - 1
    matrix = sp.Matrix(
        &#91;&#91;sp.expand(Dexpr).coeff(u, degree).coeff(var) for var in variables&#93; for degree in range(1, rows + 1)&#93;
    )
    rank = int(matrix.rank(iszerofunc=lambda x: sp.simplify(x) == 0))
    assert rank == rows
    null = matrix.nullspace(iszerofunc=lambda x: sp.simplify(x) == 0)
    assert len(null) == 1

    scaling_alpha = sp.expand(u * sp.diff(p, u))
    scaling_beta = sp.expand(u * sp.diff(q, u))
    scaling = sp.Matrix(
        &#91;scaling_alpha.coeff(u, i) for i in range(1, A + 1)&#93;
        + &#91;scaling_beta.coeff(u, j) for j in range(1, B + 1)&#93;
    )
    scaling_residual = (matrix * scaling).applyfunc(sp.simplify)
    assert scaling_residual == sp.zeros(rows, 1)
    # Kernel generator and scaling vector must be proportional.
    gen = null&#91;0&#93;
    ratios = &#91;sp.simplify(gen&#91;i&#93; / scaling&#91;i&#93;) for i in range(len(gen)) if scaling&#91;i&#93; != 0&#93;
    assert ratios and all(sp.simplify(r - ratios&#91;0&#93;) == 0 for r in ratios)
    assert all(sp.simplify(gen&#91;i&#93;) == 0 for i in range(len(gen)) if sp.simplify(scaling&#91;i&#93;) == 0)

    _, pivots = matrix.rref(iszerofunc=lambda x: sp.simplify(x) == 0)
    pivot_cols = &#91;int(j) for j in pivots&#91;:rows&#93;&#93;
    minor = sp.simplify(matrix&#91;:, pivot_cols&#93;.det())
    assert minor != 0

    return {
        "label": label,
        "degrees": &#91;A, B&#93;,
        "domain_dimension_fixed_constants": A + B,
        "target_dimension": rows,
        "rank": rank,
        "kernel_dimension": 1,
        "kernel": "span{(u p'(u), u q'(u))}",
        "pivot_columns_zero_based": pivot_cols,
        "nonzero_maximal_minor": str(minor),
    }


def maps() -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    sqrt6 = sp.sqrt(6)
    out: list&#91;dict&#91;str, Any&#93;&#93; = &#91;&#93;

    out.append(
        dict(
            label="F2_max125",
            p=1 - u,
            q=sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2,
            m=3,
            n=5,
            g=5,
        )
    )

    P = u**3 + u**2 + sp.Rational(5, 12) * u + sp.Rational(1, 18)
    Q = (
        u**5
        + sp.Rational(3, 2) * u**4
        + u**3
        + sp.Rational(1, 3) * u**2
        + sp.Rational(5, 96) * u
        + sp.Rational(1, 576)
    )
    out.append(dict(label="one_step_max126", p=18 * P, q=192 * Q, m=2, n=3, g=3))

    out.append(
        dict(
            label="two_step_max126",
            p=1
            + sp.Rational(20, 3) * u
            + 24 * u**2
            + sp.Rational(288, 7) * u**3
            + sp.Rational(288, 7) * u**4,
            q=sp.Rational(1, 2) + 5 * u + 12 * u**2 + 18 * u**3,
            m=3,
            n=2,
            g=2,
        )
    )

    for sign in (-1, 1):
        p = 1 + u + (sp.Rational(1, 3) + sign * sqrt6 / 18) * u**2
        q = (
            sp.Rational(1, 4)
            + sp.Rational(5, 8) * u
            + (sp.Rational(2, 5) + sign * sqrt6 / 40) * u**2
            + (sp.Rational(17, 160) + sign * sp.Rational(11, 480) * sqrt6) * u**3
        )
        out.append(
            dict(
                label=f"F24_max128_{'plus' if sign == 1 else 'minus'}",
                p=p,
                q=q,
                m=3,
                n=4,
                g=4,
                extension=sqrt6,
            )
        )
    return out


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    records = &#91;linearization_record(**item) for item in maps()&#93;
    if args.json:
        args.json.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps(records, indent=2))
    print("all reduced terminal maps are infinitesimally rigid modulo source scaling")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-07b7b4b6dfbd8330"></a>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact terminal-primary Belyi formulas for type-I.b complete-chain corners.

There are two distinct covers.

1. On the fractional uniformizing coordinate z=x^{-sigma/rho}y, the final
   face equation is

       n*p*q - m*z*p*q' + n*z*p'*q = 1,

   with deg(p)=m*b-1 and deg(q)=n*b.  It defines an ambient Belyi map

       tau(z)=z**n*p(z)**n/q(z)**m

   of degree m*n*b.

2. Polynomial lattice support forces p(z)=pbar(z**g), q(z)=qbar(z**g), where

       g=gap(rho,ell)=rho/gcd(rho,ell).

   Put N=n/g and u=z**g.  The lattice-compatible quotient satisfies

       N*pbar*qbar - m*u*pbar*qbar' + n*u*pbar'*qbar = 1/g

   and defines

       taubar(u)=u**N*pbar(u)**n/qbar(u)**m

   of degree m*n*b/g.  This quotient, not the ambient cyclic pullback, is the
   finite Hurwitz problem attached to the polynomial complete-chain corner.

The script checks the final-corner arithmetic, divisibility, passports,
Riemann--Hurwitz identities, and the explicit F2 quotient/lift.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from fractions import Fraction
from math import gcd
import json
from pathlib import Path
from typing import Iterable

import sympy as sp

z, u = sp.symbols("z u")


def _partition_text(parts: Iterable&#91;int&#93;) -&gt; str:
    counts: dict&#91;int, int&#93; = {}
    for part in sorted(parts, reverse=True):
        counts&#91;part&#93; = counts.get(part, 0) + 1
    pieces: list&#91;str&#93; = &#91;&#93;
    for part in sorted(counts, reverse=True):
        mult = counts&#91;part&#93;
        pieces.append(str(part) if mult == 1 else f"{part}^{mult}")
    return "(" + ",".join(pieces) + ")"


@dataclass(frozen=True)
class Passport:
    degree: int
    cycle_types: tuple&#91;tuple&#91;int, ...&#93;, tuple&#91;int, ...&#93;, tuple&#91;int, ...&#93;&#93;
    display: tuple&#91;str, str, str&#93;
    ramification_total: int


@dataclass(frozen=True)
class TerminalReduction:
    a: int
    ell: int
    b: int
    k: int
    m: int
    n: int
    rho: int
    sigma: int
    gap: int
    N: int
    deg_p: int
    deg_q: int
    deg_p_bar: int
    deg_q_bar: int
    uniformizing: Passport
    lattice_quotient: Passport
    terminal_coordinate_exponent_r: str
    uniformizing_ode: str
    quotient_ode: str


def _passport(parts0: tuple&#91;int, ...&#93;, parts1: tuple&#91;int, ...&#93;, parts2: tuple&#91;int, ...&#93;) -&gt; Passport:
    degree = sum(parts0)
    assert sum(parts1) == degree and sum(parts2) == degree
    rh = sum(x - 1 for parts in (parts0, parts1, parts2) for x in parts)
    assert rh == 2 * degree - 2
    return Passport(
        degree=degree,
        cycle_types=(parts0, parts1, parts2),
        display=tuple(_partition_text(parts) for parts in (parts0, parts1, parts2)),
        ramification_total=rh,
    )


def terminal_passport(m: int, n: int, b: int) -&gt; Passport:
    """Ambient passport on the fractional uniformizing z-line.

    Kept under the historical function name for compatibility with earlier
    scripts.  For the polynomial/lattice-compatible passport use
    ``terminal_reduction(...).lattice_quotient``.
    """
    if min(m, n, b) &lt;= 0:
        raise ValueError("m,n,b must be positive")
    if gcd(m, n) != 1 or min(m, n) &lt;= 1:
        raise ValueError("standard-pair application assumes coprime m,n&gt;1")
    D = m * n * b
    H = (m + n) * b - 1
    return _passport(
        tuple(&#91;n&#93; * (m * b)),
        tuple(&#91;m&#93; * (n * b)),
        tuple(&#91;H&#93; + &#91;1&#93; * (D - H)),
    )


def primitive_direction(*, a: int, ell: int, b: int, k: int, n: int) -&gt; tuple&#91;int, int&#93;:
    """Primitive (rho,sigma) from sigma/rho=(k-na)/(n ell b)."""
    numerator = k - n * a
    denominator = n * ell * b
    d = gcd(abs(numerator), denominator)
    rho, sigma = denominator // d, numerator // d
    assert rho &gt; 0 and gcd(rho, abs(sigma)) == 1
    return rho, sigma


def terminal_reduction(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -&gt; TerminalReduction:
    if min(a, ell, b, k, m, n) &lt;= 0:
        raise ValueError("all corner parameters must be positive")
    if gcd(m, n) != 1 or min(m, n) &lt;= 1:
        raise ValueError("m,n must be coprime and &gt;1")

    # Equation (3.17), in the orientation st(Q)=(k/ell,0).
    assert (m + n) * b * k - n * (b * ell - a) == k

    rho, sigma = primitive_direction(a=a, ell=ell, b=b, k=k, n=n)
    r = Fraction(-sigma, rho)
    assert r == Fraction(n * a - k, n * ell * b)
    gap = rho // gcd(rho, ell)

    A, B = Fraction(ell - k, ell), Fraction(1)
    C, D = Fraction(k, ell), Fraction(0)
    c_pq = A * D - B * C
    c_pqprime = A - B * r
    c_pprimeq = r * D - C
    scale = -Fraction(n * ell, k)
    assert (scale * c_pq, scale * c_pqprime, scale * c_pprimeq) == (n, -m, n)

    deg_p, deg_q = m * b - 1, n * b
    assert A + r * deg_p == Fraction(m * a, ell)
    assert B + deg_p == m * b
    assert C + r * deg_q == Fraction(n * a, ell)
    assert D + deg_q == n * b

    # Lattice support: only powers z^gap occur.  The degree divisibilities
    # are therefore necessary for a genuine complete-chain corner.
    assert deg_p % gap == 0
    assert deg_q % gap == 0
    assert gcd(gap, b) == 1
    assert n % gap == 0

    N = n // gap
    Abar, Bbar = deg_p // gap, deg_q // gap
    Dbar = m * n * b // gap
    Hbar_num = (m + n) * b - 1
    assert Hbar_num % gap == 0
    Hbar = Hbar_num // gap
    quotient = _passport(
        tuple(sorted(&#91;n&#93; * Abar + &#91;N&#93;, reverse=True)),
        tuple(&#91;m&#93; * Bbar),
        tuple(&#91;Hbar&#93; + &#91;1&#93; * (Dbar - Hbar)),
    )

    return TerminalReduction(
        a=a,
        ell=ell,
        b=b,
        k=k,
        m=m,
        n=n,
        rho=rho,
        sigma=sigma,
        gap=gap,
        N=N,
        deg_p=deg_p,
        deg_q=deg_q,
        deg_p_bar=Abar,
        deg_q_bar=Bbar,
        uniformizing=terminal_passport(m, n, b),
        lattice_quotient=quotient,
        terminal_coordinate_exponent_r=str(r),
        uniformizing_ode=f"{n}*p*q - {m}*z*p*q' + {n}*z*p'*q = 1",
        quotient_ode=f"{N}*pbar*qbar - {m}*u*pbar*qbar' + {n}*u*pbar'*qbar = 1/{gap}",
    )


def verify_final_corner_arithmetic(
    *, a: int, ell: int, b: int, k: int, m: int, n: int
) -&gt; dict&#91;str, object&#93;:
    """Backward-compatible JSON-style wrapper around :func:`terminal_reduction`."""
    rec = terminal_reduction(a=a, ell=ell, b=b, k=k, m=m, n=n)
    return {
        "direction": &#91;rec.rho, rec.sigma&#93;,
        "direction_ratio_sigma_over_rho": str(Fraction(rec.sigma, rec.rho)),
        "terminal_coordinate_exponent_r": rec.terminal_coordinate_exponent_r,
        "gap": rec.gap,
        "N": rec.N,
        "deg_p": str(rec.deg_p),
        "deg_q": str(rec.deg_q),
        "deg_p_bar": str(rec.deg_p_bar),
        "deg_q_bar": str(rec.deg_q_bar),
        "normalized_ode": rec.uniformizing_ode,
        "quotient_ode": rec.quotient_ode,
        "uniformizing_passport": rec.uniformizing.display,
        "lattice_quotient_passport": rec.lattice_quotient.display,
        "uniformizing_degree": rec.uniformizing.degree,
        "lattice_quotient_degree": rec.lattice_quotient.degree,
    }


def verify_explicit_f2_solution() -&gt; dict&#91;str, str&#93;:
    """Verify the unique lattice-compatible F2 quotient and its C5 pullback."""
    pbar = 1 - u
    qbar = sp.Rational(1, 5) - sp.Rational(3, 5) * u + sp.Rational(9, 25) * u**2
    qode = sp.expand(
        pbar * qbar
        - 3 * u * pbar * sp.diff(qbar, u)
        + 5 * u * sp.diff(pbar, u) * qbar
    )
    assert qode == sp.Rational(1, 5)
    taubar = sp.cancel(u * pbar**5 / qbar**3)
    assert sp.cancel(sp.diff(taubar, u) - sp.Rational(1, 5) * pbar**4 / qbar**4) == 0

    p = sp.expand(pbar.subs(u, z**5))
    q = sp.expand(qbar.subs(u, z**5))
    ode = sp.expand(5 * p * q - 3 * z * p * sp.diff(q, z) + 5 * z * sp.diff(p, z) * q)
    assert ode == 1
    tau = sp.cancel(z**5 * p**5 / q**3)
    assert sp.cancel(tau - taubar.subs(u, z**5)) == 0
    assert sp.cancel(sp.diff(tau, z) - z**4 * p**4 / q**4) == 0

    return {
        "pbar": str(sp.expand(pbar)),
        "qbar": str(sp.expand(qbar)),
        "taubar": "u*pbar(u)^5/qbar(u)^3",
        "p": str(p),
        "q": str(q),
        "tau": "taubar(z^5)",
    }


def _serialize(obj: object) -&gt; object:
    if isinstance(obj, Passport):
        data = asdict(obj)
        data&#91;"cycle_types"&#93; = &#91;list(x) for x in obj.cycle_types&#93;
        data&#91;"display"&#93; = list(obj.display)
        return data
    if isinstance(obj, TerminalReduction):
        return {
            **{k: v for k, v in asdict(obj).items() if k not in {"uniformizing", "lattice_quotient"}},
            "uniformizing": _serialize(obj.uniformizing),
            "lattice_quotient": _serialize(obj.lattice_quotient),
        }
    return obj


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, default=7)
    parser.add_argument("--ell", type=int, default=5)
    parser.add_argument("--b", type=int, default=2)
    parser.add_argument("--k", type=int, default=1)
    parser.add_argument("--m", type=int, default=3)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rec = terminal_reduction(a=args.a, ell=args.ell, b=args.b, k=args.k, m=args.m, n=args.n)
    payload: dict&#91;str, object&#93; = {"terminal_reduction": _serialize(rec)}
    if (args.a, args.ell, args.b, args.k, args.m, args.n) == (7, 5, 2, 1, 3, 5):
        payload&#91;"explicit_F2_solution"&#93; = verify_explicit_f2_solution()
        assert rec.gap == 5
        assert rec.lattice_quotient.degree == 6
        assert rec.lattice_quotient.display == ("(5,1)", "(3^2)", "(3,1^3)")

    if args.json:
        args.json.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    print("all terminal-face, lattice-gap, quotient, passport, derivative, and RH checks passed")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-2cdc0acae76d0682"></a>

## `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact arithmetic checks for the F2, maximum-degree-125 complete-chain seed."""
from fractions import Fraction
from math import gcd

A0 = (Fraction(5), Fraction(20))
A0p = (Fraction(1), Fraction(0))
A1 = (Fraction(7, 5), Fraction(2))
m, n = 3, 5

# Primitive normal to the edge A0-A0'.
dx = A0&#91;0&#93; - A0p&#91;0&#93;
dy = A0&#91;1&#93; - A0p&#91;1&#93;
g = gcd(dx.numerator, dy.numerator)
rho = dy / g
sigma = -dx / g
assert (rho, sigma) == (5, -1)

# Degrees in z=x^(1/5)y.
p_degree = m * (A0&#91;1&#93; - A0p&#91;1&#93;)
q_degree = n * (A0&#91;1&#93; - A0p&#91;1&#93;)
assert p_degree == 60 and q_degree == 100
assert p_degree % m == 0 and q_degree % n == 0
R_degree = p_degree / m
assert R_degree == 20
assert R_degree % 5 == 0
S_degree = R_degree / 5
assert S_degree == 4

# Child formula A1=A0' + (m_lambda/m)(-sigma/rho,1).
mult_ratio = A1&#91;1&#93; - A0p&#91;1&#93;
m_lambda = m * mult_ratio
assert m_lambda == 6
computed_A1 = (
    A0p&#91;0&#93; + mult_ratio * Fraction(-sigma, rho),
    A0p&#91;1&#93; + mult_ratio,
)
assert computed_A1 == A1

# After shifting a double root of R to zero, P has x^3 z^6.
new_x_exp = Fraction(3) + Fraction(6, 5)
new_y_exp = Fraction(6)
assert (new_x_exp / m, new_y_exp / m) == A1

print("F2 edge direction:", (rho, sigma))
print("degrees in z:", p_degree, q_degree, "common R degree:", R_degree)
print("integral common-root polynomial S(x y^5) degree:", S_degree)
print("chosen p-root multiplicity:", m_lambda, "=&gt; double root of R/S")
print("child corner verified:", computed_A1)
print("all exact F2 seed checks passed")
</code></pre>

<a id="source-e1384a8451d58dd7"></a>

## `research-notes/lane8-f2-root-divisibility-20260804-v1/README.md`

<pre><code class="language-markdown">
# Exact root-divisibility coordinates for the F2 linear descent

Date: 2026-08-04

Scope: an exact replacement for the inherited **linear** coefficient-relation
stage of the denominator-five (F_2) shear.  This packet does not solve the
subsequent nonlinear or support-stratification problems.

## Result

Fix a characteristic-zero coefficient field (K), a nonzero shear parameter
(lambda), and write

\&#91;
c=\lambda^5.
\&#93;

The (586) source coefficients of (P) split into (76) independent
weight blocks.  Terminal admissibility removes (53) Taylor coordinates,
and the resulting source incidence space has dimension (533).  The (1,576)
source coefficients of (Q) split into (126) blocks; (136) Taylor
coordinates are removed and the incidence space has dimension (1,440).

Every block has the explicit form

\&#91;
 C_w(Y)=Y^{j_0}(Y^5-c)^{F_w}E_w(Y^5),
 \qquad \deg E_w&lt;n_w-F_w.
\tag{1}
\&#93;

Here (w=5i-j), the source degrees are
(j_0,j_0+5,\ldots,j_0+5(n_w-1)), and

\&#91;
 F_w=\max\!\left(0,
 \min\!\left(j_{\max}+1,
 \left\lceil\frac{5w-t}{12}\right\rceil\right)\right),
 \qquad
 t=\begin{cases}3&amp;P,\\5&amp;Q.\end{cases}
\tag{2}
\&#93;

Consequently the exact inherited linear descent locus is an affine linear
space with

\&#91;
533+1,440=\boxed{1,973}
\&#93;

coordinates.  Its image in the (4,433+12,340) terminal-allowed output
coordinates has codimension

\&#91;
(4,433-533)+(12,340-1,440)=\boxed{14,800}.
\&#93;

Thus the linear stage does not require a (14,800)-row relation matrix.
The versioned &#91;block manifest&#93;(block_manifest.json) gives all (202) blocks,
including (j_0,n_w,F_w), the free dimension, pivot interval, and derived
output interval.

## Proof

### 1. Weight-block form of the source

For (P), the exact source envelope is

\&#91;
0\le i\le15,\qquad 0\le j\le60,\qquad5i-j\le15;
\&#93;

for (Q), it is

\&#91;
0\le i\le25,\qquad0\le j\le100,\qquad5i-j\le25.
\&#93;

At fixed (w=5i-j), the possible (j)'s form one consecutive arithmetic
progression of step five.  Therefore, if (c_{i,j}) denotes the corresponding
source coefficient,

\&#91;
C_w(Y)=\sum_{5i-j=w}c_{i,j}Y^j=Y^{j_0}H_w(Y^5),
\qquad \deg H_w&lt;n_w.
\tag{3}
\&#93;

Direct enumeration gives (76) blocks and (586) coefficients for (P),
and (126) blocks and (1,576) coefficients for (Q).

### 2. The forbidden terminal coordinates are one Taylor jet

Under

\&#91;
y\longmapsto y+\lambda x^{-1/5},
\&#93;

the output polynomial in the fixed block is

\&#91;
D_w(T)=C_w(T+\lambda).
\tag{4}
\&#93;

Indeed its coefficient of (T^J) is

\&#91;
d_{w,J}=\sum_{\substack{5i-j=w\\j\ge J}}
\binom jJ\lambda^{j-J}c_{i,j}.
\&#93;

The terminal inequalities are (5w-12J\le3) for (P) and
(5w-12J\le5) for (Q).  Hence the forbidden output degrees in the block
are exactly the initial interval

\&#91;
J=0,\ldots,F_w-1,
\&#93;

with (F_w) as in (2).  Their vanishing is equivalent to

\&#91;
T^{F_w}\mid D_w(T)
\quad\Longleftrightarrow\quad
(Y-\lambda)^{F_w}\mid C_w(Y).
\tag{5}
\&#93;

Since (lambda\ne0), the derivative of (Y\mapsto Y^5) at (lambda)
is (5\lambda^4\ne0), and the factor (Y^{j_0}) in (3) is a unit in the
local ring at (Y=\lambda).  Thus

\&#91;
\operatorname{ord}_{Y=\lambda}C_w(Y)
=\operatorname{ord}_{u=c}H_w(u).
\&#93;

Equation (5) is therefore equivalent to

\&#91;
H_w(u)=(u-c)^{F_w}E_w(u),
\qquad\deg E_w&lt;n_w-F_w,
\&#93;

which proves (1) and the block dimension (n_w-F_w).

### 3. Full row rank without elimination

At (lambda=1), the forbidden Taylor matrix is

\&#91;
\left&#91;\binom{j_k}{J}\right&#93;_{
0\le J&lt;F_w,\ 0\le k&lt;n_w}.
\&#93;

Its first (F_w) columns have determinant

\&#91;
\det\left&#91;\binom{j_k}{J}\right&#93;_{0\le J,k&lt;F_w}
=\frac{\prod_{0\le r&lt;s&lt;F_w}(j_s-j_r)}
{\prod_{J=0}^{F_w-1}J!}\ne0.
\tag{6}
\&#93;

For general nonzero (lambda), row and column powers of (lambda) are
invertible, so the rank is unchanged.  The checker verifies (6) exactly in
each of the (39) blocks with (F_w&gt;0), rather than relying only on a total
rank count.

### 4. Triangular coordinates and inverse

Expand

\&#91;
E_w(u)=\sum_{k=0}^{n_w-F_w-1}e_{w,k}(u-c)^k.
\&#93;

Then

\&#91;
D_w(T)=(T+\lambda)^{j_0}
\sum_k e_{w,k}
\left((T+\lambda)^5-\lambda^5\right)^{F_w+k}.
\tag{7}
\&#93;

The (k)-th summand starts in degree (T^{F_w+k}), with coefficient

\&#91;
\lambda^{j_0}(5\lambda^4)^{F_w+k}\ne0.
\&#93;

It follows that

\&#91;
(e_{w,0},\ldots,e_{w,n_w-F_w-1})
\longmapsto
(d_{w,F_w},\ldots,d_{w,n_w-1})
\&#93;

is triangular and invertible.  These declared pivot outputs recover all
(e_{w,k}) by forward substitution; equation (7) then produces every later
allowed output coefficient.  This gives both directions of the linear
parametrization, not just a dimension count.

## Leading common-power blocks

The leading (P)-block has (w=15), (n_w=13), and (F_w=6); the leading
(Q)-block has (w=25), (n_w=21), and (F_w=10).  Their free dimensions
are respectively (7) and (11).

When the separate common-power condition

\&#91;
H^P_{15}=\alpha S^3,\qquad H^Q_{25}=\beta S^5
\&#93;

is imposed, a double root of (S) at (c) produces precisely these
multiplicities.  Exact multiplicity additionally requires
(S(u)/(u-c)^2\) to be nonzero at (c).  The common-power condition is a
nonlinear constraint beyond the linear theorem proved here; it is not silently
built into the (202)-block manifest.

It may be imposed efficiently by writing

\&#91;
S(u)=(u-c)^2(s_2u^2+s_1u+s_0)
\&#93;

and retaining the required nonvanishing and normalization factors.  In
particular, (c) must remain related to the shear parameter by
(c=\lambda^5).  This packet does **not** identify (c) with (lambda) or
assert a gauge allowing (lambda=1).

## Quotient-coordinate determinant operator

In the terminal chart, put (u=z^5) and write

\&#91;
A_r(z)=z^\alpha a(u),\qquad B_s(z)=z^\beta b(u),
\qquad0\le\alpha,\beta&lt;5.
\&#93;

Since

\&#91;
\frac d{dz}\left(z^\alpha a(u)\right)
=z^{\alpha-1}\left(\alpha a+5ua'\right),
\&#93;

the contribution of ((A_r,B_s)) to

\&#91;
(3-r)A_rB_s'+(s-5)A_r'B_s
\&#93;

is (z^{\alpha+\beta-1}) times

\&#91;
(3-r)a(\beta b+5ub')
+(s-5)(\alpha a+5ua')b.
\tag{8}
\&#93;

For monomials (a=u^p,b=u^q), the coefficient in (8) is

\&#91;
(3-r)(\beta+5q)+(s-5)(\alpha+5p),
\&#93;

which is exactly the maintained sparse-(z) coefficient

\&#91;
(3-r)B+(s-5)A
\&#93;

for (A=\alpha+5p) and (B=\beta+5q).  The checker exercises this equality
on every supported monomial against the leading blocks.  Thus future
determinant calculations may use dense univariate polynomials in (u) while
preserving the exact (C_5)-character blocks.

## Verification

Run:

```bash
uv run python -B \
  research-notes/lane8-f2-root-divisibility-20260804-v1/verify_f2_root_divisibility.py
```

The checker independently reconstructs the source and terminal supports,
compares the complete committed manifest with the reconstruction, verifies
every forbidden-block rank and Vandermonde witness, verifies every triangular
pivot matrix, checks the leading multiplicities, checks the two dimension
totals, and checks quotient-operator compatibility.  It imports no earlier
Lane 8 implementation.  Optional JSON output is write-once.

## Exact scope boundary

This packet establishes the complete inherited **linear** descent locus for
the fixed denominator-five shear.  It does not establish:

- the common-power, exact-double-root, determinant, normalization, or open
  conditions as one solved constructible locus;
- a finite stratification or uniqueness theorem for actual post-shear
  supports;
- a forward/inverse correspondence for that nonlinear locus;
- an adjacent-chart attachment or a descent theorem;
- any plane Jacobian-conjecture conclusion.

Those are the remaining Lane 8 stages.  They should consume the (1,973)
coordinates in this packet lazily rather than reconstructing (16,773)
allowed output variables and (14,800) linear equations.
</code></pre>

<a id="source-ecdf70748a34b462"></a>

## `research-notes/lane8-f2-root-divisibility-20260804-v1/block_manifest.json`

<pre><code class="language-json">
{
  "blocks": {
    "P": &#91;
      {
        "derived_output_interval": &#91;
          1,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_P_-60_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 60,
        "source_min_degree": 60,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -60
      },
      {
        "derived_output_interval": &#91;
          1,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_P_-59_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 59,
        "source_min_degree": 59,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -59
      },
      {
        "derived_output_interval": &#91;
          1,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_P_-58_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 58,
        "source_min_degree": 58,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -58
      },
      {
        "derived_output_interval": &#91;
          1,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_P_-57_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 57,
        "source_min_degree": 57,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -57
      },
      {
        "derived_output_interval": &#91;
          1,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_P_-56_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 56,
        "source_min_degree": 56,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -56
      },
      {
        "derived_output_interval": &#91;
          2,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_P_-55_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 60,
        "source_min_degree": 55,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -55
      },
      {
        "derived_output_interval": &#91;
          2,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_P_-54_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 59,
        "source_min_degree": 54,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -54
      },
      {
        "derived_output_interval": &#91;
          2,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_P_-53_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 58,
        "source_min_degree": 53,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -53
      },
      {
        "derived_output_interval": &#91;
          2,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_P_-52_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 57,
        "source_min_degree": 52,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -52
      },
      {
        "derived_output_interval": &#91;
          2,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_P_-51_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 56,
        "source_min_degree": 51,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -51
      },
      {
        "derived_output_interval": &#91;
          3,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_P_-50_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 60,
        "source_min_degree": 50,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -50
      },
      {
        "derived_output_interval": &#91;
          3,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_P_-49_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 59,
        "source_min_degree": 49,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -49
      },
      {
        "derived_output_interval": &#91;
          3,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_P_-48_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 58,
        "source_min_degree": 48,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -48
      },
      {
        "derived_output_interval": &#91;
          3,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_P_-47_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 57,
        "source_min_degree": 47,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -47
      },
      {
        "derived_output_interval": &#91;
          3,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_P_-46_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 56,
        "source_min_degree": 46,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -46
      },
      {
        "derived_output_interval": &#91;
          4,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_P_-45_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 60,
        "source_min_degree": 45,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -45
      },
      {
        "derived_output_interval": &#91;
          4,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_P_-44_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 59,
        "source_min_degree": 44,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -44
      },
      {
        "derived_output_interval": &#91;
          4,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_P_-43_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 58,
        "source_min_degree": 43,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -43
      },
      {
        "derived_output_interval": &#91;
          4,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_P_-42_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 57,
        "source_min_degree": 42,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -42
      },
      {
        "derived_output_interval": &#91;
          4,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_P_-41_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 56,
        "source_min_degree": 41,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -41
      },
      {
        "derived_output_interval": &#91;
          5,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_P_-40_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 60,
        "source_min_degree": 40,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -40
      },
      {
        "derived_output_interval": &#91;
          5,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_P_-39_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 59,
        "source_min_degree": 39,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -39
      },
      {
        "derived_output_interval": &#91;
          5,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_P_-38_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 58,
        "source_min_degree": 38,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -38
      },
      {
        "derived_output_interval": &#91;
          5,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_P_-37_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 57,
        "source_min_degree": 37,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -37
      },
      {
        "derived_output_interval": &#91;
          5,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_P_-36_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 56,
        "source_min_degree": 36,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -36
      },
      {
        "derived_output_interval": &#91;
          6,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_-35_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 60,
        "source_min_degree": 35,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -35
      },
      {
        "derived_output_interval": &#91;
          6,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_-34_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 59,
        "source_min_degree": 34,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -34
      },
      {
        "derived_output_interval": &#91;
          6,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_-33_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 58,
        "source_min_degree": 33,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -33
      },
      {
        "derived_output_interval": &#91;
          6,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_-32_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 57,
        "source_min_degree": 32,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -32
      },
      {
        "derived_output_interval": &#91;
          6,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_-31_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 56,
        "source_min_degree": 31,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -31
      },
      {
        "derived_output_interval": &#91;
          7,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_-30_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 60,
        "source_min_degree": 30,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -30
      },
      {
        "derived_output_interval": &#91;
          7,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_-29_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 59,
        "source_min_degree": 29,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -29
      },
      {
        "derived_output_interval": &#91;
          7,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_-28_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 58,
        "source_min_degree": 28,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -28
      },
      {
        "derived_output_interval": &#91;
          7,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_-27_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 57,
        "source_min_degree": 27,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -27
      },
      {
        "derived_output_interval": &#91;
          7,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_-26_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 56,
        "source_min_degree": 26,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -26
      },
      {
        "derived_output_interval": &#91;
          8,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_-25_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 60,
        "source_min_degree": 25,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -25
      },
      {
        "derived_output_interval": &#91;
          8,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_-24_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 59,
        "source_min_degree": 24,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -24
      },
      {
        "derived_output_interval": &#91;
          8,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_-23_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 58,
        "source_min_degree": 23,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -23
      },
      {
        "derived_output_interval": &#91;
          8,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_-22_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 57,
        "source_min_degree": 22,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -22
      },
      {
        "derived_output_interval": &#91;
          8,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_-21_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 56,
        "source_min_degree": 21,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -21
      },
      {
        "derived_output_interval": &#91;
          9,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_-20_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 60,
        "source_min_degree": 20,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -20
      },
      {
        "derived_output_interval": &#91;
          9,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_-19_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 59,
        "source_min_degree": 19,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -19
      },
      {
        "derived_output_interval": &#91;
          9,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_-18_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 58,
        "source_min_degree": 18,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -18
      },
      {
        "derived_output_interval": &#91;
          9,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_-17_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 57,
        "source_min_degree": 17,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -17
      },
      {
        "derived_output_interval": &#91;
          9,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_-16_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 56,
        "source_min_degree": 16,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -16
      },
      {
        "derived_output_interval": &#91;
          10,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_-15_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 60,
        "source_min_degree": 15,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -15
      },
      {
        "derived_output_interval": &#91;
          10,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_-14_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 59,
        "source_min_degree": 14,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -14
      },
      {
        "derived_output_interval": &#91;
          10,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_-13_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 58,
        "source_min_degree": 13,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -13
      },
      {
        "derived_output_interval": &#91;
          10,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_-12_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 57,
        "source_min_degree": 12,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -12
      },
      {
        "derived_output_interval": &#91;
          10,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_-11_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 56,
        "source_min_degree": 11,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -11
      },
      {
        "derived_output_interval": &#91;
          11,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_-10_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 60,
        "source_min_degree": 10,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -10
      },
      {
        "derived_output_interval": &#91;
          11,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_-9_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 59,
        "source_min_degree": 9,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -9
      },
      {
        "derived_output_interval": &#91;
          11,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_-8_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 58,
        "source_min_degree": 8,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -8
      },
      {
        "derived_output_interval": &#91;
          11,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_-7_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 57,
        "source_min_degree": 7,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -7
      },
      {
        "derived_output_interval": &#91;
          11,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_-6_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 56,
        "source_min_degree": 6,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -6
      },
      {
        "derived_output_interval": &#91;
          12,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_P_-5_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 60,
        "source_min_degree": 5,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -5
      },
      {
        "derived_output_interval": &#91;
          12,
          59
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_P_-4_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 59,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -4
      },
      {
        "derived_output_interval": &#91;
          12,
          58
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_P_-3_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 58,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -3
      },
      {
        "derived_output_interval": &#91;
          12,
          57
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_P_-2_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 57,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -2
      },
      {
        "derived_output_interval": &#91;
          12,
          56
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_P_-1_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 56,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -1
      },
      {
        "derived_output_interval": &#91;
          13,
          60
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_P_0_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 60,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": 0
      },
      {
        "derived_output_interval": &#91;
          12,
          59
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          0
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_1_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          1,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 59,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 1,
        "weight": 1
      },
      {
        "derived_output_interval": &#91;
          12,
          58
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          0
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_2_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          1,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 58,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 1,
        "weight": 2
      },
      {
        "derived_output_interval": &#91;
          12,
          57
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          0
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_3_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          1,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 57,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 1,
        "weight": 3
      },
      {
        "derived_output_interval": &#91;
          12,
          56
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          1
        &#93;,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_P_4_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          2,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 56,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 2,
        "weight": 4
      },
      {
        "derived_output_interval": &#91;
          13,
          60
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          1
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_P_5_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          2,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 60,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 2,
        "weight": 5
      },
      {
        "derived_output_interval": &#91;
          12,
          59
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          2
        &#93;,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_6_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          3,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 59,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 3,
        "weight": 6
      },
      {
        "derived_output_interval": &#91;
          12,
          58
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          2
        &#93;,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_7_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          3,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 58,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 3,
        "weight": 7
      },
      {
        "derived_output_interval": &#91;
          12,
          57
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          3
        &#93;,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_8_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          4,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 57,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 4,
        "weight": 8
      },
      {
        "derived_output_interval": &#91;
          12,
          56
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          3
        &#93;,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_P_9_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          4,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 56,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 4,
        "weight": 9
      },
      {
        "derived_output_interval": &#91;
          13,
          60
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          3
        &#93;,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_P_10_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          4,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 60,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 4,
        "weight": 10
      },
      {
        "derived_output_interval": &#91;
          12,
          59
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          4
        &#93;,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_11_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          5,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 59,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 5,
        "weight": 11
      },
      {
        "derived_output_interval": &#91;
          12,
          58
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          4
        &#93;,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_12_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          5,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 58,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 5,
        "weight": 12
      },
      {
        "derived_output_interval": &#91;
          12,
          57
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          5
        &#93;,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_13_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          6,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 57,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 6,
        "weight": 13
      },
      {
        "derived_output_interval": &#91;
          12,
          56
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          5
        &#93;,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_P_14_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          6,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 56,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 6,
        "weight": 14
      },
      {
        "derived_output_interval": &#91;
          13,
          60
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          5
        &#93;,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_P_15_{k}"
        },
        "kind": "P",
        "pivot_output_interval": &#91;
          6,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 60,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 6,
        "weight": 15
      }
    &#93;,
    "Q": &#91;
      {
        "derived_output_interval": &#91;
          1,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_Q_-100_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 100,
        "source_min_degree": 100,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -100
      },
      {
        "derived_output_interval": &#91;
          1,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_Q_-99_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 99,
        "source_min_degree": 99,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -99
      },
      {
        "derived_output_interval": &#91;
          1,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_Q_-98_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 98,
        "source_min_degree": 98,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -98
      },
      {
        "derived_output_interval": &#91;
          1,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_Q_-97_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 97,
        "source_min_degree": 97,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -97
      },
      {
        "derived_output_interval": &#91;
          1,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 1,
        "free_variable": {
          "index_interval": &#91;
            0,
            0
          &#93;,
          "symbol_pattern": "e_Q_-96_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          0
        &#93;,
        "source_dimension": 1,
        "source_max_degree": 96,
        "source_min_degree": 96,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -96
      },
      {
        "derived_output_interval": &#91;
          2,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_Q_-95_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 100,
        "source_min_degree": 95,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -95
      },
      {
        "derived_output_interval": &#91;
          2,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_Q_-94_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 99,
        "source_min_degree": 94,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -94
      },
      {
        "derived_output_interval": &#91;
          2,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_Q_-93_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 98,
        "source_min_degree": 93,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -93
      },
      {
        "derived_output_interval": &#91;
          2,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_Q_-92_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 97,
        "source_min_degree": 92,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -92
      },
      {
        "derived_output_interval": &#91;
          2,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 2,
        "free_variable": {
          "index_interval": &#91;
            0,
            1
          &#93;,
          "symbol_pattern": "e_Q_-91_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          1
        &#93;,
        "source_dimension": 2,
        "source_max_degree": 96,
        "source_min_degree": 91,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -91
      },
      {
        "derived_output_interval": &#91;
          3,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_Q_-90_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 100,
        "source_min_degree": 90,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -90
      },
      {
        "derived_output_interval": &#91;
          3,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_Q_-89_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 99,
        "source_min_degree": 89,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -89
      },
      {
        "derived_output_interval": &#91;
          3,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_Q_-88_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 98,
        "source_min_degree": 88,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -88
      },
      {
        "derived_output_interval": &#91;
          3,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_Q_-87_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 97,
        "source_min_degree": 87,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -87
      },
      {
        "derived_output_interval": &#91;
          3,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 3,
        "free_variable": {
          "index_interval": &#91;
            0,
            2
          &#93;,
          "symbol_pattern": "e_Q_-86_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          2
        &#93;,
        "source_dimension": 3,
        "source_max_degree": 96,
        "source_min_degree": 86,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -86
      },
      {
        "derived_output_interval": &#91;
          4,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_Q_-85_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 100,
        "source_min_degree": 85,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -85
      },
      {
        "derived_output_interval": &#91;
          4,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_Q_-84_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 99,
        "source_min_degree": 84,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -84
      },
      {
        "derived_output_interval": &#91;
          4,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_Q_-83_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 98,
        "source_min_degree": 83,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -83
      },
      {
        "derived_output_interval": &#91;
          4,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_Q_-82_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 97,
        "source_min_degree": 82,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -82
      },
      {
        "derived_output_interval": &#91;
          4,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 4,
        "free_variable": {
          "index_interval": &#91;
            0,
            3
          &#93;,
          "symbol_pattern": "e_Q_-81_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          3
        &#93;,
        "source_dimension": 4,
        "source_max_degree": 96,
        "source_min_degree": 81,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -81
      },
      {
        "derived_output_interval": &#91;
          5,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_Q_-80_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 100,
        "source_min_degree": 80,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -80
      },
      {
        "derived_output_interval": &#91;
          5,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_Q_-79_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 99,
        "source_min_degree": 79,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -79
      },
      {
        "derived_output_interval": &#91;
          5,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_Q_-78_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 98,
        "source_min_degree": 78,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -78
      },
      {
        "derived_output_interval": &#91;
          5,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_Q_-77_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 97,
        "source_min_degree": 77,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -77
      },
      {
        "derived_output_interval": &#91;
          5,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 5,
        "free_variable": {
          "index_interval": &#91;
            0,
            4
          &#93;,
          "symbol_pattern": "e_Q_-76_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          4
        &#93;,
        "source_dimension": 5,
        "source_max_degree": 96,
        "source_min_degree": 76,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -76
      },
      {
        "derived_output_interval": &#91;
          6,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_Q_-75_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 100,
        "source_min_degree": 75,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -75
      },
      {
        "derived_output_interval": &#91;
          6,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_Q_-74_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 99,
        "source_min_degree": 74,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -74
      },
      {
        "derived_output_interval": &#91;
          6,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_Q_-73_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 98,
        "source_min_degree": 73,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -73
      },
      {
        "derived_output_interval": &#91;
          6,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_Q_-72_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 97,
        "source_min_degree": 72,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -72
      },
      {
        "derived_output_interval": &#91;
          6,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 6,
        "free_variable": {
          "index_interval": &#91;
            0,
            5
          &#93;,
          "symbol_pattern": "e_Q_-71_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          5
        &#93;,
        "source_dimension": 6,
        "source_max_degree": 96,
        "source_min_degree": 71,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -71
      },
      {
        "derived_output_interval": &#91;
          7,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_Q_-70_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 100,
        "source_min_degree": 70,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -70
      },
      {
        "derived_output_interval": &#91;
          7,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_Q_-69_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 99,
        "source_min_degree": 69,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -69
      },
      {
        "derived_output_interval": &#91;
          7,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_Q_-68_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 98,
        "source_min_degree": 68,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -68
      },
      {
        "derived_output_interval": &#91;
          7,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_Q_-67_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 97,
        "source_min_degree": 67,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -67
      },
      {
        "derived_output_interval": &#91;
          7,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 7,
        "free_variable": {
          "index_interval": &#91;
            0,
            6
          &#93;,
          "symbol_pattern": "e_Q_-66_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          6
        &#93;,
        "source_dimension": 7,
        "source_max_degree": 96,
        "source_min_degree": 66,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -66
      },
      {
        "derived_output_interval": &#91;
          8,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_Q_-65_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 100,
        "source_min_degree": 65,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -65
      },
      {
        "derived_output_interval": &#91;
          8,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_Q_-64_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 99,
        "source_min_degree": 64,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -64
      },
      {
        "derived_output_interval": &#91;
          8,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_Q_-63_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 98,
        "source_min_degree": 63,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -63
      },
      {
        "derived_output_interval": &#91;
          8,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_Q_-62_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 97,
        "source_min_degree": 62,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -62
      },
      {
        "derived_output_interval": &#91;
          8,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 8,
        "free_variable": {
          "index_interval": &#91;
            0,
            7
          &#93;,
          "symbol_pattern": "e_Q_-61_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          7
        &#93;,
        "source_dimension": 8,
        "source_max_degree": 96,
        "source_min_degree": 61,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -61
      },
      {
        "derived_output_interval": &#91;
          9,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_Q_-60_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 100,
        "source_min_degree": 60,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -60
      },
      {
        "derived_output_interval": &#91;
          9,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_Q_-59_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 99,
        "source_min_degree": 59,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -59
      },
      {
        "derived_output_interval": &#91;
          9,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_Q_-58_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 98,
        "source_min_degree": 58,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -58
      },
      {
        "derived_output_interval": &#91;
          9,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_Q_-57_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 97,
        "source_min_degree": 57,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -57
      },
      {
        "derived_output_interval": &#91;
          9,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 9,
        "free_variable": {
          "index_interval": &#91;
            0,
            8
          &#93;,
          "symbol_pattern": "e_Q_-56_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          8
        &#93;,
        "source_dimension": 9,
        "source_max_degree": 96,
        "source_min_degree": 56,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -56
      },
      {
        "derived_output_interval": &#91;
          10,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_-55_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 100,
        "source_min_degree": 55,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -55
      },
      {
        "derived_output_interval": &#91;
          10,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_-54_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 99,
        "source_min_degree": 54,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -54
      },
      {
        "derived_output_interval": &#91;
          10,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_-53_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 98,
        "source_min_degree": 53,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -53
      },
      {
        "derived_output_interval": &#91;
          10,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_-52_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 97,
        "source_min_degree": 52,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -52
      },
      {
        "derived_output_interval": &#91;
          10,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_-51_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          9
        &#93;,
        "source_dimension": 10,
        "source_max_degree": 96,
        "source_min_degree": 51,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -51
      },
      {
        "derived_output_interval": &#91;
          11,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_-50_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 100,
        "source_min_degree": 50,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -50
      },
      {
        "derived_output_interval": &#91;
          11,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_-49_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 99,
        "source_min_degree": 49,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -49
      },
      {
        "derived_output_interval": &#91;
          11,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_-48_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 98,
        "source_min_degree": 48,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -48
      },
      {
        "derived_output_interval": &#91;
          11,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_-47_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 97,
        "source_min_degree": 47,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -47
      },
      {
        "derived_output_interval": &#91;
          11,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_-46_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          10
        &#93;,
        "source_dimension": 11,
        "source_max_degree": 96,
        "source_min_degree": 46,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -46
      },
      {
        "derived_output_interval": &#91;
          12,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_-45_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 100,
        "source_min_degree": 45,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -45
      },
      {
        "derived_output_interval": &#91;
          12,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_-44_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 99,
        "source_min_degree": 44,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -44
      },
      {
        "derived_output_interval": &#91;
          12,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_-43_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 98,
        "source_min_degree": 43,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -43
      },
      {
        "derived_output_interval": &#91;
          12,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_-42_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 97,
        "source_min_degree": 42,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -42
      },
      {
        "derived_output_interval": &#91;
          12,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_-41_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          11
        &#93;,
        "source_dimension": 12,
        "source_max_degree": 96,
        "source_min_degree": 41,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -41
      },
      {
        "derived_output_interval": &#91;
          13,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_-40_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 100,
        "source_min_degree": 40,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -40
      },
      {
        "derived_output_interval": &#91;
          13,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_-39_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 99,
        "source_min_degree": 39,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -39
      },
      {
        "derived_output_interval": &#91;
          13,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_-38_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 98,
        "source_min_degree": 38,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -38
      },
      {
        "derived_output_interval": &#91;
          13,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_-37_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 97,
        "source_min_degree": 37,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -37
      },
      {
        "derived_output_interval": &#91;
          13,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_-36_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          12
        &#93;,
        "source_dimension": 13,
        "source_max_degree": 96,
        "source_min_degree": 36,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -36
      },
      {
        "derived_output_interval": &#91;
          14,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_-35_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          13
        &#93;,
        "source_dimension": 14,
        "source_max_degree": 100,
        "source_min_degree": 35,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -35
      },
      {
        "derived_output_interval": &#91;
          14,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_-34_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          13
        &#93;,
        "source_dimension": 14,
        "source_max_degree": 99,
        "source_min_degree": 34,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -34
      },
      {
        "derived_output_interval": &#91;
          14,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_-33_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          13
        &#93;,
        "source_dimension": 14,
        "source_max_degree": 98,
        "source_min_degree": 33,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -33
      },
      {
        "derived_output_interval": &#91;
          14,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_-32_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          13
        &#93;,
        "source_dimension": 14,
        "source_max_degree": 97,
        "source_min_degree": 32,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -32
      },
      {
        "derived_output_interval": &#91;
          14,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_-31_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          13
        &#93;,
        "source_dimension": 14,
        "source_max_degree": 96,
        "source_min_degree": 31,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -31
      },
      {
        "derived_output_interval": &#91;
          15,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_-30_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          14
        &#93;,
        "source_dimension": 15,
        "source_max_degree": 100,
        "source_min_degree": 30,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -30
      },
      {
        "derived_output_interval": &#91;
          15,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_-29_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          14
        &#93;,
        "source_dimension": 15,
        "source_max_degree": 99,
        "source_min_degree": 29,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -29
      },
      {
        "derived_output_interval": &#91;
          15,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_-28_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          14
        &#93;,
        "source_dimension": 15,
        "source_max_degree": 98,
        "source_min_degree": 28,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -28
      },
      {
        "derived_output_interval": &#91;
          15,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_-27_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          14
        &#93;,
        "source_dimension": 15,
        "source_max_degree": 97,
        "source_min_degree": 27,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -27
      },
      {
        "derived_output_interval": &#91;
          15,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_-26_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          14
        &#93;,
        "source_dimension": 15,
        "source_max_degree": 96,
        "source_min_degree": 26,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -26
      },
      {
        "derived_output_interval": &#91;
          16,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_-25_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          15
        &#93;,
        "source_dimension": 16,
        "source_max_degree": 100,
        "source_min_degree": 25,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -25
      },
      {
        "derived_output_interval": &#91;
          16,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_-24_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          15
        &#93;,
        "source_dimension": 16,
        "source_max_degree": 99,
        "source_min_degree": 24,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -24
      },
      {
        "derived_output_interval": &#91;
          16,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_-23_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          15
        &#93;,
        "source_dimension": 16,
        "source_max_degree": 98,
        "source_min_degree": 23,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -23
      },
      {
        "derived_output_interval": &#91;
          16,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_-22_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          15
        &#93;,
        "source_dimension": 16,
        "source_max_degree": 97,
        "source_min_degree": 22,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -22
      },
      {
        "derived_output_interval": &#91;
          16,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_-21_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          15
        &#93;,
        "source_dimension": 16,
        "source_max_degree": 96,
        "source_min_degree": 21,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -21
      },
      {
        "derived_output_interval": &#91;
          17,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_-20_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          16
        &#93;,
        "source_dimension": 17,
        "source_max_degree": 100,
        "source_min_degree": 20,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -20
      },
      {
        "derived_output_interval": &#91;
          17,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_-19_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          16
        &#93;,
        "source_dimension": 17,
        "source_max_degree": 99,
        "source_min_degree": 19,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -19
      },
      {
        "derived_output_interval": &#91;
          17,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_-18_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          16
        &#93;,
        "source_dimension": 17,
        "source_max_degree": 98,
        "source_min_degree": 18,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -18
      },
      {
        "derived_output_interval": &#91;
          17,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_-17_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          16
        &#93;,
        "source_dimension": 17,
        "source_max_degree": 97,
        "source_min_degree": 17,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -17
      },
      {
        "derived_output_interval": &#91;
          17,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_-16_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          16
        &#93;,
        "source_dimension": 17,
        "source_max_degree": 96,
        "source_min_degree": 16,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -16
      },
      {
        "derived_output_interval": &#91;
          18,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_-15_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          17
        &#93;,
        "source_dimension": 18,
        "source_max_degree": 100,
        "source_min_degree": 15,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -15
      },
      {
        "derived_output_interval": &#91;
          18,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_-14_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          17
        &#93;,
        "source_dimension": 18,
        "source_max_degree": 99,
        "source_min_degree": 14,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -14
      },
      {
        "derived_output_interval": &#91;
          18,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_-13_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          17
        &#93;,
        "source_dimension": 18,
        "source_max_degree": 98,
        "source_min_degree": 13,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -13
      },
      {
        "derived_output_interval": &#91;
          18,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_-12_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          17
        &#93;,
        "source_dimension": 18,
        "source_max_degree": 97,
        "source_min_degree": 12,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -12
      },
      {
        "derived_output_interval": &#91;
          18,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_-11_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          17
        &#93;,
        "source_dimension": 18,
        "source_max_degree": 96,
        "source_min_degree": 11,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -11
      },
      {
        "derived_output_interval": &#91;
          19,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_-10_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          18
        &#93;,
        "source_dimension": 19,
        "source_max_degree": 100,
        "source_min_degree": 10,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -10
      },
      {
        "derived_output_interval": &#91;
          19,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_-9_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          18
        &#93;,
        "source_dimension": 19,
        "source_max_degree": 99,
        "source_min_degree": 9,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -9
      },
      {
        "derived_output_interval": &#91;
          19,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_-8_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          18
        &#93;,
        "source_dimension": 19,
        "source_max_degree": 98,
        "source_min_degree": 8,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -8
      },
      {
        "derived_output_interval": &#91;
          19,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_-7_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          18
        &#93;,
        "source_dimension": 19,
        "source_max_degree": 97,
        "source_min_degree": 7,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -7
      },
      {
        "derived_output_interval": &#91;
          19,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_-6_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          18
        &#93;,
        "source_dimension": 19,
        "source_max_degree": 96,
        "source_min_degree": 6,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -6
      },
      {
        "derived_output_interval": &#91;
          20,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_-5_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 100,
        "source_min_degree": 5,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -5
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_-4_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -4
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_-3_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -3
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_-2_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -2
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_-1_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": -1
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 21,
        "free_variable": {
          "index_interval": &#91;
            0,
            20
          &#93;,
          "symbol_pattern": "e_Q_0_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": 0
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": null,
        "free_dimension": 20,
        "free_variable": {
          "index_interval": &#91;
            0,
            19
          &#93;,
          "symbol_pattern": "e_Q_1_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          0,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 0,
        "weight": 1
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          0
        &#93;,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_2_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          1,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 1,
        "weight": 2
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          0
        &#93;,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_3_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          1,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 1,
        "weight": 3
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          1
        &#93;,
        "free_dimension": 18,
        "free_variable": {
          "index_interval": &#91;
            0,
            17
          &#93;,
          "symbol_pattern": "e_Q_4_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          2,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 2,
        "weight": 4
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          1
        &#93;,
        "free_dimension": 19,
        "free_variable": {
          "index_interval": &#91;
            0,
            18
          &#93;,
          "symbol_pattern": "e_Q_5_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          2,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 2,
        "weight": 5
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          2
        &#93;,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_6_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          3,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 3,
        "weight": 6
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          2
        &#93;,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_7_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          3,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 3,
        "weight": 7
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          2
        &#93;,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_8_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          3,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 3,
        "weight": 8
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          3
        &#93;,
        "free_dimension": 16,
        "free_variable": {
          "index_interval": &#91;
            0,
            15
          &#93;,
          "symbol_pattern": "e_Q_9_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          4,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 4,
        "weight": 9
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          3
        &#93;,
        "free_dimension": 17,
        "free_variable": {
          "index_interval": &#91;
            0,
            16
          &#93;,
          "symbol_pattern": "e_Q_10_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          4,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 4,
        "weight": 10
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          4
        &#93;,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_11_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          5,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 5,
        "weight": 11
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          4
        &#93;,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_12_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          5,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 5,
        "weight": 12
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          4
        &#93;,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_13_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          5,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 5,
        "weight": 13
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          5
        &#93;,
        "free_dimension": 14,
        "free_variable": {
          "index_interval": &#91;
            0,
            13
          &#93;,
          "symbol_pattern": "e_Q_14_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          6,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 6,
        "weight": 14
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          5
        &#93;,
        "free_dimension": 15,
        "free_variable": {
          "index_interval": &#91;
            0,
            14
          &#93;,
          "symbol_pattern": "e_Q_15_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          6,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 6,
        "weight": 15
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          6
        &#93;,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_16_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          7,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 7,
        "weight": 16
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          6
        &#93;,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_17_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          7,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 7,
        "weight": 17
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          7
        &#93;,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_18_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          8,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 8,
        "weight": 18
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          7
        &#93;,
        "free_dimension": 12,
        "free_variable": {
          "index_interval": &#91;
            0,
            11
          &#93;,
          "symbol_pattern": "e_Q_19_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          8,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 8,
        "weight": 19
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          7
        &#93;,
        "free_dimension": 13,
        "free_variable": {
          "index_interval": &#91;
            0,
            12
          &#93;,
          "symbol_pattern": "e_Q_20_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          8,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 8,
        "weight": 20
      },
      {
        "derived_output_interval": &#91;
          20,
          99
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          8
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_21_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          9,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 99,
        "source_min_degree": 4,
        "source_step": 5,
        "terminal_multiplicity": 9,
        "weight": 21
      },
      {
        "derived_output_interval": &#91;
          20,
          98
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          8
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_22_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          9,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 98,
        "source_min_degree": 3,
        "source_step": 5,
        "terminal_multiplicity": 9,
        "weight": 22
      },
      {
        "derived_output_interval": &#91;
          20,
          97
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          9
        &#93;,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_23_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          10,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 97,
        "source_min_degree": 2,
        "source_step": 5,
        "terminal_multiplicity": 10,
        "weight": 23
      },
      {
        "derived_output_interval": &#91;
          20,
          96
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          9
        &#93;,
        "free_dimension": 10,
        "free_variable": {
          "index_interval": &#91;
            0,
            9
          &#93;,
          "symbol_pattern": "e_Q_24_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          10,
          19
        &#93;,
        "source_dimension": 20,
        "source_max_degree": 96,
        "source_min_degree": 1,
        "source_step": 5,
        "terminal_multiplicity": 10,
        "weight": 24
      },
      {
        "derived_output_interval": &#91;
          21,
          100
        &#93;,
        "forbidden_output_interval": &#91;
          0,
          9
        &#93;,
        "free_dimension": 11,
        "free_variable": {
          "index_interval": &#91;
            0,
            10
          &#93;,
          "symbol_pattern": "e_Q_25_{k}"
        },
        "kind": "Q",
        "pivot_output_interval": &#91;
          10,
          20
        &#93;,
        "source_dimension": 21,
        "source_max_degree": 100,
        "source_min_degree": 0,
        "source_step": 5,
        "terminal_multiplicity": 10,
        "weight": 25
      }
    &#93;
  },
  "coefficient_ring": "K&#91;lambda,c,lambda^{-1}&#93;/(c-lambda^5), char(K)=0",
  "coordinates": {
    "source_block": "C_w(Y)=Y^j0 H_w(Y^5)",
    "source_weight": "w=5*i-j",
    "terminal_test": "5*w-12*J&lt;=t; t=3 for P and t=5 for Q",
    "transport": "D_w(T)=C_w(T+lambda)"
  },
  "formulas": {
    "free_degree_bound": "deg(E_w)&lt;n_w-F_w",
    "generic_diagonal": "lambda^j0*(5*lambda^4)^(F_w+k)",
    "quotient_determinant_operator": "(3-r)*a*(beta*b+5*u*b')+(s-5)*(alpha*a+5*u*a')*b",
    "root_divisibility": "H_w(u)=(u-c)^F_w E_w(u)",
    "terminal_multiplicity": "F_w=max(0,min(jmax+1,ceil((5*w-t)/12)))",
    "triangular_basis": "C_w(Y)=Y^j0 sum_k e_w,k (Y^5-c)^(F_w+k)"
  },
  "packet_id": "lane8-f2-root-divisibility-20260804-v1",
  "provenance": &#91;
    {
      "path": "research-notes/lane8-f2-support-determinacy-audit-20260803-v1/README.md",
      "role": "prior exact transport and support audit",
      "sha256": "38c3c52d8deeed6036f0739da5837b98e6eac29b22f82c33f34931ca9c60da84"
    },
    {
      "path": "research-notes/lane8-f2-support-determinacy-audit-20260803-v1/verify_lane8_f2_support_determinacy_audit.py",
      "role": "prior independent support/rank checker",
      "sha256": "c5c5dfe96f3317795cbbc506a0ff4a7d6f14a5c84111778cdd76dc5914e647ab"
    },
    {
      "path": "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md",
      "role": "F2 source rectangles, shear, and common-power face",
      "sha256": "63fb30b6de06df86c9c87e968d4d72e58b9218134a9eaa8cbce978b78901eb5e"
    },
    {
      "path": "/path/to/versioned-artifact",
      "role": "maintained support-window generator and exact outputs",
      "sha256": "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64"
    }
  &#93;,
  "schema_version": 1,
  "scope": {
    "does_not_establish": &#91;
      "the nonlinear common-power or exact-double-root locus",
      "the determinant equations or their solution set",
      "actual post-shear support uniqueness or its stratification",
      "a gauge equivalence setting lambda to one",
      "an adjacent-chart attachment or a plane Jacobian-conjecture conclusion"
    &#93;,
    "establishes": &#91;
      "an exact block parametrization of all inherited linear terminal descent constraints",
      "full row rank of every forbidden Taylor-jet block in characteristic zero",
      "a triangular inverse from the declared pivot outputs",
      "compatibility with the quotient-coordinate determinant operator"
    &#93;
  },
  "top_blocks": {
    "P": {
      "free_dimension": 7,
      "source_dimension": 13,
      "terminal_multiplicity": 6,
      "weight": 15
    },
    "Q": {
      "free_dimension": 11,
      "source_dimension": 21,
      "terminal_multiplicity": 10,
      "weight": 25
    }
  },
  "totals": {
    "P": {
      "blocks": 76,
      "free_dimension": 533,
      "full_shear_coordinates": 4486,
      "inherited_linear_relations": 3900,
      "source_dimension": 586,
      "terminal_allowed_coordinates": 4433,
      "terminal_forbidden_dimension": 53
    },
    "Q": {
      "blocks": 126,
      "free_dimension": 1440,
      "full_shear_coordinates": 12476,
      "inherited_linear_relations": 10900,
      "source_dimension": 1576,
      "terminal_allowed_coordinates": 12340,
      "terminal_forbidden_dimension": 136
    },
    "blocks": 202,
    "free_dimension": 1973,
    "inherited_linear_relations": 14800
  }
}
</code></pre>

<a id="source-3d84642c02b15a3c"></a>

## `research-notes/lane8-f2-root-divisibility-20260804-v1/verify_f2_root_divisibility.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the F2 root-divisibility block parametrization.

The checker reconstructs the source rectangles and the denominator-five
shear directly.  It does not import the earlier support-window checker and
does not use a serialized coefficient matrix.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import comb, factorial
from pathlib import Path
from typing import Any


PACKET_DIR = Path(__file__).resolve().parent
REPO_ROOT = PACKET_DIR.parents&#91;1&#93;
DEFAULT_MANIFEST = PACKET_DIR / "block_manifest.json"


@dataclass(frozen=True)
class PairData:
    kind: str
    x_max: int
    y_max: int
    initial_weight_max: int
    terminal_weight_max: int


P_DATA = PairData("P", 15, 60, 15, 3)
Q_DATA = PairData("Q", 25, 100, 25, 5)


def ceil_div(numerator: int, denominator: int) -&gt; int:
    assert denominator &gt; 0
    return -((-numerator) // denominator)


def sha256(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_support(data: PairData) -&gt; set&#91;tuple&#91;int, int&#93;&#93;:
    """The exact source rectangle below the initial (5,-1) face."""
    return {
        (i, j)
        for i in range(data.x_max + 1)
        for j in range(data.y_max + 1)
        if 5 * i - j &lt;= data.initial_weight_max
    }


def source_blocks(data: PairData) -&gt; dict&#91;int, list&#91;int&#93;&#93;:
    blocks: dict&#91;int, list&#91;int&#93;&#93; = defaultdict(list)
    for i, j in source_support(data):
        blocks&#91;5 * i - j&#93;.append(j)
    return {weight: sorted(js) for weight, js in sorted(blocks.items())}


def terminal_multiplicity(
    *, weight: int, terminal_weight_max: int, source_max_degree: int
) -&gt; int:
    raw = ceil_div(5 * weight - terminal_weight_max, 12)
    return max(0, min(source_max_degree + 1, raw))


def block_record(data: PairData, weight: int, source_js: list&#91;int&#93;) -&gt; dict&#91;str, Any&#93;:
    assert source_js == list(range(source_js&#91;0&#93;, source_js&#91;-1&#93; + 1, 5))
    dimension = len(source_js)
    multiplicity = terminal_multiplicity(
        weight=weight,
        terminal_weight_max=data.terminal_weight_max,
        source_max_degree=source_js&#91;-1&#93;,
    )
    assert multiplicity &lt;= dimension
    free = dimension - multiplicity
    pivot_last = multiplicity + free - 1
    return {
        "kind": data.kind,
        "weight": weight,
        "source_min_degree": source_js&#91;0&#93;,
        "source_max_degree": source_js&#91;-1&#93;,
        "source_step": 5,
        "source_dimension": dimension,
        "terminal_multiplicity": multiplicity,
        "free_dimension": free,
        "free_variable": {
            "symbol_pattern": f"e_{data.kind}_{weight}_{{k}}",
            "index_interval": &#91;0, free - 1&#93;,
        },
        "forbidden_output_interval": (
            None if multiplicity == 0 else &#91;0, multiplicity - 1&#93;
        ),
        "pivot_output_interval": &#91;multiplicity, pivot_last&#93;,
        "derived_output_interval": (
            None if source_js&#91;-1&#93; &lt; dimension else &#91;dimension, source_js&#91;-1&#93;&#93;
        ),
    }


def all_block_records(data: PairData) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        block_record(data, weight, js)
        for weight, js in source_blocks(data).items()
    &#93;


def shear_supports(
    data: PairData,
) -&gt; tuple&#91;set&#91;tuple&#91;int, int&#93;&#93;, set&#91;tuple&#91;int, int&#93;&#93;, set&#91;tuple&#91;int, int&#93;&#93;&#93;:
    """Return full, allowed, and forbidden output coordinates (w,J)."""
    full: set&#91;tuple&#91;int, int&#93;&#93; = set()
    allowed: set&#91;tuple&#91;int, int&#93;&#93; = set()
    forbidden: set&#91;tuple&#91;int, int&#93;&#93; = set()
    for i, j in source_support(data):
        weight = 5 * i - j
        for output_degree in range(j + 1):
            coordinate = (weight, output_degree)
            full.add(coordinate)
            terminal_weight = 5 * weight - 12 * output_degree
            if terminal_weight &lt;= data.terminal_weight_max:
                allowed.add(coordinate)
            else:
                forbidden.add(coordinate)
    assert full == allowed | forbidden
    assert not allowed &amp; forbidden
    return full, allowed, forbidden


def exact_rank(matrix: list&#91;list&#91;int&#93;&#93;) -&gt; int:
    if not matrix:
        return 0
    rows = &#91;&#91;Fraction(entry) for entry in row&#93; for row in matrix&#93;
    row_count = len(rows)
    column_count = len(rows&#91;0&#93;)
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, row_count) if rows&#91;row&#93;&#91;column&#93;),
            None,
        )
        if pivot is None:
            continue
        rows&#91;rank&#93;, rows&#91;pivot&#93; = rows&#91;pivot&#93;, rows&#91;rank&#93;
        pivot_value = rows&#91;rank&#93;&#91;column&#93;
        rows&#91;rank&#93; = &#91;entry / pivot_value for entry in rows&#91;rank&#93;&#93;
        for row in range(rank + 1, row_count):
            if not rows&#91;row&#93;&#91;column&#93;:
                continue
            scale = rows&#91;row&#93;&#91;column&#93;
            rows&#91;row&#93; = &#91;
                rows&#91;row&#93;&#91;index&#93; - scale * rows&#91;rank&#93;&#91;index&#93;
                for index in range(column_count)
            &#93;
        rank += 1
        if rank == row_count:
            break
    return rank


def determinant(matrix: list&#91;list&#91;int&#93;&#93;) -&gt; Fraction:
    if not matrix:
        return Fraction(1)
    rows = &#91;&#91;Fraction(entry) for entry in row&#93; for row in matrix&#93;
    size = len(rows)
    assert all(len(row) == size for row in rows)
    value = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows&#91;row&#93;&#91;column&#93;),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows&#91;column&#93;, rows&#91;pivot&#93; = rows&#91;pivot&#93;, rows&#91;column&#93;
            value *= -1
        pivot_value = rows&#91;column&#93;&#91;column&#93;
        value *= pivot_value
        for row in range(column + 1, size):
            if not rows&#91;row&#93;&#91;column&#93;:
                continue
            scale = rows&#91;row&#93;&#91;column&#93; / pivot_value
            for index in range(column + 1, size):
                rows&#91;row&#93;&#91;index&#93; -= scale * rows&#91;column&#93;&#91;index&#93;
    return value


def vandermonde_value(degrees: list&#91;int&#93;) -&gt; Fraction:
    value = Fraction(1)
    for right in range(len(degrees)):
        for left in range(right):
            value *= degrees&#91;right&#93; - degrees&#91;left&#93;
    for order in range(len(degrees)):
        value /= factorial(order)
    return value


def shifted_coefficient(
    *, source_min_degree: int, power: int, output_degree: int
) -&gt; int:
    """Coefficient of T^output_degree in

    (T+1)^source_min_degree * ((T+1)^5-1)^power.
    """
    value = 0
    for exponent in range(power + 1):
        coefficient = comb(power, exponent) * (-1) ** (power - exponent)
        y_degree = source_min_degree + 5 * exponent
        if output_degree &lt;= y_degree:
            value += coefficient * comb(y_degree, output_degree)
    return value


def verify_block(data: PairData, record: dict&#91;str, Any&#93;) -&gt; dict&#91;str, int&#93;:
    weight = record&#91;"weight"&#93;
    source_js = source_blocks(data)&#91;weight&#93;
    multiplicity = record&#91;"terminal_multiplicity"&#93;
    free = record&#91;"free_dimension"&#93;

    forbidden_matrix = &#91;
        &#91;comb(degree, order) for degree in source_js&#93;
        for order in range(multiplicity)
    &#93;
    assert exact_rank(forbidden_matrix) == multiplicity

    witness_columns = source_js&#91;:multiplicity&#93;
    witness = &#91;row&#91;:multiplicity&#93; for row in forbidden_matrix&#93;
    witness_determinant = determinant(witness)
    assert witness_determinant == vandermonde_value(witness_columns)
    assert witness_determinant != 0

    pivot_matrix = &#91;
        &#91;
            shifted_coefficient(
                source_min_degree=source_js&#91;0&#93;,
                power=multiplicity + column,
                output_degree=multiplicity + row,
            )
            for column in range(free)
        &#93;
        for row in range(free)
    &#93;
    for row in range(free):
        for column in range(free):
            if row &lt; column:
                assert pivot_matrix&#91;row&#93;&#91;column&#93; == 0
            if row == column:
                assert pivot_matrix&#91;row&#93;&#91;column&#93; == 5 ** (multiplicity + column)
    assert exact_rank(pivot_matrix) == free

    return {
        "forbidden_rank": multiplicity,
        "free_rank": free,
        "vandermonde_witnesses": int(multiplicity &gt; 0),
    }


def terminal_layers(data: PairData) -&gt; dict&#91;int, list&#91;int&#93;&#93;:
    _, allowed, _ = shear_supports(data)
    layers: dict&#91;int, set&#91;int&#93;&#93; = defaultdict(set)
    for weight, output_degree in allowed:
        order = data.terminal_weight_max - (5 * weight - 12 * output_degree)
        layers&#91;order&#93;.add(output_degree)
    return {order: sorted(exponents) for order, exponents in sorted(layers.items())}


def quotient_operator_coefficient(
    *,
    p_order: int,
    q_order: int,
    p_residue: int,
    q_residue: int,
    p_u_degree: int,
    q_u_degree: int,
) -&gt; int:
    return (3 - p_order) * (q_residue + 5 * q_u_degree) + (
        q_order - 5
    ) * (p_residue + 5 * p_u_degree)


def verify_quotient_operator() -&gt; dict&#91;str, int&#93;:
    """Check the quotient formula on every supported monomial.

    Each P monomial is paired with the two leading Q monomials, and each Q
    monomial with the two leading P monomials.  This exercises every actual
    order and exponent; the equality checked is the universal monomial
    identity used in the proof note.
    """
    p_layers = terminal_layers(P_DATA)
    q_layers = terminal_layers(Q_DATA)
    p_leading = p_layers&#91;0&#93;
    q_leading = q_layers&#91;0&#93;
    checked = 0

    def check_pair(p_order: int, p_exp: int, q_order: int, q_exp: int) -&gt; None:
        nonlocal checked
        p_residue = p_exp % 5
        q_residue = q_exp % 5
        p_u_degree = (p_exp - p_residue) // 5
        q_u_degree = (q_exp - q_residue) // 5
        direct = (3 - p_order) * q_exp + (q_order - 5) * p_exp
        quotient = quotient_operator_coefficient(
            p_order=p_order,
            q_order=q_order,
            p_residue=p_residue,
            q_residue=q_residue,
            p_u_degree=p_u_degree,
            q_u_degree=q_u_degree,
        )
        assert direct == quotient
        if direct:
            assert p_exp + q_exp - 1 &gt;= 0
        checked += 1

    for p_order, p_exponents in p_layers.items():
        for p_exp in p_exponents:
            for q_exp in q_leading:
                check_pair(p_order, p_exp, 0, q_exp)
    for q_order, q_exponents in q_layers.items():
        for q_exp in q_exponents:
            for p_exp in p_leading:
                check_pair(0, p_exp, q_order, q_exp)

    return {
        "supported_monomial_pair_checks": checked,
        "P_nonempty_terminal_layers": len(p_layers),
        "Q_nonempty_terminal_layers": len(q_layers),
    }


def expected_manifest() -&gt; dict&#91;str, Any&#93;:
    p_blocks = all_block_records(P_DATA)
    q_blocks = all_block_records(Q_DATA)
    return {
        "schema_version": 1,
        "packet_id": "lane8-f2-root-divisibility-20260804-v1",
        "coefficient_ring": (
            "K&#91;lambda,c,lambda^{-1}&#93;/(c-lambda^5), char(K)=0"
        ),
        "coordinates": {
            "source_weight": "w=5*i-j",
            "source_block": "C_w(Y)=Y^j0 H_w(Y^5)",
            "transport": "D_w(T)=C_w(T+lambda)",
            "terminal_test": "5*w-12*J&lt;=t; t=3 for P and t=5 for Q",
        },
        "formulas": {
            "terminal_multiplicity": (
                "F_w=max(0,min(jmax+1,ceil((5*w-t)/12)))"
            ),
            "root_divisibility": "H_w(u)=(u-c)^F_w E_w(u)",
            "free_degree_bound": "deg(E_w)&lt;n_w-F_w",
            "triangular_basis": (
                "C_w(Y)=Y^j0 sum_k e_w,k (Y^5-c)^(F_w+k)"
            ),
            "generic_diagonal": (
                "lambda^j0*(5*lambda^4)^(F_w+k)"
            ),
            "quotient_determinant_operator": (
                "(3-r)*a*(beta*b+5*u*b')+"
                "(s-5)*(alpha*a+5*u*a')*b"
            ),
        },
        "totals": {
            "P": {
                "blocks": 76,
                "source_dimension": 586,
                "terminal_forbidden_dimension": 53,
                "free_dimension": 533,
                "full_shear_coordinates": 4486,
                "terminal_allowed_coordinates": 4433,
                "inherited_linear_relations": 3900,
            },
            "Q": {
                "blocks": 126,
                "source_dimension": 1576,
                "terminal_forbidden_dimension": 136,
                "free_dimension": 1440,
                "full_shear_coordinates": 12476,
                "terminal_allowed_coordinates": 12340,
                "inherited_linear_relations": 10900,
            },
            "blocks": 202,
            "free_dimension": 1973,
            "inherited_linear_relations": 14800,
        },
        "top_blocks": {
            "P": {
                "weight": 15,
                "source_dimension": 13,
                "terminal_multiplicity": 6,
                "free_dimension": 7,
            },
            "Q": {
                "weight": 25,
                "source_dimension": 21,
                "terminal_multiplicity": 10,
                "free_dimension": 11,
            },
        },
        "blocks": {"P": p_blocks, "Q": q_blocks},
        "provenance": &#91;
            {
                "path": (
                    "research-notes/lane8-f2-support-determinacy-audit-"
                    "20260803-v1/README.md"
                ),
                "sha256": (
                    "38c3c52d8deeed6036f0739da5837b98e6eac29b22f82c33f34931ca9c60da84"
                ),
                "role": "prior exact transport and support audit",
            },
            {
                "path": (
                    "research-notes/lane8-f2-support-determinacy-audit-"
                    "20260803-v1/verify_lane8_f2_support_determinacy_audit.py"
                ),
                "sha256": (
                    "c5c5dfe96f3317795cbbc506a0ff4a7d6f14a5c84111778cdd76dc5914e647ab"
                ),
                "role": "prior independent support/rank checker",
            },
            {
                "path": (
                    "manuscripts/06-plane-boundary/computational-supplement/"
                    "terminal-boundary/F2_degree125_boundary_seed.md"
                ),
                "sha256": (
                    "63fb30b6de06df86c9c87e968d4d72e58b9218134a9eaa8cbce978b78901eb5e"
                ),
                "role": "F2 source rectangles, shear, and common-power face",
            },
            {
                "path": (
                    "/path/to/versioned-artifact"
                    "materials-v3-20260803a/06-f2-support-windows-order-"
                    "520-2026-08-03-v1.zip"
                ),
                "sha256": (
                    "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64"
                ),
                "role": "maintained support-window generator and exact outputs",
            },
        &#93;,
        "scope": {
            "establishes": &#91;
                "an exact block parametrization of all inherited linear terminal descent constraints",
                "full row rank of every forbidden Taylor-jet block in characteristic zero",
                "a triangular inverse from the declared pivot outputs",
                "compatibility with the quotient-coordinate determinant operator",
            &#93;,
            "does_not_establish": &#91;
                "the nonlinear common-power or exact-double-root locus",
                "the determinant equations or their solution set",
                "actual post-shear support uniqueness or its stratification",
                "a gauge equivalence setting lambda to one",
                "an adjacent-chart attachment or a plane Jacobian-conjecture conclusion",
            &#93;,
        },
    }


def verify_manifest(manifest: dict&#91;str, Any&#93;) -&gt; dict&#91;str, Any&#93;:
    expected = expected_manifest()
    assert manifest == expected

    summary: dict&#91;str, Any&#93; = {}
    total_witnesses = 0
    for data in (P_DATA, Q_DATA):
        records = manifest&#91;"blocks"&#93;&#91;data.kind&#93;
        block_results = &#91;verify_block(data, record) for record in records&#93;
        full, allowed, forbidden = shear_supports(data)
        source_dimension = len(source_support(data))
        forbidden_dimension = sum(
            result&#91;"forbidden_rank"&#93; for result in block_results
        )
        free_dimension = sum(result&#91;"free_rank"&#93; for result in block_results)
        total_witnesses += sum(
            result&#91;"vandermonde_witnesses"&#93; for result in block_results
        )
        expected_totals = manifest&#91;"totals"&#93;&#91;data.kind&#93;
        assert len(records) == expected_totals&#91;"blocks"&#93;
        assert source_dimension == expected_totals&#91;"source_dimension"&#93;
        assert forbidden_dimension == expected_totals&#91;"terminal_forbidden_dimension"&#93;
        assert free_dimension == expected_totals&#91;"free_dimension"&#93;
        assert len(full) == expected_totals&#91;"full_shear_coordinates"&#93;
        assert len(allowed) == expected_totals&#91;"terminal_allowed_coordinates"&#93;
        assert len(forbidden) == forbidden_dimension
        assert len(allowed) - free_dimension == expected_totals&#91;
            "inherited_linear_relations"
        &#93;
        summary&#91;data.kind&#93; = expected_totals

    for provenance in manifest&#91;"provenance"&#93;:
        path = Path(provenance&#91;"path"&#93;)
        if not path.is_absolute():
            path = REPO_ROOT / path
        if path.exists():
            assert sha256(path) == provenance&#91;"sha256"&#93;

    quotient = verify_quotient_operator()
    summary.update(
        {
            "verified": True,
            "blocks": manifest&#91;"totals"&#93;&#91;"blocks"&#93;,
            "free_dimension": manifest&#91;"totals"&#93;&#91;"free_dimension"&#93;,
            "vandermonde_witness_blocks": total_witnesses,
            "top_blocks": manifest&#91;"top_blocks"&#93;,
            "quotient_operator": quotient,
            "scope": manifest&#91;"scope"&#93;,
        }
    )
    return summary


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument(
        "--write-manifest",
        type=Path,
        help="write the reconstructed manifest to a new path before checking it",
    )
    parser.add_argument("--json", type=Path, help="write summary to a new path")
    args = parser.parse_args()

    if args.write_manifest:
        if args.write_manifest.exists():
            raise FileExistsError(f"refusing to overwrite {args.write_manifest}")
        args.write_manifest.parent.mkdir(parents=True, exist_ok=True)
        args.write_manifest.write_text(
            json.dumps(expected_manifest(), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        manifest_path = args.write_manifest
    else:
        manifest_path = args.manifest

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    summary = verify_manifest(manifest)
    rendered = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.json:
        if args.json.exists():
            raise FileExistsError(f"refusing to overwrite {args.json}")
        args.json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-c897ba0ee0d3d561"></a>

## `research-notes/lane8-f2-support-determinacy-audit-20260803-v1/README.md`

<pre><code class="language-markdown">
&gt; **Current status (4 August 2026).** This is a historical pre-recovery audit. Its statement that inherited linear relations were not supplied is superseded by research-notes/lane8-f2-root-divisibility-20260804-v1/README.md, which gives exact 202-block coordinates and a triangular inverse. It is retained here only for its distinction among complete corner chains, maximal support envelopes, actual transported supports, convex polygons, and normal windows. Do not use its old task-readiness conclusions.

# Lane 8 F2 support-determinacy audit

Date: 2026-08-03

Scope: exact audit and replacement-task contract; no claim of support uniqueness.

## Conclusion

The advertised Lane 8 task does **not** currently have a supplied finite
candidate-generation algorithm for exact post-shear Newton supports.

The cited 2017 complete-chain algorithms do give a finite generator for
**corner chains**. They do not generate coefficient supports, support
polygons after a shear, inherited coefficient relations, or cancellation
branches. For F2 they have already produced the one-edge complete corner
chain

\&#91;
 ((5,20),(1,0)),\qquad (7\mathbin{\wr}5,2),
\&#93;

whose final geometric corner is \((7/5,2)\). Thus there is no ungenerated
intermediate *corner* in this chain. The v7c phrase "intervening normalized
support chain" denotes a new coefficient-level object and is not the output
type of Algorithms 2--8 in the cited paper.

The strongest task supported by the current F2 seed and maximal windows is to
construct the exact inherited coefficient-relation packet for the one
denominator-five shear. Exact-support uniqueness should remain non-ready
until that packet and a support-stratification contract are supplied.

## Material inspected

The audit read and compared:

- `private-source/research-handoff-v7c/lanes/plane-newton-queue-terminal-certificates.md`;
- `private-source/research-handoff-v7c/README.md`;
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md`;
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_boundary_gluing_program.md`;
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py`;
- `manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi_reduction.md` and its named exact verifiers;
- `research-notes/lane89-mathematical-recovery-20260803-v1/README.md` and `evidence.json`;
- the complete `scripts/f2_support_windows.py` and support-model report in the
  exact bundle with SHA-256
  `a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64`;
- Guccione--Guccione--Horruitiner--Valqui, *Some algorithms related to the
  Jacobian Conjecture*, arXiv:1708.07936v1, including Definitions 2.1, 2.2,
  2.12, 2.15, 2.19, and 2.25; Algorithms 2--8; Theorem 2.20; and the F2 rows
  in Sections 5--6. The downloaded single-file TeX source had SHA-256
  `2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e`.

The supplied support generator was replayed in a fresh temporary directory.
It reproduced 4,433 P positions, 12,340 Q positions, 981 and 1,663 nonempty
normal layers, and 2,681 nonempty determinant-output layers ending at order
2,716.

## What the 2017 finite algorithm actually generates

The paper represents a corner by \((a\mathbin{\wr}l,b)\), with geometric
realization \((a/l,b)\). Starting from a valid edge
\(C_0=(\mathcal A,\mathcal A')\):

1. Algorithm 3 enumerates the finitely many generated corners. Its
   non-simple branch loops over the explicit integer interval
   \(b'+1\le b_1\le\gamma_{\max}\); its simple branch has at most one
   generated corner.
2. Algorithm 4 enumerates child edges using finite integer ranges for
   \(\mu\) and \(1\le j\le\lfloor b_1/\operatorname{gap}(\rho_1,l_1)\rfloor\).
3. Algorithm 5 separates child edges from final generated corners.
4. Algorithm 6 performs breadth-first extension, with the exact length bound

   \&#91;
   \operatorname{length}(CH)\le
   \Omega\!\left(\gcd\!\left(b,{b-b'\over\rho}\right)\right)+1,
   \&#93;

   where \(\Omega\) counts prime factors with multiplicity and
   \((\rho,\sigma)=\operatorname{dir}(A-A')\).
5. Algorithm 7 tests the divisibility conditions of Definition 2.25, and
   Algorithm 8 runs the preceding finite procedures under a bound
   \(v_{11}(A_0)\le M\).

For F2, \((\rho,\sigma)=(5,-1)\), \(b=20\), and \(b'=0\), so Algorithm 6's
general bound is

\&#91;
 \Omega(\gcd(20,20/5))+1=\Omega(4)+1=3.
\&#93;

The published admissible-chain table is stronger than that general bound:
F2 is listed among the length-one chains with final corner
\((7\mathbin{\wr}5,2)\). Choosing the family parameter that gives
\((m,n)=(3,5)\) yields maximum degree 125.

Nothing in these algorithms has a coefficient ring, a post-shear support
set, a determinant ideal, or a branch on vanishing transformed
coefficients. They therefore cannot be cited as the missing support-polygon
candidate generator.

## The three objects currently conflated

The current Lane 8 wording treats three distinct finite objects as if they
were one:

1. **Complete corner chain.** Already fixed for F2 and of length one.
2. **Maximal independent support envelope.** Already generated by the
   support-window script. It is an outer bound obtained by allowing every
   terminal-admissible post-shear coefficient independently.
3. **Actual transported coefficient support.** Unknown. It is a point of a
   proper linear descent subspace, further cut by the common-power face and
   the determinant equations. Exact Newton polygons and actual normal
   windows depend on which coordinates vanish on this constructible locus.

If "support polygon" means only the convex hull of the maximal envelope, it
is already computed and unique. If it means the convex hull of an actual
solution, or the complete set of its nonzero coefficients, a candidate
generator needs the inherited relation ideal and explicit zero/nonzero
stratification rules. V7c does not choose among these meanings.

## Exact missing linear descent data

The missing relations can be written without solving the nonlinear Keller
system. Let \(c_{i,j}\) be a source coefficient and apply

\&#91;
 y\longmapsto y+\lambda x^{-1/5},\qquad \lambda\ne0.
\&#93;

For a fixed initial weight \(w=5i-j\), write the coefficient of
\(x^{(w+J)/5}y^J\) after the shear as \(d_{w,J}\). Then

\&#91;
 d_{w,J}=
 \sum_{\substack{(i,j)\text{ in the source envelope}\\5i-j=w,\ j\ge J}}
 \binom jJ\lambda^{j-J}c_{i,j}.
\tag{1}
\&#93;

The source envelopes are

\&#91;
\begin{aligned}
P:&amp;\quad 0\le i\le15,\ 0\le j\le60,\ 5i-j\le15,\\
Q:&amp;\quad 0\le i\le25,\ 0\le j\le100,\ 5i-j\le25.
\end{aligned}
\&#93;

They contain 586 and 1,576 coefficient positions. Their full shear images
have 4,486 and 12,476 positions. Imposing the terminal half-spaces

\&#91;
5(w+J)-17J\le3\quad(P),\qquad
5(w+J)-17J\le5\quad(Q)
\&#93;

sets 53 and 136 full-envelope coordinates to zero and leaves the familiar
4,433 and 12,340 maximal positions.

Over \(K(\lambda)\), \(\lambda\ne0\), the forbidden-coordinate matrices
have ranks 53 and 136. Consequently the linear transported loci inside the
maximal allowed coordinate spaces have dimensions

\&#91;
586-53=533\quad(P),\qquad 1576-136=1440\quad(Q).
\&#93;

Thus the independent-coordinate enlargement omits

\&#91;
(4433-533)+(12340-1440)=3900+10900=\boxed{14800}
\&#93;

independent linear descent relations. This count precedes, and therefore
does not include, additional common-power, exact-double-root, determinant,
normalization, or required-nonzero constraints.

The rank is independent of the chosen nonzero \(\lambda\): each transport
block has entries \(\binom jJ\lambda^{j-J}\), obtained from the
\(\lambda=1\) block by invertible row and column scalings. The checker below
computes the exact \(\lambda=1\) ranks block by block.

## Strongest genuinely startable replacement task

### Ready task L8-T1R — inherited F2 coefficient-relation packet

**Inputs.** The F2 corner data, the two source envelopes above, the exact
shear (1), the terminal half-spaces, the common-power leading face with its
distinguished nonzero double root, and the normalized determinant equation.

**Deliverable.** Produce one self-contained finite coefficient packet that:

1. declares every source coefficient and every post-shear coefficient;
2. exports equation (1) block by block, with the 53 P and 136 Q forbidden
   terminal coordinates explicitly set to zero;
3. eliminates the source coefficients, or exports an equivalent
   presentation, to give all inherited linear relations among the 4,433 P
   and 12,340 Q allowed coordinates;
4. adds the common-power, exact-double-root, determinant, normalization, and
   required-nonzero equations and localization factors;
5. states whether \(\lambda\) is retained, passed to a finite cover, or set
   to one by a proved gauge equivalence;
6. proves the forward and inverse correspondence between the declared
   source-pair locus and the transported constructible locus; and
7. supplies a machine-readable variable order, equation manifest, checksums,
   and a checker that reconstructs every matrix and equation.

This task is finite, begins directly from the supplied formulas, and creates
the actual input required by support determinacy. It does not require
solving the resulting nonlinear constructible system.

### Inputs still needed before full support uniqueness enumeration is ready

After L8-T1R, a separate candidate-generation contract must specify:

1. whether candidates are full nonzero support sets, convex Newton polygons,
   or only two-point normal-window intervals;
2. the required nonzero vertices in every chart and every allowed
   normalization complement;
3. the equivalence relation generated by root choice, source/target scaling,
   and complete-chain recharting;
4. an exhaustive finite stratification rule: for example, enumerate convex
   hulls from the finite allowed lattice, impose zero outside each hull,
   invert its vertices, and decide nonemptiness after saturation by all open
   factors; and
5. a proof that every actual F2 pair lands in one enumerated stratum and that
   every discarded stratum is empty.

Without these items, the current request to "prove uniqueness, or give all
finite alternatives" supplies tests for a proposed support but no declared
generator of all proposals.

## Recommended wording

### Lane 8 live problem

&gt; Construct the exact inherited coefficient-relation system for the
&gt; denominator-five F2 shear inside the terminal half-space. Use it to define
&gt; a finite constructible stratification of possible actual post-shear Newton
&gt; polygons and normal windows. Support uniqueness is the subsequent task,
&gt; not a current input-ready computation.

### Lane 8 ready-task heading and limit

&gt; **Ready task L8-T1 — inherited coefficient-relation packet for F2.**
&gt; Export and verify the complete source-to-sheared coefficient map, terminal
&gt; vanishing equations, inherited relations, common-power face, determinant
&gt; equations, normalizations, and localization factors.

&gt; **Non-ready follow-up — actual support determinacy.** Enumerate and decide
&gt; all exact support strata only after L8-T1 supplies the relation packet and a
&gt; precise candidate-equivalence contract.

### Portfolio row

- **Useful next work:** Export the exact inherited F2 coefficient relations
  for the denominator-five shear.
- **Readiness:** **Task-ready:** finite coefficient-transport packet; actual
  support uniqueness remains blocked on that packet and a support-stratification
  contract.

## Checker

Run:

```bash
uv run python \
  research-notes/lane8-f2-support-determinacy-audit-20260803-v1/verify_lane8_f2_support_determinacy_audit.py \
  --full \
  --json /new/versioned-run/summary.json
```

The checker is self-contained and refuses to overwrite its optional JSON
output. It verifies the two edge directions, the Algorithm 6 length bound,
source/shear/terminal support counts, forbidden-block ranks, the
14,800-relation lower bound, all normal layer counts, C5 characters, and the
2,681 determinant-output layers.
</code></pre>

<a id="source-08d38befa366c56b"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md`

<pre><code class="language-markdown">
# Direct terminal closure for the Lane 8 Newton roots

## 1. Scope and theorem boundary

Work in characteristic zero. The imported Newton reduction leaves two
normalized support polygons after the common degree-`21` lower face has been
selected. Call them the **truncated root** and the **full root**. This note
proves the following relative statement.

### Theorem 1 — Lane 8 closure relative to explicit imports

Assume:

1. the published below-`125` reduction routes every relevant plane Keller pair
   to one of the two displayed normalized `(8,28)` supports;
2. the common face belongs to the exact quintic orbit recorded in the Lane 8
   packet; and
3. the current Program 6 compact toric theorem is valid for its six displayed
   normalized obstruction polynomials.

Then both normalized support loci are empty over an algebraic closure of the
coefficient field. Consequently, using the imported reduction, no
characteristic-zero plane Keller counterexample has maximum coordinate degree
strictly below `125`.

The new work here is the complete raw-support reconstruction through the
necessary layer-eight obstruction, the complement ledger, proof that the
normalization loses no point of that early-layer exact-support locus, and
coefficientwise attachment of the resulting full-root projection to the
six-polynomial toric terminal. The three assumptions above are not reproved.

## 2. Common lower face and coefficient field

Let

\&#91;
K_0=\mathbf Q&#91;u&#93;/(m(u)),\qquad
m(u)=u^5-u^4+3u^3+3u^2+26.
\&#93;

The replay verifies that the reduction of `m` modulo `67` is irreducible by a
Rabin test. Since `m` is monic and primitive, this is an irreducibility witness
over \(\mathbf Q\).

For the valuation

\&#91;
\nu(x^a y^b)=-2a+b,
\&#93;
put \(z=xy^2\). Both support roots have initial forms

\&#91;
P_0=xp(z),\qquad Q_0=x^2yq(z),
\&#93;
with \(\deg p=7\), \(\deg q=10\). Direct differentiation gives

\&#91;
&#91;P_0,Q_0&#93;
=x^2\bigl(pq+2zpq'-3zp'q\bigr).
\&#93;

Hence the normalized bracket condition forces

\&#91;
pq+2zpq'-3zp'q=1. \tag{2.1}
\&#93;

The exact relation fixture reconstructs all coefficients of `p` and `q` in
\(K_0\). The replay checks all eighteen coefficients of (2.1), not merely a
numerical embedding.

## 3. Raw support and triangular layer equation

Set

\&#91;
t=y,\qquad z=xy^2,
\&#93;

and write

\&#91;
P=t^{-2}A(z,t),\qquad Q=t^{-3}B(z,t).
\&#93;

Because \(\det \partial(z,t)/\partial(x,y)=t^2\), the equation
\(&#91;P,Q&#93;=x^2\) becomes

\&#91;
2AB_z-3A_zB+t(A_zB_t-A_tB_z)=z^2. \tag{3.1}
\&#93;

Write

\&#91;
A=\sum_{r\ge0}t^rA_r(z),\qquad
B=\sum_{r\ge0}t^rB_r(z).
\&#93;

The coefficient of \(t^r\) in the left side is

\&#91;
E_r=
\sum_{i+j=r}
\left((2-i)A_iB_j'+(j-3)A_i'B_j\right). \tag{3.2}
\&#93;

The terms involving the new pair \((A_r,B_r)\) form the fixed
\(K_0\)-linear map

\&#91;
\mathscr D_r(A_r,B_r)=
(2-r)A_rB_0'-3A_r'B_0
+2A_0B_r'+(r-3)A_0'B_r. \tag{3.3}
\&#93;

All remaining terms depend only on lower layers. Thus each stage consists of
exact linear algebra over the fixed field \(K_0\), followed by compatibility
polynomials in previously introduced kernel parameters.

For a monomial \(x^a y^b\), its deficiencies are

\&#91;
d_P(a,b)=b-2a+2,\qquad d_Q(a,b)=b-2a+3. \tag{3.4}
\&#93;

The replay generates every lattice point of the two polygons and sorts it by
(3.4). No archived layer matrix is an input.

## 4. Truncated root

The truncated support contains `25` possible `P` monomials and `47` possible
`Q` monomials. Its exact layer data are

| layer | source columns | target rows | rank | kernel dimension | nonzero compatibility equations |
|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 13 | 20 | 12 | 1 | 7 |
| 4 | 0 | 20 | 0 | 0 | 18 |
| 5 | 0 | 21 | 0 | 0 | 0 |

Choose kernel coordinates

\&#91;
X,Y,U,V,W,D
\&#93;

of weights

\&#91;
1,1,2,2,2,3.
\&#93;

The two coordinates `U,D` represent the two split origin vertices. The replay
checks that they do not occur in any compatibility equation. The effective
obstruction variables are therefore

\&#91;
X,Y,V,W
\&#93;

with weights \(1,1,2,2\).

There are fourteen monomials of weighted degree four:

\&#91;
\begin{gathered}
X^4,X^3Y,X^2Y^2,XY^3,Y^4,\\
X^2V,XYV,Y^2V,X^2W,XYW,Y^2W,V^2,VW,W^2.
\end{gathered}
\&#93;

Adjoin to the eighteen layer-four equations the seven layer-three equations
multiplied by `X` and by `Y`. The resulting `32 x 14` Macaulay matrix has rank
`14` over \(K_0\). Its independently reconstructed selected-minor digest is

```text
8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
```

Thus the obstruction ideal contains every weighted-degree-four monomial. In
particular

\&#91;
X^4,Y^4,V^2,W^2\in I,
\&#93;

so

\&#91;
X,Y,V,W\in\sqrt I. \tag{4.1}
\&#93;

The required top coefficients at `(8,16)` in `P` and `(12,24)` in `Q` are
positive-weight polynomials in these four variables and have no constant
term. Equation (4.1) therefore forces both top coefficients to vanish at
every geometric solution. Exactness of the truncated Newton polygons requires
both coefficients to be nonzero. This contradiction is independent of the
free origin-vertex coordinates `U,D`.

### Conclusion 4.2

The exact truncated-root constructible locus is empty. It is therefore a
terminal-empty queue node, not an open status item.

## 5. Full root through layer four

The full support contains `61` possible `P` monomials and `125` possible `Q`
monomials. The complete layer data are

| layer | source columns | target rows | rank | kernel dimension | nonzero compatibility equations |
|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 18 | 17 | 2 | 0 |
| 2 | 21 | 19 | 18 | 3 | 0 |
| 3 | 21 | 20 | 18 | 3 | 0 |
| 4 | 19 | 20 | 18 | 1 | 2 |
| 5 | 17 | 21 | 17 | 0 | 2 |
| 6 | 15 | 20 | 15 | 0 | 4 |
| 7 | 13 | 19 | 13 | 0 | 5 |
| 8 | 11 | 18 | 11 | 0 | 6 |

Use raw kernel coordinates

\&#91;
(t_{1,0},t_{1,1},U,t_{2,1},t_{2,2},D,t_{3,1},t_{3,2},t_{4,0})
\&#93;

of weights

\&#91;
(1,1,2,2,2,3,3,3,4). \tag{5.1}
\&#93;

Again `U,D` are the split origin-vertex parameters and do not occur in any
compatibility equation.

The two nonzero layer-four compatibility polynomials are scalar multiples of
one polynomial. After unit normalization, that polynomial is

\&#91;
L^2,
\qquad
L=t_{2,2}-\alpha t_{1,1}^2, \tag{5.2}
\&#93;

for an explicitly reconstructed nonzero \(\alpha\in K_0\).

### Scheme versus reduced support

The scheme cut out at layer four contains the double hyperplane

\&#91;
\operatorname{Spec}K_0&#91;\mathbf t&#93;/(L^2).
\&#93;

It is not replaced scheme-theoretically by \((L)\). For the theorem sought
here, however, the target statement is geometric emptiness, and

\&#91;
V(L^2)=V(L)
\&#93;

as sets over an algebraic closure. The queue therefore stores two separate
nodes:

1. the nonreduced square scheme, carrying the multiplicity information; and
2. its reduced support, used only for point-set routing.

No claim about equality of schemes is made.

## 6. Exact-support complements and normalization

On the reduced support \(L=0\), the required top-vertex coefficients become

\&#91;
&#91;P&#93;_{(8,16)}=c_Pt_{1,1}^2,
\qquad
&#91;Q&#93;_{(12,24)}=c_Qt_{1,1}^3, \tag{6.1}
\&#93;

where the replay verifies \(c_P,c_Q\in K_0^\times\).

Therefore the exhaustive split

\&#91;
V(L)=V(L,t_{1,1})\ \cup\ \bigl(V(L)\cap D(t_{1,1})\bigr) \tag{6.2}
\&#93;

has the following dispositions.

- On `t1_1=0`, both coefficients in (6.1) vanish, contradicting exact support.
  This closed child is empty.
- On `t1_1!=0`, normalization is legitimate.

The origin-vertex parameters `U,D` are also required nonzero by exactness of
the declared full support. Their zero loci are not points of the parent exact
root; equivalently, they are saturation factors defining that root. Since
neither variable enters a compatibility equation, no hidden equation branch
is lost by retaining them as free units.

The reconstruction stops at deficiency eight because the fifteen equations
already arise there. It therefore forgets `3` possible `P` coefficients and
`28` possible `Q` coefficients of higher deficiency, including the extra
full-support vertices `(0,8)` and `(0,12)`, of deficiencies `10` and `15`.
None of these coefficients is divided by or set to zero. Every full-support
Keller pair projects to the layer-through-eight necessary-condition locus, so
emptiness of this larger projection excludes every possible choice of the
forgotten coefficients.

Every linear solve before this normalization divides only by a fixed nonzero
element of \(K_0\). Thus no parameter-dependent denominator and no additional
closed child is introduced by Gaussian elimination.

### Weighted cross-section

On `t1_1!=0`, define

\&#91;
\begin{aligned}
U_*&amp;=U/t_{1,1}^2,&amp; D_*&amp;=D/t_{1,1}^3,\\
x&amp;=t_{1,0}/t_{1,1},&amp; a&amp;=t_{2,1}/t_{1,1}^2,\\
b&amp;=t_{3,1}/t_{1,1}^3,&amp; c&amp;=t_{3,2}/t_{1,1}^3,\\
d&amp;=t_{4,0}/t_{1,1}^4.
\end{aligned} \tag{6.3}
\&#93;

The inverse formulas are

\&#91;
\begin{aligned}
U&amp;=t_{1,1}^2U_*,&amp;D&amp;=t_{1,1}^3D_*,\\
t_{1,0}&amp;=t_{1,1}x,&amp;t_{2,1}&amp;=t_{1,1}^2a,\\
t_{2,2}&amp;=\alpha t_{1,1}^2,&amp;t_{3,1}&amp;=t_{1,1}^3b,\\
t_{3,2}&amp;=t_{1,1}^3c,&amp;t_{4,0}&amp;=t_{1,1}^4d.
\end{aligned} \tag{6.4}
\&#93;

The replay verifies that every compatibility polynomial is weighted
homogeneous of its layer number with respect to (5.1). Substitution of (6.4)
therefore factors a nonzero power of `t1_1` from each equation. Consequently,
on the open child, the **layer-through-eight necessary-condition locus** is
isomorphic to

\&#91;
(\mathbf G_m)^3_{U_*,D_*,t_{1,1}}
\times V(F_0,\ldots,F_{14})\subset
(\mathbf G_m)^3\times\mathbf A^5_{x,a,b,c,d}. \tag{6.5}
\&#93;

Every exact full-support solution maps to (6.5); equation (6.5) is not a
parameterization of the forgotten higher-deficiency coefficients. The
weight-one coordinate `t1_1` also makes the corresponding scaling action free;
no finite stabilizer or quotient-descent issue is hidden in the early-layer
cross-section.

## 7. Reconstruction of the fifteen equations

Continuing (3.2) through layer eight, substituting (6.3), and removing only
nonzero scalar duplicates gives

\&#91;
1,3,5,6
\&#93;

distinct equations of weights

\&#91;
5,6,7,8,
\&#93;

respectively. In the replay order these are

\&#91;
F_0,F_1,\ldots,F_{14}\in K_0&#91;x,a,b,c,d&#93;.
\&#93;

Their canonical JSON digest is

```text
d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883
```

which equals the public expected digest. The replay exports a separate digest,
weight, and term count for every `F_i`; these data are pinned in
`stage-manifest.json`.

Equation normalization at this stage divides only by fixed nonzero leading
coefficients in \(K_0\). It creates no geometric complement.

## 8. Direct compact-terminal attachment

Let

\&#91;
I_{15}=(F_0,\ldots,F_{14})
\&#93;

and

\&#91;
J_6=(F_4,F_6,F_8,F_9,F_{10},F_{11}). \tag{8.1}
\&#93;

The current Program 6 residue-provenance proposition identifies exactly these
zero-based indices. The independent replay selects the same six equations
from its reconstructed ordered list and obtains canonical digest

```text
e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a
```

Because the generators of `J6` are literally among the generators of `I15`,

\&#91;
J_6\subset I_{15}
\quad\Longrightarrow\quad
V(I_{15})\subset V(J_6). \tag{8.2}
\&#93;

The imported compact toric terminal theorem states

\&#91;
V(J_6)(\overline{K_0})=\varnothing. \tag{8.3}
\&#93;

Its recorded proof uses the good fiber `(p,u)=(2053,216)`, mixed volume `296`,
`344` proper toric faces (`270` monomial and `74` saturated-unit faces), and
invertibility of multiplication by `F4`, with determinant `682` modulo `2053`.
The five split-embedding determinant residues are

\&#91;
682,116,337,242,740,
\&#93;

with norm product `51` modulo `2053`.

Combining (8.2) and (8.3) gives

\&#91;
V(I_{15})(\overline{K_0})=\varnothing.
\&#93;

Together with (6.5), this proves that the open early-layer `t1_1!=0` child is
empty. The closed child was already empty by (6.1). Every full-support
completion projects to one of these children, so the full root is empty.

This also proves emptiness of the full layer-through-eight obstruction scheme
in which the layer-four equation is retained as `L^2`, rather than only the
corresponding reduced obstruction scheme. If that full finite-type coordinate
algebra over `K0` were nonzero, faithfully flat base change to `overline(K0)`
would remain nonzero, and a nonzero finite-type algebra over an algebraically
closed field has a maximal ideal. That would produce a geometric point on the
reduced full obstruction locus, contrary to the preceding emptiness. Hence
the full obstruction scheme is zero while the square multiplicity has still
been preserved in the manifest. The layer-four hypersurface `L^2=0` alone is
not claimed empty.

### What is and is not replayed here

The coefficientwise identity of the six selected equations is independently
replayed. The large toric matrices and face-saturation archive underlying
(8.3) are not bundled or independently regenerated here; (8.3) is an explicit
imported exact theorem.

## 9. Attempted Lane 9 bridge

The stored adjacent-chart layer-five-through-seven system has an exact
terminal certificate. To use it as a child of the full root, however, one
needs a covering rechart theorem.

For the proposed bare shear

\&#91;
Y'=Y+\lambda X^{-k}
\&#93;

in lower-face coordinates \(t=Y\), \(z=XY^2\), one has \(X=z/t^2\), hence

\&#91;
Y'=t+\lambda(t^2/z)^k=t(1+h),
\qquad
h=\lambda t^{2k-1}z^{-k}, \tag{9.1}
\&#93;

and

\&#91;
z'=X(Y')^2=z(1+h)^2. \tag{9.2}
\&#93;

For `k=4`, the first nonzero normal term has order

\&#91;
2k-1=7. \tag{9.3}
\&#93;

A filtration-preserving conjugacy inducing an invertible associated-graded map
cannot move a nonzero leading symbol from order seven to order four. Thus the
bare `k=4` shear does not identify the one-dimensional layer-four residual
with the stored transformed system.

This is a useful negative Lane 9 lemma, not a covering theorem. The queue
therefore records the adjacent terminal and a noncovering candidate edge, but
no full-root closure path uses that edge.

The weaker theorem sufficient for Lane 8 is instead the direct attachment in
Section 8. It closes the full root without any chart transition.

## 10. Complement and denominator ledger

| Stage | Factor or division | Type | Complement disposition |
|---|---|---|---|
| Face reconstruction | displayed integer relation coefficients and `1+2d` | fixed nonzero scalars | no geometric complement |
| Layer solves `1`--`8` | RREF pivots | fixed nonzero elements of `K0` | no geometric complement |
| Exact support | `U,D` | saturation factors defining the declared origin vertices | zero loci lower the support and are outside the exact-root parent |
| Higher-deficiency coefficients | none | forgotten by the necessary-condition projection | both zero and nonzero values are covered; no localization occurs |
| Layer-four support | `L^2` versus `L` | nilpotent scheme structure | square retained; radical used only for geometric emptiness |
| Normalization | `t1_1` | geometric localization | closed child `t1_1=0` is empty by the two top vertices |
| Equation normalization | one coefficient of each nonzero equation | fixed nonzero element of `K0` | no geometric complement |
| Toric projection | none | generator deletion/relaxation | no complement; inclusion direction is (8.2) |
| Stored adjacent terminal | `D(x)=0` or `D(x)!=0` | internal stored split | both stored children certified, but no covering edge from the full root |
| Bare wall shear | Laurent factor `z^-4` | adjacent Laurent chart | not used in the direct Lane 8 proof |

Thus every parameter-dependent division in the direct full-root path has an
explicit complementary child, and that child is independently eliminated.

## 11. Below-`125` corollary

The literature import recorded in the Lane 8 packet has the following logical
form, after exchanging coordinates when necessary and passing to an algebraic
closure:

1. GGHV Theorem 2.1 leaves the degree pair `(72,108)` below `125`;
2. the `(9,27)` complete-chain case is excluded by the imported Proposition
   4.1/Corollary 5.7 route; and
3. GGHV Proposition 4.3 sends the remaining `(8,28)` case to exactly the
   truncated or full normalized support used above.

Sections 4 and 8 eliminate those two roots. Therefore the imported reduction
has no surviving child.

### Corollary 11.1

Relative to the cited GGHV reduction and the current Program 6 exact terminal
theorem, there is no characteristic-zero plane Keller counterexample with

\&#91;
\max(\deg P,\deg Q)&lt;125.
\&#93;

Polynomial invertibility descends along the faithfully flat extension from a
characteristic-zero base field to its algebraic closure: an isomorphism of the
base-changed affine coordinate algebras, together with its unique inverse, is
fpqc descent data. Thus it is sufficient to exclude the normalized loci over
algebraic closures.

This corollary is a proof assembly with explicit imports. It is not a new
priority claim for the `125` bound, an independent reconstruction of the
literature reduction, or a substitute for specialist review of the imported
toric theorem.
</code></pre>

<a id="source-7637370c469b9202"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 8 full-root closure packet

This write-once packet is the canonical selective harvest of public-site PR 9
at head `86af7cf1cbccf33e068c35ea4440fc22536d1072`.  It closes both normalized
`(8,28)` support roots by direct exact reconstruction; it does **not** use the
unattached adjacent-chart terminal.

The mathematical proof and exact scope are in
&#91;`FULL_ROOT_CLOSURE_PROOF.md`&#93;(FULL_ROOT_CLOSURE_PROOF.md).  The replay starts
from the two raw support polygons, the exact quintic-field relations, and the
coefficient formula for the Jacobian bracket.  It does not consume archived
layer matrices or archived obstruction equations.

## Results retained

- The truncated support has no vertex-saturated solution: the reconstructed
  obstruction ideal spans all fourteen weight-four monomials.
- For the full support, the layer-four compatibility equation is a square.
  Its closed `t1_1=0` child is excluded by the two required top vertices; the
  open child normalizes to fifteen exact equations in five variables.
- Equations with zero-based indices `4,6,8,9,10,11` are literally a subset of
  those fifteen.  The canonical Program 6 compact toric theorem proves that
  this six-equation relaxation is empty.
- The bare Lane 9 `k=4` wall shear begins at normal order seven, not four.
  This negative lemma blocks the proposed bridge but is unnecessary for the
  direct Lane 8 closure.
- Together with the inspected GGHV reduction (arXiv:2204.14178v1, Theorem
  2.1, Proposition 4.3, and the Proposition 4.1/Corollary 5.7 route), the two
  support exclusions give the below-`125` corollary.  No novelty or priority
  claim is made for that bound.

## Replay

From the repository root, with a fresh nonexisting output path:

```bash
uv run python \
  research-notes/lane8-full-root-closure-20260803-v1/verify_lane8_packet.py \
  --replay-output /path/to/versioned-artifact
```

The validator checks the proof-carrying queue, every covering edge, source
pins, stage and denominator ledgers, and then performs the independent exact
raw-support replay.  Expected core digests are:

```text
truncated Macaulay minor  8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059
full fifteen equations    d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883
six-equation projection   e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a
```

The PR's original wrapper compared a reformatted local field helper
byte-for-byte with the public embedded helper and therefore failed its source
check despite equivalent code.  This harvested validator pins the local
helper and its exact outputs instead.  The unmodified independent replay was
run separately before harvest and reproduced all expected digests in 20.7
seconds.

## Boundaries

- The GGHV Newton reduction and the existing compact toric terminal theorem
  are exact imported dependencies, not independently reproved here.
- The good-prime toric archive is not regenerated by this small packet; its
  theorem and prior replay remain in the canonical Program 6 source.
- The stored adjacent layer-five-through-seven system remains exact but
  unattached.  It is not part of the full-root proof path.
- Higher-deficiency coefficients are projected away without division; the
  layer-through-eight equations are necessary conditions for every full
  completion, not a parametrization of the complete coefficient space.
</code></pre>

<a id="source-9accc1d6c5d4c9d7"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/fixtures/belyi_exact_field_relations.json`

<pre><code class="language-json">
{
  "minimal_polynomial": "x^5 - x^4 + 3*x^3 + 3*x^2 + 26",
  "relations": {
    "2": &#91;
      -15000285910282089504192,
      -5134565172670933272,
      137539431432626359836,
      336800193197460147624,
      -84325443098952382698,
      60579126468209266677769
    &#93;,
    "3": &#91;
      1226904480739913911103730491354208,
      -15145626846222632510692702532772,
      -25812205047619065763137145542294,
      -104130346741942550519886117919428,
      27200215296791514496874102142465,
      -29820471480667863369966901978929206
    &#93;,
    "4": &#91;
      3264449436074769519960953302867233653589648,
      -1416654536542996172285603232367200883597872,
      148725684611945953158030103823084812692216,
      -3555183783735327382944597214649722070608848,
      1011336872221928971870287510246952931988480,
      -3669830563651292540100256702722208474478817361
    &#93;,
    "5": &#91;
      -130944093022209528082635510047219742278592832955123904,
      -93369115961295526137992581529023299645675371941885440,
      79954620410178210879841226102250409682919462179058816,
      -80365467842144031759719494563248567280650515063467264,
      29210432611391016065746943076582124101598753403543376,
      -903249056584503071594417102016234211800722097289832510707
    &#93;,
    "6": &#91;
      2904537848673965560983870231505961611216484953581987843838276864,
      -27139380915905548127415137801482954552161780107413095369243631360,
      30569988840281136299540789078923076865252792222802018120348518784,
      -11515632609329406031637838793544215559406566088372742650310149376,
      5180847076984791157406962461949350630412905296285784590160733184,
      -3779357207149632914103290532850228636627298428125710781575310029109353
    &#93;,
    "7": &#91;
      -587985697653650203066919462433643852598998530789582860440276756960997106688,
      364163207376347068831121008237845147451532454403442608765650380506147866112,
      -330463845892243517019896878071386300101126939914921066806649929166392606464,
      99196362661811887568094595512520927061635078997619327908217427264016147968,
      -38091354056913439826730530997349571916326149522524749218571860463219329664,
      930206660129096433749475266122359445351031352517661885125550567798599734193335611
    &#93;
  }
}
</code></pre>

<a id="source-17e90f7c7cfb3106"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/fixtures/quintic_field_fast.py`

<pre><code class="language-python">
"""Fast exact Q&#91;u&#93;/(u^5-u^4+3u^3+3u^2+26) arithmetic.

Reconstructed from the public Lane 8 executable input.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd
from typing import Iterable, Union

Scalar = Union&#91;int, Fraction&#93;
MOD_F = &#91;Fraction(26), Fraction(0), Fraction(3), Fraction(3), Fraction(-1), Fraction(1)&#93;


def _gcd_many(values):
    g = 0
    for v in values:
        g = gcd(g, abs(v))
        if g == 1:
            return 1
    return g


def _trim(p):
    while p and p&#91;-1&#93; == 0:
        p.pop()
    return p


def _padd(a, b):
    n = max(len(a), len(b))
    c = &#91;Fraction(0)&#93; * n
    for i in range(n):
        c&#91;i&#93; = (a&#91;i&#93; if i &lt; len(a) else 0) + (b&#91;i&#93; if i &lt; len(b) else 0)
    return _trim(c)


def _psub(a, b):
    n = max(len(a), len(b))
    c = &#91;Fraction(0)&#93; * n
    for i in range(n):
        c&#91;i&#93; = (a&#91;i&#93; if i &lt; len(a) else 0) - (b&#91;i&#93; if i &lt; len(b) else 0)
    return _trim(c)


def _pmul(a, b):
    if not a or not b:
        return &#91;&#93;
    c = &#91;Fraction(0)&#93; * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c&#91;i + j&#93; += x * y
    return _trim(c)


def _pscale(s, a):
    return _trim(&#91;s * x for x in a&#93;) if s else &#91;&#93;


def _pdivmod(a, b):
    a = _trim(list(a))
    b = _trim(list(b))
    if not b:
        raise ZeroDivisionError
    if len(a) &lt; len(b):
        return &#91;&#93;, a
    q = &#91;Fraction(0)&#93; * (len(a) - len(b) + 1)
    while a and len(a) &gt;= len(b):
        d = len(a) - len(b)
        c = a&#91;-1&#93; / b&#91;-1&#93;
        q&#91;d&#93; += c
        for j, v in enumerate(b):
            a&#91;d + j&#93; -= c * v
        _trim(a)
    return _trim(q), a


def _xgcd(a, b):
    r0, r1 = _trim(list(a)), _trim(list(b))
    s0, s1 = &#91;Fraction(1)&#93;, &#91;&#93;
    t0, t1 = &#91;&#93;, &#91;Fraction(1)&#93;
    while r1:
        q, r2 = _pdivmod(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, _psub(s0, _pmul(q, s1))
        t0, t1 = t1, _psub(t0, _pmul(q, t1))
    lead = r0&#91;-1&#93;
    return _pscale(1 / lead, r0), _pscale(1 / lead, s0), _pscale(1 / lead, t0)


def _as_frac(x: Scalar) -&gt; Fraction:
    return x if isinstance(x, Fraction) else Fraction(x)


@dataclass(frozen=True, slots=True, init=False)
class K5:
    nums: tuple&#91;int, int, int, int, int&#93;
    den: int

    def __init__(self, coeffs: Iterable&#91;Scalar&#93; = (), den: int = 1):
        vals = list(coeffs)
        if den != 1:
            ns = &#91;int(x) for x in vals&#93;
            ns += &#91;0&#93; * (5 - len(ns))
            self._set(ns&#91;:5&#93;, den)
            return
        fs = &#91;_as_frac(x) for x in vals&#93;
        fs += &#91;Fraction(0)&#93; * (5 - len(fs))
        if len(fs) &gt; 5:
            raise ValueError
        d = 1
        for f in fs:
            d = d * f.denominator // gcd(d, f.denominator)
        ns = &#91;f.numerator * (d // f.denominator) for f in fs&#93;
        self._set(ns, d)

    def _set(self, ns, den):
        if den &lt; 0:
            ns = &#91;-x for x in ns&#93;
            den = -den
        g = _gcd_many(&#91;den, *ns&#93;)
        if g:
            den //= g
            ns = &#91;x // g for x in ns&#93;
        object.__setattr__(self, "nums", tuple(ns))
        object.__setattr__(self, "den", den)

    @classmethod
    def raw(cls, ns, den=1):
        obj = object.__new__(cls)
        obj._set(list(ns), den)
        return obj

    @classmethod
    def coerce(cls, x):
        if isinstance(x, K5):
            return x
        f = _as_frac(x)
        return cls.raw(&#91;f.numerator, 0, 0, 0, 0&#93;, f.denominator)

    @property
    def coeffs(self):
        return tuple(Fraction(n, self.den) for n in self.nums)

    def __bool__(self):
        return any(self.nums)

    def __eq__(self, other):
        if isinstance(other, K5):
            return self.den == other.den and self.nums == other.nums
        if isinstance(other, (int, Fraction)):
            return self == K5.coerce(other)
        return False

    def __hash__(self):
        return hash((self.nums, self.den))

    def __neg__(self):
        return K5.raw(&#91;-x for x in self.nums&#93;, self.den)

    def __add__(self, other):
        other = K5.coerce(other)
        if not self:
            return other
        if not other:
            return self
        g = gcd(self.den, other.den)
        a = other.den // g
        b = self.den // g
        d = self.den * a
        return K5.raw(&#91;x * a + y * b for x, y in zip(self.nums, other.nums)&#93;, d)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-K5.coerce(other))

    def __rsub__(self, other):
        return K5.coerce(other) - self

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            f = _as_frac(other)
            if not f or not self:
                return K5()
            return K5.raw(&#91;x * f.numerator for x in self.nums&#93;, self.den * f.denominator)
        other = K5.coerce(other)
        if not self or not other:
            return K5()
        c = &#91;0&#93; * 9
        for i, a in enumerate(self.nums):
            if a:
                for j, b in enumerate(other.nums):
                    if b:
                        c&#91;i + j&#93; += a * b
        # u^5 = u^4 - 3u^3 - 3u^2 - 26.
        for d in range(8, 4, -1):
            v = c&#91;d&#93;
            if v:
                c&#91;d - 1&#93; += v
                c&#91;d - 2&#93; -= 3 * v
                c&#91;d - 3&#93; -= 3 * v
                c&#91;d - 5&#93; -= 26 * v
                c&#91;d&#93; = 0
        return K5.raw(c&#91;:5&#93;, self.den * other.den)

    def __rmul__(self, other):
        return self * other

    @lru_cache(maxsize=None)
    def inverse(self):
        if not self:
            raise ZeroDivisionError
        a = &#91;Fraction(n, self.den) for n in self.nums&#93;
        a = _trim(a)
        g, s, _ = _xgcd(a, MOD_F)
        if g != &#91;Fraction(1)&#93;:
            raise ArithmeticError(g)
        _, rem = _pdivmod(s, MOD_F)
        rem += &#91;Fraction(0)&#93; * (5 - len(rem))
        return K5(rem&#91;:5&#93;)

    def __truediv__(self, other):
        if isinstance(other, (int, Fraction)):
            f = _as_frac(other)
            if not f:
                raise ZeroDivisionError
            return K5.raw(&#91;x * f.denominator for x in self.nums&#93;, self.den * f.numerator)
        return self * K5.coerce(other).inverse()

    def __rtruediv__(self, other):
        return K5.coerce(other) * self.inverse()

    def __pow__(self, n):
        if n &lt; 0:
            return self.inverse() ** (-n)
        out = K5(&#91;1&#93;)
        base = self
        while n:
            if n &amp; 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __repr__(self):
        return f"K5(nums={self.nums},den={self.den})"


class KDomain:
    zero = K5()
    one = K5(&#91;1&#93;)
    unit = K5(&#91;0, 1&#93;)

    @staticmethod
    def convert(x):
        return K5.coerce(x)


K = KDomain()
</code></pre>

<a id="source-d48d3823ed65bdc1"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/independent_raw_support_replay.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independently rebuild both Lane 8 roots from raw Newton supports.

The replay uses the published support polygons, the exact degree-21 face
relations, and the coefficient formula for a polynomial Jacobian bracket. It
does not consume archived layer matrices or archived obstruction equations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from lane8_replay.certificates import analyze_full, analyze_truncated, write_json
from lane8_replay.model import FIELD_POLYNOMIAL, FULL, TRUNCATED, build_face, run_layers

SCRIPT_DIR = Path(__file__).resolve().parent


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--relations",
        type=Path,
        default=(
            SCRIPT_DIR / "fixtures" / "belyi_exact_field_relations.json"
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="write only summary.json after performing the complete exact reconstruction",
    )
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)

    p, q = build_face(args.relations)
    truncated = run_layers(TRUNCATED, p, q)
    full = run_layers(FULL, p, q)
    truncated_summary = analyze_truncated(truncated)
    full_summary, full_equations, legacy, selected = analyze_full(full)

    args.output.mkdir(parents=True)
    if not args.summary_only:
        write_json(args.output / "full_equations.json", full_equations)
        write_json(args.output / "full_exact_fivevar_w8.json", legacy)
        write_json(args.output / "full_terminal_projection.json", selected)
    summary = {
        "schema": "lane8-independent-raw-support-replay-v1",
        "field": {
            "minimal_polynomial": FIELD_POLYNOMIAL,
            "basis": &#91;"1", "u", "u^2", "u^3", "u^4"&#93;,
            "irreducible_over_Q": True,
            "irreducibility_witness": {"prime": 67, "method": "Rabin test"},
        },
        "inputs": {
            "relations_file_sha256": hashlib.sha256(args.relations.read_bytes()).hexdigest(),
            "archived_layers_used": False,
            "archived_equations_used": False,
        },
        "face": {
            "p_degree": len(p) - 1,
            "q_degree": len(q) - 1,
            "jacobian_coefficients_verified": 18,
            "endpoint_coefficients_nonzero": True,
        },
        "truncated": truncated_summary,
        "full": full_summary,
        "public_expected": {
            "truncated_minor_determinant_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059",
            "full_equation_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883",
        },
    }
    summary&#91;"matches_public_expected"&#93; = {
        "truncated_minor": truncated_summary&#91;"minor_determinant_sha256"&#93;
        == summary&#91;"public_expected"&#93;&#91;"truncated_minor_determinant_sha256"&#93;,
        "full_equations": full_summary&#91;"final_equation_sha256"&#93;
        == summary&#91;"public_expected"&#93;&#91;"full_equation_sha256"&#93;,
    }
    if not all(summary&#91;"matches_public_expected"&#93;.values()):
        raise AssertionError(summary&#91;"matches_public_expected"&#93;)
    write_json(args.output / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-57b89af6ad61a7ba"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/__init__.py`

<pre><code class="language-python">
"""Exact independent Lane 8 raw-support replay package."""
</code></pre>

<a id="source-f9a58ccf95e56275"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/algebra.py`

<pre><code class="language-python">
"""Small exact polynomial-linear-algebra layer for the Lane 8 replay."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
from typing import Any

PACKAGE_DIR = Path(__file__).resolve().parent
FIELD_DIR = (PACKAGE_DIR.parent / "fixtures").resolve()
sys.path.insert(0, str(FIELD_DIR))
from quintic_field_fast import K, K5  # noqa: E402

ZERO = K.zero
ONE = K.one
U = K.unit
KElement = K5
Monomial = tuple&#91;int, ...&#93;
ParamPoly = dict&#91;Monomial, KElement&#93;
NVAR = 0
ZEXP: Monomial = ()


def set_parameter_count(count: int) -&gt; None:
    global NVAR, ZEXP
    NVAR = count
    ZEXP = (0,) * count


def k_vector(value: KElement) -&gt; list&#91;str&#93;:
    return &#91;str(q) for q in value.coeffs&#93;


def k_expr(value: KElement, symbol: str = "u") -&gt; str:
    pieces: list&#91;str&#93; = &#91;&#93;
    for degree, coefficient in enumerate(value.coeffs):
        if coefficient == 0:
            continue
        c = str(coefficient)
        if degree == 0:
            pieces.append(f"({c})")
        elif degree == 1:
            pieces.append(f"({c})*{symbol}")
        else:
            pieces.append(f"({c})*{symbol}^{degree}")
    return " + ".join(pieces) if pieces else "0"


def clean(poly: ParamPoly) -&gt; ParamPoly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient != ZERO}


def constant(coefficient: KElement) -&gt; ParamPoly:
    return {} if coefficient == ZERO else {ZEXP: coefficient}


def variable(index: int) -&gt; ParamPoly:
    exponent = &#91;0&#93; * NVAR
    exponent&#91;index&#93; = 1
    return {tuple(exponent): ONE}


def add(left: ParamPoly, right: ParamPoly) -&gt; ParamPoly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out&#91;monomial&#93; = out.get(monomial, ZERO) + coefficient
    return clean(out)


def negate(poly: ParamPoly) -&gt; ParamPoly:
    return {monomial: -coefficient for monomial, coefficient in poly.items()}


def scale(coefficient: KElement | int | Fraction, poly: ParamPoly) -&gt; ParamPoly:
    coefficient = K.convert(coefficient)
    if coefficient == ZERO:
        return {}
    return clean({monomial: coefficient * value for monomial, value in poly.items()})


def multiply(left: ParamPoly, right: ParamPoly) -&gt; ParamPoly:
    out: ParamPoly = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            out&#91;monomial&#93; = out.get(monomial, ZERO) + left_coefficient * right_coefficient
    return clean(out)


def weighted_degree(poly: ParamPoly, weights: tuple&#91;int, ...&#93;) -&gt; int:
    values = {sum(exponent * weight for exponent, weight in zip(monomial, weights)) for monomial in poly}
    if len(values) != 1:
        raise AssertionError(values)
    return next(iter(values))


def normalized(poly: ParamPoly) -&gt; tuple&#91;KElement, ParamPoly&#93;:
    first = min(poly)
    coefficient = ONE / poly&#91;first&#93;
    return coefficient, {monomial: coefficient * value for monomial, value in poly.items()}


def polynomial_json(poly: ParamPoly) -&gt; list&#91;dict&#91;str, Any&#93;&#93;:
    return &#91;
        {"exp": list(monomial), "coeff_basis": k_vector(coefficient), "coeff_expr": k_expr(coefficient)}
        for monomial, coefficient in sorted(poly.items())
    &#93;


def rref_transform_details(matrix: list&#91;list&#91;KElement&#93;&#93;) -&gt; tuple&#91;list&#91;list&#91;KElement&#93;&#93;, list&#91;list&#91;KElement&#93;&#93;, list&#91;int&#93;, list&#91;KElement&#93;&#93;:
    row_count = len(matrix)
    column_count = len(matrix&#91;0&#93;) if matrix else 0
    augmented = &#91;
        list(matrix&#91;row&#93;) + &#91;ONE if row == identity_column else ZERO for identity_column in range(row_count)&#93;
        for row in range(row_count)
    &#93;
    pivot_row = 0
    pivots: list&#91;int&#93; = &#91;&#93;
    pivot_units: list&#91;KElement&#93; = &#91;&#93;
    for column in range(column_count):
        source = next((row for row in range(pivot_row, row_count) if augmented&#91;row&#93;&#91;column&#93; != ZERO), None)
        if source is None:
            continue
        augmented&#91;pivot_row&#93;, augmented&#91;source&#93; = augmented&#91;source&#93;, augmented&#91;pivot_row&#93;
        pivot_units.append(augmented&#91;pivot_row&#93;&#91;column&#93;)
        inverse = ONE / augmented&#91;pivot_row&#93;&#91;column&#93;
        augmented&#91;pivot_row&#93; = &#91;inverse * value for value in augmented&#91;pivot_row&#93;&#93;
        for row in range(row_count):
            if row == pivot_row or augmented&#91;row&#93;&#91;column&#93; == ZERO:
                continue
            factor = augmented&#91;row&#93;&#91;column&#93;
            augmented&#91;row&#93; = &#91;
                augmented&#91;row&#93;&#91;index&#93; - factor * augmented&#91;pivot_row&#93;&#91;index&#93;
                for index in range(column_count + row_count)
            &#93;
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return (
        &#91;row&#91;:column_count&#93; for row in augmented&#93;,
        &#91;row&#91;column_count:&#93; for row in augmented&#93;,
        pivots,
        pivot_units,
    )


def rref_transform(matrix: list&#91;list&#91;KElement&#93;&#93;) -&gt; tuple&#91;list&#91;list&#91;KElement&#93;&#93;, list&#91;list&#91;KElement&#93;&#93;, list&#91;int&#93;&#93;:
    reduced, transform, pivots, _ = rref_transform_details(matrix)
    return reduced, transform, pivots


def transform_polynomials(transform: list&#91;list&#91;KElement&#93;&#93;, vector: list&#91;ParamPoly&#93;) -&gt; list&#91;ParamPoly&#93;:
    out: list&#91;ParamPoly&#93; = &#91;&#93;
    for row in transform:
        value: ParamPoly = {}
        for coefficient, poly in zip(row, vector):
            value = add(value, scale(coefficient, poly))
        out.append(value)
    return out


def determinant(matrix: list&#91;list&#91;KElement&#93;&#93;) -&gt; KElement:
    work = &#91;list(row) for row in matrix&#93;
    size = len(work)
    value = ONE
    sign = 1
    for column in range(size):
        source = next(row for row in range(column, size) if work&#91;row&#93;&#91;column&#93; != ZERO)
        if source != column:
            work&#91;column&#93;, work&#91;source&#93; = work&#91;source&#93;, work&#91;column&#93;
            sign = -sign
        pivot = work&#91;column&#93;&#91;column&#93;
        value *= pivot
        inverse = ONE / pivot
        for row in range(column + 1, size):
            if work&#91;row&#93;&#91;column&#93; == ZERO:
                continue
            factor = work&#91;row&#93;&#91;column&#93; * inverse
            for index in range(column, size):
                work&#91;row&#93;&#91;index&#93; -= factor * work&#91;column&#93;&#91;index&#93;
    return -value if sign &lt; 0 else value
</code></pre>

<a id="source-5af7c6845d045cd4"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/certificates.py`

<pre><code class="language-python">
"""Exact truncated and full-root certificates derived from reconstructed layers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from . import algebra
from .algebra import (
    ONE,
    ZERO,
    KElement,
    ParamPoly,
    clean,
    determinant,
    k_expr,
    k_vector,
    normalized,
    polynomial_json,
    rref_transform,
    weighted_degree,
)
from .model import FIELD_POLYNOMIAL, LayerRun


def weight_four_monomials() -&gt; list&#91;tuple&#91;int, int, int, int&#93;&#93;:
    out = &#91;&#93;
    for a in range(5):
        for b in range(5):
            for c in range(3):
                for d in range(3):
                    if a + b + 2 * c + 2 * d == 4:
                        out.append((a, b, c, d))
    return out


def analyze_truncated(run: LayerRun) -&gt; dict&#91;str, Any&#93;:
    expected = &#91;
        &#91;1, 19, 18, 17, 2, 0&#93;,
        &#91;2, 21, 19, 18, 3, 0&#93;,
        &#91;3, 13, 20, 12, 1, 7&#93;,
        &#91;4, 0, 20, 0, 0, 18&#93;,
        &#91;5, 0, 21, 0, 0, 0&#93;,
    &#93;
    if run.layer_data != expected:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3)
    for layer, poly in run.equations:
        if weighted_degree(poly, weights) != layer:
            raise AssertionError("unexpected truncated obstruction weight")
        if any(monomial&#91;2&#93; or monomial&#91;5&#93; for monomial in poly):
            raise AssertionError("a split parameter entered a truncated obstruction")

    core = (0, 1, 3, 4)

    def project(poly: ParamPoly) -&gt; ParamPoly:
        return {tuple(monomial&#91;index&#93; for index in core): coefficient for monomial, coefficient in poly.items()}

    weight_three = &#91;project(poly) for layer, poly in run.equations if layer == 3&#93;
    weight_four = &#91;project(poly) for layer, poly in run.equations if layer == 4&#93;
    monomials = weight_four_monomials()
    monomial_index = {monomial: index for index, monomial in enumerate(monomials)}
    rows: list&#91;list&#91;KElement&#93;&#93; = &#91;&#93;
    labels: list&#91;tuple&#91;str, int&#93;&#93; = &#91;&#93;
    for equation_index, poly in enumerate(weight_four):
        row = &#91;ZERO&#93; * len(monomials)
        for monomial, coefficient in poly.items():
            row&#91;monomial_index&#91;monomial&#93;&#93; = coefficient
        rows.append(row)
        labels.append(("E4", equation_index))
    for variable_index in (0, 1):
        for equation_index, poly in enumerate(weight_three):
            row = &#91;ZERO&#93; * len(monomials)
            for monomial, coefficient in poly.items():
                shifted = list(monomial)
                shifted&#91;variable_index&#93; += 1
                row&#91;monomial_index&#91;tuple(shifted)&#93;&#93; = coefficient
            rows.append(row)
            labels.append((f"t1_{variable_index}*E3", equation_index))

    _, _, pivots = rref_transform(rows)
    if len(pivots) != 14 or len(monomials) != 14:
        raise AssertionError((len(pivots), len(monomials)))
    transpose = &#91;&#91;rows&#91;row&#93;&#91;column&#93; for row in range(len(rows))&#93; for column in range(len(monomials))&#93;
    _, _, independent_rows = rref_transform(transpose)
    selected = independent_rows&#91;:14&#93;
    minor = &#91;&#91;rows&#91;row&#93;&#91;column&#93; for column in range(14)&#93; for row in selected&#93;
    determinant_value = determinant(minor)
    if determinant_value == ZERO:
        raise AssertionError("truncated Macaulay minor vanished")

    top_p = run.p_solution&#91;2&#93;&#91;(8, 16)&#93;
    top_q = run.q_solution&#91;3&#93;&#91;(12, 24)&#93;
    if not top_p or not top_q:
        raise AssertionError("a truncated top-vertex coefficient vanished identically")
    if weighted_degree(top_p, weights) != 2 or weighted_degree(top_q, weights) != 3:
        raise AssertionError("unexpected truncated top-vertex weight")
    if any(monomial&#91;2&#93; or monomial&#91;5&#93; for monomial in top_p) or any(
        monomial&#91;2&#93; or monomial&#91;5&#93; for monomial in top_q
    ):
        raise AssertionError("a split parameter entered a truncated top vertex")

    return {
        "support_sizes": {"P": len(run.p_support), "Q": len(run.q_support)},
        "layer_data": run.layer_data,
        "stage_data": run.stage_data,
        "origin_vertex_parameters": {
            "P_(0,0)": "parameter_index_2",
            "Q_(0,0)": "parameter_index_5",
        },
        "higher_deficiency_coefficients_projected_away": {"P": 0, "Q": 0},
        "weight_three_equation_count": len(weight_three),
        "weight_four_equation_count": len(weight_four),
        "weight_four_monomial_count": len(monomials),
        "macaulay_rank": len(pivots),
        "selected_rows": &#91;{"row_index": row, "source": list(labels&#91;row&#93;)} for row in selected&#93;,
        "minor_determinant_nonzero": True,
        "minor_determinant_sha256": hashlib.sha256(
            json.dumps(k_vector(determinant_value), separators=(",", ":")).encode()
        ).hexdigest(),
        "top_vertex_weights": {"P_8_16": 2, "Q_12_24": 3},
        "top_vertex_coefficients_depend_only_on_radical_variables": True,
        "top_vertex_coefficients_vanish_when_the_four_effective_variables_vanish": True,
        "exact_support_requires_both_top_vertices_nonzero": True,
        "conclusion": "vertex-saturated truncated system is empty",
    }


def specialize_full(poly: ParamPoly, alpha: KElement) -&gt; ParamPoly:
    keep = (0, 3, 6, 7, 8)
    out: ParamPoly = {}
    for monomial, coefficient in poly.items():
        reduced = tuple(monomial&#91;index&#93; for index in keep)
        out&#91;reduced&#93; = out.get(reduced, ZERO) + coefficient * alpha**monomial&#91;4&#93;
    return clean(out)


def endpoint_after_square(poly: ParamPoly, alpha: KElement) -&gt; tuple&#91;int, KElement&#93;:
    out: dict&#91;int, KElement&#93; = {}
    for monomial, coefficient in poly.items():
        if any(monomial&#91;index&#93; for index in range(algebra.NVAR) if index not in (1, 4)):
            raise AssertionError("unexpected parameter in a full top-vertex coefficient")
        exponent = monomial&#91;1&#93; + 2 * monomial&#91;4&#93;
        out&#91;exponent&#93; = out.get(exponent, ZERO) + coefficient * alpha**monomial&#91;4&#93;
    out = {exponent: coefficient for exponent, coefficient in out.items() if coefficient != ZERO}
    if len(out) != 1:
        raise AssertionError(out)
    return next(iter(out.items()))


def analyze_full(run: LayerRun):
    expected = &#91;
        &#91;1, 19, 18, 17, 2, 0&#93;,
        &#91;2, 21, 19, 18, 3, 0&#93;,
        &#91;3, 21, 20, 18, 3, 0&#93;,
        &#91;4, 19, 20, 18, 1, 2&#93;,
        &#91;5, 17, 21, 17, 0, 2&#93;,
        &#91;6, 15, 20, 15, 0, 4&#93;,
        &#91;7, 13, 19, 13, 0, 5&#93;,
        &#91;8, 11, 18, 11, 0, 6&#93;,
    &#93;
    if run.layer_data != expected:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3, 3, 3, 4)
    for layer, poly in run.equations:
        if weighted_degree(poly, weights) != layer:
            raise AssertionError("unexpected full obstruction weight")
        if any(monomial&#91;2&#93; or monomial&#91;5&#93; for monomial in poly):
            raise AssertionError("a split parameter entered a full obstruction")

    weight_four: list&#91;ParamPoly&#93; = &#91;&#93;
    for layer, poly in run.equations:
        if layer == 4:
            _, candidate = normalized(poly)
            if not any(candidate == old for old in weight_four):
                weight_four.append(candidate)
    if len(weight_four) != 1:
        raise AssertionError(len(weight_four))
    square = weight_four&#91;0&#93;
    if any(any(monomial&#91;index&#93; for index in range(algebra.NVAR) if index not in (1, 4)) for monomial in square):
        raise AssertionError("unexpected square support")
    t22_squared = (0, 0, 0, 0, 2, 0, 0, 0, 0)
    t11_squared_t22 = (0, 2, 0, 0, 1, 0, 0, 0, 0)
    t11_fourth = (0, 4, 0, 0, 0, 0, 0, 0, 0)
    leading = square.get(t22_squared, ZERO)
    middle = square.get(t11_squared_t22, ZERO)
    trailing = square.get(t11_fourth, ZERO)
    if leading == ZERO:
        raise AssertionError("square leading coefficient vanished")
    alpha = -middle / (2 * leading)
    if trailing / leading != alpha**2:
        raise AssertionError("weight-four equation is not the claimed square")

    p_exponent, p_endpoint = endpoint_after_square(run.p_solution&#91;2&#93;&#91;(8, 16)&#93;, alpha)
    q_exponent, q_endpoint = endpoint_after_square(run.q_solution&#91;3&#93;&#91;(12, 24)&#93;, alpha)
    if (p_exponent, q_exponent) != (2, 3) or p_endpoint == ZERO or q_endpoint == ZERO:
        raise AssertionError("full top-vertex normalization failed")

    final: list&#91;tuple&#91;int, ParamPoly&#93;&#93; = &#91;&#93;
    for layer, poly in run.equations:
        specialized = specialize_full(poly, alpha)
        if not specialized:
            continue
        _, candidate = normalized(specialized)
        if not any(layer == old_layer and candidate == old for old_layer, old in final):
            final.append((layer, candidate))
    counts = {layer: sum(candidate_layer == layer for candidate_layer, _ in final) for layer in (5, 6, 7, 8)}
    if counts != {5: 1, 6: 3, 7: 5, 8: 6}:
        raise AssertionError(counts)

    equations = &#91;{"weight": layer, "terms": polynomial_json(poly)} for layer, poly in final&#93;
    canonical = (json.dumps(equations, sort_keys=True, separators=(",", ":")) + "\n").encode()
    equation_digest = hashlib.sha256(canonical).hexdigest()
    legacy = {
        "field_polynomial": FIELD_POLYNOMIAL,
        "normalization": "p0=q0=p1=1; t1_1=1; t2_2=alpha",
        "variables": &#91;"x", "a", "b", "c", "d"&#93;,
        "original_parameter_indices": &#91;0, 3, 6, 7, 8&#93;,
        "layer_data": run.layer_data,
        "stage_data": run.stage_data,
        "alpha": k_expr(alpha, symbol="x"),
        "Ptop": k_expr(p_endpoint, symbol="x"),
        "Qtop": k_expr(q_endpoint, symbol="x"),
        "equations": &#91;
            {
                "weight": layer,
                "terms": &#91;
                    {"exp": list(monomial), "coeff": k_expr(coefficient, symbol="x")}
                    for monomial, coefficient in sorted(poly.items())
                &#93;,
            }
            for layer, poly in final
        &#93;,
    }
    selected_indices = &#91;4, 6, 8, 9, 10, 11&#93;
    selected = &#91;equations&#91;index&#93; for index in selected_indices&#93;
    selected_canonical = (json.dumps(selected, sort_keys=True, separators=(",", ":")) + "\n").encode()
    equation_manifest = &#91;
        {
            "index": index,
            "weight": equation&#91;"weight"&#93;,
            "term_count": len(equation&#91;"terms"&#93;),
            "sha256": hashlib.sha256(
                (json.dumps(equation, sort_keys=True, separators=(",", ":")) + "\n").encode()
            ).hexdigest(),
        }
        for index, equation in enumerate(equations)
    &#93;
    summary = {
        "support_sizes": {"P": len(run.p_support), "Q": len(run.q_support)},
        "layer_data": run.layer_data,
        "stage_data": run.stage_data,
        "origin_vertex_parameters": {
            "P_(0,0)": "parameter_index_2",
            "Q_(0,0)": "parameter_index_5",
        },
        "higher_deficiency_coefficients_projected_away": {
            "cutoff": 8,
            "P": 3,
            "Q": 28,
            "extra_vertices": {"P_(0,8)": 10, "Q_(0,12)": 15},
        },
        "weight_four_is_square": True,
        "alpha_basis": k_vector(alpha),
        "top_P_after_square": {"t11_exponent": p_exponent, "coefficient_basis": k_vector(p_endpoint)},
        "top_Q_after_square": {"t11_exponent": q_exponent, "coefficient_basis": k_vector(q_endpoint)},
        "vertex_saturation_forces_t11_nonzero": True,
        "normalization": "t1_1=1; t2_2=alpha; retain t1_0,t2_1,t3_1,t3_2,t4_0",
        "final_equation_counts": counts,
        "final_equation_sha256": equation_digest,
        "equation_manifest": equation_manifest,
        "terminal_projection": {
            "zero_based_indices": selected_indices,
            "equation_count": len(selected),
            "sha256": hashlib.sha256(selected_canonical).hexdigest(),
            "logical_direction": "V(all fifteen) is contained in V(the selected six)",
        },
        "denominator_audit": {
            "layer_matrix_entries": "fixed elements of K0",
            "row_reduction_pivots": "nonzero fixed elements of K0",
            "variable_denominators_introduced_before_normalization": &#91;&#93;,
            "only_open_factor": "t1_1",
            "closed_complement": "t1_1=0 contradicts exact top-vertex support",
        },
        "conclusion": "raw full support reduces exactly to fifteen normalized equations",
    }
    return summary, equations, legacy, selected


def write_json(path: Path, value: Any) -&gt; None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
</code></pre>

<a id="source-0f27a7fc3768a4bf"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_replay/model.py`

<pre><code class="language-python">
"""Raw Newton-support and Jacobian-layer reconstruction for Lane 8."""
from __future__ import annotations

from collections import defaultdict
import hashlib
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable

from .algebra import (
    K,
    ONE,
    U,
    ZERO,
    ParamPoly,
    add,
    constant,
    multiply,
    negate,
    k_vector,
    rref_transform_details,
    scale,
    set_parameter_count,
    transform_polynomials,
    variable,
)

FIELD_POLYNOMIAL = "u^5-u^4+3*u^3+3*u^2+26"
RawTerm = tuple&#91;int, int&#93;


def _ff_trim(poly: list&#91;int&#93;, prime: int) -&gt; list&#91;int&#93;:
    out = &#91;coefficient % prime for coefficient in poly&#93;
    while out and out&#91;-1&#93; == 0:
        out.pop()
    return out


def _ff_sub(left: list&#91;int&#93;, right: list&#91;int&#93;, prime: int) -&gt; list&#91;int&#93;:
    size = max(len(left), len(right))
    return _ff_trim(
        &#91;
            (left&#91;index&#93; if index &lt; len(left) else 0)
            - (right&#91;index&#93; if index &lt; len(right) else 0)
            for index in range(size)
        &#93;,
        prime,
    )


def _ff_divmod(dividend: list&#91;int&#93;, divisor: list&#91;int&#93;, prime: int) -&gt; tuple&#91;list&#91;int&#93;, list&#91;int&#93;&#93;:
    remainder = _ff_trim(list(dividend), prime)
    divisor = _ff_trim(list(divisor), prime)
    if not divisor:
        raise ZeroDivisionError
    if len(remainder) &lt; len(divisor):
        return &#91;&#93;, remainder
    quotient = &#91;0&#93; * (len(remainder) - len(divisor) + 1)
    inverse_lead = pow(divisor&#91;-1&#93;, -1, prime)
    while remainder and len(remainder) &gt;= len(divisor):
        offset = len(remainder) - len(divisor)
        coefficient = remainder&#91;-1&#93; * inverse_lead % prime
        quotient&#91;offset&#93; = coefficient
        for index, value in enumerate(divisor):
            remainder&#91;offset + index&#93; = (remainder&#91;offset + index&#93; - coefficient * value) % prime
        remainder = _ff_trim(remainder, prime)
    return _ff_trim(quotient, prime), remainder


def _ff_gcd(left: list&#91;int&#93;, right: list&#91;int&#93;, prime: int) -&gt; list&#91;int&#93;:
    left = _ff_trim(left, prime)
    right = _ff_trim(right, prime)
    while right:
        _, remainder = _ff_divmod(left, right, prime)
        left, right = right, remainder
    if not left:
        return &#91;&#93;
    inverse_lead = pow(left&#91;-1&#93;, -1, prime)
    return _ff_trim(&#91;inverse_lead * coefficient for coefficient in left&#93;, prime)


def _ff_multiply_mod(
    left: list&#91;int&#93;, right: list&#91;int&#93;, modulus: list&#91;int&#93;, prime: int
) -&gt; list&#91;int&#93;:
    product = &#91;0&#93; * max(0, len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product&#91;left_degree + right_degree&#93; = (
                product&#91;left_degree + right_degree&#93; + left_coefficient * right_coefficient
            ) % prime
    _, remainder = _ff_divmod(product, modulus, prime)
    return remainder


def _ff_power_mod(base: list&#91;int&#93;, exponent: int, modulus: list&#91;int&#93;, prime: int) -&gt; list&#91;int&#93;:
    out = &#91;1&#93;
    base = _ff_trim(base, prime)
    while exponent:
        if exponent &amp; 1:
            out = _ff_multiply_mod(out, base, modulus, prime)
        base = _ff_multiply_mod(base, base, modulus, prime)
        exponent //= 2
    return out


def irreducible_mod_prime(coefficients: list&#91;int&#93;, prime: int) -&gt; bool:
    """Rabin irreducibility test for this prime-degree polynomial."""
    polynomial = _ff_trim(coefficients, prime)
    degree = len(polynomial) - 1
    if degree != 5:
        raise ValueError("this compact witness is specialized to degree five")
    inverse_lead = pow(polynomial&#91;-1&#93;, -1, prime)
    polynomial = _ff_trim(&#91;inverse_lead * value for value in polynomial&#93;, prime)
    x = &#91;0, 1&#93;
    frobenius = x
    for iteration in range(degree):
        frobenius = _ff_power_mod(frobenius, prime, polynomial, prime)
        if iteration == 0:
            if len(_ff_gcd(polynomial, _ff_sub(frobenius, x, prime), prime)) != 1:
                return False
    return _ff_sub(frobenius, x, prime) == &#91;&#93;


@dataclass(frozen=True)
class SupportCase:
    name: str
    p_vertices: list&#91;RawTerm&#93;
    q_vertices: list&#91;RawTerm&#93;
    parameter_count: int
    parameters_by_layer: dict&#91;int, list&#91;int&#93;&#93;
    last_layer: int


TRUNCATED = SupportCase(
    "truncated",
    &#91;(0, 0), (1, 0), (8, 14), (8, 16)&#93;,
    &#91;(0, 0), (2, 1), (12, 21), (12, 24)&#93;,
    6,
    {1: &#91;0, 1&#93;, 2: &#91;2, 3, 4&#93;, 3: &#91;5&#93;},
    5,
)
FULL = SupportCase(
    "full",
    &#91;(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)&#93;,
    &#91;(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)&#93;,
    9,
    {1: &#91;0, 1&#93;, 2: &#91;2, 3, 4&#93;, 3: &#91;5, 6, 7&#93;, 4: &#91;8&#93;},
    8,
)


@dataclass
class LayerRun:
    case: SupportCase
    p_support: list&#91;RawTerm&#93;
    q_support: list&#91;RawTerm&#93;
    p_layers: defaultdict&#91;int, list&#91;RawTerm&#93;&#93;
    q_layers: defaultdict&#91;int, list&#91;RawTerm&#93;&#93;
    p_solution: dict&#91;int, dict&#91;RawTerm, ParamPoly&#93;&#93;
    q_solution: dict&#91;int, dict&#91;RawTerm, ParamPoly&#93;&#93;
    equations: list&#91;tuple&#91;int, ParamPoly&#93;&#93;
    layer_data: list&#91;list&#91;int&#93;&#93;
    stage_data: list&#91;dict&#93;


def hull(points: Iterable&#91;RawTerm&#93;) -&gt; list&#91;RawTerm&#93;:
    points = sorted(set(points))

    def cross(origin: RawTerm, left: RawTerm, right: RawTerm) -&gt; int:
        return (left&#91;0&#93; - origin&#91;0&#93;) * (right&#91;1&#93; - origin&#91;1&#93;) - (left&#91;1&#93; - origin&#91;1&#93;) * (right&#91;0&#93; - origin&#91;0&#93;)

    lower: list&#91;RawTerm&#93; = &#91;&#93;
    for point in points:
        while len(lower) &gt;= 2 and cross(lower&#91;-2&#93;, lower&#91;-1&#93;, point) &lt;= 0:
            lower.pop()
        lower.append(point)
    upper: list&#91;RawTerm&#93; = &#91;&#93;
    for point in reversed(points):
        while len(upper) &gt;= 2 and cross(upper&#91;-2&#93;, upper&#91;-1&#93;, point) &lt;= 0:
            upper.pop()
        upper.append(point)
    return lower&#91;:-1&#93; + upper&#91;:-1&#93;


def inside(point: RawTerm, vertices: list&#91;RawTerm&#93;) -&gt; bool:
    boundary = hull(vertices)
    crosses = &#91;
        (right&#91;0&#93; - left&#91;0&#93;) * (point&#91;1&#93; - left&#91;1&#93;) - (right&#91;1&#93; - left&#91;1&#93;) * (point&#91;0&#93; - left&#91;0&#93;)
        for left, right in zip(boundary, boundary&#91;1:&#93; + boundary&#91;:1&#93;)
    &#93;
    return all(value &gt;= 0 for value in crosses) or all(value &lt;= 0 for value in crosses)


def lattice_points(vertices: list&#91;RawTerm&#93;) -&gt; list&#91;RawTerm&#93;:
    return sorted(
        (x, y)
        for x in range(max(x for x, _ in vertices) + 1)
        for y in range(max(y for _, y in vertices) + 1)
        if inside((x, y), vertices)
    )


def support_layers(case: SupportCase):
    p_support = lattice_points(case.p_vertices)
    q_support = lattice_points(case.q_vertices)
    p_layers: defaultdict&#91;int, list&#91;RawTerm&#93;&#93; = defaultdict(list)
    q_layers: defaultdict&#91;int, list&#91;RawTerm&#93;&#93; = defaultdict(list)
    for x, y in p_support:
        p_layers&#91;y - 2 * x + 2&#93;.append((x, y))
    for x, y in q_support:
        q_layers&#91;y - 2 * x + 3&#93;.append((x, y))
    return p_support, q_support, p_layers, q_layers


def build_face(relation_path: Path):
    data = json.loads(relation_path.read_text(encoding="utf-8"))
    displayed = data&#91;"minimal_polynomial"&#93;.replace(" ", "").replace("x", "u")
    if displayed != FIELD_POLYNOMIAL:
        raise AssertionError(displayed)
    if not irreducible_mod_prime(&#91;26, 0, 3, 3, -1, 1&#93;, 67):
        raise AssertionError("the displayed quintic failed its mod-67 irreducibility witness")

    p = &#91;ONE, ONE&#93;
    for degree in range(2, 8):
        relation = data&#91;"relations"&#93;&#91;str(degree)&#93;
        numerator = sum((K.convert(relation&#91;index&#93;) * U**index for index in range(5)), ZERO)
        p.append(-numerator / relation&#91;5&#93;)
    q = &#91;ONE&#93;
    for degree in range(1, 11):
        total = ZERO
        for p_degree in range(1, min(7, degree) + 1):
            total += (1 + 2 * degree - 5 * p_degree) * p&#91;p_degree&#93; * q&#91;degree - p_degree&#93;
        q.append(-total / (1 + 2 * degree))

    for degree in range(18):
        total = ZERO
        for p_degree in range(max(0, degree - 10), min(7, degree) + 1):
            q_degree = degree - p_degree
            total += (1 + 2 * q_degree - 3 * p_degree) * p&#91;p_degree&#93; * q&#91;q_degree&#93;
        total -= ONE if degree == 0 else ZERO
        if total != ZERO:
            raise AssertionError(("face residual", degree, total))
    if p&#91;-1&#93; == ZERO or q&#91;-1&#93; == ZERO:
        raise AssertionError("face endpoint")
    return p, q


def bracket(p_terms: dict&#91;RawTerm, ParamPoly&#93;, q_terms: dict&#91;RawTerm, ParamPoly&#93;):
    out: dict&#91;RawTerm, ParamPoly&#93; = {}
    for (i, j), p_coefficient in p_terms.items():
        for (k, ell), q_coefficient in q_terms.items():
            target = (i + k - 1, j + ell - 1)
            out&#91;target&#93; = add(
                out.get(target, {}),
                scale(i * ell - j * k, multiply(p_coefficient, q_coefficient)),
            )
    return out


def run_layers(case: SupportCase, p_coefficients, q_coefficients) -&gt; LayerRun:
    set_parameter_count(case.parameter_count)
    p_support, q_support, p_layers, q_layers = support_layers(case)
    p_solution = {0: {(degree + 1, 2 * degree): constant(value) for degree, value in enumerate(p_coefficients)}}
    q_solution = {0: {(degree + 2, 2 * degree + 1): constant(value) for degree, value in enumerate(q_coefficients)}}
    equations: list&#91;tuple&#91;int, ParamPoly&#93;&#93; = &#91;&#93;
    layer_data: list&#91;list&#91;int&#93;&#93; = &#91;&#93;
    stage_data: list&#91;dict&#93; = &#91;&#93;

    def target_rows(layer: int) -&gt; list&#91;RawTerm&#93;:
        rows: set&#91;RawTerm&#93; = set()
        for p_layer in range(layer + 1):
            for i, j in p_layers.get(p_layer, &#91;&#93;):
                for k, ell in q_layers.get(layer - p_layer, &#91;&#93;):
                    rows.add((i + k - 1, j + ell - 1))
        return sorted(rows)

    for layer in range(1, case.last_layer + 1):
        rows = target_rows(layer)
        row_index = {term: index for index, term in enumerate(rows)}
        columns = &#91;("P", term) for term in p_layers.get(layer, &#91;&#93;)&#93; + &#91;("Q", term) for term in q_layers.get(layer, &#91;&#93;)&#93;
        matrix = &#91;&#91;ZERO&#93; * len(columns) for _ in rows&#93;
        for column_index, (kind, term) in enumerate(columns):
            if kind == "P":
                i, j = term
                for (k, ell), coefficient_poly in q_solution&#91;0&#93;.items():
                    matrix&#91;row_index&#91;(i + k - 1, j + ell - 1)&#93;&#93;&#91;column_index&#93; += (i * ell - j * k) * next(iter(coefficient_poly.values()))
            else:
                k, ell = term
                for (i, j), coefficient_poly in p_solution&#91;0&#93;.items():
                    matrix&#91;row_index&#91;(i + k - 1, j + ell - 1)&#93;&#93;&#91;column_index&#93; += (i * ell - j * k) * next(iter(coefficient_poly.values()))

        forcing = {row: {} for row in rows}
        for p_layer in range(1, layer):
            q_layer = layer - p_layer
            if p_layer not in p_solution or q_layer not in q_solution:
                continue
            for row, poly in bracket(p_solution&#91;p_layer&#93;, q_solution&#91;q_layer&#93;).items():
                forcing&#91;row&#93; = add(forcing&#91;row&#93;, poly)
        right_hand_side = &#91;negate(forcing&#91;row&#93;) for row in rows&#93;

        matrix_payload = json.dumps(
            &#91;&#91;k_vector(value) for value in row&#93; for row in matrix&#93;,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
        basis_payload = json.dumps(
            {"rows": rows, "columns": columns}, sort_keys=True, separators=(",", ":")
        ).encode()
        if not columns:
            obstruction_count = sum(bool(poly) for poly in forcing.values())
            equations.extend((layer, poly) for poly in forcing.values() if poly)
            layer_data.append(&#91;layer, 0, len(rows), 0, 0, obstruction_count&#93;)
            stage_data.append(
                {
                    "layer": layer,
                    "basis_sha256": hashlib.sha256(basis_payload).hexdigest(),
                    "matrix_sha256": hashlib.sha256(matrix_payload).hexdigest(),
                    "pivot_columns": &#91;&#93;,
                    "pivot_unit_count": 0,
                    "pivot_units_sha256": hashlib.sha256(b"&#91;&#93;").hexdigest(),
                    "inverted_parameter_polynomials": &#91;&#93;,
                }
            )
            continue

        reduced, transform, pivots, pivot_units = rref_transform_details(matrix)
        transformed_rhs = transform_polynomials(transform, right_hand_side)
        compatibility = transformed_rhs&#91;len(pivots):&#93;
        equations.extend((layer, poly) for poly in compatibility if poly)
        free_columns = &#91;index for index in range(len(columns)) if index not in pivots&#93;
        kernel: list&#91;list&#93; = &#91;&#93;
        for free in free_columns:
            vector = &#91;ZERO&#93; * len(columns)
            vector&#91;free&#93; = ONE
            for pivot_row, pivot_column in enumerate(pivots):
                vector&#91;pivot_column&#93; = -reduced&#91;pivot_row&#93;&#91;free&#93;
            kernel.append(vector)
        expected_parameters = case.parameters_by_layer.get(layer, &#91;&#93;)
        if len(kernel) != len(expected_parameters):
            raise AssertionError((case.name, layer, len(kernel), len(expected_parameters)))

        solution = &#91;{} for _ in columns&#93;
        for pivot_row, pivot_column in enumerate(pivots):
            solution&#91;pivot_column&#93; = transformed_rhs&#91;pivot_row&#93;
        for parameter_index, vector in zip(expected_parameters, kernel):
            for column_index, coefficient in enumerate(vector):
                solution&#91;column_index&#93; = add(solution&#91;column_index&#93;, scale(coefficient, variable(parameter_index)))
        p_solution&#91;layer&#93; = {}
        q_solution&#91;layer&#93; = {}
        for poly, (kind, term) in zip(solution, columns):
            (p_solution if kind == "P" else q_solution)&#91;layer&#93;&#91;term&#93; = poly
        layer_data.append(
            &#91;layer, len(columns), len(rows), len(pivots), len(kernel), sum(bool(poly) for poly in compatibility)&#93;
        )
        pivot_payload = json.dumps(
            &#91;k_vector(value) for value in pivot_units&#93;,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
        stage_data.append(
            {
                "layer": layer,
                "basis_sha256": hashlib.sha256(basis_payload).hexdigest(),
                "matrix_sha256": hashlib.sha256(matrix_payload).hexdigest(),
                "pivot_columns": pivots,
                "pivot_unit_count": len(pivot_units),
                "pivot_units_sha256": hashlib.sha256(pivot_payload).hexdigest(),
                "inverted_parameter_polynomials": &#91;&#93;,
            }
        )

    return LayerRun(
        case,
        p_support,
        q_support,
        p_layers,
        q_layers,
        p_solution,
        q_solution,
        equations,
        layer_data,
        stage_data,
    )
</code></pre>

<a id="source-25fe326b81beaecf"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/__init__.py`

<pre><code class="language-python">
"""Fail-closed validation package for contribution JCG-C-0015."""
</code></pre>

<a id="source-ad118b41f1258c2a"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/common.py`

<pre><code class="language-python">
"""Shared validation utilities and indexed-manifest loader."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

CONTRIBUTION_DIR = Path(__file__).resolve().parents&#91;1&#93;
REPOSITORY_ROOT = CONTRIBUTION_DIR.parents&#91;1&#93;


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -&gt; None:
    if not condition:
        raise ValidationError(message)


def sha256_file(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_sha1(path: Path) -&gt; str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def extract_fenced_text(page: str, heading: str, language: str) -&gt; str:
    marker = f"## {heading}"
    start = page.find(marker)
    require(start &gt;= 0, f"missing heading {marker!r}")
    opening = re.search(rf"```{re.escape(language)}\s*\n", page&#91;start:&#93;)
    require(opening is not None, f"missing {language} fence after {marker!r}")
    content_start = start + opening.end()
    content_end = page.find("\n```", content_start)
    require(content_end &gt;= 0, f"unterminated fence after {marker!r}")
    return page&#91;content_start:content_end&#93;.rstrip("\n") + "\n"


def extract_fenced_json(page: str, heading: str) -&gt; dict&#91;str, Any&#93;:
    return json.loads(extract_fenced_text(page, heading, "json"))


def load_indexed_manifest(path: Path) -&gt; dict&#91;str, Any&#93;:
    def resolve(value: Any) -&gt; Any:
        if isinstance(value, dict) and set(value) == {"$include"}:
            relative = value&#91;"$include"&#93;
            require(isinstance(relative, str), "fragment include must be a path")
            loaded = json.loads((CONTRIBUTION_DIR / relative).read_text(encoding="utf-8"))
            return resolve(loaded)
        if isinstance(value, dict):
            return {key: resolve(item) for key, item in value.items()}
        if isinstance(value, list):
            return &#91;resolve(item) for item in value&#93;
        return value

    index = json.loads(path.read_text(encoding="utf-8"))
    includes = index.pop("includes", None)
    if includes is None:
        return resolve(index)

    manifest = dict(index)
    for key, value in includes.items():
        if key == "stages":
            require(isinstance(value, list), "manifest stage includes must be a list")
            manifest&#91;key&#93; = &#91;
                resolve(json.loads((CONTRIBUTION_DIR / relative).read_text(encoding="utf-8")))
                for relative in value
            &#93;
        else:
            require(isinstance(value, str), f"manifest include {key} must be a path")
            manifest&#91;key&#93; = resolve(
                json.loads((CONTRIBUTION_DIR / value).read_text(encoding="utf-8"))
            )
    return manifest


def source_by_id(manifest: dict&#91;str, Any&#93;, source_id: str) -&gt; dict&#91;str, Any&#93;:
    matches = &#91;source for source in manifest&#91;"sources"&#93; if source&#91;"id"&#93; == source_id&#93;
    require(len(matches) == 1, f"expected one source {source_id}, found {len(matches)}")
    return matches&#91;0&#93;


def stage_by_id(manifest: dict&#91;str, Any&#93;, stage_id: str) -&gt; dict&#91;str, Any&#93;:
    matches = &#91;stage for stage in manifest&#91;"stages"&#93; if stage&#91;"id"&#93; == stage_id&#93;
    require(len(matches) == 1, f"expected one stage {stage_id}, found {len(matches)}")
    return matches&#91;0&#93;


def run_replay(output_dir: Path) -&gt; dict&#91;str, Any&#93;:
    command = &#91;
        sys.executable,
        str(CONTRIBUTION_DIR / "independent_raw_support_replay.py"),
        "--output",
        str(output_dir),
        "--summary-only",
    &#93;
    completed = subprocess.run(
        command,
        cwd=REPOSITORY_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
        check=False,
    )
    require(completed.returncode == 0, "independent replay failed:\n" + completed.stdout&#91;-8000:&#93;)
    summary_path = output_dir / "summary.json"
    require(summary_path.is_file(), "independent replay did not write summary.json")
    return json.loads(summary_path.read_text(encoding="utf-8"))
</code></pre>

<a id="source-047a2847b42f12df"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/main.py`

<pre><code class="language-python">
"""CLI orchestration for the Lane 8 validator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile

from .common import CONTRIBUTION_DIR, ValidationError, load_indexed_manifest, require, run_replay
from .manifest import validate_manifest_shape
from .queue import validate_queue
from .replay import validate_replay
from .sources import validate_sources


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-output", type=Path,
                        help="optional nonexisting directory in which to retain replay summary output")
    args = parser.parse_args()
    manifest = load_indexed_manifest(CONTRIBUTION_DIR / "stage-manifest.json")
    validate_manifest_shape(manifest)
    validate_sources(manifest)
    if args.replay_output is not None:
        require(not args.replay_output.exists(), f"replay output already exists: {args.replay_output}")
        summary = run_replay(args.replay_output)
    else:
        with tempfile.TemporaryDirectory(prefix="lane8-validation-") as directory:
            summary = run_replay(Path(directory) / "replay")
    validate_replay(manifest, summary)
    validate_queue(manifest)

    edges = manifest&#91;"queue"&#93;&#91;"edges"&#93;
    covering = sum(bool(edge&#91;"covering"&#93;) for edge in edges)
    print("lane8 submission validation: PASS")
    print(f"nodes={len(manifest&#91;'queue'&#93;&#91;'nodes'&#93;)}")
    print(f"edges={len(edges)} covering={covering} noncovering={len(edges)-covering}")
    print(f"truncated_rank={summary&#91;'truncated'&#93;&#91;'macaulay_rank'&#93;}")
    print(f"truncated_minor_sha256={summary&#91;'truncated'&#93;&#91;'minor_determinant_sha256'&#93;}")
    print(f"full_equations={len(summary&#91;'full'&#93;&#91;'equation_manifest'&#93;)}")
    print(f"full_equation_sha256={summary&#91;'full'&#93;&#91;'final_equation_sha256'&#93;}")
    print(f"terminal_projection_sha256={summary&#91;'full'&#93;&#91;'terminal_projection'&#93;&#91;'sha256'&#93;}")
    print("full_closure_paths=2")
    print("adjacent_terminal=empty_but_unattached")
    print("below_125=relative_to_imported_GGHV_and_toric_theorems")
    return 0


def cli() -&gt; None:
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as exc:
        print(f"validation error: {exc}", file=sys.stderr)
        raise SystemExit(2)
</code></pre>

<a id="source-348ac607606cf592"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/manifest.py`

<pre><code class="language-python">
"""Manifest-shape and theorem-boundary validation."""
from __future__ import annotations

from typing import Any

from .common import require


def validate_manifest_shape(manifest: dict&#91;str, Any&#93;) -&gt; None:
    require(manifest&#91;"schema"&#93; == "jcg-lane8-proof-carrying-queue-v1", "unexpected manifest schema")
    require(manifest&#91;"contribution_id"&#93; == "JCG-C-0015-HARVEST", "unexpected contribution ID")
    source_ids = &#91;source&#91;"id"&#93; for source in manifest&#91;"sources"&#93;&#93;
    require(len(source_ids) == len(set(source_ids)), "duplicate source ID")
    require(len(manifest&#91;"checklist"&#93;) == 11, "checklist length changed")
    statuses = {item&#91;"item"&#93;: item&#91;"status"&#93; for item in manifest&#91;"checklist"&#93;}
    require(all(status not in {"open", "not_attempted"} for status in statuses.values()),
            "an item was not attempted")
    require(statuses&#91;"Attach the stored adjacent-chart terminal certificate"&#93; == "attempted_not_covering",
            "adjacent-chart result is overstated")
    require(statuses&#91;"Prove all full-root children reach an empty terminal node"&#93;
            == "complete_for_direct_queue", "direct full-root closure not recorded")

    stage_ids = &#91;stage&#91;"id"&#93; for stage in manifest&#91;"stages"&#93;&#93;
    require(len(stage_ids) == len(set(stage_ids)) == 10,
            "stage manifest must contain ten unique stages")
    keys = ("root", "role", "status", "field", "ring", "variables",
            "ideal_or_equations", "denominators", "denominator_zero_complements",
            "saturation_factors", "output", "evidence")
    for stage in manifest&#91;"stages"&#93;:
        for key in keys:
            require(key in stage, f"stage {stage&#91;'id'&#93;} lacks {key}")
        for denominator in stage&#91;"denominators"&#93;:
            require("geometric_complement" in denominator,
                    f"stage {stage&#91;'id'&#93;} denominator lacks complement ledger")

    scheme_lift = manifest&#91;"queue"&#93;&#91;"closure"&#93;&#91;"full"&#93;&#91;"scheme_lift"&#93;
    require("full layer-through-eight obstruction scheme" in scheme_lift
            and "layer-four square hypersurface alone is not claimed empty" in scheme_lift,
            "full closure does not state the reduced/scheme-level boundary correctly")
    below = manifest&#91;"queue"&#93;&#91;"closure"&#93;&#91;"below_125"&#93;
    require(below&#91;"status"&#93; == "deduced_from_imported_reduction",
            "below-125 boundary is not explicit")
    require(not below&#91;"independent_literature_reproof"&#93;,
            "manifest falsely claims a literature reproof")
    require("SRC-GGHV-2022" in below&#91;"imports"&#93;,
            "below-125 deduction lacks the external reduction")
</code></pre>

<a id="source-7bfbfcd699f91d45"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/queue.py`

<pre><code class="language-python">
"""Proof-carrying queue validation."""
from __future__ import annotations

from typing import Any

from .common import require


def validate_queue(manifest: dict&#91;str, Any&#93;) -&gt; None:
    queue = manifest&#91;"queue"&#93;
    nodes, edges = queue&#91;"nodes"&#93;, queue&#91;"edges"&#93;
    node_ids = &#91;node&#91;"id"&#93; for node in nodes&#93;
    edge_ids = &#91;edge&#91;"id"&#93; for edge in edges&#93;
    require(len(node_ids) == len(set(node_ids)), "duplicate queue node ID")
    require(len(edge_ids) == len(set(edge_ids)), "duplicate queue edge ID")
    node_map = {node&#91;"id"&#93;: node for node in nodes}
    edge_map: dict&#91;tuple&#91;str, str&#93;, list&#91;dict&#91;str, Any&#93;&#93;&#93; = {}
    adjacency: dict&#91;str, list&#91;str&#93;&#93; = {node_id: &#91;&#93; for node_id in node_ids}
    for edge in edges:
        require(edge&#91;"from"&#93; in node_map, f"edge {edge&#91;'id'&#93;} has unknown parent")
        require(edge&#91;"to"&#93; in node_map, f"edge {edge&#91;'id'&#93;} has unknown child")
        require(edge&#91;"from"&#93; != edge&#91;"to"&#93;, f"edge {edge&#91;'id'&#93;} is a self-loop")
        edge_map.setdefault((edge&#91;"from"&#93;, edge&#91;"to"&#93;), &#91;&#93;).append(edge)
        adjacency&#91;edge&#91;"from"&#93;&#93;.append(edge&#91;"to"&#93;)

    state = {node_id: 0 for node_id in node_ids}
    def visit(node_id: str) -&gt; None:
        require(state&#91;node_id&#93; != 1, f"cycle detected at {node_id}")
        if state&#91;node_id&#93; == 2:
            return
        state&#91;node_id&#93; = 1
        for child in adjacency&#91;node_id&#93;:
            visit(child)
        state&#91;node_id&#93; = 2
    for node_id in node_ids:
        visit(node_id)

    cover_ids: set&#91;str&#93; = set()
    for group in queue&#91;"cover_groups"&#93;:
        require(group&#91;"id"&#93; not in cover_ids, f"duplicate cover group {group&#91;'id'&#93;}")
        cover_ids.add(group&#91;"id"&#93;)
        require(group&#91;"parent"&#93; in node_map, f"unknown cover parent {group&#91;'parent'&#93;}")
        require(len(group&#91;"children"&#93;) &gt;= 2, f"cover group {group&#91;'id'&#93;} is not a split")
        for child in group&#91;"children"&#93;:
            candidates = edge_map.get((group&#91;"parent"&#93;, child), &#91;&#93;)
            require(candidates, f"cover group {group&#91;'id'&#93;} lacks edge to {child}")
            require(any(edge.get("cover_group") == group&#91;"id"&#93; and edge&#91;"covering"&#93;
                        for edge in candidates), f"cover group {group&#91;'id'&#93;} edge to {child} is not covering")

    roots = {"truncated": "L8-T-ROOT", "full": "L8-F-ROOT"}
    closure_paths: dict&#91;str, list&#91;list&#91;str&#93;&#93;&#93; = {}
    for root_name in ("truncated", "full"):
        closure = queue&#91;"closure"&#93;&#91;root_name&#93;
        paths = &#91;closure&#91;"path"&#93;&#93; if "path" in closure else closure&#91;"paths"&#93;
        closure_paths&#91;root_name&#93; = paths
        for path in paths:
            require(path and path&#91;0&#93; == roots&#91;root_name&#93;, f"bad closure root for {root_name}")
            for parent, child in zip(path, path&#91;1:&#93;):
                candidates = edge_map.get((parent, child), &#91;&#93;)
                require(candidates, f"missing closure edge {parent}-&gt;{child}")
                require(any(edge&#91;"covering"&#93; for edge in candidates),
                        f"closure uses noncovering edge {parent}-&gt;{child}")
            require(node_map&#91;path&#91;-1&#93;&#93;&#91;"status"&#93;.startswith("terminal_empty"),
                    f"closure path ends at nonempty node {path&#91;-1&#93;}")

    full_paths = closure_paths&#91;"full"&#93;
    require(len(full_paths) == 2, "full closure must contain exactly two split-child paths")
    split_parent = "L8-F-SQUARE-RED"
    observed: set&#91;str&#93; = set()
    for path in full_paths:
        require(split_parent in path, f"full closure path omits {split_parent}")
        index = path.index(split_parent)
        require(index + 1 &lt; len(path), "full closure stops before a split child")
        observed.add(path&#91;index + 1&#93;)
        require("L8-ADJ-STORED" not in path, "full closure improperly uses adjacent terminal")
    require(observed == {"L8-F-T11-ZERO", "L8-F-T11-OPEN"},
            f"full closure does not cover both split children: {sorted(observed)}")
    require(queue&#91;"closure"&#93;&#91;"full"&#93;&#91;"noncovering_edges_used"&#93; == &#91;&#93;,
            "full closure records a noncovering edge")
    candidate = next(edge for edge in edges if edge&#91;"id"&#93; == "E-F-ADJ-CANDIDATE")
    require(not candidate&#91;"covering"&#93;, "adjacent candidate was promoted without a theorem")
    require(node_map&#91;"L8-ADJ-STORED"&#93;&#91;"status"&#93; == "terminal_empty_unattached",
            "adjacent terminal boundary changed")

    certificate_ids = {certificate&#91;"id"&#93; for certificate in manifest&#91;"terminal_certificates"&#93;}
    for node in nodes:
        if node&#91;"status"&#93;.startswith("terminal_empty"):
            require(node.get("certificate") in certificate_ids,
                    f"terminal node {node&#91;'id'&#93;} lacks a certificate")
</code></pre>

<a id="source-55805a9e3aea256f"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/replay.py`

<pre><code class="language-python">
"""Independent replay and stage-digest validation."""
from __future__ import annotations

from typing import Any

from .common import CONTRIBUTION_DIR, require, stage_by_id


def validate_replay(manifest: dict&#91;str, Any&#93;, summary: dict&#91;str, Any&#93;) -&gt; None:
    require(summary&#91;"schema"&#93; == "lane8-independent-raw-support-replay-v1", "unexpected replay schema")
    scripts = &#91;CONTRIBUTION_DIR / "independent_raw_support_replay.py",
               *(CONTRIBUTION_DIR / "lane8_replay").glob("*.py")&#93;
    for path in scripts:
        require("sympy" not in path.read_text(encoding="utf-8").lower(),
                f"{path.name} reintroduced a nonstandard CAS dependency")
    require(all(summary&#91;"matches_public_expected"&#93;.values()),
            "replay disagrees with public expected digests")
    require(summary&#91;"field"&#93; == manifest&#91;"field"&#93;, "field manifest disagrees with replay")

    replay = manifest&#91;"replay"&#93;
    require(summary&#91;"truncated"&#93;&#91;"minor_determinant_sha256"&#93; == replay&#91;"truncated_minor_sha256"&#93;,
            "truncated minor digest mismatch")
    require(summary&#91;"full"&#93;&#91;"final_equation_sha256"&#93; == replay&#91;"full_fifteen_sha256"&#93;,
            "fifteen-equation digest mismatch")
    require(summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"sha256"&#93; == replay&#91;"terminal_projection_sha256"&#93;,
            "terminal-projection digest mismatch")
    require(summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"zero_based_indices"&#93;
            == replay&#91;"selected_zero_based_indices"&#93;, "terminal-projection index mismatch")
    require(summary&#91;"full"&#93;&#91;"equation_manifest"&#93; == replay&#91;"equation_manifest"&#93;,
            "equation manifest mismatch")
    selected = &#91;replay&#91;"equation_manifest"&#93;&#91;index&#93; for index in replay&#91;"selected_zero_based_indices"&#93;&#93;
    require(&#91;row&#91;"term_count"&#93; for row in selected&#93; == &#91;52, 52, 23, 75, 75, 75&#93;,
            "terminal projection no longer selects the six expected equations")
    require(summary&#91;"truncated"&#93;&#91;"stage_data"&#93; == replay&#91;"truncated_stage_data"&#93;,
            "truncated stage data mismatch")
    require(summary&#91;"full"&#93;&#91;"stage_data"&#93; == replay&#91;"full_stage_data"&#93;,
            "full stage data mismatch")
    require(summary&#91;"full"&#93;&#91;"origin_vertex_parameters"&#93; == replay&#91;"origin_vertex_parameters"&#93;,
            "origin parameter mismatch")
    require(summary&#91;"full"&#93;&#91;"higher_deficiency_coefficients_projected_away"&#93;
            == replay&#91;"higher_deficiency_projection"&#93;, "higher-deficiency projection mismatch")

    for root_name in ("truncated", "full"):
        for stage in summary&#91;root_name&#93;&#91;"stage_data"&#93;:
            require(stage&#91;"inverted_parameter_polynomials"&#93; == &#91;&#93;,
                    f"unrecorded variable denominator at {root_name} layer {stage&#91;'layer'&#93;}")
            require(stage&#91;"pivot_unit_count"&#93; == len(stage&#91;"pivot_columns"&#93;),
                    f"pivot ledger mismatch at {root_name} layer {stage&#91;'layer'&#93;}")

    require(summary&#91;"truncated"&#93;&#91;"macaulay_rank"&#93; == 14, "truncated rank is not 14")
    require(summary&#91;"truncated"&#93;&#91;"weight_four_monomial_count"&#93; == 14,
            "truncated target is not complete")
    require(summary&#91;"full"&#93;&#91;"weight_four_is_square"&#93;, "layer-four square was not reconstructed")
    require(summary&#91;"full"&#93;&#91;"vertex_saturation_forces_t11_nonzero"&#93;,
            "t1_1 complement was not closed")
    require(summary&#91;"full"&#93;&#91;"final_equation_counts"&#93; == {"5": 1, "6": 3, "7": 5, "8": 6},
            "unexpected fifteen-equation weight distribution")

    require(stage_by_id(manifest, "S1-TRUNCATED-LAYERS")&#91;"evidence"&#93;&#91;"stage_data"&#93;
            == summary&#91;"truncated"&#93;&#91;"stage_data"&#93;, "stage S1 does not pin the replayed layer data")
    require(stage_by_id(manifest, "S2-FULL-LAYERS-1-4")&#91;"evidence"&#93;&#91;"stage_data"&#93;
            == summary&#91;"full"&#93;&#91;"stage_data"&#93;&#91;:4&#93;, "stage S2 does not pin layers one through four")
    require(stage_by_id(manifest, "S5-FULL-LAYERS-5-8")&#91;"evidence"&#93;&#91;"stage_data"&#93;
            == summary&#91;"full"&#93;&#91;"stage_data"&#93;&#91;4:&#93;, "stage S5 does not pin layers five through eight")
</code></pre>

<a id="source-d1f052461df06a78"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/lane8_validator/sources.py`

<pre><code class="language-python">
"""Source pins for the canonical Lane 8 harvest packet."""
from __future__ import annotations

import json
from typing import Any

from .common import CONTRIBUTION_DIR, REPOSITORY_ROOT, require, sha256_file, source_by_id


def validate_sources(manifest: dict&#91;str, Any&#93;) -&gt; None:
    reconstruction = source_by_id(manifest, "SRC-L8-RECONSTRUCTION")
    reconstruction_path = REPOSITORY_ROOT / reconstruction&#91;"path"&#93;
    require(reconstruction_path.is_file(), f"missing {reconstruction_path}")
    require(sha256_file(reconstruction_path) == reconstruction&#91;"sha256"&#93;,
            "Lane 8 reconstruction packet SHA-256 mismatch")

    source_packet = source_by_id(manifest, "SRC-L8-SOURCE-PACKET")
    source_packet_path = REPOSITORY_ROOT / source_packet&#91;"path"&#93;
    require(source_packet_path.is_file(), f"missing {source_packet_path}")
    require(sha256_file(source_packet_path) == source_packet&#91;"sha256"&#93;,
            "Lane 8 source packet SHA-256 mismatch")

    appendix = source_by_id(manifest, "SRC-PROGRAM6-APPENDIX")
    appendix_path = REPOSITORY_ROOT / appendix&#91;"path"&#93;
    require(appendix_path.is_file(), f"missing {appendix_path}")
    require(sha256_file(appendix_path) == appendix&#91;"sha256"&#93;,
            "Program 6 theorem source SHA-256 mismatch")
    appendix_text = appendix_path.read_text(encoding="utf-8")
    for label in appendix&#91;"labels"&#93;:
        require(f"\\label{{{label}}}" in appendix_text, f"missing Program 6 label {label}")
    require("4,6,8,9,10,11" in appendix_text.replace(" ", ""),
            "Program 6 source does not expose the six archived indices")

    fixture_path = CONTRIBUTION_DIR / "fixtures" / "belyi_exact_field_relations.json"
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    require(sha256_file(fixture_path) == manifest&#91;"replay"&#93;&#91;"fixture_relations_sha256"&#93;,
            "exact-relations fixture SHA-256 mismatch")
    require(fixture&#91;"minimal_polynomial"&#93;.replace(" ", "").replace("x", "u")
            == "u^5-u^4+3*u^3+3*u^2+26",
            "fixture minimal polynomial mismatch")
    require(set(fixture&#91;"relations"&#93;) == {str(index) for index in range(2, 8)},
            "fixture relation-degree inventory mismatch")

    helper_path = CONTRIBUTION_DIR / "fixtures" / "quintic_field_fast.py"
    require(sha256_file(helper_path) == manifest&#91;"replay"&#93;&#91;"fixture_field_helper_sha256"&#93;,
            "exact field-helper fixture SHA-256 mismatch")
</code></pre>

<a id="source-c23f1c6df4346e40"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/checklist.json`

<pre><code class="language-json">
&#91;{"evidence":&#91;"L8-T-ROOT","CERT-TRUNCATED-RANK"&#93;,"item":"Mark the truncated (8,28) root as closed","status":"complete"},{"evidence":&#91;"independent_raw_support_replay.py","8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059"&#93;,"item":"Independently replay the truncated-root certificate","status":"complete"},{"evidence":&#91;"stage-manifest.json"&#93;,"item":"Publish a complete stage manifest for the full-support elimination","status":"complete"},{"evidence":&#91;"S2-FULL-LAYERS-1-4"&#93;,"item":"Reconstruct layers (1)-(4) of the full root","status":"complete"},{"evidence":&#91;"S5-FULL-LAYERS-5-8","d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883"&#93;,"item":"Reconstruct the complete elimination to the fifteen equations","status":"complete"},{"evidence":&#91;"S0-FACE","S3-FULL-SQUARE-ROUTING","S4-FULL-NORMALIZATION"&#93;,"item":"Preserve every denominator-zero complement","scope":"all divisions and saturations in the public raw-support reconstruction; external face-classification complements remain imported","status":"complete_with_scope"},{"evidence":&#91;"S2-FULL-LAYERS-1-4","S3-FULL-SQUARE-ROUTING"&#93;,"item":"Distinguish reduced geometric routing from scheme-level square structure","status":"complete"},{"evidence":&#91;"S6-TORIC-PROJECTION","S7-TORIC-TERMINAL","E-F-PROJECT"&#93;,"item":"Attach the compact toric terminal certificate to the full root","status":"complete"},{"evidence":&#91;"S8-ADJACENT-STORED","S9-LANE9-ORDER-OBSTRUCTION","E-F-ADJ-CANDIDATE"&#93;,"item":"Attach the stored adjacent-chart terminal certificate","result":"the stored terminal is exact, but no valid covering edge is proved; it is not used","status":"attempted_not_covering"},{"evidence":&#91;"queue.closure.full"&#93;,"item":"Prove all full-root children reach an empty terminal node","status":"complete_for_direct_queue"},{"boundary":"not an independent reproof of the published reduction or the compact toric archive","evidence":&#91;"queue.closure.below_125"&#93;,"item":"Deduce the standalone below-125 exclusion","status":"complete_with_imported_theorems"}&#93;
</code></pre>

<a id="source-593fe9efb431bec7"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/field.json`

<pre><code class="language-json">
{"basis":&#91;"1","u","u^2","u^3","u^4"&#93;,"irreducibility_witness":{"method":"Rabin test","prime":67},"irreducible_over_Q":true,"minimal_polynomial":"u^5-u^4+3*u^3+3*u^2+26"}
</code></pre>

<a id="source-88bb00bdcf4735d7"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/queue.json`

<pre><code class="language-json">
{"closure":{"below_125":{"argument":&#91;"GGHV Theorem 2.1 leaves only the degree pair (72,108) up to symmetry.","GGHV Corollary 5.7 excludes the (9,27) case.","GGHV Proposition 4.3 routes the remaining (8,28) case to the full or truncated normalized support.","Both Lane 8 roots are empty by this manifest."&#93;,"imports":&#91;"SRC-GGHV-2022","SRC-PROGRAM6-APPENDIX"&#93;,"independent_literature_reproof":false,"statement":"There is no characteristic-zero plane Keller counterexample with max(deg P,deg Q)&lt;125.","status":"deduced_from_imported_reduction"},"full":{"noncovering_edges_used":&#91;&#93;,"paths":&#91;&#91;"L8-F-ROOT","L8-F-SQUARE-SCHEME","L8-F-SQUARE-RED","L8-F-T11-ZERO"&#93;,&#91;"L8-F-ROOT","L8-F-SQUARE-SCHEME","L8-F-SQUARE-RED","L8-F-T11-OPEN","L8-F-FIFTEEN","L8-F-TORIC-SIX"&#93;&#93;,"projection_logic":"Every exact full-support solution has a layer-through-eight image. The target necessary-condition scheme is empty, hence no higher-deficiency completion exists.","scheme_lift":"The reduced geometric support of the full layer-through-eight obstruction scheme is empty over an algebraic closure. A nonzero finite-type K0-algebra stays nonzero after faithfully flat base change and then has a maximal ideal, so the full layer-through-eight obstruction scheme retaining the square equation is empty as well; the layer-four square hypersurface alone is not claimed empty.","status":"closed"},"truncated":{"path":&#91;"L8-T-ROOT"&#93;,"status":"closed"}},"cover_groups":&#91;{"children":&#91;"L8-F-T11-ZERO","L8-F-T11-OPEN"&#93;,"id":"t11-split","identity":"V(L)=V(L,t1_1) union (V(L) intersect D(t1_1))","parent":"L8-F-SQUARE-RED"}&#93;,"edges":&#91;{"covering":true,"from":"L8-F-ROOT","id":"E-F-LAYERS","kind":"necessary_condition_projection","proof":"every exact full-support Keller pair projects to the raw deficiency-through-eight recursion; coefficients of higher deficiency are never divided by and are safely forgotten","to":"L8-F-SQUARE-SCHEME"},{"covering":true,"from":"L8-F-SQUARE-SCHEME","id":"E-F-REDUCE","kind":"underlying_reduced_support","proof":"V(L^2)=V(L) set-theoretically; the square is retained in scheme metadata","to":"L8-F-SQUARE-RED"},{"condition":"t1_1=0","cover_group":"t11-split","covering":true,"from":"L8-F-SQUARE-RED","id":"E-F-SPLIT-ZERO","kind":"open_closed_split","to":"L8-F-T11-ZERO"},{"condition":"t1_1!=0","cover_group":"t11-split","covering":true,"from":"L8-F-SQUARE-RED","id":"E-F-SPLIT-OPEN","kind":"open_closed_split","to":"L8-F-T11-OPEN"},{"covering":true,"from":"L8-F-T11-OPEN","id":"E-F-NORMALIZE","kind":"weighted_Gm_cross_section","proof":"explicit forward and inverse formulas on the early-layer open locus; U,D,t1_1 remain free units","to":"L8-F-FIFTEEN"},{"covering":true,"from":"L8-F-FIFTEEN","id":"E-F-PROJECT","kind":"relaxation","proof":"the six generators are a literal subset of the ordered fifteen","to":"L8-F-TORIC-SIX"},{"covering":false,"from":"L8-F-T11-OPEN","id":"E-F-ADJ-CANDIDATE","kind":"candidate_rechart","proof":"no covering rechart theorem; the bare k=4 shear starts at layer seven and cannot identify the layer-four residual","to":"L8-ADJ-STORED"}&#93;,"nodes":&#91;{"certificate":"CERT-TRUNCATED-RANK","id":"L8-T-ROOT","kind":"root","locus":"exact truncated support after the five-face substitution","open_factors":&#91;"coefficient(P_(0,0))=U","coefficient(Q_(0,0))=D","face endpoints p0,p7,q0,q10","coefficient(P_(8,16))","coefficient(Q_(12,24))"&#93;,"root":"truncated","status":"terminal_empty"},{"id":"L8-F-ROOT","kind":"root","locus":"exact full support after the five-face substitution","open_factors":&#91;"all eight polygon-vertex coefficients, including P_(0,8) and Q_(0,12)"&#93;,"projection_boundary":"the layer-through-eight reconstruction forgets all higher-deficiency coefficients; it is a necessary-condition projection, not a parameterization of the entire full-support coefficient space","root":"full","status":"closed"},{"id":"L8-F-SQUARE-SCHEME","kind":"scheme_node","locus":"compatibility scheme with unit*(t2_2-alpha*t1_1^2)^2","root":"full","status":"routed"},{"id":"L8-F-SQUARE-RED","kind":"reduced_support_node","locus":"t2_2=alpha*t1_1^2 with inherited exact-support saturations","root":"full","status":"routed"},{"certificate":"CERT-T11-VERTEX","id":"L8-F-T11-ZERO","kind":"closed_complement","locus":"t1_1=0 intersect exact-support vertex conditions","root":"full","status":"terminal_empty"},{"id":"L8-F-T11-OPEN","kind":"open_node","locus":"D(U*D*t1_1) in the reduced layer-through-eight necessary-condition locus","root":"full","status":"routed"},{"id":"L8-F-FIFTEEN","kind":"normalized_node","locus":"V(F0,...,F14) in algebraic_closure(K0)^5","root":"full","status":"routed"},{"certificate":"CERT-TORIC-SIX","id":"L8-F-TORIC-SIX","kind":"relaxation_terminal","locus":"V(F4,F6,F8,F9,F10,F11)","root":"full","status":"terminal_empty"},{"certificate":"CERT-ADJ-STORED","id":"L8-ADJ-STORED","kind":"stored_terminal","locus":"stored transformed layer-five-through-seven system","root":"adjacent","status":"terminal_empty_unattached"}&#93;,"roots":&#91;"L8-T-ROOT","L8-F-ROOT"&#93;}
</code></pre>

<a id="source-0422289841495ac7"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/replay-full-stages.json`

<pre><code class="language-json">
&#91;{"basis_sha256":"8201d3432e85b1ead42b0747fa32286171ca1bfba2d1b42027a6c64287594b05","inverted_parameter_polynomials":&#91;&#93;,"layer":1,"matrix_sha256":"58a43b5b88b2e0ca68874bbd2b508409490f81800b089ca12f00fa317e0b3f94","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"6dd7a3a5410cdf243f8ce2a1a80f672cbc73e92fccb846baf012c7f7af2a754d"},{"basis_sha256":"56f90fac190a96f89261323efc05db41abbece1e25eda0469b229238a6027da9","inverted_parameter_polynomials":&#91;&#93;,"layer":2,"matrix_sha256":"e652824202ccd04704ac0e975107b46df5795e3976a6f8af06b6af3190a1bd89","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"d5d332efb2cee330350526ab43badfaa6e410315ce9c0e0b0fa575af60af691b"},{"basis_sha256":"218c2be5d73ca580a8ec8a1f045d1ae8ed6f6009e03e4b88650fe387a7cc7a07","inverted_parameter_polynomials":&#91;&#93;,"layer":3,"matrix_sha256":"8a7e3d523ae4bf0c993adad8dd5a6bed5e41deac3060b1cbf2674d84b3402f7b","pivot_columns":&#91;0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,20&#93;,"pivot_unit_count":18,"pivot_units_sha256":"afa36e1bab8875a2e330e3740d3817be5022df6a83006f67cc6f36dcc85a4072"},{"basis_sha256":"11d9bc772ead372972ec6c6fbdc9207ec002a0772f632467a78e870b25e919cb","inverted_parameter_polynomials":&#91;&#93;,"layer":4,"matrix_sha256":"2db2d9e5f9b0a87aade3fef4cd8429732ceba68dabb8e8de2aadd2688e594c1c","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"a0cd7b4e9f12c9ab8a091cf7615ec884d07c17e6d70b110bd72c2bbd0074608f"},{"basis_sha256":"089ec887c10b11ef0132a17bd45d077b894b1698f6cb7ff3d43fcd123f5850e1","inverted_parameter_polynomials":&#91;&#93;,"layer":5,"matrix_sha256":"62ec9bfbae456fc70ec2b4bcd4c3e6fac1b98c1768730f74734952c3ba57d36c","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"f7073d52a9f2158c18dd22a8ff1f3e88adef40303f799b98930f5f90fe8ca43a"},{"basis_sha256":"4af93eea033599783272e2344ec48a6a80071afe08f0113e98624c6d1e842b7a","inverted_parameter_polynomials":&#91;&#93;,"layer":6,"matrix_sha256":"d2ef04ba147b885fe1268378358faa042d15f115be360ecf99d6bf5f48b46a2f","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14&#93;,"pivot_unit_count":15,"pivot_units_sha256":"1b3fe2ca43ee432ff82570fd33fd06c82c408f1d1da87966e6b9b31c03776767"},{"basis_sha256":"006a7a7321995ab8ca5e34498bf24841fc1ea3ce229c561a625a06dc3839752a","inverted_parameter_polynomials":&#91;&#93;,"layer":7,"matrix_sha256":"cf50345c5970539914b1de3d78058e51a99549224482f2d90bcdeaa072d61ca9","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12&#93;,"pivot_unit_count":13,"pivot_units_sha256":"a11fd90b963720f84087358c10dbb18939a19a89e241553032de27df97fb4558"},{"basis_sha256":"d8250d71b48a6c273030e0bab44fc1033997cc669473a30c8364aba017fc114a","inverted_parameter_polynomials":&#91;&#93;,"layer":8,"matrix_sha256":"27b44013be558dc3018da7977b6b6520610ce935e7e5a7b8567a4d12c59a88f3","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10&#93;,"pivot_unit_count":11,"pivot_units_sha256":"71b63dbd3102eb50520b0ae50cdf4c8faba3d2573f6f3307274c2227ea596eda"}&#93;
</code></pre>

<a id="source-ee3fb966b7e4afcb"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/replay-truncated-stages.json`

<pre><code class="language-json">
&#91;{"basis_sha256":"8201d3432e85b1ead42b0747fa32286171ca1bfba2d1b42027a6c64287594b05","inverted_parameter_polynomials":&#91;&#93;,"layer":1,"matrix_sha256":"58a43b5b88b2e0ca68874bbd2b508409490f81800b089ca12f00fa317e0b3f94","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"6dd7a3a5410cdf243f8ce2a1a80f672cbc73e92fccb846baf012c7f7af2a754d"},{"basis_sha256":"56f90fac190a96f89261323efc05db41abbece1e25eda0469b229238a6027da9","inverted_parameter_polynomials":&#91;&#93;,"layer":2,"matrix_sha256":"e652824202ccd04704ac0e975107b46df5795e3976a6f8af06b6af3190a1bd89","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"d5d332efb2cee330350526ab43badfaa6e410315ce9c0e0b0fa575af60af691b"},{"basis_sha256":"77849fe9039c2adaa8757eaa5202ccc1944e65aca521a6a15b2a4b1950466bb8","inverted_parameter_polynomials":&#91;&#93;,"layer":3,"matrix_sha256":"92aebab2a3eb46dd04c50d9945d9c1e49422f15e3a0e5a40c77900dba45a30db","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12&#93;,"pivot_unit_count":12,"pivot_units_sha256":"c88305cb6949dfc19a85ea749cf50901557612eba7122da38fd13352ab8b0efd"},{"basis_sha256":"95a58979964db7dab23e892d65ec8b3cd49ab1de2959106f81a2deec0ee78d2b","inverted_parameter_polynomials":&#91;&#93;,"layer":4,"matrix_sha256":"8c6e351b83642ea4d58e5bb456624576be95d6ad699a0d0e0f71ba49e32b2356","pivot_columns":&#91;&#93;,"pivot_unit_count":0,"pivot_units_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"},{"basis_sha256":"ddafdf46e8ca39a8be60901dc1b7f9fc4383a3b105366a793b08aafd32a3d943","inverted_parameter_polynomials":&#91;&#93;,"layer":5,"matrix_sha256":"bb45d92a89f3927d38c9c14d673e8fb4e10328ea2c888fa46e951ebfd8b2e9bc","pivot_columns":&#91;&#93;,"pivot_unit_count":0,"pivot_units_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"}&#93;
</code></pre>

<a id="source-546e947b1ca05fc3"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/replay.json`

<pre><code class="language-json">
{"archived_equations_used":false,"archived_layers_used":false,"entrypoint":"independent_raw_support_replay.py","equation_manifest":&#91;{"index":0,"sha256":"1138bfb34e507932850c240a5db2bf4fe1dd61437f7c15961371dfdc7f8cba51","term_count":22,"weight":5},{"index":1,"sha256":"e92fe06e1e5b74bfcdb008cbcc0aa31a5e98608094a574035f6a34686eadb1cf","term_count":35,"weight":6},{"index":2,"sha256":"f1a0e3f66fefc9979e222aa9b563ca2d8ba2d8292c212ac0a7e3182d7917046b","term_count":35,"weight":6},{"index":3,"sha256":"7258119efbdedf0710cc86a06ef09e4047b6c6cc4be6515d282113bd645f8262","term_count":23,"weight":6},{"index":4,"sha256":"851f565c57212b3aadf22fcb61cc9470d2c194868ef679e409f793b08c19cb41","term_count":52,"weight":7},{"index":5,"sha256":"a48ece6e69c103c6a32e39201a3e56f3ba0b7a9048e6c08b9715d8ae3187b7b2","term_count":52,"weight":7},{"index":6,"sha256":"d9e0776f8d68a71bd161a2b553d87b5eb21c2f4d7c87a517ccda87e1ba858c6e","term_count":52,"weight":7},{"index":7,"sha256":"4449f88c75ef9b6cd7c36ab3ca8eb7e894f4ef12ee3b4a5f5b85ec18fcda5758","term_count":45,"weight":7},{"index":8,"sha256":"5d3d16aabbe9dd39877d36a04f3b0d3562cf2a923fa134926f9dfb9d0ea38a4f","term_count":23,"weight":7},{"index":9,"sha256":"0c5b875304b1862761e69ee3800be6a0e517065ec3fc7c3d84e23c2ddf2c5d23","term_count":75,"weight":8},{"index":10,"sha256":"902299536d933e8bab617657a338fb0f2cc61d598596692c1b0425784b3a4a10","term_count":75,"weight":8},{"index":11,"sha256":"37d97e104e980bfa5fd9d055eaafc3f3981c28b1fbdf324ce899893423f18700","term_count":75,"weight":8},{"index":12,"sha256":"143ef7910ade145c5842c35982a36ecd60c13f6decbf9f913770e15849502346","term_count":75,"weight":8},{"index":13,"sha256":"e7167f8e15bf4ddbbe07a0903cf5a5aa7f3e0484bc96780458764bfa8fdb78f4","term_count":73,"weight":8},{"index":14,"sha256":"6a4e10544dd1f9f0620c7c0a5129804304efde0d60d32426743f83fa4fece43f","term_count":55,"weight":8}&#93;,"fixture_field_helper_sha256":"028cac6094ae01d090c4cefecc62bd77261d8e5218c013e7af4457e864610600","fixture_relations_sha256":"5f20a89c3b832fea512f16a9452762d461f0fd783266ad91cbe72972ed38e7b8","full_fifteen_sha256":"d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883","full_stage_data":{"$include":"manifest/replay-full-stages.json"},"higher_deficiency_projection":{"P":3,"Q":28,"cutoff":8,"extra_vertices":{"P_(0,8)":10,"Q_(0,12)":15}},"origin_vertex_parameters":{"P_(0,0)":"parameter_index_2","Q_(0,0)":"parameter_index_5"},"public_relations_projection":"minimal_polynomial and relations; the decimal embedding is unused","selected_zero_based_indices":&#91;4,6,8,9,10,11&#93;,"terminal_projection_sha256":"e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a","truncated_minor_sha256":"8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059","truncated_stage_data":{"$include":"manifest/replay-truncated-stages.json"}}
</code></pre>

<a id="source-872badec8715a0c5"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/sources.json`

<pre><code class="language-json">
&#91;
  {
    "id": "SRC-L8-HANDOFF",
    "kind": "project_handoff",
    "path": "private-source/research-handoff-v6f/lanes/plane-newton-queue-terminal-certificates.md",
    "role": "pre-harvest checklist, support roots, and queue semantics",
    "status": "audited_input"
  },
  {
    "id": "SRC-L8-RECONSTRUCTION",
    "kind": "project_packet",
    "path": "research-notes/lane8-full-root-closure-20260803-v1/FULL_ROOT_CLOSURE_PROOF.md",
    "role": "complete raw-support reconstruction, complement ledger, and proof assembly",
    "sha256": "2eeb8b32471a6d0cc46bbdb35adb3e58a9aaa055c44fb3399970f53e9eb1e670",
    "status": "independently_replayed"
  },
  {
    "id": "SRC-L8-SOURCE-PACKET",
    "kind": "project_packet",
    "path": "research-notes/lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md",
    "role": "earlier truncated-root reconstruction and queue boundary",
    "sha256": "bdbe6c5557e93c3dbafac75ffbf3c833eb22d5988af9e3f7bfcbdd4b040b94f0",
    "status": "hash_pinned_input"
  },
  {
    "id": "SRC-PROGRAM6-APPENDIX",
    "kind": "project_theorem_source",
    "labels": &#91;
      "prop:terminal-residue-provenance",
      "thm:terminal-toric-certificate",
      "prop:k4-chart-transition",
      "thm:stored-terminal-layer-seven"
    &#93;,
    "path": "manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex",
    "role": "coefficientwise terminal projection, compact toric theorem, and adjacent-chart boundary",
    "sha256": "dd35e507d5c0c41255853ff37676d96f2d09255f76ca9fe2f4e044fc99423ba2",
    "status": "imported_exact_theorems"
  },
  {
    "citation": "J. A. Guccione, J. J. Guccione, R. Horruitiner, C. Valqui, arXiv:2204.14178v1",
    "id": "SRC-GGHV-2022",
    "kind": "external_theorem",
    "role": "below-125 reduction to the (8,28) case and its two normalized supports, with the other (9,27) case excluded",
    "statements": &#91;
      "Theorem 2.1",
      "Proposition 4.1",
      "Proposition 4.3",
      "Corollary 5.7"
    &#93;,
    "status": "primary_source_inspected_not_reproved"
  }
&#93;
</code></pre>

<a id="source-68539ea3cb17d0c9"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s0-face.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;{"factor":"p0*q0","resolution":"constant coefficient equation gives p0*q0=1"},{"factor":"p1","resolution":"nonvanishing belongs to the imported five-face classification and fixes z-scaling"}&#93;,"denominators":&#91;{"factor":"relation coefficient r_d,5 for d=2,...,7","geometric_complement":"none","type":"nonzero rational integer"},{"factor":"1+2*d for d=1,...,10","geometric_complement":"none","type":"nonzero rational integer"}&#93;,"evidence":{"irreducibility_witness":{"method":"Rabin test","prime":67},"relations_sha256":"5f20a89c3b832fea512f16a9452762d461f0fd783266ad91cbe72972ed38e7b8"},"field":"K0","id":"S0-FACE","ideal_or_equations":{"generators":"the 18 coefficients of p*q+2*z*p*q_prime-3*z*p_prime*q-1","normalization":&#91;"p0=1","q0=1","p1=1"&#93;},"output":{"field_orbit_degree":5,"jacobian_coefficients_checked":18,"p_degree":7,"q_degree":10},"ring":"K0&#91;p0,...,p7,q0,...,q10&#93;","role":"reconstruct the forced degree-21 lower face","root":"both","saturation_factors":&#91;"p0","q0","p1","p7","q10"&#93;,"status":"replayed_exact","variables":&#91;"p0","p1","p2","p3","p4","p5","p6","p7","q0","q1","q2","q3","q4","q5","q6","q7","q8","q9","q10"&#93;}
</code></pre>

<a id="source-6f17b4887d709bb1"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s1-truncated-layers.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;{"factor":"all Gaussian pivots","geometric_complement":"none","type":"fixed nonzero elements of K0"}&#93;,"evidence":{"matches_public_digest":true,"minor_determinant_sha256":"8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059","stage_data":&#91;{"basis_sha256":"8201d3432e85b1ead42b0747fa32286171ca1bfba2d1b42027a6c64287594b05","inverted_parameter_polynomials":&#91;&#93;,"layer":1,"matrix_sha256":"58a43b5b88b2e0ca68874bbd2b508409490f81800b089ca12f00fa317e0b3f94","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"6dd7a3a5410cdf243f8ce2a1a80f672cbc73e92fccb846baf012c7f7af2a754d"},{"basis_sha256":"56f90fac190a96f89261323efc05db41abbece1e25eda0469b229238a6027da9","inverted_parameter_polynomials":&#91;&#93;,"layer":2,"matrix_sha256":"e652824202ccd04704ac0e975107b46df5795e3976a6f8af06b6af3190a1bd89","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"d5d332efb2cee330350526ab43badfaa6e410315ce9c0e0b0fa575af60af691b"},{"basis_sha256":"77849fe9039c2adaa8757eaa5202ccc1944e65aca521a6a15b2a4b1950466bb8","inverted_parameter_polynomials":&#91;&#93;,"layer":3,"matrix_sha256":"92aebab2a3eb46dd04c50d9945d9c1e49422f15e3a0e5a40c77900dba45a30db","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12&#93;,"pivot_unit_count":12,"pivot_units_sha256":"c88305cb6949dfc19a85ea749cf50901557612eba7122da38fd13352ab8b0efd"},{"basis_sha256":"95a58979964db7dab23e892d65ec8b3cd49ab1de2959106f81a2deec0ee78d2b","inverted_parameter_polynomials":&#91;&#93;,"layer":4,"matrix_sha256":"8c6e351b83642ea4d58e5bb456624576be95d6ad699a0d0e0f71ba49e32b2356","pivot_columns":&#91;&#93;,"pivot_unit_count":0,"pivot_units_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"},{"basis_sha256":"ddafdf46e8ca39a8be60901dc1b7f9fc4383a3b105366a793b08aafd32a3d943","inverted_parameter_polynomials":&#91;&#93;,"layer":5,"matrix_sha256":"bb45d92a89f3927d38c9c14d673e8fb4e10328ea2c888fa46e951ebfd8b2e9bc","pivot_columns":&#91;&#93;,"pivot_unit_count":0,"pivot_units_sha256":"4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"}&#93;},"field":"K0","id":"S1-TRUNCATED-LAYERS","ideal_or_equations":{"effective_variables":&#91;"X","Y","V","W"&#93;,"layer_data":&#91;&#91;1,19,18,17,2,0&#93;,&#91;2,21,19,18,3,0&#93;,&#91;3,13,20,12,1,7&#93;,&#91;4,0,20,0,0,18&#93;,&#91;5,0,21,0,0,0&#93;&#93;,"weight_four_generators":18,"weight_three_generators":7},"output":{"conclusion":"the exact-support locus is empty","macaulay_target":"all 14 weight-four monomials in X,Y,V,W","rank":14},"ring":"K0&#91;X,Y,U,V,W,D&#93;","role":"solve all layers and form the truncated obstruction ideal","root":"truncated","saturation_factors":&#91;"U","D","coefficient(P_(8,16))","coefficient(Q_(12,24))"&#93;,"status":"closed","variables":&#91;"X","Y","U","V","W","D"&#93;}
</code></pre>

<a id="source-3a7b99d8233b2143"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s2-full-layers-1-4.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;{"factor":"all Gaussian pivots","geometric_complement":"none","type":"fixed nonzero elements of K0"}&#93;,"evidence":{"stage_data":&#91;{"basis_sha256":"8201d3432e85b1ead42b0747fa32286171ca1bfba2d1b42027a6c64287594b05","inverted_parameter_polynomials":&#91;&#93;,"layer":1,"matrix_sha256":"58a43b5b88b2e0ca68874bbd2b508409490f81800b089ca12f00fa317e0b3f94","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"6dd7a3a5410cdf243f8ce2a1a80f672cbc73e92fccb846baf012c7f7af2a754d"},{"basis_sha256":"56f90fac190a96f89261323efc05db41abbece1e25eda0469b229238a6027da9","inverted_parameter_polynomials":&#91;&#93;,"layer":2,"matrix_sha256":"e652824202ccd04704ac0e975107b46df5795e3976a6f8af06b6af3190a1bd89","pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"d5d332efb2cee330350526ab43badfaa6e410315ce9c0e0b0fa575af60af691b"},{"basis_sha256":"218c2be5d73ca580a8ec8a1f045d1ae8ed6f6009e03e4b88650fe387a7cc7a07","inverted_parameter_polynomials":&#91;&#93;,"layer":3,"matrix_sha256":"8a7e3d523ae4bf0c993adad8dd5a6bed5e41deac3060b1cbf2674d84b3402f7b","pivot_columns":&#91;0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,20&#93;,"pivot_unit_count":18,"pivot_units_sha256":"afa36e1bab8875a2e330e3740d3817be5022df6a83006f67cc6f36dcc85a4072"},{"basis_sha256":"11d9bc772ead372972ec6c6fbdc9207ec002a0772f632467a78e870b25e919cb","inverted_parameter_polynomials":&#91;&#93;,"layer":4,"matrix_sha256":"2db2d9e5f9b0a87aade3fef4cd8429732ceba68dabb8e8de2aadd2688e594c1c","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18&#93;,"pivot_unit_count":18,"pivot_units_sha256":"a0cd7b4e9f12c9ab8a091cf7615ec884d07c17e6d70b110bd72c2bbd0074608f"}&#93;,"weight_four_is_square":true},"field":"K0","id":"S2-FULL-LAYERS-1-4","ideal_or_equations":{"compatibility_output":"unit*(t2_2-alpha*t1_1^2)^2","layer_data":&#91;&#91;1,19,18,17,2,0&#93;,&#91;2,21,19,18,3,0&#93;,&#91;3,21,20,18,3,0&#93;,&#91;4,19,20,18,1,2&#93;&#93;},"output":{"alpha_basis":&#91;"52997840439195400499214253529193985607/31417214745025250638518288384","5555918314866222562593336157913468353/2416708826540403895270637568","2372511924832314307988492642389521871/31417214745025250638518288384","-7979171228684868353152453773971375057/31417214745025250638518288384","1765973597254894233103892181936480871/15708607372512625319259144192"&#93;,"projection_boundary":"only coefficients of deficiency at most four are reconstructed here; higher-deficiency coefficients are untouched","scheme_equation":"unit*(t2_2-alpha*t1_1^2)^2","top_P_after_reduction":{"coefficient_basis":&#91;"545767170557029296400958821855081486974617222217235/161290579756076107957467128715609636864","2732609956648367937078978269116651840935140706617/9305225755158236997546180502823632896","-25677608043823499688979070361945837564582380055739/80645289878038053978733564357804818432","10161369770629785945022030510226645058680020564313/13440881646339675663122260726300803072","95088719512342234810569345434148348611119581793553/483871739268228323872401386146828910592"&#93;,"t11_exponent":2},"top_Q_after_reduction":{"coefficient_basis":&#91;"-11899410448443124612343017144434297657884119944380542509493922501507883106285/2961124147005096073471666521404038876286989802498967994368","147669325007525328675357551578911153087968024415983490555484714248619605587/56944695134713386028301279257769978390134419278826307584","2456116201140611605932150937143062385730665692801250187400766473470324848581/1480562073502548036735833260702019438143494901249483997184","-630454251485783782110282606428671911434853961775292385332913332102461809973/740281036751274018367916630351009719071747450624741998592","-2688663464413868993115596141007932491178714344313110845202665512075045951/109671264703892447165617278570519958380999622314776592384"&#93;,"t11_exponent":3},"underlying_reduced_equation":"t2_2-alpha*t1_1^2"},"ring":"K0&#91;t1_0,t1_1,U,t2_1,t2_2,D,t3_1,t3_2,t4_0&#93;","role":"solve the raw full-support recursion through layer four","root":"full","saturation_factors":&#91;"U=coefficient(P_(0,0))","D=coefficient(Q_(0,0))","coefficient(P_(8,16))","coefficient(Q_(12,24))"&#93;,"status":"replayed_exact","variables":&#91;"t1_0","t1_1","U","t2_1","t2_2","D","t3_1","t3_2","t4_0"&#93;}
</code></pre>

<a id="source-c0d6bbf214c90a82"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s3-full-square-routing.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;{"factor":"t1_1","locus":"t1_1=0","resolution":"both required top vertices vanish because their coefficients are c_P*t1_1^2 and c_Q*t1_1^3 with c_P,c_Q nonzero"},{"factor":"U","locus":"U=0","resolution":"U is coefficient(P_(0,0)); U=0 leaves the declared exact support"},{"factor":"D","locus":"D=0","resolution":"D is coefficient(Q_(0,0)); D=0 leaves the declared exact support"}&#93;,"denominators":&#91;&#93;,"evidence":{"vertex_saturation_forces_t1_1_nonzero":true},"field":"K0","id":"S3-FULL-SQUARE-ROUTING","ideal_or_equations":{"forgotten_full_support_data":"all coefficients of deficiency greater than eight, including the extra vertices P_(0,8) and Q_(0,12), are projected away without division; the empty relaxation therefore covers their zero and nonzero loci simultaneously","geometric_support":"replace the square by its radical only for point-set emptiness","scheme_structure":"the unreduced ideal contains the square of the displayed linear factor"},"output":{"closed_t1_1_complement":"empty","only_surviving_early_layer_exact_support_branch":"D(U*D*t1_1)"},"ring":"K0&#91;t1_0,t1_1,U,t2_1,t2_2,D,t3_1,t3_2,t4_0&#93;/(t2_2-alpha*t1_1^2)","role":"separate scheme structure from geometric routing and audit the normalization complement","root":"full","saturation_factors":&#91;"U","D","t1_1"&#93;,"status":"closed_complement_audited","variables":&#91;"t1_0","t1_1","U","t2_1","t2_2","D","t3_1","t3_2","t4_0"&#93;}
</code></pre>

<a id="source-dbc1ad9159b2251f"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s4-full-normalization.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;{"factor":"t1_1","resolution":"S3-FULL-SQUARE-ROUTING"}&#93;,"denominators":&#91;{"factor":"t1_1","geometric_complement":"closed and empty at S3","type":"geometric localization"}&#93;,"evidence":{"parameter_weights":&#91;1,1,2,2,2,3,3,3,4&#93;},"field":"K0","id":"S4-FULL-NORMALIZATION","ideal_or_equations":{"forward":&#91;"U_norm=U/t1_1^2","D_norm=D/t1_1^3","x=t1_0/t1_1","a=t2_1/t1_1^2","b=t3_1/t1_1^3","c=t3_2/t1_1^3","d=t4_0/t1_1^4"&#93;,"inverse":&#91;"U=t1_1^2*U_norm","D=t1_1^3*D_norm","t1_0=t1_1*x","t2_1=t1_1^2*a","t2_2=alpha*t1_1^2","t3_1=t1_1^3*b","t3_2=t1_1^3*c","t4_0=t1_1^4*d"&#93;,"isomorphism":"the early-layer locus D(U*D*t1_1) is isomorphic to G_m^3 with coordinates (U_norm,D_norm,t1_1) times the normalized five-variable locus"},"output":{"free_unit_factors":&#91;"U_norm","D_norm","t1_1"&#93;,"normalization":&#91;"t1_1=1","t2_2=alpha"&#93;,"normalized_variables":&#91;"x","a","b","c","d"&#93;,"relation_to_full_support":"every full-support solution maps to this early-layer locus; higher-deficiency coefficients are free only after satisfying these necessary equations"},"ring":"K0&#91;U_norm^+-1,D_norm^+-1,t1_1^+-1,x,a,b,c,d&#93;","role":"take the weighted G_m cross-section t1_1=1 on the early-layer necessary-condition locus","root":"full","saturation_factors":&#91;"U","D","t1_1"&#93;,"status":"exact_isomorphism_on_open_locus","variables":&#91;"U_norm","D_norm","t1_1","x","a","b","c","d"&#93;}
</code></pre>

<a id="source-c1b0583cf38dfd28"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s5-full-layers-5-8.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;{"factor":"all Gaussian pivots and equation normalizing coefficients","geometric_complement":"none","type":"fixed nonzero elements of K0"}&#93;,"evidence":{"matches_public_digest":true,"stage_data":&#91;{"basis_sha256":"089ec887c10b11ef0132a17bd45d077b894b1698f6cb7ff3d43fcd123f5850e1","inverted_parameter_polynomials":&#91;&#93;,"layer":5,"matrix_sha256":"62ec9bfbae456fc70ec2b4bcd4c3e6fac1b98c1768730f74734952c3ba57d36c","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16&#93;,"pivot_unit_count":17,"pivot_units_sha256":"f7073d52a9f2158c18dd22a8ff1f3e88adef40303f799b98930f5f90fe8ca43a"},{"basis_sha256":"4af93eea033599783272e2344ec48a6a80071afe08f0113e98624c6d1e842b7a","inverted_parameter_polynomials":&#91;&#93;,"layer":6,"matrix_sha256":"d2ef04ba147b885fe1268378358faa042d15f115be360ecf99d6bf5f48b46a2f","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12,13,14&#93;,"pivot_unit_count":15,"pivot_units_sha256":"1b3fe2ca43ee432ff82570fd33fd06c82c408f1d1da87966e6b9b31c03776767"},{"basis_sha256":"006a7a7321995ab8ca5e34498bf24841fc1ea3ce229c561a625a06dc3839752a","inverted_parameter_polynomials":&#91;&#93;,"layer":7,"matrix_sha256":"cf50345c5970539914b1de3d78058e51a99549224482f2d90bcdeaa072d61ca9","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10,11,12&#93;,"pivot_unit_count":13,"pivot_units_sha256":"a11fd90b963720f84087358c10dbb18939a19a89e241553032de27df97fb4558"},{"basis_sha256":"d8250d71b48a6c273030e0bab44fc1033997cc669473a30c8364aba017fc114a","inverted_parameter_polynomials":&#91;&#93;,"layer":8,"matrix_sha256":"27b44013be558dc3018da7977b6b6520610ce935e7e5a7b8567a4d12c59a88f3","pivot_columns":&#91;0,1,2,3,4,5,6,7,8,9,10&#93;,"pivot_unit_count":11,"pivot_units_sha256":"71b63dbd3102eb50520b0ae50cdf4c8faba3d2573f6f3307274c2227ea596eda"}&#93;},"field":"K0","id":"S5-FULL-LAYERS-5-8","ideal_or_equations":{"distinct_counts_by_weight":{"5":1,"6":3,"7":5,"8":6},"layer_data":&#91;&#91;5,17,21,17,0,2&#93;,&#91;6,15,20,15,0,4&#93;,&#91;7,13,19,13,0,5&#93;,&#91;8,11,18,11,0,6&#93;&#93;,"ordered_generators":"F0,...,F14"},"output":{"canonical_sha256":"d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883","equation_manifest":&#91;{"index":0,"sha256":"1138bfb34e507932850c240a5db2bf4fe1dd61437f7c15961371dfdc7f8cba51","term_count":22,"weight":5},{"index":1,"sha256":"e92fe06e1e5b74bfcdb008cbcc0aa31a5e98608094a574035f6a34686eadb1cf","term_count":35,"weight":6},{"index":2,"sha256":"f1a0e3f66fefc9979e222aa9b563ca2d8ba2d8292c212ac0a7e3182d7917046b","term_count":35,"weight":6},{"index":3,"sha256":"7258119efbdedf0710cc86a06ef09e4047b6c6cc4be6515d282113bd645f8262","term_count":23,"weight":6},{"index":4,"sha256":"851f565c57212b3aadf22fcb61cc9470d2c194868ef679e409f793b08c19cb41","term_count":52,"weight":7},{"index":5,"sha256":"a48ece6e69c103c6a32e39201a3e56f3ba0b7a9048e6c08b9715d8ae3187b7b2","term_count":52,"weight":7},{"index":6,"sha256":"d9e0776f8d68a71bd161a2b553d87b5eb21c2f4d7c87a517ccda87e1ba858c6e","term_count":52,"weight":7},{"index":7,"sha256":"4449f88c75ef9b6cd7c36ab3ca8eb7e894f4ef12ee3b4a5f5b85ec18fcda5758","term_count":45,"weight":7},{"index":8,"sha256":"5d3d16aabbe9dd39877d36a04f3b0d3562cf2a923fa134926f9dfb9d0ea38a4f","term_count":23,"weight":7},{"index":9,"sha256":"0c5b875304b1862761e69ee3800be6a0e517065ec3fc7c3d84e23c2ddf2c5d23","term_count":75,"weight":8},{"index":10,"sha256":"902299536d933e8bab617657a338fb0f2cc61d598596692c1b0425784b3a4a10","term_count":75,"weight":8},{"index":11,"sha256":"37d97e104e980bfa5fd9d055eaafc3f3981c28b1fbdf324ce899893423f18700","term_count":75,"weight":8},{"index":12,"sha256":"143ef7910ade145c5842c35982a36ecd60c13f6decbf9f913770e15849502346","term_count":75,"weight":8},{"index":13,"sha256":"e7167f8e15bf4ddbbe07a0903cf5a5aa7f3e0484bc96780458764bfa8fdb78f4","term_count":73,"weight":8},{"index":14,"sha256":"6a4e10544dd1f9f0620c7c0a5129804304efde0d60d32426743f83fa4fece43f","term_count":55,"weight":8}&#93;,"generator_count":15,"projection_boundary":"these fifteen equations are necessary for every full-support completion; coefficients of deficiency greater than eight cannot alter them"},"ring":"K0&#91;x,a,b,c,d&#93;","role":"continue the exact recursion and deduplicate normalized compatibility equations","root":"full","saturation_factors":&#91;&#93;,"status":"replayed_exact","variables":&#91;"x","a","b","c","d"&#93;}
</code></pre>

<a id="source-cddc42b218cb9b0f"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s6-toric-projection.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;&#93;,"evidence":{"source_label":"prop:terminal-residue-provenance"},"field":"K0","id":"S6-TORIC-PROJECTION","ideal_or_equations":{"logical_direction":"V(F0,...,F14) is contained in V(F4,F6,F8,F9,F10,F11)","parent_ideal":"(F0,...,F14)","selected_ideal":"(F4,F6,F8,F9,F10,F11)"},"output":{"canonical_sha256":"e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a","selected_zero_based_indices":&#91;4,6,8,9,10,11&#93;},"ring":"K0&#91;x,a,b,c,d&#93;","role":"attach the compact terminal system as a relaxation of the fifteen-equation locus","root":"full","saturation_factors":&#91;&#93;,"status":"proved_consequence_edge","variables":&#91;"x","a","b","c","d"&#93;}
</code></pre>

<a id="source-4157d50990ad2a23"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s7-toric-terminal.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;&#93;,"evidence":{"source_label":"thm:terminal-toric-certificate"},"field":"K0","id":"S7-TORIC-TERMINAL","ideal_or_equations":{"generators":&#91;"rho=F4","g1=F6","g2=F8","g3=F9","g4=F10","g5=F11"&#93;},"output":{"geometric_conclusion":"V(rho,g1,g2,g3,g4,g5)(algebraic_closure(K0)) is empty","good_fiber":{"mixed_volume":296,"monomial_faces":270,"prime":2053,"proper_faces":344,"rho_determinant_mod_prime":682,"saturated_unit_faces":74,"u_value":216},"norm_product_mod_2053":51,"split_embedding_determinants_mod_2053":&#91;682,116,337,242,740&#93;},"ring":"K0&#91;x,a,b,c,d&#93;","role":"apply the existing compact toric terminal theorem","root":"full","saturation_factors":&#91;&#93;,"status":"terminal_empty_imported_exact","variables":&#91;"x","a","b","c","d"&#93;}
</code></pre>

<a id="source-641b3ee74f85e4a3"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s8-adjacent-stored.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;{"factor":"D(x)","locus":"D=0","resolution":"stored exact Nullstellensatz identity"},{"factor":"D(x)","locus":"D!=0","resolution":"eliminate d; weighted compactification excludes the resulting five-generator system"}&#93;,"denominators":&#91;{"factor":"D(x)","geometric_complement":"the D=0 branch has its own exact nineteen-term unit identity","type":"stored branch split"}&#93;,"evidence":{"source_label":"thm:stored-terminal-layer-seven"},"field":"K0","id":"S8-ADJACENT-STORED","ideal_or_equations":{"stored_system":"displayed layers five through seven after the adjacent-chart linear equation"},"output":{"coverage_from_full_root":"not proved","stored_system_conclusion":"empty"},"ring":"K0&#91;x,a,b,d&#93; before the stored D=0/D!=0 split; K0&#91;x,a,b&#93; after eliminating d on D!=0","role":"record the exact stored adjacent-chart terminal certificate without asserting coverage","root":"adjacent","saturation_factors":&#91;&#93;,"status":"terminal_empty_but_unattached","variables":&#91;"x","a","b","d"&#93;}
</code></pre>

<a id="source-6f0975d7fc918e96"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/stages/s9-lane9-order-obstruction.json`

<pre><code class="language-json">
{"denominator_zero_complements":&#91;&#93;,"denominators":&#91;{"factor":"z","geometric_complement":"belongs to the separate chart compactification problem","type":"Laurent chart coordinate"}&#93;,"evidence":{"source_label":"prop:k4-chart-transition"},"field":"K0","id":"S9-LANE9-ORDER-OBSTRUCTION","ideal_or_equations":{"transformation":&#91;"t_prime=t*(1+h)","z_prime=z*(1+h)^2","h=lambda*t^7*z^-4"&#93;},"output":{"claimed_layer_four_bridge":false,"first_normal_order":7,"weaker_sufficient_lane8_result":"the direct toric route closes the full root, so no adjacent-chart covering theorem is needed for Lane 8"},"ring":"K0((z))&#91;&#91;t&#93;&#93;","role":"test the proposed bare k=4 wall shear as a covering bridge","root":"adjacent","saturation_factors":&#91;&#93;,"status":"negative_lemma_proved_bridge_blocked","variables":&#91;"t","z","lambda"&#93;}
</code></pre>

<a id="source-77da4c6680fab5f7"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/terminal-certificates.json`

<pre><code class="language-json">
&#91;{"claim":"empty exact-support locus","data":{"minor_sha256":"8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059","rank":14,"target_monomials":14},"id":"CERT-TRUNCATED-RANK","node":"L8-T-ROOT","status":"replayed_here"},{"claim":"empty exact-support complement","data":{"P_endpoint":"c_P*t1_1^2","Q_endpoint":"c_Q*t1_1^3","c_P_nonzero":true,"c_Q_nonzero":true},"id":"CERT-T11-VERTEX","node":"L8-F-T11-ZERO","status":"proved_here"},{"claim":"empty six-equation locus","id":"CERT-TORIC-SIX","node":"L8-F-TORIC-SIX","source":"SRC-PROGRAM6-APPENDIX","source_label":"thm:terminal-toric-certificate","status":"imported_exact_attached_here"},{"claim":"stored transformed system empty","id":"CERT-ADJ-STORED","node":"L8-ADJ-STORED","source":"SRC-PROGRAM6-APPENDIX","source_label":"thm:stored-terminal-layer-seven","status":"imported_exact_not_covering"}&#93;
</code></pre>

<a id="source-8ba456338695e7f2"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/theorem-scope.json`

<pre><code class="language-json">
{"full_root_projection":"the replay proves emptiness of the layer-through-eight necessary-condition scheme; this excludes the exact full support because every completion projects to that scheme. Higher-deficiency coefficients are not reconstructed or divided by.","geometric_target":"set-theoretic emptiness over an algebraic closure in characteristic zero","global_boundary":"the below-125 corollary imports the published Newton-polygon reduction and the existing exact face and toric theorems; this contribution does not reprove those external inputs","scheme_boundary":"the layer-four square is retained as a nonreduced double hyperplane; only its underlying support is used for routing"}
</code></pre>

<a id="source-b98b1e3b33c17163"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/manifest/variable-systems.json`

<pre><code class="language-json">
{"full_normalized":&#91;{"definition":"t1_0/t1_1","name":"x","weight":1},{"definition":"t2_1/t1_1^2","name":"a","weight":2},{"definition":"t3_1/t1_1^3","name":"b","weight":3},{"definition":"t3_2/t1_1^3","name":"c","weight":3},{"definition":"t4_0/t1_1^4","name":"d","weight":4}&#93;,"full_raw":&#91;{"index":0,"name":"t1_0","role":"retained","weight":1},{"index":1,"name":"t1_1","role":"normalizing parameter","weight":1},{"index":2,"name":"U","role":"split origin-vertex parameter","weight":2},{"index":3,"name":"t2_1","role":"retained","weight":2},{"index":4,"name":"t2_2","role":"square parameter","weight":2},{"index":5,"name":"D","role":"split origin-vertex parameter","weight":3},{"index":6,"name":"t3_1","role":"retained","weight":3},{"index":7,"name":"t3_2","role":"retained","weight":3},{"index":8,"name":"t4_0","role":"retained","weight":4}&#93;,"truncated_raw":&#91;{"name":"X","role":"effective layer-one parameter","weight":1},{"name":"Y","role":"effective layer-one parameter","weight":1},{"name":"U","role":"split origin-vertex parameter; absent from compatibility equations","weight":2},{"name":"V","role":"effective layer-two parameter","weight":2},{"name":"W","role":"effective layer-two parameter","weight":2},{"name":"D","role":"split origin-vertex parameter; absent from compatibility equations","weight":3}&#93;}
</code></pre>

<a id="source-f2a5a9b855b4c6e5"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/stage-manifest.json`

<pre><code class="language-json">
{
  "audit_date": "2026-08-03",
  "base": {
    "branch": "main",
    "commit": "75da31f1a28eed187e9f825bd764a578e94d1bb2",
    "repository": "nmonson1/jacobian"
  },
  "contribution_id": "JCG-C-0015-HARVEST",
  "includes": {
    "checklist": "manifest/checklist.json",
    "field": "manifest/field.json",
    "queue": "manifest/queue.json",
    "replay": "manifest/replay.json",
    "sources": "manifest/sources.json",
    "stages": &#91;
      "manifest/stages/s0-face.json",
      "manifest/stages/s1-truncated-layers.json",
      "manifest/stages/s2-full-layers-1-4.json",
      "manifest/stages/s3-full-square-routing.json",
      "manifest/stages/s4-full-normalization.json",
      "manifest/stages/s5-full-layers-5-8.json",
      "manifest/stages/s6-toric-projection.json",
      "manifest/stages/s7-toric-terminal.json",
      "manifest/stages/s8-adjacent-stored.json",
      "manifest/stages/s9-lane9-order-obstruction.json"
    &#93;,
    "terminal_certificates": "manifest/terminal-certificates.json",
    "theorem_scope": "manifest/theorem-scope.json",
    "variable_systems": "manifest/variable-systems.json"
  },
  "schema": "jcg-lane8-proof-carrying-queue-v1",
  "source_pr": {
    "head": "86af7cf1cbccf33e068c35ea4440fc22536d1072",
    "number": 9,
    "repository": "nmonson1/guide-to-jacobian-conjecture"
  },
  "title": "Lane 8 direct terminal closure for the two normalized (8,28) supports"
}
</code></pre>

<a id="source-1aeef542ed770f29"></a>

## `research-notes/lane8-full-root-closure-20260803-v1/verify_lane8_packet.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Fail-closed validation entrypoint for contribution JCG-C-0015."""
from lane8_validator.main import cli

if __name__ == "__main__":
    cli()
</code></pre>

<a id="source-c4b71016901540c7"></a>

## `research-notes/lane8-proof-queue-20260802-v1/check_queue.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Validate the Lane 8 proof queue and its emptiness-propagation contract."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

PROOF_STATUSES = {
    "verified_in_packet",
    "audited_external_theorem",
    "verified_in_public_source",
    "source_replay_needed",
    "open",
}
EDGE_TYPES = {
    "external_import",
    "exhaustive_split",
    "forced_initial_form",
    "forced_consequence",
    "classification",
    "coefficient_reconstruction",
    "equivalence",
    "rechart",
    "relaxation",
    "localization",
    "saturation",
    "normalization",
    "finite_cover",
    "quotient",
    "forced_specialization",
    "noncovering_specialization",
    "elimination",
    "terminal_certificate",
    "discard",
}


def unique_ids(items: list&#91;dict&#91;str, Any&#93;&#93;, key: str, failures: list&#91;str&#93;) -&gt; set&#91;str&#93;:
    values = &#91;str(item.get(key, "")) for item in items&#93;
    missing = &#91;i for i, value in enumerate(values) if not value&#93;
    if missing:
        failures.append(f"{key}: missing at indices {missing}")
    duplicates = sorted({value for value in values if values.count(value) &gt; 1})
    if duplicates:
        failures.append(f"{key}: duplicate values {duplicates}")
    return set(values)


def topological_check(nodes: set&#91;str&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;, failures: list&#91;str&#93;) -&gt; None:
    adjacency: dict&#91;str, set&#91;str&#93;&#93; = defaultdict(set)
    indegree = {node: 0 for node in nodes}
    for edge in edges:
        parent = edge&#91;"from"&#93;
        for child in edge&#91;"to"&#93;:
            if child not in adjacency&#91;parent&#93;:
                adjacency&#91;parent&#93;.add(child)
                indegree&#91;child&#93; += 1
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for child in sorted(adjacency&#91;node&#93;):
            indegree&#91;child&#93; -= 1
            if indegree&#91;child&#93; == 0:
                queue.append(child)
    if visited != len(nodes):
        failures.append("routing graph contains a directed cycle")


def established_nodes(
    starts: set&#91;str&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;, accepted: set&#91;str&#93;
) -&gt; set&#91;str&#93;:
    established = set(starts)
    changed = True
    while changed:
        changed = False
        for edge in edges:
            if edge&#91;"proof_status"&#93; not in accepted:
                continue
            if edge&#91;"coverage"&#93; == "noncovering" or edge&#91;"edge_type"&#93; == "noncovering_specialization":
                continue
            if edge&#91;"from"&#93; not in established:
                continue
            if not set(edge.get("requires", &#91;&#93;)) &lt;= established:
                continue
            before = len(established)
            established.update(edge&#91;"to"&#93;)
            changed |= len(established) != before
    return established


def empty_nodes(
    assumptions: set&#91;str&#93;,
    node_map: dict&#91;str, dict&#91;str, Any&#93;&#93;,
    edges: list&#91;dict&#91;str, Any&#93;&#93;,
    accepted: set&#91;str&#93;,
) -&gt; tuple&#91;set&#91;str&#93;, set&#91;str&#93;, list&#91;str&#93;&#93;:
    """Return established nodes, proved-empty nodes, and an explanation trace."""
    established = established_nodes(assumptions, edges, accepted)
    empty = {
        node_id
        for node_id, node in node_map.items()
        if node.get("terminal")
        and node.get("proof_status") in accepted
        and node.get("certificate_refs")
    }
    trace = &#91;f"terminal certificate: {node_id}" for node_id in sorted(empty)&#93;

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if edge&#91;"proof_status"&#93; not in accepted or not edge.get("propagates_emptiness"):
                continue
            if edge&#91;"coverage"&#93; in {"noncovering", "dependency"}:
                continue
            if edge&#91;"from"&#93; not in established:
                continue
            if not set(edge.get("requires", &#91;&#93;)) &lt;= established:
                continue
            # An exhaustive split excludes its parent only after every child
            # is empty. The same all-children rule is harmless for one-child
            # covers, relaxations, eliminations, and terminal certificates.
            if not set(edge&#91;"to"&#93;) &lt;= empty:
                continue
            parent = edge&#91;"from"&#93;
            if parent not in empty:
                empty.add(parent)
                trace.append(f"{edge&#91;'edge_id'&#93;}: all children empty =&gt; {parent} empty")
                changed = True
    return established, empty, trace


def target_result(
    target: dict&#91;str, Any&#93;, node_map: dict&#91;str, dict&#91;str, Any&#93;&#93;, edges: list&#91;dict&#91;str, Any&#93;&#93;
) -&gt; tuple&#91;bool, list&#91;str&#93;&#93;:
    accepted = set(target&#91;"accepted_proof_statuses"&#93;)
    details: list&#91;str&#93; = &#91;&#93;
    if target&#91;"kind"&#93; == "routing":
        passed = True
        for requirement in target&#91;"requirements"&#93;:
            start = requirement&#91;"from_node"&#93;
            reached = established_nodes({start}, edges, accepted)
            if "all_of" in requirement:
                missing = sorted(set(requirement&#91;"all_of"&#93;) - reached)
                ok = not missing
                details.append(f"from {start}: all_of missing={missing}")
            else:
                found = sorted(set(requirement&#91;"any_of"&#93;) &amp; reached)
                ok = bool(found)
                details.append(f"from {start}: any_of reached={found}")
            passed &amp;= ok
        return passed, details

    established, empty, trace = empty_nodes(
        set(target&#91;"assumption_nodes"&#93;), node_map, edges, accepted
    )
    missing = sorted(set(target&#91;"prove_empty"&#93;) - empty)
    details.append(f"established nodes: {len(established)}")
    details.append(f"proved-empty nodes: {sorted(empty)}")
    details.append(f"missing emptiness proofs: {missing}")
    details.extend(trace)
    return not missing, details


def validate(data: dict&#91;str, Any&#93;, require_global: bool) -&gt; int:
    failures: list&#91;str&#93; = &#91;&#93;
    if data.get("schema_version") != 1:
        failures.append("schema_version must be 1")

    node_ids = unique_ids(data.get("nodes", &#91;&#93;), "node_id", failures)
    edge_ids = unique_ids(data.get("edges", &#91;&#93;), "edge_id", failures)
    source_ids = unique_ids(data.get("sources", &#91;&#93;), "source_id", failures)
    obligation_ids = unique_ids(data.get("obligations", &#91;&#93;), "obligation_id", failures)
    target_ids = unique_ids(data.get("coverage_targets", &#91;&#93;), "target_id", failures)
    del source_ids, obligation_ids, target_ids

    node_pattern = re.compile(r"^L8-&#91;A-Z0-9-&#93;+$")
    edge_pattern = re.compile(r"^L8-E-&#91;A-Z0-9-&#93;+$")
    for node_id in node_ids:
        if not node_pattern.fullmatch(node_id):
            failures.append(f"invalid node id: {node_id}")
    for edge_id in edge_ids:
        if not edge_pattern.fullmatch(edge_id):
            failures.append(f"invalid edge id: {edge_id}")

    node_map = {node&#91;"node_id"&#93;: node for node in data.get("nodes", &#91;&#93;) if node.get("node_id")}
    edge_map = {edge&#91;"edge_id"&#93;: edge for edge in data.get("edges", &#91;&#93;) if edge.get("edge_id")}

    for node_id, node in node_map.items():
        if node.get("proof_status") not in PROOF_STATUSES:
            failures.append(f"{node_id}: invalid proof status")
        if node.get("terminal") and not node.get("certificate_refs"):
            failures.append(f"{node_id}: terminal node lacks certificate_refs")
        if not isinstance(node.get("constructible_data", {}).get("inverted_elements"), list):
            failures.append(f"{node_id}: inverted_elements must be an explicit list")

    for edge_id, edge in edge_map.items():
        if edge.get("from") not in node_ids:
            failures.append(f"{edge_id}: unknown parent {edge.get('from')}")
        for key in ("to", "requires"):
            for node_id in edge.get(key, &#91;&#93;):
                if node_id not in node_ids:
                    failures.append(f"{edge_id}: unknown {key} node {node_id}")
        if edge.get("edge_type") not in EDGE_TYPES:
            failures.append(f"{edge_id}: invalid edge type {edge.get('edge_type')}")
        if edge.get("proof_status") not in PROOF_STATUSES:
            failures.append(f"{edge_id}: invalid proof status")
        if edge.get("edge_type") == "noncovering_specialization":
            if edge.get("coverage") != "noncovering" or edge.get("propagates_emptiness"):
                failures.append(f"{edge_id}: noncovering specialization has unsafe semantics")
        if edge.get("coverage") == "dependency" and edge.get("propagates_emptiness"):
            failures.append(f"{edge_id}: dependency edge cannot propagate emptiness")
        if edge.get("edge_type") == "terminal_certificate":
            if edge.get("coverage") != "terminal" or not edge.get("propagates_emptiness"):
                failures.append(f"{edge_id}: terminal certificate semantics are malformed")
            for child in edge.get("to", &#91;&#93;):
                if child in node_map and not node_map&#91;child&#93;.get("terminal"):
                    failures.append(f"{edge_id}: terminal certificate points to nonterminal {child}")
        if edge.get("edge_type") in {"localization", "saturation"}:
            complements = edge.get("complement_edges", &#91;&#93;)
            if not complements:
                failures.append(f"{edge_id}: localization/saturation lacks complementary branch")
            for complement in complements:
                if complement not in edge_ids:
                    failures.append(f"{edge_id}: unknown complement edge {complement}")
                elif edge_map&#91;complement&#93;.get("from") != edge.get("from"):
                    failures.append(f"{edge_id}: complement {complement} has a different parent")

    for obligation in data.get("obligations", &#91;&#93;):
        for edge_id in obligation.get("blocks", &#91;&#93;):
            if edge_id not in edge_ids:
                failures.append(f"{obligation&#91;'obligation_id'&#93;}: blocks unknown edge {edge_id}")

    for target in data.get("coverage_targets", &#91;&#93;):
        for status in target.get("accepted_proof_statuses", &#91;&#93;):
            if status not in PROOF_STATUSES:
                failures.append(f"{target&#91;'target_id'&#93;}: invalid accepted proof status {status}")
        references: set&#91;str&#93; = set()
        if target.get("kind") == "routing":
            for req in target.get("requirements", &#91;&#93;):
                references.add(req.get("from_node", ""))
                references.update(req.get("all_of", &#91;&#93;))
                references.update(req.get("any_of", &#91;&#93;))
        elif target.get("kind") == "exclusion":
            references.update(target.get("assumption_nodes", &#91;&#93;))
            references.update(target.get("prove_empty", &#91;&#93;))
        else:
            failures.append(f"{target&#91;'target_id'&#93;}: invalid target kind")
        for node_id in references:
            if node_id not in node_ids:
                failures.append(f"{target&#91;'target_id'&#93;}: unknown node {node_id}")

    topological_check(node_ids, data.get("edges", &#91;&#93;), failures)

    if failures:
        print("STRUCTURAL FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 2

    print(
        f"STRUCTURAL PASS: {len(node_ids)} nodes, {len(edge_ids)} edges, "
        f"{len(data.get('obligations', &#91;&#93;))} obligations"
    )

    expectation_failures: list&#91;str&#93; = &#91;&#93;
    global_incomplete = False
    for target in data&#91;"coverage_targets"&#93;:
        actual, details = target_result(target, node_map, data&#91;"edges"&#93;)
        actual_label = "complete" if actual else "incomplete"
        expected = target&#91;"expected"&#93;
        print(f"{target&#91;'target_id'&#93;}: {actual_label} (expected {expected})")
        for detail in details:
            print(f"  {detail}")
        if actual_label != expected:
            expectation_failures.append(
                f"{target&#91;'target_id'&#93;}: expected {expected}, got {actual_label}"
            )
        if target&#91;"target_id"&#93; == "L8-COVERAGE-SUB125-EXCLUSION" and not actual:
            global_incomplete = True

    if expectation_failures:
        print("EXPECTATION FAIL")
        for failure in expectation_failures:
            print(f"- {failure}")
        return 3
    if require_global and global_incomplete:
        print("GLOBAL FAIL: the standalone below-125 exclusion is not certified")
        return 1

    print("PASS: declared complete targets are complete and declared gaps remain visible")
    return 0


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("queue", nargs="?", default="queue.seed.json")
    parser.add_argument(
        "--require-global",
        action="store_true",
        help="fail unless the standalone below-125 exclusion target is complete",
    )
    args = parser.parse_args()
    path = Path(args.queue)
    data = json.loads(path.read_text(encoding="utf-8"))
    return validate(data, require_global=args.require_global)


if __name__ == "__main__":
    sys.exit(main())
</code></pre>

<a id="source-825cbf7a3e2c79ec"></a>

## `research-notes/lane8-proof-queue-20260802-v1/full_early_layer_reduction.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact early-layer reduction for the full (8,28) Newton root.

The calculation reconstructs layers 1 through 4 over the quintic field.  The
first three compatibility functionals vanish identically.  The sole layer-4
condition is an exact square a*(W-kappa*Y^2)^2.  Thus the reduced geometric
branch is forced to W=kappa*Y^2, while the scheme-level double structure must
be retained in any elimination proof.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import quintic_face_reconstruction as face
import truncated_support_certificate as exact

# Nine early free coordinates:
# layer 1: X,Y; layer 2: U,V,W; layer 3: R,S,T; layer 4: H.
exact.N = 9


def reconstruct_base():
    K, ONE, ZERO = exact.K, exact.ONE, exact.ZERO
    a = {i: K.from_expr(v) for i, v in face.A_RAW.items()}
    reverse_p = &#91;ONE&#93; + &#91;a&#91;i&#93; for i in range(1, 8)&#93;
    cube = &#91;&#93;
    for total in range(21):
        value = ZERO
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    if i + j + k == total:
                        value = value + reverse_p&#91;i&#93; * reverse_p&#91;j&#93; * reverse_p&#91;k&#93;
        cube.append(value)
    reverse_q = &#91;ONE&#93;
    for total in range(1, 11):
        known = ZERO
        for i in range(1, total):
            known = known + reverse_q&#91;i&#93; * reverse_q&#91;total - i&#93;
        reverse_q.append((cube&#91;total&#93; - known) / K(2))
    inverse_constant = (a&#91;7&#93; * reverse_q&#91;10&#93;).inv()
    p = {7: ONE}
    p.update({7 - i: a&#91;i&#93; for i in range(1, 8)})
    q = {10: inverse_constant}
    q.update({10 - i: reverse_q&#91;i&#93; * inverse_constant for i in range(1, 11)})
    return (
        exact.z_from_field({degree + 1: value for degree, value in p.items()}),
        exact.z_from_field({degree + 2: value for degree, value in q.items()}),
    )


def a_exponents(layer):
    if layer == 1:
        return list(range(1, 9))
    if layer == 2:
        return list(range(0, 9))
    if 3 &lt;= layer &lt;= 10:
        return list(range(0, 11 - layer))
    return &#91;&#93;


def b_exponents(layer):
    if layer == 1:
        return list(range(2, 13))
    if layer == 2:
        return list(range(1, 13))
    if layer == 3:
        return list(range(0, 13))
    if 4 &lt;= layer &lt;= 15:
        return list(range(0, 16 - layer))
    return &#91;&#93;


def forcing(layer, A, B):
    pieces = &#91;&#93;
    for i in range(1, layer):
        j = layer - i
        if i &gt;= len(A) or j &gt;= len(B) or not A&#91;i&#93; or not B&#91;j&#93;:
            continue
        pieces.append(
            exact.zscale(exact.zmul(A&#91;i&#93;, exact.zder(B&#91;j&#93;)), 2 - i)
        )
        pieces.append(
            exact.zscale(exact.zmul(exact.zder(A&#91;i&#93;), B&#91;j&#93;), j - 3)
        )
    return exact.zadd(*pieces)


def build_reduction():
    A0, B0 = reconstruct_base()
    X, Y, U, V, W, R, S, T, H = &#91;exact.pp_var(i) for i in range(9)&#93;
    A = &#91;A0&#93;
    B = &#91;B0&#93;
    compatibilities = {}

    free_parameters = {
        1: &#91;X, Y&#93;,
        2: &#91;U, V, W&#93;,
        3: &#91;R, S, T&#93;,
        4: &#91;H&#93;,
    }
    expected = {
        1: (17, &#91;17, 18&#93;),
        2: (18, &#91;0, 19, 20&#93;),
        3: (18, &#91;8, 18, 19&#93;),
        4: (18, &#91;17&#93;),
    }

    for layer in range(1, 5):
        data = exact.linear_data(
            layer, a_exponents(layer), b_exponents(layer), A0, B0
        )
        assert (len(data&#91;4&#93;), data&#91;5&#93;) == expected&#91;layer&#93;
        rhs = {} if layer == 1 else exact.zscale(forcing(layer, A, B), -1)
        solution, compatibility = exact.solve(
            data, rhs, free_parameters&#91;layer&#93;
        )
        Ar, Br = exact.vecpair(
            solution, a_exponents(layer), b_exponents(layer)
        )
        A.append(Ar)
        B.append(Br)
        compatibilities&#91;layer&#93; = compatibility

    assert all(not equation for layer in (1, 2, 3)
               for equation in compatibilities&#91;layer&#93;)
    assert len(compatibilities&#91;4&#93;) == 1
    equation = compatibilities&#91;4&#93;&#91;0&#93;
    expected_support = {
        (0, 0, 0, 0, 2, 0, 0, 0, 0),  # W^2
        (0, 2, 0, 0, 1, 0, 0, 0, 0),  # Y^2 W
        (0, 4, 0, 0, 0, 0, 0, 0, 0),  # Y^4
    }
    assert set(equation) == expected_support
    a = equation&#91;(0, 0, 0, 0, 2, 0, 0, 0, 0)&#93;
    b = equation&#91;(0, 2, 0, 0, 1, 0, 0, 0, 0)&#93;
    c = equation&#91;(0, 4, 0, 0, 0, 0, 0, 0, 0)&#93;
    assert not (b * b - exact.K(4) * a * c)
    kappa = -b / (exact.K(2) * a)
    assert not (c - a * kappa * kappa)

    return {
        "schema_version": 1,
        "field_polynomial": str(face.M_EXPR),
        "early_free_parameters": {
            "layer_1": &#91;"X", "Y"&#93;,
            "layer_2": &#91;"U", "V", "W"&#93;,
            "layer_3": &#91;"R", "S", "T"&#93;,
            "layer_4": &#91;"H"&#93;,
        },
        "ranks": {
            "D1": 17,
            "D2": 18,
            "D3": 18,
            "D4": 18,
        },
        "compatibility": {
            "layers_1_to_3_identically_zero": True,
            "layer_4_support": &#91;"W^2", "Y^2*W", "Y^4"&#93;,
            "leading_coefficient": str(a.expr()),
            "kappa": str(kappa.expr()),
            "exact_factorization": "a*(W-kappa*Y^2)^2",
        },
        "conclusion": {
            "reduced_geometric_branch": "W=kappa*Y^2",
            "scheme_structure": "double square; do not replace by the reduced branch in scheme-level arguments",
            "all_later_free_parameters": "none after layer 4; see full_layer_rank_profile.json",
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_reduction()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("exact early ranks: D1=17, D2=18, D3=18, D4=18")
    print("compatibility at layers 1,2,3: identically zero")
    print("layer-4 compatibility: a*(W-kappa*Y^2)^2")
    print("reduced geometric branch: W=kappa*Y^2")
    if args.output:
        print(f"reduction export: {args.output.name}")
    print("PASS: the full-support square branch is independently reconstructed")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-86a7146cd6277db5"></a>

## `research-notes/lane8-proof-queue-20260802-v1/hurwitz_degree21.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent exact Hurwitz count for the forced degree-21 Lane 8 face.

The Murnaghan--Nakayama implementation is self-contained and uses no data from
the Program 6 computational supplement.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial
from typing import Iterable

Partition = tuple&#91;int, ...&#93;


@lru_cache(None)
def partitions_with_bound(n: int, max_part: int) -&gt; tuple&#91;Partition, ...&#93;:
    if n == 0:
        return ((),)
    if max_part &lt;= 0:
        return ()
    result: list&#91;Partition&#93; = &#91;&#93;
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions_with_bound(n - first, first):
            result.append((first,) + rest)
    return tuple(result)


def partitions(n: int) -&gt; tuple&#91;Partition, ...&#93;:
    return partitions_with_bound(n, n)


def contains(lam: Partition, mu: Partition) -&gt; bool:
    rows = max(len(lam), len(mu))
    return all(
        (mu&#91;i&#93; if i &lt; len(mu) else 0) &lt;= (lam&#91;i&#93; if i &lt; len(lam) else 0)
        for i in range(rows)
    )


def border_strip_height(lam: Partition, mu: Partition) -&gt; int | None:
    cells = {
        (row, col)
        for row, length in enumerate(lam)
        for col in range(mu&#91;row&#93; if row &lt; len(mu) else 0, length)
    }
    if not cells:
        return None

    seen = {next(iter(cells))}
    stack = list(seen)
    while stack:
        row, col = stack.pop()
        for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if neighbor in cells and neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    if len(seen) != len(cells):
        return None

    for row, col in cells:
        if {
            (row, col),
            (row + 1, col),
            (row, col + 1),
            (row + 1, col + 1),
        } &lt;= cells:
            return None
    return len({row for row, _ in cells}) - 1


@lru_cache(None)
def border_strip_removals(lam: Partition, size: int) -&gt; tuple&#91;tuple&#91;Partition, int&#93;, ...&#93;:
    remaining = sum(lam) - size
    if remaining &lt; 0:
        return ()
    result = &#91;&#93;
    for mu in partitions(remaining):
        if contains(lam, mu):
            height = border_strip_height(lam, mu)
            if height is not None:
                result.append((mu, height))
    return tuple(result)


@lru_cache(None)
def character(lam: Partition, cycle_type: Partition) -&gt; int:
    if not cycle_type:
        return int(sum(lam) == 0)
    first = cycle_type&#91;0&#93;
    return sum(
        (-1) ** height * character(mu, cycle_type&#91;1:&#93;)
        for mu, height in border_strip_removals(lam, first)
    )


def representation_dimension(lam: Partition) -&gt; int:
    n = sum(lam)
    hook_product = 1
    for row, row_length in enumerate(lam):
        for col in range(row_length):
            below = sum(1 for lower_row in lam&#91;row + 1 :&#93; if lower_row &gt; col)
            hook_product *= row_length - col + below
    return factorial(n) // hook_product


def centralizer_size(cycle_type: Iterable&#91;int&#93;) -&gt; int:
    multiplicities = Counter(cycle_type)
    result = 1
    for length, multiplicity in multiplicities.items():
        result *= length**multiplicity * factorial(multiplicity)
    return result


def conjugacy_class_size(cycle_type: Partition) -&gt; int:
    return factorial(sum(cycle_type)) // centralizer_size(cycle_type)


def weighted_hurwitz_number(c0: Partition, c1: Partition, cinfinity: Partition) -&gt; Fraction:
    n = sum(c0)
    assert sum(c1) == n == sum(cinfinity)
    character_sum = Fraction(0)
    for lam in partitions(n):
        character_sum += Fraction(
            character(lam, c0) * character(lam, c1) * character(lam, cinfinity),
            representation_dimension(lam),
        )
    prefactor = Fraction(
        conjugacy_class_size(c0) * conjugacy_class_size(c1) * conjugacy_class_size(cinfinity),
        factorial(n) ** 2,
    )
    return prefactor * character_sum


def compose(left: tuple&#91;int, ...&#93;, right: tuple&#91;int, ...&#93;) -&gt; tuple&#91;int, ...&#93;:
    return tuple(left&#91;right&#91;i&#93;&#93; for i in range(len(left)))


def cycle_type(permutation: tuple&#91;int, ...&#93;) -&gt; tuple&#91;int, ...&#93;:
    seen: set&#91;int&#93; = set()
    lengths: list&#91;int&#93; = &#91;&#93;
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation&#91;current&#93;
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def check_transitivity_obstruction() -&gt; None:
    # Any disconnected degree-21 triple with a 17-cycle and seven 3-cycles
    # would split as 18+3. On the three-point orbit, the cycle types would be
    # (2,1), (3), and identity. No such three permutations multiply to one.
    s3 = tuple(permutations(range(3)))
    identity = (0, 1, 2)
    transpositions = &#91;p for p in s3 if cycle_type(p) == (2, 1)&#93;
    three_cycles = &#91;p for p in s3 if cycle_type(p) == (3,)&#93;
    assert not any(compose(compose(a, b), identity) == identity for a in transpositions for b in three_cycles)


def main() -&gt; None:
    c0 = (2,) * 10 + (1,)
    c1 = (3,) * 7
    cinfinity = (17,) + (1,) * 4
    value = weighted_hurwitz_number(c0, c1, cinfinity)
    assert value == 5
    print(f"weighted Hurwitz number for (2^10 1),(3^7),(17 1^4): {value}")

    check_transitivity_obstruction()
    print("disconnected 18+3 orbit decomposition excluded by an exact S3 check")

    # Parity and block-size conditions used by the stated Jordan argument.
    assert (-1) ** (21 - len(c0)) == 1
    assert (-1) ** (21 - len(c1)) == 1
    assert (-1) ** (21 - len(cinfinity)) == 1
    assert &#91;d for d in range(2, 21) if 21 % d == 0&#93; == &#91;3, 7&#93;
    assert 17 &gt; 7 and 17 &gt; 3 and 17 &lt;= 21 - 3
    print("parity, primitivity block-size, and Jordan prime-cycle hypotheses checked")
    print("PASS: the weighted count is five connected classes; the standard Jordan argument gives monodromy A_21")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-417fb9530af82c25"></a>

## `research-notes/lane8-proof-queue-20260802-v1/lane8-proof-queue-repair.md`

<pre><code class="language-markdown">
---
title: "Lane 8 proof-queue repair"
description: "A proof-carrying contract for the plane Newton queue, with an audited literature import and exact root-to-face checks."
---

# Lane 8 proof-queue repair

&lt;p class="dek"&gt;This additive repair separates the imported below-125 reduction,
the post-root coefficient queue, and adjacent-chart attachment.  It also closes
the first exact segment of the queue: both normalized `(8,28)` Newton
alternatives force the same degree-21 Belyi face, its five normalized covers
are reconstructed as one explicit quintic Galois orbit, and the entire
truncated root is excluded by a new exact normal-layer certificate.&lt;/p&gt;

!!! warning "Scope"
    This page does not alter the stable claim graph and does not promote the
    public below-125 statement.  It repairs the operational contract for
    &#91;Lane 8&#93;(handoffs/plane-newton-queue-terminal-certificates.md).  The stored
    terminal certificates remain exact for their displayed systems; global
    coverage still requires independently replaying the coefficient-routing
    edges recorded below.

## 1. Repaired theorem architecture

Three logically separate results are required.

### A. Imported root theorem

Let `K` have characteristic zero.  If a noninvertible plane Keller pair over
`K` has maximum coordinate degree below `125`, then, after exchanging the two
coordinates if necessary and applying the reductions in Guccione--Guccione--
Horruitiner--Valqui, it reaches the `(8,28)` family.  Proposition 4.3 of that
paper then produces a Laurent pair

```text
P,Q in K&#91;x,x^(-1),y&#93;,        &#91;P,Q&#93;=x^2,
```

with one of the two Newton-polygon pairs listed in section 2 below.

The primary sources are &#91;the 2022 degree-reduction paper&#93;(https://arxiv.org/abs/2204.14178)
and &#91;the 2017 complete-chain algorithms paper&#93;(https://arxiv.org/abs/1708.07936).
This import is the combination of:

1. Theorem 2.1, which leaves only degree pair `(72,108)` below `125`;
2. Proposition 4.1 and Corollary 5.7, which eliminate the other `(72,108)`
   family `(9,27)`;
3. Proposition 4.3, which gives the two `(8,28)` roots.

The packet independently checks the last monomial-coordinate transformation
and its Jacobian multiplier.  It does not reprove every cited theorem used
inside the literature reduction.

### B. Post-root queue theorem

For each root constructible locus `X_R`, construct a finite directed acyclic
graph with two distinct classes of edges.  A **covering edge** must justify the
backward implication

```text
all covering children empty  =&gt;  parent empty.
```

A **dependency edge** may establish a passport, field model, classification,
or other auxiliary datum, but it cannot propagate emptiness.  Every
nonterminal locus must be covered by its geometric children, and every
terminal locus must carry a replayable exact emptiness certificate.  This is
the mathematical content of Lane 8 after the literature import.

### C. Chart-correspondence theorem

Any edge that changes complete-chain chart must identify the common formal
branch, transport the support and residue conditions, and prove the relevant
overlap statement.  That is principally &#91;Lane 9&#93;(handoffs/plane-chart-correspondence-global-attachment.md).
A stored specialization in an adjacent chart is not a covering edge unless
this correspondence is proved.

The global implication has the form

```text
sub-125 Keller pair
    -- imported theorem --&gt; one of two normalized roots
    -- proof-carrying DAG --&gt; a certified empty terminal system
    -- chart descent when used --&gt; contradiction.
```

## 2. The two exact roots

The two alternatives are named `truncated` and `full` in this repair.
`N(P)` denotes the convex Newton polygon, not the set of coefficients required
to be nonzero.

| root | `N(P)` vertices | `N(Q)` vertices | lattice points `(P,Q)` |
|---|---|---|---:|
| truncated | `(0,0),(1,0),(8,14),(8,16)` | `(0,0),(2,1),(12,21),(12,24)` | `(25,47)` |
| full | `(0,0),(1,0),(8,14),(8,16),(0,8)` | `(0,0),(2,1),(12,21),(12,24),(0,12)` | `(61,125)` |

The lattice-point counts are independently regenerated by
&#91;`root_face_check.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/root_face_check.py).
Exact Newton polygon means that each listed vertex coefficient is nonzero and
that no exponent outside the polygon occurs.  Interior and nonvertex boundary
coefficients may vanish.

The final coordinate map in Proposition 4.3 is

```text
phi(x)=x^(-1),       phi(y)=x^4 y.
```

It sends exponent `(a,b)` to `(-a+4b,b)` and has Jacobian determinant `-x^2`.
The packet verifies that it sends the pre-final vertices in the proof to the
two polygon pairs above.  Thus the displayed bracket normalization is also
checked rather than treated as a diagrammatic convention.

### Polygon versus coefficient window

The truncated lattice windows are subsets of the full windows.  Consequently
both roots may be embedded in one full coefficient ambient space by setting
the full-only coefficients to zero on the truncated branch.  This is a sound
**relaxation**, but it does not merge the two exact roots whenever a later step
inverts a full-only coefficient.  Any such localization must retain the
closed complementary branch.

## 3. Exact progress: the common degree-21 face is forced

Give a monomial `x^a y^b` the value

```text
nu(a,b)=-2a+b.
```

For both roots, the minimum values are `-2` on the edge from `(1,0)` to
`(8,14)` in `P`, and `-3` on the edge from `(2,1)` to `(12,21)` in `Q`.
With

```text
z = x y^2,
```

the initial forms therefore have the unique shapes

```text
P_face = x p(z),          deg p = 7,
Q_face = x^2 y q(z),      deg q = 10,
```

where the constant and leading coefficients of `p,q` are nonzero.  Direct
differentiation gives

```text
&#91;P_face,Q_face&#93;
 = x^2 (p q + 2 z p q' - 3 z p' q).
```

Since the full bracket is `x^2`, its least-valuation part forces

```text
p q + 2 z p q' - 3 z p' q = 1.                 (3.1)
```

This closes a previously ambiguous routing step: passage from either
Proposition 4.3 root to the degree-21 face is a forced initial-form edge, not a
chosen specialization.

### The Belyi map

Set

```text
tau(z) = z q(z)^2 / p(z)^3.
```

An exact identity is

```text
tau'(z)
 = q(z)/p(z)^4 * (p q + 2 z p q' - 3 z p' q).
```

Hence (3.1) gives `tau'=q/p^4`.  Equation (3.1) also implies:

- `p(0)q(0)=1`;
- every root of `p` is simple and is not a root of `q`;
- every root of `q` is simple and is not a root of `p`.

It follows that `tau` has degree `21` and passport

```text
(2^10 1),       (3^7),       (17 1^4).
```

The ramification contribution is

```text
10 + 14 + 16 = 40 = 2*21-2,
```

so there is no fourth branch value.  The exact Murnaghan--Nakayama check in
&#91;`hurwitz_degree21.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/hurwitz_degree21.py)
returns weighted Hurwitz number `5`.  A disconnected triple would have orbit
sizes `18+3`; on the three-point orbit the required transposition, 3-cycle,
and identity cannot multiply to one.  Thus all triples are transitive.  The
standard primitivity/Jordan argument then gives monodromy `A_21`, hence
trivial deck group, so the weighted count is exactly five isomorphism classes.

### Exact quintic coefficient orbit

The packet now reconstructs the five classes independently of the large
Program 6 archive.  Normalize

```text
p(z)=z^7+z^6+s z^5+...,
q_monic(z)=z^10+(3/2)z^9+... .
```

In reverse coordinates at infinity, the index-17 contact condition is

```text
Q(T)^2-P(T)^3 = O(T^17).
```

Solving its coefficients successively leaves the primitive parameter `s`
with irreducible polynomial

```text
287548593020928 s^5 - 688401965085696 s^4
+ 640652914818432 s^3 - 292066554895024 s^2
+ 65563255857792 s - 5817852446211 = 0.       (3.2)
```

&#91;`quintic_face_reconstruction.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/quintic_face_reconstruction.py)
constructs every coefficient of `p` and `q_monic` in `Q(s)`, and
&#91;`quintic_face_coefficients.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/quintic_face_coefficients.json)
exports them exactly.  It verifies

```text
deg(z q_monic^2-p^3) &lt;= 4,
p q_monic + 2z p q_monic' - 3z p' q_monic = c != 0.
```

Thus `q=q_monic/c` satisfies equation (3.1) exactly.  The coefficient of
`z^6` in `p` fixes the remaining source scaling: the unique simple point over
one branch value and the unique index-17 point over another already fix `0`
and infinity.  Distinct embeddings of the irreducible quintic therefore give
five distinct normalized covers.  Since the Hurwitz calculation gives only
five classes, these covers exhaust them and form one Galois orbit.

The reconstruction also verifies the exact field isomorphism to the public
Program 6 model

```text
K0 = Q&#91;u&#93;/(u^5-u^4+3u^3+3u^2+26)
```

by the map

```text
s = (20481190 - 2578004u + 1664322u^2
     - 709604u^3 + 221083u^4) / 42799752.       (3.3)
```

This closes the coefficient-field dependency and supplies canonical exact
lower-face input for both normal-layer branches.

## 4. Exact normal-layer equation

Put

```text
t=y,       z=x y^2,
P=t^(-2) A(z,t),       Q=t^(-3) B(z,t).
```

Because `det d(z,t)/d(x,y)=t^2`, the equation `&#91;P,Q&#93;=x^2` is exactly

```text
2 A B_z - 3 A_z B + t(A_z B_t - A_t B_z) = z^2.       (4.1)
```

Write

```text
A=sum_(r&gt;=0) t^r A_r(z),       B=sum_(r&gt;=0) t^r B_r(z).
```

The coefficient of `t^r` in the left side of (4.1) is

```text
E_r = sum_(i+j=r) ((2-i) A_i B_j' + (j-3) A_i' B_j).  (4.2)
```

For `r&gt;0`, the terms containing the new unknowns are

```text
D_r(A_r,B_r)
 = (2-r) A_r B_0' - 3 A_r' B_0
   + 2 A_0 B_r' + (r-3) A_0' B_r,
```

and all other summands are forcing terms from lower layers.  This identifies
the precise triangular operator that a queue implementation must transport.
For a monomial `x^a y^b`, its layer is

```text
d_P(a,b)=b-2a+2,       d_Q(a,b)=b-2a+3.
```

The independently regenerated layer-window sizes are:

```text
truncated P: 8,8,9
truncated Q: 11,11,12,13
full P:      8,8,9,8,7,6,5,4,3,2,1
full Q:      11,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1.
```

These formulas supply a canonical source for every later row and column
label.  A fixed-chart kernel may be quotiented only after its action on these
windows has been proved; a complete-chain operation that changes the window
is a rechart edge instead.


### Exact truncated-support certificate

For the truncated root, the support windows terminate at `A_2` and `B_3`.
Using the exact quintic face as `(A_0,B_0)=(z p,z^2 q)`, the layer maps are

| layer | source dimensions | target dimension | exact rank | free coordinates |
|---:|---:|---:|---:|---|
| `1` | `8+11=19` | `18` | `17` | `X,Y` |
| `2` | `9+12=21` | `19` | `18` | `U,V,W` |
| `3` | `0+13=13` | `19` | `12` | `D` |

The single layer-two compatibility functional vanishes identically.  The
parameters `U` and `D` are the free constant terms that realize the two
origin vertices; they disappear from all later compatibility equations.
The effective parameters are therefore

```text
X,Y,V,W,        weights 1,1,2,2.
```

Layer three gives seven weighted-degree-three equations.  Layer four gives
the eighteen coefficients of

```text
A_1 B_3' - A_2' B_2 = 0,
```

in degrees `z^2,...,z^19`; layer five vanishes identically because the two
coefficients in (4.2) are zero for `(i,j)=(2,3)`.

There are exactly fourteen monomials of weighted degree four:

```text
X^4,X^3Y,X^2Y^2,XY^3,Y^4,
X^2V,XYV,Y^2V,X^2W,XYW,Y^2W,
V^2,VW,W^2.
```

Multiply each layer-three equation by `X` and by `Y`, and adjoin the eighteen
layer-four equations.  The resulting `32 x 14` coefficient matrix has rank
`14` over the quintic field.  The verifier exhibits a selected `14 x 14`
minor with determinant

```text
894 mod 2053
```

at the unramified reduction `u=216`, corresponding to `s=1831`.  Because the
matrix was constructed exactly over the number field and every denominator
is a unit at this prime, the nonzero reduction proves that the same minor is
nonzero in characteristic zero.

Consequently the compatibility ideal contains every weighted-degree-four
monomial, so its radical contains `(X,Y,V,W)`.  The required top vertex
coefficients

```text
coefficient of A_2 z^8   &lt;-&gt;   P exponent (8,16),
coefficient of B_3 z^12  &lt;-&gt;   Q exponent (12,24)
```

have no constant term in these four variables and therefore vanish at every
geometric solution.  Exactness of the truncated Newton polygons requires
both to be nonzero.  This is a contradiction; the origin-vertex parameters
`U,D` remain unrestricted, so no complementary saturation branch has been
discarded.

&#91;`truncated_support_certificate.py`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/truncated_support_certificate.py)
reconstructs the whole calculation, and
&#91;`truncated_support_certificate.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/truncated_support_certificate.json)
records the ranks, free columns, selected minor, and vertex conclusion.

## 5. Constructible-locus and edge contract

Represent a node by

```text
X(I;S) = V(I) intersect intersection_(s in S) D(s),
```

where `I` is an ideal over a declared coefficient field and `S` is the list of
all inverted elements.  Required nonzero vertex coefficients belong in `S`,
not in prose.

A branch on a polynomial `h` must record the exhaustive identity

```text
X(I;S)
 = X(I+(h);S) union X(I;S union {h}).
```

On the open branch,

```text
V(I) intersect D(h) = V(I:h^infinity) intersect D(h),
```

but the closed branch `h=0` remains a child until it is independently
eliminated.

Every edge must declare whether it is a covering edge or a dependency
edge.  The main semantics are:

| edge type | role | required implication or data |
|---|---|---|
| `exhaustive_split` | covering | every parent point belongs to a listed child; all children must be empty to exclude the parent |
| `equivalence` | covering | inverse maps on the stated constructible loci |
| `rechart` | covering | same formal branch, transformed support/residue data, overlap theorem |
| `relaxation` | covering | parent maps into a larger child locus; child emptiness excludes parent |
| `localization` / `saturation` | covering | open branch plus an explicit complementary closed branch |
| `normalization` / `finite_cover` | covering | every relevant parent point lifts, or omitted image is separately routed |
| `quotient` | covering | lifting/descent and stabilizers are stated |
| `forced_specialization` | covering | equations or symmetry prove that every parent point reaches the fiber |
| `noncovering_specialization` | neither | useful test case only; cannot propagate terminal emptiness to the parent |
| `elimination` | covering | projection and extension/contraction statement, including all denominators |
| `terminal_certificate` | covering | exact identity, unit ideal, or proper compactification argument proving emptiness |
| `discard` | covering | an exact proof that the discarded constructible locus is empty |
| `forced_consequence` | dependency | derives an auxiliary invariant from an established locus |
| `classification` | dependency | classifies auxiliary objects but does not itself exclude the parent locus |
| `coefficient_reconstruction` | dependency | constructs the exact coefficient field/orbit used by later geometric edges |

The schema uses one geometric `from` node and a separate `requires` list.
This prevents an auxiliary fact such as the quintic reconstruction from being
mistaken for a second parent locus whose emptiness could be inferred from a
terminal certificate.

The machine-readable version is
&#91;`queue.schema.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/queue.schema.json),
and the current seed graph is
&#91;`queue.seed.json`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/queue.seed.json).

## 6. Current certified and uncertified edges

| stage | present conclusion | repair status |
|---|---|---|
| sub-125 candidate to degree `(72,108)` | Theorem 2.1 | external theorem statement audited |
| removal of `(9,27)` | Proposition 4.1 plus Corollary 5.7 | external theorem statement audited |
| `(8,28)` family to the two roots | Proposition 4.3 | external theorem statement audited; final monomial transform independently checked |
| either root to equation (3.1) | common lower face | independently proved and checked in this packet |
| equation (3.1) to degree-21 passport | derivative and ramification calculation | independently proved and checked in this packet |
| passport to five dessin classes | Hurwitz count, transitivity, trivial deck group | independently checked, with the group-theoretic argument stated above |
| five classes to one explicit quintic orbit | coefficient reconstruction and field identification | independently reconstructed; exact formulas and an isomorphism to the public `K0` model are exported in this packet |
| truncated root to its vertex-saturated empty system | exact layers `1`--`4`, fourteen-monomial span, and top-vertex contradiction | independently reconstructed and certified in this packet; the queue now propagates emptiness back to the truncated root |
| full root to fifteen normalized equations | layer recursion, square branch, normalization, elimination | stated exact in the Program 6 source; stage-by-stage replay and branch ledger still needed |
| six selected full-support equations to empty locus | compact toric certificate | exact for the displayed polynomials; independent large replay not performed here |
| stored `k=4` adjacent-chart system to empty locus | layer-five-through-seven certificate | exact for the stored system |
| full root to the stored `k=4` system | global coverage | not established; a specialization is not an exhaustive rechart |

Running

```text
python check_queue.py
```

validates the graph, confirms that the literature-root chain and common-face
chain are complete at their declared evidence levels, and deliberately reports
the global root-to-terminal coverage as incomplete.  The checker exits with a
failure under `--require-global`, so a release cannot silently convert the
open queue into a theorem.

## 7. Immediate theorem-facing work

The smallest useful next repairs are now sharply defined.

1. **Publish a stage manifest for the Program 6 archive.**  Every generated
   ideal, saturation element, normalization, branch condition, field model,
   and terminal input needs a node identifier and semantic digest.
2. **Close the full elimination edge.**  Starting with all `61+125`
   coefficient variables and the exact `Q(s)` face coefficients, reproduce
   every elimination and localization that leads to the fifteen equations.
   A denominator introduced during solving creates an explicit closed child;
   it is not silently discarded.
3. **Separate the two terminal architectures.**  The compact six-polynomial
   toric certificate and the later two-branch Nullstellensatz certificates are
   independent terminal proofs.  Each needs its own upstream provenance path.
4. **Use the `k=4` result only after a covering theorem.**  Either prove that
   the relevant branch necessarily crosses to that adjacent chart, or retain
   it as a noncovering stored specialization and continue the full branch by
   another route.

A discovered missing branch is a successful audit result: it becomes a new
queue node rather than being removed by a broader saturation.

## 8. Exact conclusion after this repair

The following statement is now independently checked from the two imported
root polygons:

&gt; Every normalized `(8,28)` root in Proposition 4.3 has the same forced
&gt; degree-21 face equation (3.1), and hence the same Belyi passport
&gt; `(2^10 1),(3^7),(17 1^4)`.  Its five classes are exactly the five
&gt; embeddings of the irreducible quintic (3.2), with the exact field
&gt; identification (3.3) to the Program 6 coefficient model.  Moreover, the
&gt; complete vertex-saturated truncated root is empty in characteristic zero.

The global statement remains:

&gt; The truncated root is now excluded independently.  The standalone
&gt; below-125 theorem is reduced to the full root: its layer elimination,
&gt; localization ledger, and attachment to one of the exact full-support
&gt; terminal certificates still require a covering proof.

The executable packet, captured outputs, and checksum manifest are under
&#91;`lane8-proof-queue-v1`&#93;(../assets/audit-repairs/lane8-proof-queue-v1/README.md).
</code></pre>

<a id="source-048b1950297f5eb0"></a>

## `research-notes/lane8-proof-queue-20260802-v1/queue.schema.json`

<pre><code class="language-json">
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://nmonson1.github.io/guide-to-jacobian-conjecture/schemas/lane8-proof-queue-v1.json",
  "title": "Lane 8 proof-carrying Newton queue",
  "type": "object",
  "required": &#91;
    "schema_version",
    "queue_id",
    "scope",
    "sources",
    "nodes",
    "edges",
    "obligations",
    "coverage_targets"
  &#93;,
  "properties": {
    "schema_version": {
      "const": 1
    },
    "queue_id": {
      "type": "string",
      "minLength": 1
    },
    "scope": {
      "type": "object",
      "required": &#91;
        "base_characteristic",
        "geometric_semantics",
        "claim_boundary"
      &#93;,
      "properties": {
        "base_characteristic": {
          "const": 0
        },
        "geometric_semantics": {
          "type": "string"
        },
        "claim_boundary": {
          "type": "string"
        }
      },
      "additionalProperties": true
    },
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": &#91;
          "source_id",
          "kind",
          "title",
          "locator"
        &#93;,
        "properties": {
          "source_id": {
            "type": "string"
          },
          "kind": {
            "enum": &#91;
              "literature",
              "public_proof_source",
              "technical_archive",
              "repair_packet"
            &#93;
          },
          "title": {
            "type": "string"
          },
          "locator": {
            "type": "string"
          },
          "sha256": {
            "type": "string",
            "pattern": "^&#91;0-9a-f&#93;{64}$"
          }
        },
        "additionalProperties": true
      }
    },
    "nodes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/node"
      }
    },
    "edges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/edge"
      }
    },
    "obligations": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/obligation"
      }
    },
    "coverage_targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/coverage_target"
      }
    }
  },
  "$defs": {
    "proof_status": {
      "enum": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source",
        "source_replay_needed",
        "open"
      &#93;
    },
    "node": {
      "type": "object",
      "required": &#91;
        "node_id",
        "kind",
        "statement",
        "field",
        "constructible_data",
        "proof_status",
        "terminal"
      &#93;,
      "properties": {
        "node_id": {
          "type": "string",
          "pattern": "^L8-&#91;A-Z0-9-&#93;+$"
        },
        "kind": {
          "enum": &#91;
            "candidate_class",
            "degree_family",
            "newton_root",
            "face_locus",
            "passport_locus",
            "dessin_classification",
            "coefficient_field_orbit",
            "finite_system",
            "terminal_empty"
          &#93;
        },
        "statement": {
          "type": "string"
        },
        "field": {
          "type": "object",
          "required": &#91;
            "base",
            "geometric_points"
          &#93;,
          "properties": {
            "base": {
              "type": "string"
            },
            "geometric_points": {
              "type": "string"
            },
            "defining_polynomial": {
              "type": "string"
            }
          },
          "additionalProperties": false
        },
        "constructible_data": {
          "type": "object",
          "required": &#91;
            "equations",
            "inverted_elements"
          &#93;,
          "properties": {
            "equations": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "inverted_elements": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "required_zero": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "variables": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "additionalProperties": true
        },
        "support": {
          "type": "object"
        },
        "proof_status": {
          "$ref": "#/$defs/proof_status"
        },
        "terminal": {
          "type": "boolean"
        },
        "certificate_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "notes": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "edge": {
      "type": "object",
      "required": &#91;
        "edge_id",
        "from",
        "to",
        "edge_type",
        "coverage",
        "propagates_emptiness",
        "proof_status",
        "statement",
        "source_refs"
      &#93;,
      "properties": {
        "edge_id": {
          "type": "string",
          "pattern": "^L8-E-&#91;A-Z0-9-&#93;+$"
        },
        "from": {
          "type": "string"
        },
        "to": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1
        },
        "requires": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "edge_type": {
          "enum": &#91;
            "external_import",
            "exhaustive_split",
            "forced_initial_form",
            "forced_consequence",
            "classification",
            "coefficient_reconstruction",
            "equivalence",
            "rechart",
            "relaxation",
            "localization",
            "saturation",
            "normalization",
            "finite_cover",
            "quotient",
            "forced_specialization",
            "noncovering_specialization",
            "elimination",
            "terminal_certificate",
            "discard"
          &#93;
        },
        "coverage": {
          "enum": &#91;
            "cover",
            "equivalence",
            "superset",
            "noncovering",
            "dependency",
            "terminal"
          &#93;
        },
        "propagates_emptiness": {
          "type": "boolean"
        },
        "proof_status": {
          "$ref": "#/$defs/proof_status"
        },
        "statement": {
          "type": "string"
        },
        "hypotheses": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "source_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "verifier": {
          "type": "string"
        },
        "complement_edges": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "semantic_digest": {
          "type": "string"
        },
        "notes": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "obligation": {
      "type": "object",
      "required": &#91;
        "obligation_id",
        "statement",
        "status",
        "blocks"
      &#93;,
      "properties": {
        "obligation_id": {
          "type": "string",
          "pattern": "^L8-O-&#91;A-Z0-9-&#93;+$"
        },
        "statement": {
          "type": "string"
        },
        "status": {
          "enum": &#91;
            "closed",
            "partially_closed",
            "open",
            "blocked"
          &#93;
        },
        "blocks": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "next_action": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "route_requirement": {
      "type": "object",
      "required": &#91;
        "from_node"
      &#93;,
      "properties": {
        "from_node": {
          "type": "string"
        },
        "all_of": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1
        },
        "any_of": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1
        }
      },
      "oneOf": &#91;
        {
          "required": &#91;
            "all_of"
          &#93;
        },
        {
          "required": &#91;
            "any_of"
          &#93;
        }
      &#93;,
      "additionalProperties": false
    },
    "coverage_target": {
      "type": "object",
      "required": &#91;
        "target_id",
        "kind",
        "expected",
        "accepted_proof_statuses"
      &#93;,
      "properties": {
        "target_id": {
          "type": "string"
        },
        "kind": {
          "enum": &#91;
            "routing",
            "exclusion"
          &#93;
        },
        "expected": {
          "enum": &#91;
            "complete",
            "incomplete"
          &#93;
        },
        "accepted_proof_statuses": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/proof_status"
          }
        },
        "requirements": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/route_requirement"
          },
          "minItems": 1
        },
        "assumption_nodes": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1
        },
        "prove_empty": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1
        },
        "notes": {
          "type": "string"
        }
      },
      "allOf": &#91;
        {
          "if": {
            "properties": {
              "kind": {
                "const": "routing"
              }
            }
          },
          "then": {
            "required": &#91;
              "requirements"
            &#93;
          }
        },
        {
          "if": {
            "properties": {
              "kind": {
                "const": "exclusion"
              }
            }
          },
          "then": {
            "required": &#91;
              "assumption_nodes",
              "prove_empty"
            &#93;
          }
        }
      &#93;,
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
</code></pre>

<a id="source-963267c8285aa781"></a>

## `research-notes/lane8-proof-queue-20260802-v1/queue.seed.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "queue_id": "lane8-proof-queue-v1",
  "scope": {
    "base_characteristic": 0,
    "geometric_semantics": "Terminal emptiness means no points over an algebraic closure of the declared coefficient field.",
    "claim_boundary": "This audit graph validates evidence and routing semantics. It does not promote the public degree-below-125 claim until the root-to-terminal coverage target becomes complete."
  },
  "sources": &#91;
    {
      "source_id": "GGHV-2022",
      "kind": "literature",
      "title": "Increasing the degree of a possible counterexample to the Jacobian Conjecture from 100 to 108",
      "locator": "arXiv:2204.14178; Theorem 2.1, Proposition 4.1, Proposition 4.3, Corollary 5.7"
    },
    {
      "source_id": "GGHV-2017",
      "kind": "literature",
      "title": "Some algorithms related to the Jacobian Conjecture",
      "locator": "arXiv:1708.07936; Theorem 2.20, Definition 2.25, Algorithm 8"
    },
    {
      "source_id": "PROGRAM6-SOURCE",
      "kind": "public_proof_source",
      "title": "Program 6 current text proof source",
      "locator": "research/proof-sources/06-plane-boundary/main/ and appendix degree-twenty-one-certificates"
    },
    {
      "source_id": "PROGRAM6-ARCHIVE",
      "kind": "technical_archive",
      "title": "Program 6 complete computational supplement",
      "locator": "assets/technical-materials/06-plane-boundary-computational-supplement.zip",
      "sha256": "4238149caa6e8a73723368e997b8c714a99258600268f14a008c5e514ecea585"
    },
    {
      "source_id": "L8-REPAIR-PACKET",
      "kind": "repair_packet",
      "title": "Lane 8 root-to-face and proof-queue checks",
      "locator": "assets/audit-repairs/lane8-proof-queue-v1/"
    }
  &#93;,
  "nodes": &#91;
    {
      "node_id": "L8-CANDIDATE-SUB125",
      "kind": "candidate_class",
      "statement": "Noninvertible plane Keller pairs in characteristic zero with maximum coordinate degree below 125, modulo exchange of coordinates.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93; is a nonzero constant"
        &#93;,
        "inverted_elements": &#91;
          "Jacobian constant"
        &#93;,
        "variables": &#91;
          "coefficients of P",
          "coefficients of Q"
        &#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;&#93;,
      "notes": "The imported literature theorem concerns hypothetical counterexamples; noninvertibility is not encoded by one finite coefficient ideal here."
    },
    {
      "node_id": "L8-DEGREE-72-108",
      "kind": "degree_family",
      "statement": "The surviving below-125 degree pair is (72,108), up to exchange.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;&#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Theorem-2.1"
      &#93;
    },
    {
      "node_id": "L8-FAMILY-828",
      "kind": "degree_family",
      "statement": "The surviving (72,108) case is the complete-chain family denoted (8,28); the (9,27) family is excluded.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "after extension to an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;&#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.1",
        "GGHV-2022:Corollary-5.7"
      &#93;
    },
    {
      "node_id": "L8-ROOT-828-TRUNCATED",
      "kind": "newton_root",
      "statement": "A Laurent Keller pair with bracket x^2 and the truncated Proposition 4.3 Newton polygons.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93;=x^2"
        &#93;,
        "inverted_elements": &#91;
          "product of P vertex coefficients",
          "product of Q vertex coefficients"
        &#93;,
        "required_zero": &#91;
          "all coefficients outside the two declared polygons"
        &#93;,
        "variables": &#91;
          "25 allowed P coefficients",
          "47 allowed Q coefficients"
        &#93;
      },
      "support": {
        "P": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              1,
              0
            &#93;,
            &#91;
              8,
              14
            &#93;,
            &#91;
              8,
              16
            &#93;
          &#93;,
          "lattice_count": 25,
          "deficiency": "b-2a+2",
          "layer_counts": &#91;
            8,
            8,
            9
          &#93;
        },
        "Q": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              2,
              1
            &#93;,
            &#91;
              12,
              21
            &#93;,
            &#91;
              12,
              24
            &#93;
          &#93;,
          "lattice_count": 47,
          "deficiency": "b-2a+3",
          "layer_counts": &#91;
            11,
            11,
            12,
            13
          &#93;
        }
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.3-case-2"
      &#93;
    },
    {
      "node_id": "L8-ROOT-828-FULL",
      "kind": "newton_root",
      "statement": "A Laurent Keller pair with bracket x^2 and the full Proposition 4.3 Newton polygons.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "&#91;P,Q&#93;=x^2"
        &#93;,
        "inverted_elements": &#91;
          "product of P vertex coefficients",
          "product of Q vertex coefficients"
        &#93;,
        "required_zero": &#91;
          "all coefficients outside the two declared polygons"
        &#93;,
        "variables": &#91;
          "61 allowed P coefficients",
          "125 allowed Q coefficients"
        &#93;
      },
      "support": {
        "P": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              1,
              0
            &#93;,
            &#91;
              8,
              14
            &#93;,
            &#91;
              8,
              16
            &#93;,
            &#91;
              0,
              8
            &#93;
          &#93;,
          "lattice_count": 61,
          "deficiency": "b-2a+2",
          "layer_counts": &#91;
            8,
            8,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1
          &#93;
        },
        "Q": {
          "vertices": &#91;
            &#91;
              0,
              0
            &#93;,
            &#91;
              2,
              1
            &#93;,
            &#91;
              12,
              21
            &#93;,
            &#91;
              12,
              24
            &#93;,
            &#91;
              0,
              12
            &#93;
          &#93;,
          "lattice_count": 125,
          "deficiency": "b-2a+3",
          "layer_counts": &#91;
            11,
            11,
            12,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1
          &#93;
        }
      },
      "proof_status": "audited_external_theorem",
      "terminal": false,
      "certificate_refs": &#91;
        "GGHV-2022:Proposition-4.3-case-1"
      &#93;
    },
    {
      "node_id": "L8-FACE-DEG21",
      "kind": "face_locus",
      "statement": "Polynomials p,q of degrees 7 and 10 with nonzero endpoint coefficients satisfying p*q+2*z*p*q'-3*z*p'*q=1.",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "p*q+2*z*p*q'-3*z*p'*q=1"
        &#93;,
        "inverted_elements": &#91;
          "p(0)",
          "q(0)",
          "lc(p)",
          "lc(q)"
        &#93;,
        "variables": &#91;
          "coefficients of p of degree at most 7",
          "coefficients of q of degree at most 10"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;
    },
    {
      "node_id": "L8-PASSPORT-DEG21",
      "kind": "passport_locus",
      "statement": "The rational map tau=z*q^2/p^3 has degree 21 and passport (2^10 1),(3^7),(17 1^4).",
      "field": {
        "base": "arbitrary characteristic-zero field",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "tau=z*q^2/p^3",
          "tau'=q/p^4"
        &#93;,
        "inverted_elements": &#91;
          "resultant(p,q)",
          "p(0)",
          "q(0)",
          "lc(p)",
          "lc(q)"
        &#93;,
        "variables": &#91;
          "z"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;
    },
    {
      "node_id": "L8-DESSIN-COUNT-5",
      "kind": "dessin_classification",
      "statement": "The degree-21 passport has five connected isomorphism classes, each with trivial deck group.",
      "field": {
        "base": "characteristic zero",
        "geometric_points": "over an algebraic closure"
      },
      "constructible_data": {
        "equations": &#91;
          "sigma_0*sigma_1*sigma_infinity=1"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "permutation triples with the declared cycle types"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:hurwitz_degree21.py"
      &#93;
    },
    {
      "node_id": "L8-QUINTIC-ORBIT",
      "kind": "coefficient_field_orbit",
      "statement": "The five normalized degree-21 faces form one Galois orbit over K0=Q&#91;u&#93;/(u^5-u^4+3u^3+3u^2+26); exact coefficient formulas are reconstructed in the repair packet.",
      "field": {
        "base": "K0",
        "geometric_points": "all five embeddings into an algebraic closure",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "exact p,q coefficient formulas in quintic_face_coefficients.json",
          "p*q+2*z*p*q'-3*z*p'*q=1",
          "z*q_monic^2-p^3 has degree at most 4"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "u"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "L8-REPAIR-PACKET:quintic_face_reconstruction.out"
      &#93;,
      "notes": "The packet reconstructs an irreducible quintic in the normalized coefficient s, verifies all face and order-17 contact identities, and gives an exact field isomorphism s=(20481190-2578004u+1664322u^2-709604u^3+221083u^4)/42799752 to the public Program 6 K0 model."
    },
    {
      "node_id": "L8-TRUNCATED-LAYER-SYSTEM",
      "kind": "finite_system",
      "statement": "The complete truncated-support compatibility system reconstructed exactly from the quintic face and all 25+47 coefficient windows.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "7 exact weight-three compatibility polynomials",
          "18 exact weight-four compatibility polynomials",
          "the 14-dimensional weighted-degree-four monomial span"
        &#93;,
        "inverted_elements": &#91;
          "P coefficient at exponent (8,16)",
          "Q coefficient at exponent (12,24)",
          "the already nonzero lower-face vertex coefficients"
        &#93;,
        "variables": &#91;
          "four effective positive-weight parameters"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json",
        "L8-REPAIR-PACKET:truncated_support_certificate.out"
      &#93;
    },
    {
      "node_id": "L8-TRUNCATED-EMPTY",
      "kind": "terminal_empty",
      "statement": "The exact vertex-saturated truncated Proposition 4.3 root is empty in characteristic zero for the complete quintic orbit.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 after radical/vertex contradiction"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": true,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;
    },
    {
      "node_id": "L8-FULL-EARLY-LAYERS",
      "kind": "finite_system",
      "statement": "The exact full-support layers 1 through 4 over the quintic face, including the forced square relation a*(W-kappa*Y^2)^2.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "layer-1, layer-2, and layer-3 compatibility functionals vanish identically",
          "layer-4 compatibility is a*(W-kappa*Y^2)^2"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "X,Y at layer 1",
          "U,V,W at layer 2",
          "R,S,T at layer 3",
          "H at layer 4"
        &#93;
      },
      "proof_status": "verified_in_packet",
      "terminal": false,
      "certificate_refs": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_early_layer_reduction.json",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.json"
      &#93;,
      "notes": "The reduced geometric locus satisfies W=kappa*Y^2, but the exact scheme-level equation is a square and its double structure is retained. All full-support layer maps from layer 5 onward are injective."
    },
    {
      "node_id": "L8-FULL-15-EQUATIONS",
      "kind": "finite_system",
      "statement": "The fifteen normalized compatibility equations in five variables obtained from the full support through layers five to eight.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "15 normalized equations with layer counts 1,3,5,6"
        &#93;,
        "inverted_elements": &#91;
          "the recorded normalization factor t_(1,1)"
        &#93;,
        "variables": &#91;
          "five normalized terminal variables"
        &#93;
      },
      "proof_status": "source_replay_needed",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance"
      &#93;
    },
    {
      "node_id": "L8-FULL-SIX-POLYNOMIALS",
      "kind": "finite_system",
      "statement": "The six selected obstruction polynomials rho,g1,...,g5 used in the compact toric certificate.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "rho",
          "g1",
          "g2",
          "g3",
          "g4",
          "g5"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "five normalized terminal variables"
        &#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate"
      &#93;
    },
    {
      "node_id": "L8-FULL-TORIC-EMPTY",
      "kind": "terminal_empty",
      "statement": "The six displayed full-support obstruction polynomials have no common geometric zero over K0.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 on the six-polynomial zero locus"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": true,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate",
        "PROGRAM6-ARCHIVE"
      &#93;
    },
    {
      "node_id": "L8-K4-STORED-SYSTEM",
      "kind": "finite_system",
      "statement": "The stored degree-21 specialization after the canonical k=4 adjacent-chart transition and forced common approximate root.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "complete layer-five-through-seven support and chart-matching equations"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;
          "stored adjacent-chart coefficients"
        &#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": false,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;
    },
    {
      "node_id": "L8-K4-LAYER7-EMPTY",
      "kind": "terminal_empty",
      "statement": "The stored adjacent-chart layer-five-through-seven system has no common geometric zero over K0.",
      "field": {
        "base": "K0",
        "geometric_points": "over an algebraic closure of K0",
        "defining_polynomial": "u^5-u^4+3u^3+3u^2+26"
      },
      "constructible_data": {
        "equations": &#91;
          "1=0 after the two recorded affine/weighted branches"
        &#93;,
        "inverted_elements": &#91;&#93;,
        "variables": &#91;&#93;
      },
      "proof_status": "verified_in_public_source",
      "terminal": true,
      "certificate_refs": &#91;
        "PROGRAM6-SOURCE:stored-terminal-layer-seven",
        "PROGRAM6-ARCHIVE"
      &#93;
    }
  &#93;,
  "edges": &#91;
    {
      "edge_id": "L8-E-SUB125-DEGREE",
      "from": "L8-CANDIDATE-SUB125",
      "to": &#91;
        "L8-DEGREE-72-108"
      &#93;,
      "edge_type": "external_import",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "Theorem 2.1 leaves only degree pair (72,108), up to exchange, below 125.",
      "hypotheses": &#91;
        "characteristic zero",
        "hypothetical noninvertible Keller pair",
        "maximum coordinate degree below 125"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Theorem-2.1"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-DEGREE-FAMILY",
      "from": "L8-DEGREE-72-108",
      "to": &#91;
        "L8-FAMILY-828"
      &#93;,
      "edge_type": "external_import",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "The (9,27) family is reduced by Proposition 4.1 to the system excluded by Corollary 5.7, leaving (8,28).",
      "hypotheses": &#91;
        "the complete-chain family list used in GGHV-2022"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Proposition-4.1",
        "GGHV-2022:Corollary-5.7"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FAMILY-ROOT-SPLIT",
      "from": "L8-FAMILY-828",
      "to": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "edge_type": "exhaustive_split",
      "coverage": "cover",
      "proof_status": "audited_external_theorem",
      "statement": "Proposition 4.3 gives exactly the two normalized Newton-polygon alternatives.",
      "hypotheses": &#91;
        "the (8,28) family",
        "the Laurent transformations in Proposition 4.3"
      &#93;,
      "source_refs": &#91;
        "GGHV-2022:Proposition-4.3"
      &#93;,
      "verifier": "root_face_check.py verifies the final exponent transform and bracket multiplier",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-TRUNCATED-FACE",
      "from": "L8-ROOT-828-TRUNCATED",
      "to": &#91;
        "L8-FACE-DEG21"
      &#93;,
      "edge_type": "forced_initial_form",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The minimum (-2,1)-valuation faces are x*p(x*y^2) and x^2*y*q(x*y^2), and their bracket forces the degree-21 face equation.",
      "hypotheses": &#91;
        "exact truncated Newton polygons",
        "&#91;P,Q&#93;=x^2"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-FACE",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-FACE-DEG21"
      &#93;,
      "edge_type": "forced_initial_form",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The full polygons have the same minimum (-2,1)-valuation faces, hence force the identical degree-21 face equation.",
      "hypotheses": &#91;
        "exact full Newton polygons",
        "&#91;P,Q&#93;=x^2"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FACE-PASSPORT",
      "from": "L8-FACE-DEG21",
      "to": &#91;
        "L8-PASSPORT-DEG21"
      &#93;,
      "edge_type": "forced_consequence",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "For tau=z*q^2/p^3, the face equation gives tau'=q/p^4 and the complete degree-21 passport.",
      "hypotheses": &#91;
        "degree p=7",
        "degree q=10",
        "nonzero endpoint coefficients"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "root_face_check.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-PASSPORT-DESSINS",
      "from": "L8-PASSPORT-DEG21",
      "to": &#91;
        "L8-DESSIN-COUNT-5"
      &#93;,
      "edge_type": "classification",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "The exact Frobenius/Murnaghan--Nakayama count is five; transitivity and trivial deck group turn the weighted count into five connected isomorphism classes.",
      "hypotheses": &#91;
        "cycle types (2^10 1),(3^7),(17 1^4)"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET"
      &#93;,
      "verifier": "hurwitz_degree21.py",
      "requires": &#91;&#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-DESSINS-QUINTIC",
      "from": "L8-DESSIN-COUNT-5",
      "to": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "edge_type": "coefficient_reconstruction",
      "coverage": "dependency",
      "proof_status": "verified_in_packet",
      "statement": "Under the monic normalization p=z^7+z^6+s z^5+... and q_monic monic of degree 10, exact order-17 contact determines p,q over an irreducible quintic. Its five embeddings give five distinct normalized covers and an exact isomorphism to the public Program 6 field K0.",
      "hypotheses": &#91;
        "a fixed normalization of p,q and z",
        "the five connected dessin classes"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "PROGRAM6-SOURCE:degree-21-Belyi-reconstruction"
      &#93;,
      "notes": "Because the passport has exactly five connected classes, the five distinct embeddings of the irreducible quintic exhaust the classes and form one Galois orbit.",
      "requires": &#91;&#93;,
      "propagates_emptiness": false,
      "verifier": "quintic_face_reconstruction.py"
    },
    {
      "edge_id": "L8-E-TRUNCATED-LAYERS",
      "from": "L8-ROOT-828-TRUNCATED",
      "to": &#91;
        "L8-TRUNCATED-LAYER-SYSTEM"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "The exact layer recursion has ranks 17,18,12 at layers 1,2,3; it produces seven weight-three and eighteen weight-four equations in effective parameters X,Y,V,W of weights 1,1,2,2.",
      "hypotheses": &#91;
        "one of the five normalized face embeddings",
        "truncated coefficient windows"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;,
      "notes": "The origin-vertex parameters U,D remain free. The required top vertices are explicit polynomials in X,Y,V,W.",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true,
      "verifier": "truncated_support_certificate.py"
    },
    {
      "edge_id": "L8-E-TRUNCATED-CERTIFICATE",
      "from": "L8-TRUNCATED-LAYER-SYSTEM",
      "to": &#91;
        "L8-TRUNCATED-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_packet",
      "statement": "Products of the seven weight-three equations with X,Y together with the eighteen weight-four equations span all fourteen weighted-degree-four monomials. A selected 14x14 minor has determinant 894 modulo (2053,u-216), so X,Y,V,W lie in the radical; the required top P and Q vertices therefore vanish.",
      "hypotheses": &#91;
        "the exact regenerated truncated system",
        "the declared vertex saturation"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true,
      "verifier": "truncated_support_certificate.py"
    },
    {
      "edge_id": "L8-E-FULL-EARLY",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-FULL-EARLY-LAYERS"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "verified_in_packet",
      "statement": "Reconstruct the complete full-support layers 1 through 4 exactly. The only nonzero early compatibility condition is the square a*(W-kappa*Y^2)^2; the exact layer-rank profile is recorded through layer 15.",
      "hypotheses": &#91;
        "one of the five normalized quintic face embeddings",
        "the full Proposition 4.3 coefficient windows"
      &#93;,
      "source_refs": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py"
      &#93;,
      "verifier": "full_early_layer_reduction.py; full_layer_rank_profile.py",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-LAYERS",
      "from": "L8-FULL-EARLY-LAYERS",
      "to": &#91;
        "L8-FULL-15-EQUATIONS"
      &#93;,
      "edge_type": "elimination",
      "coverage": "cover",
      "proof_status": "source_replay_needed",
      "statement": "Starting from the exact square branch and the injective layer maps from layer 5 onward, reproduce the obstruction equations through layer 8, every normalization/localization, and the reduction to the fifteen equations in five variables.",
      "hypotheses": &#91;
        "the exact full early-layer system",
        "the scheme-level square relation is retained until a radical argument is declared",
        "the full coefficient windows"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": true,
      "notes": "The early layers and all linear ranks are now independently closed. The remaining gap begins with nonlinear forcing at layer 5 and the provenance of the five-variable normalization."
    },
    {
      "edge_id": "L8-E-FULL-PROJECTION",
      "from": "L8-FULL-15-EQUATIONS",
      "to": &#91;
        "L8-FULL-SIX-POLYNOMIALS"
      &#93;,
      "edge_type": "relaxation",
      "coverage": "superset",
      "proof_status": "source_replay_needed",
      "statement": "Forget nine equations and retain the six indexed equations used in the compact toric certificate; emptiness of the larger six-equation zero locus excludes the fifteen-equation locus.",
      "hypotheses": &#91;
        "coefficientwise identification of the fifteen regenerated equations with the stored normalized system"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "notes": "This direction is a relaxation: V(15 equations) is contained in V(the selected 6).",
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-TORIC-CERTIFICATE",
      "from": "L8-FULL-SIX-POLYNOMIALS",
      "to": &#91;
        "L8-FULL-TORIC-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_public_source",
      "statement": "The compact toric argument proves that the six displayed polynomials have no common geometric zero over K0.",
      "hypotheses": &#91;
        "the exact six displayed polynomials",
        "the recorded good-prime and toric data"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:compact-toric-terminal-certificate",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    },
    {
      "edge_id": "L8-E-FULL-K4-STORED",
      "from": "L8-ROOT-828-FULL",
      "to": &#91;
        "L8-K4-STORED-SYSTEM"
      &#93;,
      "edge_type": "noncovering_specialization",
      "coverage": "noncovering",
      "proof_status": "verified_in_public_source",
      "statement": "The stored specialization admits the canonical k=4 adjacent-chart calculation, but no theorem presently says every full-root point reaches this stored system.",
      "hypotheses": &#91;
        "the additional stored specialization conditions"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;,
      "notes": "This edge is deliberately excluded from global coverage propagation.",
      "requires": &#91;
        "L8-QUINTIC-ORBIT"
      &#93;,
      "propagates_emptiness": false
    },
    {
      "edge_id": "L8-E-K4-CERTIFICATE",
      "from": "L8-K4-STORED-SYSTEM",
      "to": &#91;
        "L8-K4-LAYER7-EMPTY"
      &#93;,
      "edge_type": "terminal_certificate",
      "coverage": "terminal",
      "proof_status": "verified_in_public_source",
      "statement": "The complete stored layer-five-through-seven equations are empty after the two recorded branches are certified.",
      "hypotheses": &#91;
        "the exact stored adjacent-chart system"
      &#93;,
      "source_refs": &#91;
        "PROGRAM6-SOURCE:stored-terminal-layer-seven",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "requires": &#91;&#93;,
      "propagates_emptiness": true
    }
  &#93;,
  "obligations": &#91;
    {
      "obligation_id": "L8-O-LITERATURE-IMPORT",
      "statement": "State the exact external theorem chain from a sub-125 candidate to the two Proposition 4.3 roots and independently check the final monomial transformation.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "GGHV-2022",
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;,
      "next_action": "A full rederivation of the imported literature proofs is optional specialist verification, not an unrecorded queue edge."
    },
    {
      "obligation_id": "L8-O-COMMON-FACE",
      "statement": "Prove that both roots force the same degree-21 face and normal-layer operator.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:root_face_check.py"
      &#93;,
      "next_action": "Use the canonical layer labels in every downstream manifest."
    },
    {
      "obligation_id": "L8-O-QUINTIC-RECONSTRUCTION",
      "statement": "Independently regenerate normalized p,q for all five dessins and prove the displayed quintic field realizes one complete Galois orbit.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:quintic_face_reconstruction.py",
        "L8-REPAIR-PACKET:quintic_face_coefficients.json",
        "L8-REPAIR-PACKET:quintic_face_reconstruction.out"
      &#93;,
      "next_action": "Use the exported exact coefficients as the canonical lower-face input for the truncated and full normal-layer replays."
    },
    {
      "obligation_id": "L8-O-ARCHIVE-STAGE-MANIFEST",
      "statement": "Expose every root-to-terminal generation stage with node identifiers, branch conditions, code/input/output hashes, and semantic digests.",
      "status": "open",
      "blocks": &#91;
        "L8-E-TRUNCATED-LAYERS",
        "L8-E-FULL-LAYERS",
        "L8-E-FULL-PROJECTION"
      &#93;,
      "evidence": &#91;
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Materialize the archive and generate a deterministic stage manifest rather than relying on filenames and narrative provenance."
    },
    {
      "obligation_id": "L8-O-TRUNCATED-REPLAY",
      "statement": "Rebuild the 7+18 compatibility equations, the fourteen-monomial span, and the exact vertex saturation from the raw truncated windows.",
      "status": "closed",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:truncated_support_certificate.py",
        "L8-REPAIR-PACKET:truncated_support_certificate.json",
        "L8-REPAIR-PACKET:truncated_support_certificate.out"
      &#93;,
      "next_action": "Use the closed truncated branch as an independently certified child while auditing the full branch."
    },
    {
      "obligation_id": "L8-O-FULL-ELIMINATION-REPLAY",
      "statement": "Continue the independently reconstructed full branch from layer 5 through the fifteen normalized equations, preserving every denominator-zero branch and the nonreduced square structure.",
      "status": "open",
      "blocks": &#91;
        "L8-E-FULL-LAYERS",
        "L8-E-FULL-PROJECTION"
      &#93;,
      "evidence": &#91;
        "L8-REPAIR-PACKET:full_early_layer_reduction.py",
        "L8-REPAIR-PACKET:full_layer_rank_profile.py",
        "PROGRAM6-SOURCE:terminal-residue-provenance",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Derive the layer-5 obstruction from the exact square branch, then emit a row/column and extension/contraction ledger through layer 8. Use W=kappa*Y^2 only when explicitly passing to geometric radicals."
    },
    {
      "obligation_id": "L8-O-K4-COVERAGE",
      "statement": "Determine whether the k=4 adjacent-chart system covers a full-root branch or is only a stored specialization.",
      "status": "blocked",
      "blocks": &#91;
        "L8-E-FULL-K4-STORED"
      &#93;,
      "evidence": &#91;
        "PROGRAM6-SOURCE:k4-chart-transition"
      &#93;,
      "next_action": "Prove a Lane 9 chart-correspondence theorem or keep the edge noncovering."
    },
    {
      "obligation_id": "L8-O-INDEPENDENT-TERMINAL-REPLAY",
      "statement": "Independently replay at least one large terminal certificate from its exact generators and archived data.",
      "status": "open",
      "blocks": &#91;&#93;,
      "evidence": &#91;
        "PROGRAM6-SOURCE",
        "PROGRAM6-ARCHIVE"
      &#93;,
      "next_action": "Prefer the compact six-polynomial toric certificate because its mathematical lifting argument is already isolated."
    }
  &#93;,
  "coverage_targets": &#91;
    {
      "target_id": "L8-COVERAGE-LITERATURE-ROOTS",
      "kind": "routing",
      "expected": "complete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "requirements": &#91;
        {
          "from_node": "L8-CANDIDATE-SUB125",
          "all_of": &#91;
            "L8-ROOT-828-TRUNCATED",
            "L8-ROOT-828-FULL"
          &#93;
        }
      &#93;,
      "notes": "Statement-level audit of the imported theorem chain, not a new proof of every cited literature lemma."
    },
    {
      "target_id": "L8-COVERAGE-ROOTS-TO-FACE",
      "kind": "routing",
      "expected": "complete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "requirements": &#91;
        {
          "from_node": "L8-ROOT-828-TRUNCATED",
          "all_of": &#91;
            "L8-FACE-DEG21",
            "L8-PASSPORT-DEG21",
            "L8-DESSIN-COUNT-5"
          &#93;
        },
        {
          "from_node": "L8-ROOT-828-FULL",
          "all_of": &#91;
            "L8-FACE-DEG21",
            "L8-PASSPORT-DEG21",
            "L8-DESSIN-COUNT-5"
          &#93;
        }
      &#93;,
      "notes": "The common face, passport, and count are independently checked in this packet."
    },
    {
      "target_id": "L8-COVERAGE-ROOTS-TO-TERMINALS",
      "kind": "exclusion",
      "expected": "incomplete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "assumption_nodes": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "prove_empty": &#91;
        "L8-ROOT-828-TRUNCATED",
        "L8-ROOT-828-FULL"
      &#93;,
      "notes": "The missing independently replayed edges are the quintic reconstruction and the raw-support-to-terminal elimination ledgers."
    },
    {
      "target_id": "L8-COVERAGE-SUB125-EXCLUSION",
      "kind": "exclusion",
      "expected": "incomplete",
      "accepted_proof_statuses": &#91;
        "verified_in_packet",
        "audited_external_theorem",
        "verified_in_public_source"
      &#93;,
      "assumption_nodes": &#91;
        "L8-CANDIDATE-SUB125"
      &#93;,
      "prove_empty": &#91;
        "L8-CANDIDATE-SUB125"
      &#93;,
      "notes": "This is the standalone below-125 conclusion. It can become complete only after both imported roots are excluded through covering edges."
    }
  &#93;
}
</code></pre>

<a id="source-68d42e1275446a86"></a>

## `research-notes/lane8-proof-queue-20260802-v1/quintic_face_coefficients.json`

<pre><code class="language-json">
{
  "checks": {
    "face_equation_after_scaling": "1",
    "five_distinct_normalized_embeddings": true,
    "one_galois_orbit": true,
    "p0_times_q_face0": "1",
    "reverse_contact_zero_degrees": &#91;
      11,
      12,
      13,
      14,
      15,
      16
    &#93;,
    "z_q_squared_minus_p_cubed_nonzero_degrees": &#91;
      0,
      1,
      2,
      3,
      4
    &#93;
  },
  "face_constant": "17*(777960184039372392872832784982762474838303744*s**4 - 1237708637975020902558626849050592674716724992*s**3 + 739224456278760216429747831425173330430701328*s**2 - 196428297681210369803773783027972852412730024*s + 19593013520468071527462229586068430071003845)/28063178201577871798641123727342560497991317452750848",
  "normalization": {
    "p": "monic degree 7 with coefficient of z^6 equal to 1",
    "q_face": "q_monic / face_constant, so pq+2zpq'-3zp'q=1",
    "q_monic": "monic degree 10",
    "source_scaling": "fixed by the coefficient of z^6 in p"
  },
  "p_coefficients_descending": &#91;
    "1",
    "1",
    "s",
    "(3771978574908902400*s**4 - 7556165936778735360*s**3 + 5450946367591254384*s**2 - 1699030592727011128*s + 194711288931974931)/2789916527204736",
    "7*(1472867824488238080*s**4 - 2950502889599315712*s**3 + 2129064709044490224*s**2 - 664388468462807608*s + 76242600010205835)/11159666108818944",
    "7*(1898608366334131200*s**4 - 3803361970401319680*s**3 + 2745126606514279984*s**2 - 857130636468363480*s + 98443252126745919)/66957996652913664",
    "(5513086784810050560*s**4 - 11023906566235965696*s**3 + 7949047218967327952*s**2 - 2481117197487437928*s + 284986511308009521)/401747979917481984",
    "(2473699609838592*s**4 - 4880250718447104*s**3 + 3484831588909616*s**2 - 1079655594514872*s + 123291106405875)/15858472891479552"
  &#93;,
  "public_program6_field": {
    "defining_polynomial": "u**5 - u**4 + 3*u**3 + 3*u**2 + 26",
    "degree": 5,
    "field_isomorphism_s_in_terms_of_u": "221083*u**4/42799752 - 177401*u**3/10699938 + 277387*u**2/7133292 - 644501*u/10699938 + 10240595/21399876",
    "generator": "u",
    "irreducible_over_Q": true
  },
  "q_face_relation": "q_face = q_monic / face_constant",
  "q_monic_coefficients_descending": &#91;
    "1",
    "3/2",
    "3*(4*s + 1)/8",
    "(3771978574908902400*s**4 - 7556165936778735360*s**3 + 5450946367591254384*s**2 - 1697635634463408760*s + 194595042410008067)/1859944351469824",
    "3*(5951343973745157120*s**4 - 11921950700250893568*s**3 + 8602711871673715024*s**2 - 2683391807652425960*s + 307765049239447001)/7439777405879296",
    "(101187260483145016320*s**4 - 202702034413640072448*s**3 + 146303191485735418192*s**2 - 45669472371113295336*s + 5242686174291914649)/89277328870551552",
    "11*(26465322115245229056*s**4 - 52986755217653851392*s**3 + 38239288659333073616*s**2 - 11940187746533774760*s + 1371484762039086417)/1071327946446618624",
    "(2011173821479514059776*s**4 - 4018261479831380553984*s**3 + 2896577844049680326288*s**2 - 904008543328493848968*s + 103833145536070320765)/57851709108117405696",
    "7*(346588300924295777280*s**4 - 685966291053658497792*s**3 + 491386077685161753584*s**2 - 152695897588184593272*s + 17485281252141209739)/1041330763946113302528",
    "(145747783471882319004672*s**4 - 277442752789030304083968*s**3 + 193224993139507972184944*s**2 - 58770307670861825957064*s + 6616984467616228417779)/1806448542755520051560448",
    "(3893628591744609832031232*s**4 - 6621734527051672154873088*s**3 + 4204765332332831448412304*s**2 - 1182767987201814807052488*s + 124452063517833423529533)/1857029101952674613004140544"
  &#93;,
  "reconstructed_field": {
    "defining_polynomial": "287548593020928*s**5 - 688401965085696*s**4 + 640652914818432*s**3 - 292066554895024*s**2 + 65563255857792*s - 5817852446211",
    "degree": 5,
    "generator": "s",
    "irreducible_over_Q": true
  },
  "schema_version": 1
}
</code></pre>

<a id="source-de3965d83ed72274"></a>

## `research-notes/lane8-proof-queue-20260802-v1/quintic_face_reconstruction.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact reconstruction of the five normalized degree-21 face covers.

This script is independent of the large Program 6 certificate archive.  It
works in the explicitly reconstructed quintic field Q(s), builds normalized
polynomials p and q, checks the order-17 Belyi contact, normalizes the face
Jacobian equation to 1, and verifies an exact isomorphism with the quintic
field model used by the public Program 6 source.

The normalization is

    p(z) = z^7 + z^6 + s z^5 + ...,
    q_monic(z) = z^10 + (3/2) z^9 + ... .

The unique simple point over 0 and the unique index-17 point over the third
branch value fix 0 and infinity on the source.  The remaining source scaling
is killed by the coefficient of z^6 in p being 1.  Thus the five embeddings
of the irreducible quintic give five distinct normalized covers.  Combined
with the independent Hurwitz count of five, they exhaust the dessin classes
and form one Galois orbit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import sympy as sp

s, z, u = sp.symbols("s z u")

# Positive-leading defining polynomial of the reconstructed coefficient field.
M_EXPR = (
    287548593020928 * s**5
    - 688401965085696 * s**4
    + 640652914818432 * s**3
    - 292066554895024 * s**2
    + 65563255857792 * s
    - 5817852446211
)
M = sp.Poly(M_EXPR, s, domain=sp.QQ)

# Public Program 6 field model.
K0_EXPR = u**5 - u**4 + 3 * u**3 + 3 * u**2 + 26
K0 = sp.Poly(K0_EXPR, u, domain=sp.QQ)

# Exact embedding of the reconstructed primitive element into K0.
S_IN_K0 = (
    20481190
    - 2578004 * u
    + 1664322 * u**2
    - 709604 * u**3
    + 221083 * u**4
) / sp.Integer(42799752)

# Coefficients a_i of p(z)=z^7+a_1 z^6+...+a_7.
A_RAW: dict&#91;int, sp.Expr&#93; = {
    1: sp.Integer(1),
    2: s,
    3: (
        3771978574908902400 * s**4
        - 7556165936778735360 * s**3
        + 5450946367591254384 * s**2
        - 1699030592727011128 * s
        + 194711288931974931
    )
    / sp.Integer(2789916527204736),
    4: 7
    * (
        1472867824488238080 * s**4
        - 2950502889599315712 * s**3
        + 2129064709044490224 * s**2
        - 664388468462807608 * s
        + 76242600010205835
    )
    / sp.Integer(11159666108818944),
    5: 7
    * (
        1898608366334131200 * s**4
        - 3803361970401319680 * s**3
        + 2745126606514279984 * s**2
        - 857130636468363480 * s
        + 98443252126745919
    )
    / sp.Integer(66957996652913664),
    6: (
        5513086784810050560 * s**4
        - 11023906566235965696 * s**3
        + 7949047218967327952 * s**2
        - 2481117197487437928 * s
        + 284986511308009521
    )
    / sp.Integer(401747979917481984),
    7: (
        2473699609838592 * s**4
        - 4880250718447104 * s**3
        + 3484831588909616 * s**2
        - 1079655594514872 * s
        + 123291106405875
    )
    / sp.Integer(15858472891479552),
}


def reduce_field(expr: sp.Expr) -&gt; sp.Expr:
    """Reduce a rational function in s to the degree-&lt;5 basis of Q(s)."""
    expr = sp.cancel(expr)
    numerator, denominator = sp.fraction(expr)
    denominator_poly = sp.Poly(denominator, s, domain=sp.QQ)
    try:
        inverse = sp.invert(denominator_poly, M).as_expr()
    except sp.polys.polyerrors.NotInvertible as exc:
        raise ValueError(f"denominator is zero in Q(s): {denominator}") from exc
    reduced = sp.rem(
        sp.Poly(sp.expand(numerator * inverse), s, domain=sp.QQ), M
    ).as_expr()
    return sp.cancel(reduced)


def reduce_z_coefficients(expr: sp.Expr) -&gt; sp.Poly:
    """Reduce every z coefficient of expr in the field Q(s)."""
    polynomial = sp.Poly(sp.expand(expr), z)
    result = sp.Integer(0)
    for (power,), coefficient in polynomial.terms():
        result += reduce_field(coefficient) * z**power
    return sp.Poly(sp.expand(result), z)


def coefficient_list_descending(poly: sp.Poly, degree: int) -&gt; list&#91;sp.Expr&#93;:
    return &#91;reduce_field(poly.coeff_monomial(z**power)) for power in range(degree, -1, -1)&#93;


def expression_strings(values: Iterable&#91;sp.Expr&#93;) -&gt; list&#91;str&#93;:
    return &#91;sp.sstr(sp.factor(value)) for value in values&#93;


def reconstruct() -&gt; dict&#91;str, object&#93;:
    assert M.degree() == 5 and M.is_irreducible
    assert K0.degree() == 5 and K0.is_irreducible

    a = {index: reduce_field(value) for index, value in A_RAW.items()}
    p = sp.Poly(z**7 + sum(a&#91;i&#93; * z ** (7 - i) for i in range(1, 8)), z)

    # Reverse-polynomial contact condition.  If
    # P(T)=1+a_1 T+...+a_7 T^7 and Q(T)=1+b_1 T+...+b_10 T^10,
    # solve Q(T)^2=P(T)^3 successively through degree 10.
    p_reverse = &#91;sp.Integer(1)&#93; + &#91;a&#91;i&#93; for i in range(1, 8)&#93;
    p_cube: list&#91;sp.Expr&#93; = &#91;&#93;
    for total in range(21):
        coefficient = sum(
            p_reverse&#91;i&#93; * p_reverse&#91;j&#93; * p_reverse&#91;k&#93;
            for i in range(8)
            for j in range(8)
            for k in range(8)
            if i + j + k == total
        )
        p_cube.append(reduce_field(coefficient))

    q_reverse = &#91;sp.Integer(1)&#93;
    for total in range(1, 11):
        known = sum(q_reverse&#91;i&#93; * q_reverse&#91;total - i&#93; for i in range(1, total))
        q_reverse.append(reduce_field((p_cube&#91;total&#93; - known) / 2))

    # The remaining contact equations, degrees 11 through 16, produce M(s).
    contact_residuals: dict&#91;int, sp.Expr&#93; = {}
    for total in range(11, 17):
        q_square = sum(
            q_reverse&#91;i&#93; * q_reverse&#91;total - i&#93;
            for i in range(max(0, total - 10), min(10, total) + 1)
        )
        contact_residuals&#91;total&#93; = reduce_field(q_square - p_cube&#91;total&#93;)
    assert all(value == 0 for value in contact_residuals.values())

    q_monic = sp.Poly(
        z**10 + sum(q_reverse&#91;i&#93; * z ** (10 - i) for i in range(1, 11)), z
    )

    # In z coordinates, order-17 contact at infinity means z*q^2-p^3 has
    # degree at most 4.
    belyi_residual = reduce_z_coefficients(z * q_monic.as_expr() ** 2 - p.as_expr() ** 3)
    nonzero_residual_degrees = sorted(
        power&#91;0&#93;
        for power, coefficient in belyi_residual.terms()
        if reduce_field(coefficient) != 0
    )
    assert nonzero_residual_degrees == &#91;0, 1, 2, 3, 4&#93;

    face_expression = reduce_z_coefficients(
        p.as_expr() * q_monic.as_expr()
        + 2 * z * p.as_expr() * sp.diff(q_monic.as_expr(), z)
        - 3 * z * sp.diff(p.as_expr(), z) * q_monic.as_expr()
    )
    nonzero_face_terms = &#91;
        (power&#91;0&#93;, reduce_field(coefficient))
        for power, coefficient in face_expression.terms()
        if reduce_field(coefficient) != 0
    &#93;
    assert len(nonzero_face_terms) == 1 and nonzero_face_terms&#91;0&#93;&#91;0&#93; == 0
    face_constant = nonzero_face_terms&#91;0&#93;&#91;1&#93;
    assert face_constant != 0
    assert reduce_field(p.nth(0) * q_monic.nth(0) - face_constant) == 0

    # Normalize q so the Jacobian face equation has right side 1.
    q_face_expr = sp.expand(q_monic.as_expr() / face_constant)
    normalized_face = reduce_z_coefficients(
        p.as_expr() * q_face_expr
        + 2 * z * p.as_expr() * sp.diff(q_face_expr, z)
        - 3 * z * sp.diff(p.as_expr(), z) * q_face_expr
    )
    assert normalized_face.as_expr() == 1
    assert reduce_field(p.nth(0) * q_monic.nth(0) / face_constant) == 1

    # Verify exact compatibility with the public K0 field model.
    map_numerator, _ = sp.fraction(sp.cancel(M_EXPR.subs(s, S_IN_K0)))
    map_remainder = sp.rem(sp.Poly(map_numerator, u, domain=sp.QQ), K0).as_expr()
    assert map_remainder == 0
    # Since both defining polynomials are irreducible of degree five and the
    # image is visibly nonconstant, this homomorphism is an isomorphism.
    assert sp.Poly(sp.together(S_IN_K0).as_numer_denom()&#91;0&#93;, u).degree() &gt; 0

    p_coefficients = coefficient_list_descending(p, 7)
    q_coefficients = coefficient_list_descending(q_monic, 10)

    return {
        "schema_version": 1,
        "normalization": {
            "p": "monic degree 7 with coefficient of z^6 equal to 1",
            "q_monic": "monic degree 10",
            "q_face": "q_monic / face_constant, so pq+2zpq'-3zp'q=1",
            "source_scaling": "fixed by the coefficient of z^6 in p",
        },
        "reconstructed_field": {
            "generator": "s",
            "defining_polynomial": sp.sstr(M_EXPR),
            "degree": 5,
            "irreducible_over_Q": True,
        },
        "public_program6_field": {
            "generator": "u",
            "defining_polynomial": sp.sstr(K0_EXPR),
            "degree": 5,
            "irreducible_over_Q": True,
            "field_isomorphism_s_in_terms_of_u": sp.sstr(S_IN_K0),
        },
        "p_coefficients_descending": expression_strings(p_coefficients),
        "q_monic_coefficients_descending": expression_strings(q_coefficients),
        "face_constant": sp.sstr(sp.factor(face_constant)),
        "q_face_relation": "q_face = q_monic / face_constant",
        "checks": {
            "reverse_contact_zero_degrees": sorted(contact_residuals),
            "z_q_squared_minus_p_cubed_nonzero_degrees": nonzero_residual_degrees,
            "face_equation_after_scaling": "1",
            "p0_times_q_face0": "1",
            "five_distinct_normalized_embeddings": True,
            "one_galois_orbit": True,
        },
    }


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        help="write the exact reconstructed coefficients and field map as JSON",
    )
    args = parser.parse_args()

    result = reconstruct()
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    print("reconstructed field degree: 5")
    print("reconstructed field irreducible over Q: yes")
    print("order-17 contact equations: exact")
    print("z*q_monic^2-p^3 nonzero degrees: 0,1,2,3,4")
    print("normalized face equation: p*q+2z*p*q'-3z*p'*q = 1")
    print("exact field isomorphism to Program 6 K0: verified")
    print("five embeddings: five distinct normalized covers in one Galois orbit")
    if args.output is not None:
        print(f"coefficient export: {args.output.name}")
    print("PASS: exact quintic degree-21 face reconstruction succeeded")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-0362c0ea7e22f043"></a>

## `research-notes/lane8-proof-queue-20260802-v1/root_face_check.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent exact checks for the first certified Lane 8 queue edges.

This script uses only the two Proposition 4.3 Newton polygons and elementary
symbolic algebra. It does not read the Program 6 terminal archive.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy as sp

Point = tuple&#91;int, int&#93;


@dataclass(frozen=True)
class RootData:
    name: str
    p_vertices: tuple&#91;Point, ...&#93;
    q_vertices: tuple&#91;Point, ...&#93;
    p_count: int
    q_count: int
    p_layers: tuple&#91;int, ...&#93;
    q_layers: tuple&#91;int, ...&#93;


def signed_area2(vertices: Sequence&#91;Point&#93;) -&gt; int:
    return sum(
        vertices&#91;i&#93;&#91;0&#93; * vertices&#91;(i + 1) % len(vertices)&#93;&#91;1&#93;
        - vertices&#91;(i + 1) % len(vertices)&#93;&#91;0&#93; * vertices&#91;i&#93;&#91;1&#93;
        for i in range(len(vertices))
    )


def convex_lattice_points(vertices: Sequence&#91;Point&#93;) -&gt; set&#91;Point&#93;:
    """Return all lattice points in a convex polygon, including its boundary."""
    polygon = list(vertices)
    if signed_area2(polygon) &lt; 0:
        polygon.reverse()
    xmin = min(x for x, _ in polygon)
    xmax = max(x for x, _ in polygon)
    ymin = min(y for _, y in polygon)
    ymax = max(y for _, y in polygon)
    answer: set&#91;Point&#93; = set()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            cross_products = &#91;&#93;
            for i, (x1, y1) in enumerate(polygon):
                x2, y2 = polygon&#91;(i + 1) % len(polygon)&#93;
                cross_products.append((x2 - x1) * (y - y1) - (y2 - y1) * (x - x1))
            if all(value &gt;= 0 for value in cross_products):
                answer.add((x, y))
    return answer


def layer_profile(points: Iterable&#91;Point&#93;, offset: int) -&gt; tuple&#91;int, ...&#93;:
    counts = Counter(y - 2 * x + offset for x, y in points)
    assert min(counts) == 0, counts
    assert set(counts) == set(range(max(counts) + 1)), counts
    return tuple(counts&#91;i&#93; for i in range(max(counts) + 1))


def transform_exponent(point: Point) -&gt; Point:
    """Exponent map for phi(x)=x^-1, phi(y)=x^4 y."""
    a, b = point
    return (-a + 4 * b, b)


def check_roots() -&gt; None:
    roots = (
        RootData(
            name="truncated",
            p_vertices=((0, 0), (1, 0), (8, 14), (8, 16)),
            q_vertices=((0, 0), (2, 1), (12, 21), (12, 24)),
            p_count=25,
            q_count=47,
            p_layers=(8, 8, 9),
            q_layers=(11, 11, 12, 13),
        ),
        RootData(
            name="full",
            p_vertices=((0, 0), (1, 0), (8, 14), (8, 16), (0, 8)),
            q_vertices=((0, 0), (2, 1), (12, 21), (12, 24), (0, 12)),
            p_count=61,
            q_count=125,
            p_layers=(8, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1),
            q_layers=(11, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1),
        ),
    )

    point_sets: dict&#91;str, tuple&#91;set&#91;Point&#93;, set&#91;Point&#93;&#93;&#93; = {}
    for root in roots:
        p_points = convex_lattice_points(root.p_vertices)
        q_points = convex_lattice_points(root.q_vertices)
        assert len(p_points) == root.p_count
        assert len(q_points) == root.q_count
        assert layer_profile(p_points, 2) == root.p_layers
        assert layer_profile(q_points, 3) == root.q_layers
        point_sets&#91;root.name&#93; = (p_points, q_points)
        print(
            f"{root.name}: lattice points P/Q={len(p_points)}/{len(q_points)}; "
            f"layer profiles P={root.p_layers}, Q={root.q_layers}"
        )

    truncated_p, truncated_q = point_sets&#91;"truncated"&#93;
    full_p, full_q = point_sets&#91;"full"&#93;
    assert truncated_p &lt;= full_p
    assert truncated_q &lt;= full_q
    print("truncated windows are subsets of full windows")

    # Vertices immediately before the final Laurent monomial map in the proof
    # of Proposition 4.3. Cases a,b omit the extra vertices; case c includes them.
    pre_p_truncated = {(-1, 0), (0, 0), (56, 16), (48, 14)}
    pre_q_truncated = {(2, 1), (0, 0), (84, 24), (72, 21)}
    pre_p_full = pre_p_truncated | {(32, 8)}
    pre_q_full = pre_q_truncated | {(48, 12)}
    assert {transform_exponent(p) for p in pre_p_truncated} == set(roots&#91;0&#93;.p_vertices)
    assert {transform_exponent(p) for p in pre_q_truncated} == set(roots&#91;0&#93;.q_vertices)
    assert {transform_exponent(p) for p in pre_p_full} == set(roots&#91;1&#93;.p_vertices)
    assert {transform_exponent(p) for p in pre_q_full} == set(roots&#91;1&#93;.q_vertices)

    x, y = sp.symbols("x y", nonzero=True)
    jacobian = sp.Matrix(
        &#91;
            &#91;sp.diff(x**-1, x), sp.diff(x**-1, y)&#93;,
            &#91;sp.diff(x**4 * y, x), sp.diff(x**4 * y, y)&#93;,
        &#93;
    ).det()
    assert sp.simplify(jacobian + x**2) == 0
    print("final monomial map: all vertices match and Jacobian determinant is -x^2")

    # The minimum-valuation faces are exactly the z-strings claimed in the repair.
    for root in roots:
        p_points, q_points = point_sets&#91;root.name&#93;
        p_min = min(-2 * a + b for a, b in p_points)
        q_min = min(-2 * a + b for a, b in q_points)
        p_face = {(a, b) for a, b in p_points if -2 * a + b == p_min}
        q_face = {(a, b) for a, b in q_points if -2 * a + b == q_min}
        assert p_min == -2
        assert q_min == -3
        assert p_face == {(k + 1, 2 * k) for k in range(8)}
        assert q_face == {(k + 2, 2 * k + 1) for k in range(11)}
    print("both roots force P_face=x p(xy^2), deg p=7, and Q_face=x^2 y q(xy^2), deg q=10")


def check_face_and_belyi_identities() -&gt; None:
    x, y, z = sp.symbols("x y z", nonzero=True)
    zxy = x * y**2
    p = sp.Function("p")
    q = sp.Function("q")
    pxy = p(zxy)
    qxy = q(zxy)
    p_face = x * pxy
    q_face = x**2 * y * qxy
    bracket = sp.diff(p_face, x) * sp.diff(q_face, y) - sp.diff(p_face, y) * sp.diff(q_face, x)
    expected = x**2 * (
        pxy * qxy
        + 2 * zxy * pxy * sp.diff(q(z), z).subs(z, zxy)
        - 3 * zxy * sp.diff(p(z), z).subs(z, zxy) * qxy
    )
    assert sp.simplify(bracket - expected) == 0
    print("face bracket identity verified exactly")

    pz = p(z)
    qz = q(z)
    face_ode = pz * qz + 2 * z * pz * sp.diff(qz, z) - 3 * z * sp.diff(pz, z) * qz
    tau = z * qz**2 / pz**3
    derivative_identity = sp.diff(tau, z) - qz / pz**4 * face_ode
    assert sp.simplify(derivative_identity) == 0
    assert 10 + 14 + 16 == 2 * 21 - 2
    print("Belyi derivative identity and degree-21 Riemann-Hurwitz count verified")


def check_normal_layer_identity() -&gt; None:
    x, y = sp.symbols("x y", nonzero=True)
    zxy = x * y**2
    A = sp.Function("A")
    B = sp.Function("B")
    p_expr = y**-2 * A(zxy, y)
    q_expr = y**-3 * B(zxy, y)
    bracket = sp.diff(p_expr, x) * sp.diff(q_expr, y) - sp.diff(p_expr, y) * sp.diff(q_expr, x)

    z, t = sp.symbols("z t", nonzero=True)
    Az = A(z, t)
    Bz = B(z, t)
    normal_numerator = (
        2 * Az * sp.diff(Bz, z)
        - 3 * sp.diff(Az, z) * Bz
        + t * (sp.diff(Az, z) * sp.diff(Bz, t) - sp.diff(Az, t) * sp.diff(Bz, z))
    )
    converted = sp.simplify((bracket * y**4).subs({x: z / t**2, y: t}) - normal_numerator)
    assert converted == 0
    print("normal-coordinate determinant equation verified exactly")

    # Check the all-r coefficient formula through a nontrivial finite truncation.
    order = 7
    a = &#91;sp.Function(f"A{i}")(z) for i in range(order + 1)&#93;
    b = &#91;sp.Function(f"B{i}")(z) for i in range(order + 1)&#93;
    a_series = sum(t**i * a&#91;i&#93; for i in range(order + 1))
    b_series = sum(t**i * b&#91;i&#93; for i in range(order + 1))
    expression = sp.expand(
        2 * a_series * sp.diff(b_series, z)
        - 3 * sp.diff(a_series, z) * b_series
        + t * (
            sp.diff(a_series, z) * sp.diff(b_series, t)
            - sp.diff(a_series, t) * sp.diff(b_series, z)
        )
    )
    for r in range(order + 1):
        actual = sp.expand(expression).coeff(t, r)
        expected = sum(
            (2 - i) * a&#91;i&#93; * sp.diff(b&#91;j&#93;, z)
            + (j - 3) * sp.diff(a&#91;i&#93;, z) * b&#91;j&#93;
            for i in range(r + 1)
            for j in &#91;r - i&#93;
        )
        assert sp.simplify(actual - expected) == 0
    print(f"triangular layer recurrence verified for all coefficients r=0,...,{order}")


def main() -&gt; None:
    check_roots()
    check_face_and_belyi_identities()
    check_normal_layer_identity()
    print("PASS: all independent root-to-face checks succeeded")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-640bafff64cc649e"></a>

## `research-notes/lane8-proof-queue-20260802-v1/truncated_support_certificate.json`

<pre><code class="language-json">
{
  "conclusion": {
    "P_top_vertex": "A2 coefficient of z^8, exponent (8,16)",
    "Q_top_vertex": "B3 coefficient of z^12, exponent (12,24)",
    "both_vanish_on_geometric_zero_set": true,
    "vertex_saturated_truncated_locus_empty": true
  },
  "degree_four_span": {
    "basis_dimension": 14,
    "equation_rows": 32,
    "good_reduction": {
      "minor_determinant": 894,
      "prime": 2053,
      "s": 1831,
      "selected_row_indices": &#91;
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        14,
        15,
        16
      &#93;,
      "selected_row_labels": &#91;
        "X*layer3&#91;0&#93;",
        "Y*layer3&#91;0&#93;",
        "X*layer3&#91;1&#93;",
        "Y*layer3&#91;1&#93;",
        "X*layer3&#91;2&#93;",
        "Y*layer3&#91;2&#93;",
        "X*layer3&#91;3&#93;",
        "Y*layer3&#91;3&#93;",
        "X*layer3&#91;4&#93;",
        "Y*layer3&#91;4&#93;",
        "X*layer3&#91;5&#93;",
        "layer4&#91;z^2&#93;",
        "layer4&#91;z^3&#93;",
        "layer4&#91;z^4&#93;"
      &#93;,
      "u": 216
    },
    "rank": 14
  },
  "effective_parameters": {
    "free_origin_vertices": &#91;
      "U",
      "D"
    &#93;,
    "names": &#91;
      "X",
      "Y",
      "V",
      "W"
    &#93;,
    "weights": &#91;
      1,
      1,
      2,
      2
    &#93;
  },
  "field": {
    "public_model": "u**5 - u**4 + 3*u**3 + 3*u**2 + 26",
    "reconstructed": "287548593020928*s**5 - 688401965085696*s**4 + 640652914818432*s**3 - 292066554895024*s**2 + 65563255857792*s - 5817852446211"
  },
  "linear_layers": {
    "D1": {
      "free_columns": &#91;
        17,
        18
      &#93;,
      "rank": 17,
      "shape": &#91;
        18,
        19
      &#93;
    },
    "D2": {
      "compatibility_zero": true,
      "free_columns": &#91;
        0,
        19,
        20
      &#93;,
      "rank": 18,
      "shape": &#91;
        19,
        21
      &#93;
    },
    "D3": {
      "compatibility_count": 7,
      "free_columns": &#91;
        0
      &#93;,
      "rank": 12,
      "shape": &#91;
        19,
        13
      &#93;
    },
    "layer4_equation_count": 18
  },
  "schema_version": 1
}
</code></pre>

<a id="source-aebcda934fbbb291"></a>

## `research-notes/lane8-proof-queue-20260802-v1/truncated_support_certificate.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact independent certificate for the truncated (8,28) Newton root.

The script reconstructs the quintic degree-21 face, solves the complete
truncated normal-layer system over the exact number field, and proves that
the required top P and Q vertex coefficients vanish on every solution.

No Program 6 terminal archive is read.
"""
from __future__ import annotations
from fractions import Fraction
import argparse
import json
from pathlib import Path
import sympy as sp
import quintic_face_reconstruction as qr

class K:
    __slots__=('c',)
    def __init__(self,c=(0,0,0,0,0)):
        if isinstance(c,K): self.c=c.c
        elif isinstance(c,(int,Fraction)): self.c=(Fraction(c),Fraction(0),Fraction(0),Fraction(0),Fraction(0))
        else:
            cc=tuple(Fraction(x) for x in c); self.c=cc+(Fraction(0),)*(5-len(cc))
    @staticmethod
    def from_expr(e):
        e=qr.reduce_field(e); p=sp.Poly(e,qr.s,domain=sp.QQ)
        return K(tuple(Fraction(int(p.nth(i).p),int(p.nth(i).q)) for i in range(5)))
    def expr(self): return sum(sp.Rational(x.numerator,x.denominator)*qr.s**i for i,x in enumerate(self.c))
    def __add__(self,o):
        o=K(o); return K(tuple(a+b for a,b in zip(self.c,o.c)))
    __radd__=__add__
    def __neg__(self):return K(tuple(-a for a in self.c))
    def __sub__(self,o):return self+(-K(o))
    def __rsub__(self,o):return K(o)-self
    def __mul__(self,o):
        o=K(o); conv=&#91;Fraction(0)&#93;*9
        for i,a in enumerate(self.c):
            for j,b in enumerate(o.c):conv&#91;i+j&#93;+=a*b
        # relation L s5 = 688...s4 -640...s3 +292...s2 -655...s +5817...
        L=287548593020928
        rel=&#91;Fraction(5817852446211,L),Fraction(-65563255857792,L),Fraction(292066554895024,L),Fraction(-640652914818432,L),Fraction(688401965085696,L)&#93;
        for d in range(8,4,-1):
            x=conv&#91;d&#93;
            if x:
                conv&#91;d&#93;=0
                for i,r in enumerate(rel):conv&#91;d-5+i&#93;+=x*r
        return K(tuple(conv&#91;:5&#93;))
    __rmul__=__mul__
    def inv(self):
        if not self:raise ZeroDivisionError
        e=sp.invert(sp.Poly(self.expr(),qr.s,domain=sp.QQ),qr.M).as_expr()
        return K.from_expr(e)
    def __truediv__(self,o):return self*K(o).inv()
    def __bool__(self):return any(self.c)
    def __eq__(self,o):return self.c==K(o).c
    def mod(self,p,s0):
        ans=0
        for i,x in enumerate(self.c):ans=(ans+(x.numerator%p)*pow(x.denominator%p,-1,p)*pow(s0,i,p))%p
        return ans
    def __repr__(self):return str(self.expr())
ZERO=K();ONE=K(1)

# parameter polynomial six vars exponents tuple
N=6
def pp_const(c):
 c=K(c);return {} if not c else {(0,)*N:c}
def pp_var(i):
 e=&#91;0&#93;*N;e&#91;i&#93;=1;return {tuple(e):ONE}
def pp_add(*aa):
 out={}
 for a in aa:
  for m,c in a.items():
   v=out.get(m,ZERO)+c
   if v:out&#91;m&#93;=v
   elif m in out:del out&#91;m&#93;
 return out
def pp_neg(a):return {m:-c for m,c in a.items()}
def pp_sub(a,b):return pp_add(a,pp_neg(b))
def pp_scale(a,c):
 c=K(c);return {m:c*v for m,v in a.items() if c*v}
def pp_mul(a,b):
 out={}
 for m,c in a.items():
  for n,d in b.items():
   k=tuple(x+y for x,y in zip(m,n));v=out.get(k,ZERO)+c*d
   if v:out&#91;k&#93;=v
   elif k in out:del out&#91;k&#93;
 return out

def zadd(*aa):
 out={}
 for a in aa:
  for k,v in a.items():
   w=pp_add(out.get(k,{}),v)
   if w:out&#91;k&#93;=w
   elif k in out:del out&#91;k&#93;
 return out
def zscale(a,c):return {k:pp_scale(v,c) for k,v in a.items() if pp_scale(v,c)}
def zder(a):return {k-1:pp_scale(v,k) for k,v in a.items() if k and pp_scale(v,k)}
def zmul(a,b):
 out={}
 for i,x in a.items():
  for j,y in b.items():
   out&#91;i+j&#93;=pp_add(out.get(i+j,{}),pp_mul(x,y))
 return {k:v for k,v in out.items() if v}

def z_from_field(d):return {k:pp_const(v) for k,v in d.items() if v}

def rref_transform(mat):
 m=len(mat);n=len(mat&#91;0&#93;);R=&#91;&#91;K(x) for x in row&#93; for row in mat&#93;;T=&#91;&#91;ONE if i==j else ZERO for j in range(m)&#93; for i in range(m)&#93;
 piv=&#91;&#93;;row=0
 for col in range(n):
  pr=next((r for r in range(row,m) if R&#91;r&#93;&#91;col&#93;),None)
  if pr is None:continue
  R&#91;row&#93;,R&#91;pr&#93;=R&#91;pr&#93;,R&#91;row&#93;;T&#91;row&#93;,T&#91;pr&#93;=T&#91;pr&#93;,T&#91;row&#93;
  inv=R&#91;row&#93;&#91;col&#93;.inv();R&#91;row&#93;=&#91;x*inv for x in R&#91;row&#93;&#93;;T&#91;row&#93;=&#91;x*inv for x in T&#91;row&#93;&#93;
  for r in range(m):
   if r!=row and R&#91;r&#93;&#91;col&#93;:
    c=R&#91;r&#93;&#91;col&#93;;R&#91;r&#93;=&#91;R&#91;r&#93;&#91;j&#93;-c*R&#91;row&#93;&#91;j&#93; for j in range(n)&#93;;T&#91;r&#93;=&#91;T&#91;r&#93;&#91;j&#93;-c*T&#91;row&#93;&#91;j&#93; for j in range(m)&#93;
  piv.append(col);row+=1
  if row==m:break
 return R,T,piv

def Dmap(r,A,B,A0,B0):
 return zadd(zscale(zmul(A,zder(B0)),2-r),zscale(zmul(zder(A),B0),-3),zscale(zmul(A0,zder(B)),2),zscale(zmul(zder(A0),B),r-3))
def linear_data(r,ae,be,A0,B0):
 cols=&#91;&#93;
 for e in ae:cols.append(Dmap(r,{e:pp_const(1)},{},A0,B0))
 for e in be:cols.append(Dmap(r,{}, {e:pp_const(1)},A0,B0))
 ds=sorted(set().union(*(x.keys() for x in cols)));degrees=list(range(min(ds),max(ds)+1))
 M=&#91;&#93;
 for d in degrees:
  row=&#91;&#93;
  for col in cols:
   pp=col.get(d,{})
   row.append(pp.get((0,)*N,ZERO))
  M.append(row)
 R,T,piv=rref_transform(M);free=&#91;j for j in range(len(M&#91;0&#93;)) if j not in piv&#93;
 ns=&#91;&#93;
 for f in free:
  v=&#91;ZERO&#93;*len(M&#91;0&#93;);v&#91;f&#93;=ONE
  for i,pc in enumerate(piv):v&#91;pc&#93;=-R&#91;i&#93;&#91;f&#93;
  ns.append(v)
 return degrees,M,R,T,piv,free,ns

def solve(data,rhs,freepps):
 degrees,M,R,T,piv,free,ns=data
 rv=&#91;rhs.get(d,{}) for d in degrees&#93;
 tr=&#91;&#93;
 for i in range(len(degrees)):
  tr.append(pp_add(*(pp_scale(rv&#91;j&#93;,T&#91;i&#93;&#91;j&#93;) for j in range(len(degrees)))))
 compat=tr&#91;len(piv):&#93;
 sol=&#91;{} for _ in range(len(M&#91;0&#93;))&#93;
 for i,pc in enumerate(piv):sol&#91;pc&#93;=tr&#91;i&#93;
 for par,v in zip(freepps,ns):
  for j,c in enumerate(v):
   if c:sol&#91;j&#93;=pp_add(sol&#91;j&#93;,pp_scale(par,c))
 return sol,compat

def vecpair(vec,ae,be):
 return ({e:vec&#91;i&#93; for i,e in enumerate(ae) if vec&#91;i&#93;},{e:vec&#91;len(ae)+j&#93; for j,e in enumerate(be) if vec&#91;len(ae)+j&#93;})


def rank_mod(rows, prime):
 if not rows:return 0
 a=&#91;&#91;x%prime for x in row&#93; for row in rows&#93;;m=len(a);n=len(a&#91;0&#93;);rank=0
 for col in range(n):
  pivot=next((r for r in range(rank,m) if a&#91;r&#93;&#91;col&#93;),None)
  if pivot is None:continue
  a&#91;rank&#93;,a&#91;pivot&#93;=a&#91;pivot&#93;,a&#91;rank&#93;
  inv=pow(a&#91;rank&#93;&#91;col&#93;,-1,prime)
  a&#91;rank&#93;=&#91;(x*inv)%prime for x in a&#91;rank&#93;&#93;
  for r in range(m):
   if r!=rank and a&#91;r&#93;&#91;col&#93;:
    c=a&#91;r&#93;&#91;col&#93;
    a&#91;r&#93;=&#91;(a&#91;r&#93;&#91;j&#93;-c*a&#91;rank&#93;&#91;j&#93;)%prime for j in range(n)&#93;
  rank+=1
  if rank==m:break
 return rank

def determinant_mod(matrix, prime):
 a=&#91;&#91;x%prime for x in row&#93; for row in matrix&#93;;n=len(a);det=1
 assert all(len(row)==n for row in a)
 for col in range(n):
  pivot=next((r for r in range(col,n) if a&#91;r&#93;&#91;col&#93;),None)
  if pivot is None:return 0
  if pivot!=col:
   a&#91;col&#93;,a&#91;pivot&#93;=a&#91;pivot&#93;,a&#91;col&#93;;det=-det
  pv=a&#91;col&#93;&#91;col&#93;%prime;det=det*pv%prime;inv=pow(pv,-1,prime)
  for r in range(col+1,n):
   c=a&#91;r&#93;&#91;col&#93;*inv%prime
   a&#91;r&#93;=&#91;(a&#91;r&#93;&#91;j&#93;-c*a&#91;col&#93;&#91;j&#93;)%prime for j in range(n)&#93;
 return det%prime

def build_certificate():
 # Exact lower face in Q(s).
 a={i:K.from_expr(v) for i,v in qr.A_RAW.items()}
 reverse_p=&#91;ONE&#93;+&#91;a&#91;i&#93; for i in range(1,8)&#93;
 cube=&#91;&#93;
 for total in range(21):
  c=ZERO
  for i in range(8):
   for j in range(8):
    for k in range(8):
     if i+j+k==total:c=c+reverse_p&#91;i&#93;*reverse_p&#91;j&#93;*reverse_p&#91;k&#93;
  cube.append(c)
 reverse_q=&#91;ONE&#93;
 for total in range(1,11):
  known=ZERO
  for i in range(1,total):known=known+reverse_q&#91;i&#93;*reverse_q&#91;total-i&#93;
  reverse_q.append((cube&#91;total&#93;-known)/K(2))
 face_constant=a&#91;7&#93;*reverse_q&#91;10&#93;;inverse_constant=face_constant.inv()
 pcoef={7:ONE};pcoef.update({7-i:a&#91;i&#93; for i in range(1,8)})
 qcoef={10:inverse_constant};qcoef.update({10-i:reverse_q&#91;i&#93;*inverse_constant for i in range(1,11)})
 A0=z_from_field({k+1:v for k,v in pcoef.items()})
 B0=z_from_field({k+2:v for k,v in qcoef.items()})

 X,Y,U,V,W,D=&#91;pp_var(i) for i in range(6)&#93;
 data1=linear_data(1,list(range(1,9)),list(range(2,13)),A0,B0)
 assert len(data1&#91;4&#93;)==17 and data1&#91;5&#93;==&#91;17,18&#93;
 sol1,compat1=solve(data1,{},&#91;X,Y&#93;);assert all(not equation for equation in compat1)
 A1,B1=vecpair(sol1,list(range(1,9)),list(range(2,13)))

 forcing2=zadd(zmul(A1,zder(B1)),zscale(zmul(zder(A1),B1),-2))
 data2=linear_data(2,list(range(0,9)),list(range(1,13)),A0,B0)
 assert len(data2&#91;4&#93;)==18 and data2&#91;5&#93;==&#91;0,19,20&#93;
 sol2,compat2=solve(data2,zscale(forcing2,-1),&#91;U,V,W&#93;)
 assert all(not equation for equation in compat2)
 A2,B2=vecpair(sol2,list(range(0,9)),list(range(1,13)))

 forcing3=zadd(zmul(A1,zder(B2)),zscale(zmul(zder(A1),B2),-1),zscale(zmul(zder(A2),B1),-2))
 data3=linear_data(3,&#91;&#93;,list(range(0,13)),A0,B0)
 assert len(data3&#91;4&#93;)==12 and data3&#91;5&#93;==&#91;0&#93;
 sol3,compat3=solve(data3,zscale(forcing3,-1),&#91;D&#93;)
 _,B3=vecpair(sol3,&#91;&#93;,list(range(0,13)))
 assert len(compat3)==7

 E4=zadd(zmul(A1,zder(B3)),zscale(zmul(zder(A2),B2),-1))
 assert sorted(E4)==list(range(2,20)) and len(E4)==18

 # U,D are free origin-vertex coefficients. Compatibility uses only X,Y,V,W.
 for equation in compat3+list(E4.values()):
  assert all(m&#91;2&#93;==0 and m&#91;5&#93;==0 for m in equation)
  weights={sum((m&#91;0&#93;,m&#91;1&#93;,m&#91;3&#93;*2,m&#91;4&#93;*2)) for m in equation}
  assert len(weights)==1 and next(iter(weights)) in (3,4)

 m4=&#91;
  (4,0,0,0,0,0),(3,1,0,0,0,0),(2,2,0,0,0,0),(1,3,0,0,0,0),(0,4,0,0,0,0),
  (2,0,0,1,0,0),(1,1,0,1,0,0),(0,2,0,1,0,0),
  (2,0,0,0,1,0),(1,1,0,0,1,0),(0,2,0,0,1,0),
  (0,0,0,2,0,0),(0,0,0,1,1,0),(0,0,0,0,2,0),
 &#93;
 equations=&#91;&#93;;labels=&#91;&#93;
 for i,equation in enumerate(compat3):
  equations.extend(&#91;pp_mul(X,equation),pp_mul(Y,equation)&#93;)
  labels.extend(&#91;f'X*layer3&#91;{i}&#93;',f'Y*layer3&#91;{i}&#93;'&#93;)
 for degree in sorted(E4):
  equations.append(E4&#91;degree&#93;);labels.append(f'layer4&#91;z^{degree}&#93;')
 kmatrix=&#91;&#91;equation.get(m,ZERO) for m in m4&#93; for equation in equations&#93;

 prime=2053;u_value=216
 num,den=sp.fraction(sp.cancel(qr.S_IN_K0.subs(qr.u,u_value)))
 s_value=int(num)%prime*pow(int(den)%prime,-1,prime)%prime
 assert int(qr.K0_EXPR.subs(qr.u,u_value))%prime==0
 assert int(sp.diff(qr.K0_EXPR,qr.u).subs(qr.u,u_value))%prime!=0
 assert int(qr.M_EXPR.subs(qr.s,s_value))%prime==0
 matrix=&#91;&#91;coefficient.mod(prime,s_value) for coefficient in row&#93; for row in kmatrix&#93;
 selected=&#91;&#93;
 for i,row in enumerate(matrix):
  if rank_mod(&#91;matrix&#91;j&#93; for j in selected&#93;+&#91;row&#93;,prime)&gt;len(selected):selected.append(i)
  if len(selected)==14:break
 assert len(selected)==14
 determinant=determinant_mod(&#91;matrix&#91;i&#93; for i in selected&#93;,prime)
 assert determinant

 # Exact top vertices are in the radical (X,Y,V,W).
 for top in (A2&#91;8&#93;,B3&#91;12&#93;):
  assert top and (0,0,0,0,0,0) not in top
  assert all(m&#91;2&#93;==0 and m&#91;5&#93;==0 for m in top)

 return {
  'schema_version':1,
  'field':{
   'reconstructed':sp.sstr(qr.M_EXPR),
   'public_model':sp.sstr(qr.K0_EXPR),
  },
  'linear_layers':{
   'D1':{'shape':&#91;18,19&#93;,'rank':17,'free_columns':&#91;17,18&#93;},
   'D2':{'shape':&#91;19,21&#93;,'rank':18,'free_columns':&#91;0,19,20&#93;,'compatibility_zero':True},
   'D3':{'shape':&#91;19,13&#93;,'rank':12,'free_columns':&#91;0&#93;,'compatibility_count':7},
   'layer4_equation_count':18,
  },
  'effective_parameters':{'names':&#91;'X','Y','V','W'&#93;,'weights':&#91;1,1,2,2&#93;,
                          'free_origin_vertices':&#91;'U','D'&#93;},
  'degree_four_span':{
   'basis_dimension':14,'equation_rows':32,'rank':14,
   'good_reduction':{'prime':prime,'u':u_value,'s':s_value,
                     'selected_row_indices':selected,
                     'selected_row_labels':&#91;labels&#91;i&#93; for i in selected&#93;,
                     'minor_determinant':determinant},
  },
  'conclusion':{
   'P_top_vertex':'A2 coefficient of z^8, exponent (8,16)',
   'Q_top_vertex':'B3 coefficient of z^12, exponent (12,24)',
   'both_vanish_on_geometric_zero_set':True,
   'vertex_saturated_truncated_locus_empty':True,
  },
 }

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--output',type=Path)
 args=parser.parse_args()
 result=build_certificate()
 if args.output:
  args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
 witness=result&#91;'degree_four_span'&#93;&#91;'good_reduction'&#93;
 print('exact layer ranks: D1=17, D2=18, D3=12')
 print('compatibility equations: 7 at weight 3 and 18 at weight 4')
 print('effective parameter weights: X,Y,V,W = 1,1,2,2')
 print(f"weighted-degree-four span: rank 14/14; determinant {witness&#91;'minor_determinant'&#93;} mod 2053")
 print('required top P and Q vertex coefficients vanish on every solution')
 if args.output:print(f'certificate export: {args.output.name}')
 print('PASS: the vertex-saturated truncated Newton root is empty')

if __name__=='__main__':main()
</code></pre>

<a id="source-38ab8bd19d25aff4"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 8/9 mathematical recovery

This packet records an independent replay and scope audit of two distinct
pieces of the degree-`125` boundary program. It does not update a canonical
graph, research handoff, release selector, or public site.

## Classification

| result | primary lane | connection |
|---|---|---|
| direct closure of the two normalized `(8,28)` roots | Lane 8 | supplies the terminal Newton-root calculation used in the relative below-`125` assembly |
| `F_2` support windows and normal recurrence | Lane 9 | starts from the degree-`125` Lane 8 boundary seed, but is a chart/recurrence and descent problem |

The second item should therefore be described as **Lane 9 primary, with a
Lane 8 connection**. It is not another proof path for the Lane 8 full root.

## Lane 8 direct closure

The tracked full-root packet was replayed from the raw Newton polygons, the
exact quintic face relations, and the Jacobian coefficient formula. It did
not consume archived layer matrices or obstruction equations.

- The truncated root again has Macaulay rank `14` on the complete set of
  fourteen weight-four monomials. Its selected minor has SHA-256
  `8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059`.
- The full root again produces a layer-four square, closes the
  `t1_1=0` complement using the two top vertices, and normalizes the open
  child to fifteen equations. Their canonical SHA-256 is
  `d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883`.
- Zero-based equations `4,6,8,9,10,11` are literally a relaxation of those
  fifteen. The selected-six digest is
  `e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a`.
  Their emptiness remains an imported exact Program 6 toric theorem.
- The stored adjacent-chart terminal remains empty but unattached and is not
  used in either closure path.

The resulting below-`125` statement has exactly the following scope: it is a
proof assembly relative to the inspected GGHV Newton reduction, its exclusion
of the `(9,27)` case, its routing of `(8,28)` to the two normalized roots, the
imported face orbit, and the imported compact toric terminal. It is not an
independent reproof of those inputs and carries no priority claim.

## Exact `F_2` support windows

After the denominator-five shear, write a monomial as `x^(a/5)y^J`, put
`w=a-J`, and use the terminal direction `(25,-17)`. The exact maximal
Newton-bounded supports are

\&#91;
S_P=\{(a,J):-60\le w\le15,\ 0\le J\le60-\langle w\rangle_5,
\ 5a-17J\le3\},
\&#93;

\&#91;
S_Q=\{(a,J):-100\le w\le25,\ 0\le J\le100-\langle w\rangle_5,
\ 5a-17J\le5\}.
\&#93;

In the terminal chart `x=t^-25`, `y=t^17 z`, `u=z^5`, write

\&#91;
P=t^{-3}\sum_r t^rA_r(z),\qquad
Q=t^{-5}\sum_r t^rB_r(z).
\&#93;

The `C_5` characters are

\&#91;
A_r=z^{(1-2r)\bmod5}\bar A_r(u),\qquad
B_r=z^{-2r\bmod5}\bar B_r(u).
\&#93;

For either coordinate, the exact `u` interval is obtained by intersecting the
raw `J` bounds with the required residue class and then applying the single
top sawtooth correction `J_top &lt;= Y-&lt;w_top&gt;_5`. The verifier checks this
closed formula at every order, not only selected rows.

The regenerated inventory is:

| object | exact count |
|---|---:|
| propagated `P` coefficients | 4,433 |
| nonempty `P` layers | 981 |
| propagated `Q` coefficients | 12,340 |
| nonempty `Q` layers | 1,663 |
| determinant-output layers | 2,681 |

The first target coordinate outside the linearized image is the constant
coefficient at order `510`.

## Orders 510, 520, and 530

The retained exact rational generator fixes the order-10 coordinate, uses an
order-260 kernel coordinate to cancel `omega510`, chooses an order-270
direction in the kernel of that functional, and uses its scalar to cancel
`omega520`. The independent determinant verifier checks all layers `0..520`
and all serialized support bounds. Both values are exactly zero.

The old nonzero `omega530` value is obtained only after every unselected RREF
kernel coordinate is assigned zero. The retained multiple-of-10 slice has
`212` free slots across its `52` positive layers through order `520`, while
the generator explicitly selects only the order-10, order-260, and constrained
order-270 values.

The new exact probe reopens the five order-280 RREF coordinates:

- the kernel of `omega510` on that space has dimension `4`;
- the joint kernel of `omega510` and `omega520` has dimension `3`;
- `omega530` is nonzero as a functional on that joint kernel; and
- one displayed exact rational direction cancels `omega530` and verifies the
  determinant identity through order `530`.

Thus the old order-530 value is decisively a **zero-new-coordinate slice** and
not an obstruction. The new order-530 certificate is still a slice: it reopens
only order `280` and sets all other omitted coordinates to zero.

## Why no parameter-complete Slurm run was submitted

A parameter-complete continuation of the actual `F_2` complete-chain chart is
not runnable from the retained inputs. The public support model is explicitly
the maximal Newton-bounded independent-coefficient enlargement and omits the
inherited cross-layer relations needed to identify the actual chart. The
retained rational generator does not construct the full symbolic family of
all RREF coordinates, and the adjacent-chart/global descent data remain
unattached.

Submitting the rational slice as a “parameter-complete” cluster job would
overstate both the input model and the calculation. No Slurm job was submitted.
The exact order-530 slice replay is small enough to run locally and
is retained at the immutable versioned path recorded in `evidence.json`.

## Verification

Metadata-only validation is portable:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py \
  --metadata-only
```

On the internal workspace, the full checker verifies both immutable run
paths, every ZIP member digest, every support-window formula, both determinant
certificates, and optionally regenerates the support and linear-rank JSON:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py \
  --regenerate
```

The fresh-parameter order-530 result can be reproduced only at a new,
nonexisting output path:

```bash
uv run python \
  research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py \
  --bundle /path/to/06-f2-support-windows-order-520-2026-08-03-v1.zip \
  --output-dir /path/to/new-versioned-run
```
</code></pre>

<a id="source-ab81932dfb3d4762"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/evidence.json`

<pre><code class="language-json">
{
  "base_commit": "25fd4547397cca49fbff3293e381359930cbdbf0",
  "classification": {
    "f2_recurrence": "lane9_primary_lane8_connection",
    "full_root_closure": "lane8"
  },
  "f2": {
    "P_coefficients": 4433,
    "P_nonempty_layers": 981,
    "Q_coefficients": 12340,
    "Q_nonempty_layers": 1663,
    "determinant_output_layers": 2681,
    "first_external_forcing_window": 510,
    "linear_complex_replay_path": "/path/to/versioned-artifact",
    "order520_certificate_sha256": "8a410747ab17dfaff51756138c795c2667ab3f922318f5aa0e8cc5cd54e810d5",
    "order520_replay_path": "/path/to/versioned-artifact",
    "public_bundle_path": "/path/to/versioned-artifact",
    "public_bundle_sha256": "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64",
    "support_windows_sha256": "81b7750a8510c00250b508a3b919e62be860e051f72059183ef45ad416d0720f",
    "total_rref_free_slots_in_retained_multiple_of_10_slice_through_520": 212,
    "zero_slice_omega530_mod_1000003": 856714
  },
  "lane8": {
    "full_fifteen_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883",
    "replay_summary_path": "/path/to/versioned-artifact",
    "source_packet": "research-notes/lane8-full-root-closure-20260803-v1",
    "summary_sha256": "8ad4054e2efb8f8a682e67ad6fbe15feccb1eae0bf3181750e6a3fff7d708907",
    "terminal_projection_sha256": "e4bf0e1842fcd0d3d7c403e6a5ec17fb800914f3208887f0b05d8727b563bb6a",
    "truncated_minor_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059"
  },
  "order530": {
    "fresh_parameter_certificate_path": "/path/to/versioned-artifact",
    "certificate_sha256": "c3dc5244862956c4c834d09af43abd0d294d17966e6fa5efb65e4c850a95ddbb",
    "fresh_parameter_scope": {
      "joint_omega510_omega520_kernel_dimension": 3,
      "omega510_kernel_dimension": 4,
      "reopened_order": 280,
      "reopened_rref_coordinates": 5,
      "verified_through": 530
    },
    "parameter_complete_assessment": {
      "reasons": &#91;
        "the maximal support model omits inherited cross-layer descent relations",
        "the retained rational generator assigns unselected RREF kernel coordinates to zero",
        "the adjacent-chart and global descent inputs remain unattached"
      &#93;,
      "runnable": false,
      "slurm_job_submitted": false
    }
  },
  "schema": "lane89-mathematical-recovery-evidence-v1"
}
</code></pre>

<a id="source-151645a0e17f5aa6"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/run_f2_omega530_fresh_parameter.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Extend the retained F2 weighted slice through order 530 exactly.

This is deliberately not a parameter-complete complete-chain calculation.
It reopens only the five RREF-kernel coordinates at order 280, finds the
joint kernel of the order-510 and order-520 functionals, and uses one exact
rational direction in that joint kernel to cancel order 530.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
from types import ModuleType
from zipfile import ZipFile


EXPECTED_BUNDLE_SHA256 = (
    "a0017d6537021b80098b78349cd7ad5566f6606d053b7e8f3f1dbd634d14ca64"
)
GENERATOR_MEMBER = "f2_omega520_kuranishi.py"
WINDOW_MEMBER = "f2_support_windows.json"


def sha256_path(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_generator(bundle: Path, destination: Path) -&gt; tuple&#91;ModuleType, Path&#93;:
    if sha256_path(bundle) != EXPECTED_BUNDLE_SHA256:
        raise ValueError("unexpected F2 public-bundle SHA-256")
    with ZipFile(bundle) as archive:
        names = set(archive.namelist())
        for member in (GENERATOR_MEMBER, WINDOW_MEMBER):
            if member not in names:
                raise ValueError(f"bundle lacks {member}")
        archive.extract(GENERATOR_MEMBER, destination)
        archive.extract(WINDOW_MEMBER, destination)
    generator_path = destination / GENERATOR_MEMBER
    spec = importlib.util.spec_from_file_location("f2_o520_recovered", generator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load recovered order-520 generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, generator_path


def selected_order520_assignments(module: ModuleType) -&gt; tuple&#91;dict, dict&#93;:
    eta = F(1)
    seed = {10: {0: eta}}
    omega510_base = module.omega(510, seed)
    omega510_mu_slope = (
        module.omega(510, {10: {0: eta}, 260: {0: F(1)}})
        - omega510_base
    )
    if not omega510_mu_slope:
        raise AssertionError("order-260 direction does not move omega510")
    mu = -omega510_base / omega510_mu_slope

    nu0_slope = (
        module.omega(510, {10: {0: eta}, 270: {0: F(1)}})
        - omega510_base
    )
    nu1_slope = (
        module.omega(510, {10: {0: eta}, 270: {1: F(1)}})
        - omega510_base
    )
    if not nu1_slope:
        raise AssertionError("second order-270 direction does not move omega510")
    ratio = -nu0_slope / nu1_slope

    def assignments(value: F) -&gt; dict:
        return {
            10: {0: eta},
            260: {0: mu},
            270: {0: value, 1: value * ratio},
        }

    omega520_at_zero = module.omega(520, assignments(F(0)))
    omega520_slope = module.omega(520, assignments(F(1))) - omega520_at_zero
    if not omega520_slope:
        raise AssertionError("order-270 null direction does not move omega520")
    value = -omega520_at_zero / omega520_slope
    selected = assignments(value)
    if module.omega(510, selected) or module.omega(520, selected):
        raise AssertionError("failed to reconstruct the retained order-520 slice")
    audit = {
        "eta": str(eta),
        "mu": str(mu),
        "order270_direction_ratio": str(ratio),
        "lambda": str(value),
    }
    return selected, audit


def combine(vectors: list&#91;list&#91;F&#93;&#93;, coefficients: list&#91;F&#93;) -&gt; list&#91;F&#93;:
    return &#91;
        sum(
            (
                coefficient * vector&#91;index&#93;
                for vector, coefficient in zip(vectors, coefficients)
            ),
            F(0),
        )
        for index in range(len(vectors&#91;0&#93;))
    &#93;


def one_row_kernel(vectors: list&#91;list&#91;F&#93;&#93;, values: list&#91;F&#93;) -&gt; list&#91;list&#91;F&#93;&#93;:
    """Return an exact basis for the kernel of one functional on a basis."""
    pivot = next((index for index, value in enumerate(values) if value), None)
    if pivot is None:
        return vectors
    output: list&#91;list&#91;F&#93;&#93; = &#91;&#93;
    for index in range(len(vectors)):
        if index == pivot:
            continue
        coefficients = &#91;F(0)&#93; * len(vectors)
        coefficients&#91;index&#93; = F(1)
        coefficients&#91;pivot&#93; = -values&#91;index&#93; / values&#91;pivot&#93;
        output.append(combine(vectors, coefficients))
    return output


def with_order280_direction(
    base: dict,
    vector: list&#91;F&#93;,
    scalar: F = F(1),
) -&gt; dict:
    output = {order: dict(values) for order, values in base.items()}
    output&#91;280&#93; = {
        index: scalar * coefficient
        for index, coefficient in enumerate(vector)
        if coefficient
    }
    return output


def fraction_list(values: list&#91;F&#93;) -&gt; list&#91;str&#93;:
    return &#91;str(value) for value in values&#93;


def make_certificate(module: ModuleType) -&gt; dict:
    base, retained_parameters = selected_order520_assignments(module)
    _, _, partial_records = module.solve(base, 280)
    free_dimension = partial_records&#91;-1&#93;&#91;"free_dim"&#93;
    if partial_records&#91;-1&#93;&#91;"r"&#93; != 280 or free_dimension != 5:
        raise AssertionError("unexpected order-280 RREF kernel")

    standard = &#91;
        &#91;F(index == column) for index in range(free_dimension)&#93;
        for column in range(free_dimension)
    &#93;
    omega510_values = &#91;
        module.omega(510, with_order280_direction(base, vector))
        for vector in standard
    &#93;
    kernel510 = one_row_kernel(standard, omega510_values)
    for vector in kernel510:
        if module.omega(510, with_order280_direction(base, vector)):
            raise AssertionError("computed order-510 kernel direction failed")

    omega520_values = &#91;
        module.omega(520, with_order280_direction(base, vector))
        for vector in kernel510
    &#93;
    joint_kernel = one_row_kernel(kernel510, omega520_values)
    for vector in joint_kernel:
        trial = with_order280_direction(base, vector)
        if module.omega(510, trial) or module.omega(520, trial):
            raise AssertionError("computed joint-kernel direction failed")

    zero_slice_omega530 = module.omega(530, base)
    if not zero_slice_omega530:
        raise AssertionError("retained zero-new-coordinate omega530 unexpectedly vanished")
    omega530_values = &#91;
        module.omega(530, with_order280_direction(base, vector))
        - zero_slice_omega530
        for vector in joint_kernel
    &#93;
    pivot = next(
        (index for index, value in enumerate(omega530_values) if value),
        None,
    )
    if pivot is None:
        raise AssertionError("omega530 vanishes on the entire computed joint kernel")
    direction = joint_kernel&#91;pivot&#93;
    scalar = -zero_slice_omega530 / omega530_values&#91;pivot&#93;
    final_assignments = with_order280_direction(base, direction, scalar)
    for order in (510, 520, 530):
        if module.omega(order, final_assignments):
            raise AssertionError(f"omega{order} did not cancel")

    a_layers, b_layers, records = module.solve(final_assignments, 530)
    if module.full_layer(0, a_layers, b_layers) != {0: F(-1)}:
        raise AssertionError("leading determinant layer changed")
    for order in range(1, 531):
        if module.full_layer(order, a_layers, b_layers):
            raise AssertionError(f"nonzero determinant layer {order}")

    return {
        "schema": "f2-omega530-fresh-order280-certificate-v1",
        "model": (
            "F2 maximal Newton-bounded independent-coefficient recursion; "
            "C5-invariant weighted slice"
        ),
        "claim": "exact rational weighted-slice jet through order 530",
        "boundary": (
            "Only the five order-280 RREF-kernel coordinates are reopened. "
            "This is not the all-parameter complete-chain recurrence and does "
            "not restore the omitted inherited descent relations."
        ),
        "base": {
            "A0": {str(exponent): str(value) for exponent, value in module.A0.items()},
            "B0": {str(exponent): str(value) for exponent, value in module.B0.items()},
        },
        "retained_order520_parameters": retained_parameters,
        "fresh_parameter_analysis": {
            "order": 280,
            "free_dimension": free_dimension,
            "omega510_values_on_rref_basis": fraction_list(omega510_values),
            "omega510_kernel_dimension": len(kernel510),
            "omega520_values_on_omega510_kernel": fraction_list(omega520_values),
            "joint_omega510_omega520_kernel_dimension": len(joint_kernel),
            "omega530_values_on_joint_kernel": fraction_list(omega530_values),
            "zero_new_coordinate_omega530": str(zero_slice_omega530),
            "cancelling_joint_kernel_index": pivot,
            "cancelling_direction": fraction_list(direction),
            "cancelling_scalar": str(scalar),
            "final_order280_rref_coordinates": {
                str(index): str(value)
                for index, value in sorted(final_assignments&#91;280&#93;.items())
            },
        },
        "verified": {
            "determinant_layers": "0..530",
            "omega510": "0",
            "omega520": "0",
            "omega530": "0",
            "recorded_positive_layers": len(records),
        },
        "layers": records,
    }


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    bundle = args.bundle.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite {output}")
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="f2-omega530-generator-") as temporary:
        module, _ = load_generator(bundle, Path(temporary))
        certificate = make_certificate(module)

    output.mkdir()
    script_copy = output / Path(__file__).name
    bundle_copy = output / bundle.name
    certificate_path = output / "f2_omega530_fresh_parameter_certificate.json"
    shutil.copyfile(Path(__file__), script_copy)
    shutil.copyfile(bundle, bundle_copy)
    certificate_path.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    files = (script_copy, bundle_copy, certificate_path)
    (output / "SHA256SUMS").write_text(
        "".join(f"{sha256_path(path)}  {path.name}\n" for path in files),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "certificate": str(certificate_path),
                "certificate_sha256": sha256_path(certificate_path),
                "omega510": "0",
                "omega520": "0",
                "omega530": "0",
                "joint_kernel_dimension": certificate&#91;
                    "fresh_parameter_analysis"
                &#93;&#91;"joint_omega510_omega520_kernel_dimension"&#93;,
                "scope": "order-280 fresh-parameter slice, not parameter-complete",
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-de9fde3d3aea4139"></a>

## `research-notes/lane89-mathematical-recovery-20260803-v1/verify_lane89_recovery.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Fail-closed verifier for the Lane 8/9 mathematical recovery packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from typing import Any
from zipfile import ZipFile


PACKET = Path(__file__).resolve().parent
REPOSITORY_ROOT = PACKET.parents&#91;1&#93;
EVIDENCE_PATH = PACKET / "evidence.json"


def require(condition: bool, message: str) -&gt; None:
    if not condition:
        raise AssertionError(message)


def sha256_path(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_evidence() -&gt; dict&#91;str, Any&#93;:
    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))
    require(
        evidence&#91;"schema"&#93; == "lane89-mathematical-recovery-evidence-v1",
        "unexpected evidence schema",
    )
    require(evidence&#91;"base_commit"&#93;.startswith("25fd454"), "wrong private base")
    classification = evidence&#91;"classification"&#93;
    require(
        classification == {
            "full_root_closure": "lane8",
            "f2_recurrence": "lane9_primary_lane8_connection",
        },
        "lane classification changed",
    )
    assessment = evidence&#91;"order530"&#93;&#91;"parameter_complete_assessment"&#93;
    require(assessment&#91;"runnable"&#93; is False, "parameter-complete scope overstated")
    require(assessment&#91;"slurm_job_submitted"&#93; is False, "unexpected Slurm claim")
    require(
        assessment&#91;"reasons"&#93;
        == &#91;
            "the maximal support model omits inherited cross-layer descent relations",
            "the retained rational generator assigns unselected RREF kernel coordinates to zero",
            "the adjacent-chart and global descent inputs remain unattached",
        &#93;,
        "parameter-complete boundary changed",
    )
    return evidence


def verify_lane8_summary(path: Path, expected: dict&#91;str, Any&#93;) -&gt; None:
    require(sha256_path(path) == expected&#91;"summary_sha256"&#93;, "Lane 8 summary SHA-256")
    summary = json.loads(path.read_text(encoding="utf-8"))
    require(summary&#91;"schema"&#93; == "lane8-independent-raw-support-replay-v1", "Lane 8 schema")
    require(summary&#91;"inputs"&#93;&#91;"archived_layers_used"&#93; is False, "Lane 8 used archived layers")
    require(summary&#91;"inputs"&#93;&#91;"archived_equations_used"&#93; is False, "Lane 8 used archived equations")
    require(summary&#91;"truncated"&#93;&#91;"macaulay_rank"&#93; == 14, "truncated rank")
    require(
        summary&#91;"truncated"&#93;&#91;"minor_determinant_sha256"&#93;
        == expected&#91;"truncated_minor_sha256"&#93;,
        "truncated minor digest",
    )
    require(summary&#91;"full"&#93;&#91;"weight_four_is_square"&#93; is True, "full layer-four square")
    require(
        summary&#91;"full"&#93;&#91;"vertex_saturation_forces_t11_nonzero"&#93; is True,
        "full closed complement",
    )
    require(len(summary&#91;"full"&#93;&#91;"equation_manifest"&#93;) == 15, "full equation count")
    require(
        summary&#91;"full"&#93;&#91;"final_equation_sha256"&#93;
        == expected&#91;"full_fifteen_sha256"&#93;,
        "full fifteen digest",
    )
    require(
        summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"zero_based_indices"&#93;
        == &#91;4, 6, 8, 9, 10, 11&#93;,
        "toric projection indices",
    )
    require(
        summary&#91;"full"&#93;&#91;"terminal_projection"&#93;&#91;"sha256"&#93;
        == expected&#91;"terminal_projection_sha256"&#93;,
        "terminal projection digest",
    )
    require(
        summary&#91;"full"&#93;&#91;"higher_deficiency_coefficients_projected_away"&#93;
        == {
            "cutoff": 8,
            "P": 3,
            "Q": 28,
            "extra_vertices": {"P_(0,8)": 10, "Q_(0,12)": 15},
        },
        "higher-deficiency projection boundary",
    )


def safe_archive_members(archive: ZipFile) -&gt; dict&#91;str, bytes&#93;:
    members: dict&#91;str, bytes&#93; = {}
    for info in archive.infolist():
        path = PurePosixPath(info.filename)
        require(not path.is_absolute() and ".." not in path.parts, "unsafe ZIP member")
        require(not info.is_dir(), f"unexpected directory member {info.filename}")
        members&#91;info.filename&#93; = archive.read(info)
    return members


def verify_file_manifest(members: dict&#91;str, bytes&#93;) -&gt; None:
    manifest = json.loads(members&#91;"FILE_MANIFEST.json"&#93;)
    expected_names = {row&#91;"path"&#93; for row in manifest&#91;"files"&#93;}
    require(expected_names == set(members) - {"FILE_MANIFEST.json"}, "bundle inventory")
    for row in manifest&#91;"files"&#93;:
        payload = members&#91;row&#91;"path"&#93;&#93;
        require(len(payload) == row&#91;"bytes"&#93;, f"bundle size {row&#91;'path'&#93;}")
        require(
            hashlib.sha256(payload).hexdigest() == row&#91;"sha256"&#93;,
            f"bundle digest {row&#91;'path'&#93;}",
        )


def expected_window(data: dict&#91;str, Any&#93;, order: int) -&gt; dict&#91;str, int&#93; | None:
    metadata = data&#91;"metadata"&#93;
    lower = max(
        0,
        -(
            -(
                order
                + 5 * metadata&#91;"initial_weight_min"&#93;
                - metadata&#91;"terminal_weight_max"&#93;
            )
            // 12
        ),
    )
    upper = min(
        metadata&#91;"y_max"&#93;,
        (
            order
            + 5 * metadata&#91;"initial_weight_max"&#93;
            - metadata&#91;"terminal_weight_max"&#93;
        )
        // 12,
    )
    residue = (3 * (order - metadata&#91;"terminal_weight_max"&#93;)) % 5
    u_min = -(-(lower - residue) // 5)
    u_max = (upper - residue) // 5
    if u_min &gt; u_max:
        return None
    top = residue + 5 * u_max
    numerator = metadata&#91;"terminal_weight_max"&#93; + 12 * top - order
    require(numerator % 5 == 0, "window character congruence")
    initial_weight = numerator // 5
    if top &gt; metadata&#91;"y_max"&#93; - initial_weight % 5:
        u_max -= 1
    if u_min &gt; u_max:
        return None
    return {
        "J_min": residue + 5 * u_min,
        "J_max": residue + 5 * u_max,
        "dimension": u_max - u_min + 1,
    }


def verify_all_support_windows(windows: dict&#91;str, Any&#93;, expected: dict&#91;str, Any&#93;) -&gt; None:
    for label in ("P", "Q"):
        support = windows&#91;"support"&#93;&#91;label&#93;
        rows = {int(order): row for order, row in windows&#91;f"{label}_windows"&#93;.items()}
        require(
            support&#91;"propagated_support_size"&#93; == expected&#91;f"{label}_coefficients"&#93;,
            f"{label} support size",
        )
        require(
            len(rows) == expected&#91;f"{label}_nonempty_layers"&#93;,
            f"{label} layer count",
        )
        require(
            sum(row&#91;"dimension"&#93; for row in rows.values())
            == expected&#91;f"{label}_coefficients"&#93;,
            f"{label} coefficient total",
        )
        last_order = support&#91;"summary"&#93;&#91;"last_layer"&#93;
        for order in range(last_order + 1):
            formula = expected_window(support, order)
            serialized = rows.get(order)
            require((formula is None) == (serialized is None), f"{label} window presence {order}")
            if formula is not None and serialized is not None:
                require(
                    {
                        "J_min": serialized&#91;"J_min"&#93;,
                        "J_max": serialized&#91;"J_max"&#93;,
                        "dimension": serialized&#91;"dimension"&#93;,
                    }
                    == formula,
                    f"{label} window formula {order}",
                )
    require(
        len(windows&#91;"full_jacobian_output_windows"&#93;)
        == expected&#91;"determinant_output_layers"&#93;,
        "determinant output layer count",
    )


def parse_poly(data: dict&#91;str, str&#93;) -&gt; dict&#91;int, F&#93;:
    return {int(exponent): F(value) for exponent, value in data.items()}


def derivative(poly: dict&#91;int, F&#93;) -&gt; dict&#91;int, F&#93;:
    return {
        exponent - 1: F(exponent) * value
        for exponent, value in poly.items()
        if exponent and value
    }


def add_product(
    output: dict&#91;int, F&#93;,
    left: dict&#91;int, F&#93;,
    right: dict&#91;int, F&#93;,
    scale: F,
) -&gt; None:
    for left_exponent, left_value in left.items():
        for right_exponent, right_value in right.items():
            exponent = left_exponent + right_exponent
            output&#91;exponent&#93; = (
                output.get(exponent, F(0))
                + scale * left_value * right_value
            )


def determinant_layer(
    order: int,
    a_layers: dict&#91;int, dict&#91;int, F&#93;&#93;,
    b_layers: dict&#91;int, dict&#91;int, F&#93;&#93;,
) -&gt; dict&#91;int, F&#93;:
    output: dict&#91;int, F&#93; = {}
    for left_order in range(order + 1):
        right_order = order - left_order
        a_layer = a_layers.get(left_order, {})
        b_layer = b_layers.get(right_order, {})
        if not a_layer or not b_layer:
            continue
        add_product(output, a_layer, derivative(b_layer), F(3 - left_order))
        add_product(output, derivative(a_layer), b_layer, F(right_order - 5))
    return {exponent: value for exponent, value in output.items() if value}


def allowed_exponents(window: dict&#91;str, Any&#93;) -&gt; set&#91;int&#93;:
    return set(range(window&#91;"J_min"&#93;, window&#91;"J_max"&#93; + 1, 5))


def verify_jet_layers(
    certificate: dict&#91;str, Any&#93;,
    windows: dict&#91;str, Any&#93;,
    through: int,
) -&gt; None:
    p_windows = {int(order): row for order, row in windows&#91;"P_windows"&#93;.items()}
    q_windows = {int(order): row for order, row in windows&#91;"Q_windows"&#93;.items()}
    a_layers = {0: parse_poly(certificate&#91;"base"&#93;&#91;"A0"&#93;)}
    b_layers = {0: parse_poly(certificate&#91;"base"&#93;&#91;"B0"&#93;)}
    seen: set&#91;int&#93; = set()
    for record in certificate&#91;"layers"&#93;:
        order = int(record&#91;"r"&#93;)
        require(order not in seen, f"duplicate jet layer {order}")
        seen.add(order)
        a_layers&#91;order&#93; = parse_poly(record&#91;"A"&#93;)
        b_layers&#91;order&#93; = parse_poly(record&#91;"B"&#93;)
        require(
            set(a_layers&#91;order&#93;).issubset(allowed_exponents(p_windows&#91;order&#93;)),
            f"P support at order {order}",
        )
        require(
            set(b_layers&#91;order&#93;).issubset(allowed_exponents(q_windows&#91;order&#93;)),
            f"Q support at order {order}",
        )
    require(determinant_layer(0, a_layers, b_layers) == {0: F(-1)}, "leading layer")
    for order in range(1, through + 1):
        require(
            determinant_layer(order, a_layers, b_layers) == {},
            f"nonzero determinant layer {order}",
        )


def verify_order520(
    members: dict&#91;str, bytes&#93;,
    windows: dict&#91;str, Any&#93;,
    expected: dict&#91;str, Any&#93;,
) -&gt; None:
    support_payload = members&#91;"f2_support_windows.json"&#93;
    require(
        support_payload == members&#91;"data/f2_support_windows.json"&#93;,
        "two support-window payloads differ",
    )
    require(
        hashlib.sha256(support_payload).hexdigest()
        == expected&#91;"support_windows_sha256"&#93;,
        "support-window digest",
    )
    certificate_payload = members&#91;"f2_omega520_exact_certificate.json"&#93;
    require(
        hashlib.sha256(certificate_payload).hexdigest()
        == expected&#91;"order520_certificate_sha256"&#93;,
        "order-520 certificate digest",
    )
    certificate = json.loads(certificate_payload)
    require(
        sum(record&#91;"free_dim"&#93; for record in certificate&#91;"layers"&#93;)
        == expected&#91;
            "total_rref_free_slots_in_retained_multiple_of_10_slice_through_520"
        &#93;,
        "retained-slice free-coordinate inventory",
    )
    require(certificate&#91;"kuranishi_data"&#93;&#91;"verified_omega510"&#93; == "0", "omega510")
    require(certificate&#91;"kuranishi_data"&#93;&#91;"verified_omega520"&#93; == "0", "omega520")
    require(
        F(certificate&#91;"kuranishi_data"&#93;&#91;"next_zero-slice_constant_omega530"&#93;),
        "zero-new-coordinate omega530 unexpectedly zero",
    )
    require(
        certificate&#91;"mod_1000003_checks"&#93;&#91;"omega530"&#93;
        == expected&#91;"zero_slice_omega530_mod_1000003"&#93;,
        "omega530 modular check",
    )
    verify_jet_layers(certificate, windows, 520)


def verify_order530(
    path: Path,
    windows: dict&#91;str, Any&#93;,
    expected: dict&#91;str, Any&#93;,
) -&gt; None:
    require(sha256_path(path) == expected&#91;"certificate_sha256"&#93;, "order-530 certificate digest")
    certificate = json.loads(path.read_text(encoding="utf-8"))
    require(
        certificate&#91;"schema"&#93; == "f2-omega530-fresh-order280-certificate-v1",
        "order-530 schema",
    )
    analysis = certificate&#91;"fresh_parameter_analysis"&#93;
    require(analysis&#91;"free_dimension"&#93; == 5, "order-280 free dimension")
    require(analysis&#91;"omega510_kernel_dimension"&#93; == 4, "omega510 kernel dimension")
    require(
        analysis&#91;"joint_omega510_omega520_kernel_dimension"&#93; == 3,
        "joint kernel dimension",
    )
    require(F(analysis&#91;"zero_new_coordinate_omega530"&#93;), "zero slice vanished")
    require(
        any(F(value) for value in analysis&#91;"omega530_values_on_joint_kernel"&#93;),
        "omega530 did not move on the joint kernel",
    )
    require(
        certificate&#91;"verified"&#93;
        == {
            "determinant_layers": "0..530",
            "omega510": "0",
            "omega520": "0",
            "omega530": "0",
            "recorded_positive_layers": 53,
        },
        "order-530 verification summary",
    )
    verify_jet_layers(certificate, windows, 530)


def run_checked(command: list&#91;str&#93;, cwd: Path, timeout: int) -&gt; str:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )
    require(completed.returncode == 0, completed.stdout&#91;-8000:&#93;)
    return completed.stdout


def regenerate_bundle_artifacts(extracted: Path, temporary: Path) -&gt; None:
    support_output = temporary / "support"
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "scripts" / "f2_support_windows.py"),
            "--outdir",
            str(support_output),
        &#93;,
        extracted,
        120,
    )
    require(
        (support_output / "f2_support_windows.json").read_bytes()
        == (extracted / "data" / "f2_support_windows.json").read_bytes(),
        "support-window regeneration differs",
    )
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "scripts" / "f2_kuranishi_linear.py"),
            "--windows",
            str(support_output / "f2_support_windows.json"),
            "--outdir",
            str(support_output),
        &#93;,
        extracted,
        120,
    )
    for name in ("f2_linear_complexes.json", "f2_linear_complexes_summary.json"):
        require(
            (support_output / name).read_bytes()
            == (extracted / "data" / name).read_bytes(),
            f"linear-complex regeneration differs: {name}",
        )
    run_checked(
        &#91;
            sys.executable,
            str(extracted / "verify_f2_omega520_certificate.py"),
            str(extracted / "f2_omega520_exact_certificate.json"),
        &#93;,
        extracted,
        120,
    )


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--lane8-summary", type=Path)
    parser.add_argument("--f2-bundle", type=Path)
    parser.add_argument("--order530-certificate", type=Path)
    parser.add_argument("--regenerate", action="store_true")
    args = parser.parse_args()
    evidence = load_evidence()
    if args.metadata_only:
        print("lane89 recovery metadata validation: PASS")
        return 0

    lane8_summary = (
        args.lane8_summary
        or Path(evidence&#91;"lane8"&#93;&#91;"replay_summary_path"&#93;)
    )
    f2_bundle = args.f2_bundle or Path(evidence&#91;"f2"&#93;&#91;"public_bundle_path"&#93;)
    order530_certificate = (
        args.order530_certificate
        or Path(evidence&#91;"order530"&#93;&#91;"fresh_parameter_certificate_path"&#93;)
    )
    verify_lane8_summary(lane8_summary, evidence&#91;"lane8"&#93;)
    require(sha256_path(f2_bundle) == evidence&#91;"f2"&#93;&#91;"public_bundle_sha256"&#93;, "F2 bundle digest")

    with ZipFile(f2_bundle) as archive:
        members = safe_archive_members(archive)
        verify_file_manifest(members)
        windows = json.loads(members&#91;"f2_support_windows.json"&#93;)
        verify_all_support_windows(windows, evidence&#91;"f2"&#93;)
        verify_order520(members, windows, evidence&#91;"f2"&#93;)
        verify_order530(order530_certificate, windows, evidence&#91;"order530"&#93;)
        if args.regenerate:
            with tempfile.TemporaryDirectory(prefix="lane89-regenerate-") as directory:
                extracted = Path(directory) / "bundle"
                archive.extractall(extracted)
                regenerate_bundle_artifacts(extracted, Path(directory))

    print("lane89 mathematical recovery validation: PASS")
    print("lane8_roots=truncated_closed,full_closed")
    print("below_125=relative_to_imported_GGHV_and_compact_toric_theorems")
    print("f2_support_windows=exact_maximal_newton_bounded_enlargement")
    print("omega510=0 omega520=0 omega530_fresh_order280_slice=0")
    print("parameter_complete_order530=not_runnable_from_retained_inputs")
    print("classification=lane8_full_root;lane9_f2_recurrence_with_lane8_connection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-e5ed63a9f4cbb255"></a>

## `research-notes/planar-descent-no-go-20260802-v1/README.md`

<pre><code class="language-markdown">
# Planar descent from the known higher-dimensional examples

&gt; **Status: incomplete proof strategy — not a proof of the planar Jacobian
&gt; conjecture.**

This packet tests a possible route to the planar Jacobian conjecture: descend
one of the known higher-dimensional noninjective constant-Jacobian or
constant-Hessian examples to dimension two, then remove the ramification
introduced by the descent.  The supplied calculations rule out several
natural versions of the first step.  They do not supply the missing global
descent theorem or a way to remove the branch factor.

## Proposed proof route

For a minimal plane Keller counterexample, run the normalized Newton reduction
to a terminal complete-chain system.  The desired global theorem would say
that every terminal system has one of two outcomes:

1. it cannot have simultaneous finite polynomial support in the two adjacent
   boundary charts; or
2. it comes from an admissible polynomial approximate-root operation that
   strictly lowers the chosen Newton complexity.

Together with an exhaustive starting reduction and termination, this would
exclude a minimal counterexample.  Lane 8 owns the exhaustive Newton queue and
terminal systems; Lane 9 owns the adjacent-chart correspondence and polynomial
descent step.

## Exact evidence supplied

For the displayed three-dimensional Keller map, the scripts check:

- its invariant quotient has Jacobian `-2*C^2`, and in affine-modification
  coordinates the residual Jacobian is `2*c`;
- no affine source plane followed by a rank-two linear target projection gives
  a planar counterexample—the only Keller restriction is triangular;
- no polynomial graph over any coordinate plane followed by a rank-two linear
  target projection is Keller; and
- no nonzero linear target combination is a source coordinate, using the
  recorded generic-fibre calculation.

For the displayed five-variable constant-Hessian example, the scripts check:

- there is no second constant linear Schur direction;
- no affine hyperplane through the recorded collision yields a four-variable
  nonzero constant-Hessian restriction;
- the birational near-descent is a planar fold with Hessian determinant
  `64*s^2`; and
- the displayed six-parameter square correction cannot make that determinant
  a nonzero constant.

These are exact, sharply bounded no-go calculations.  They show that
noninjectivity can survive while a boundary or fold factor remains.  They do
not show that all possible descents fail.

## Missing proof obligations

- Prove—or replace—the imported reduction from a hypothetical planar Keller
  counterexample to the normalized support queue.
- Prove that the queue routes every saturation complement, coefficient branch,
  and rechart and terminates in the stated systems.
- Construct the actual adjacent complete-chain charts and prove simultaneous
  two-sided finite support is impossible, or identify an admissible
  complexity-lowering operation.
- Show that every possible higher-dimensional descent is covered by an
  invariant class broad enough to matter; the affine-plane, polynomial-graph,
  linear-projection, and displayed square-correction families are not
  exhaustive.
- Verify the literature attributions and the source formulas independently
  before treating the no-go statements as publication-ready results.

## Reproducible checks

- `three_dimensional_descent_no_go.py`
- `affine_plane_linear_projection_no_go.py`
- `y_graph_descent_no_go.py`
- `linear_target_coordinate_fibres.py`
- `hc4_linear_descent_no_go.py`
- `hc4_square_correction_no_go.py`

All six scripts use exact SymPy arithmetic.  A successful replay establishes
only the identities and finite coefficient eliminations encoded in that
script; it does not establish the proposed global proof route.
</code></pre>

<a id="source-78e62daae2246c31"></a>

## `research-notes/planar-descent-no-go-20260802-v1/affine_plane_linear_projection_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Classify all affine-plane / linear-projection descents of the 2026 JC_3 map.

Let F:A^3-&gt;A^3 be the explicit Keller counterexample.  Let

    S={m_1 x+m_2 y+m_3 z=d}

be an affine source plane, and let pi:A^3-&gt;A^2 be a rank-two linear map with
kernel direction k.  Up to fixed nonzero choices of volume forms, the Jacobian
of pi o F|_S is

    R_{m,k}=m^T adj(JF) k   modulo (m.X-d).

The exact coefficient calculation below proves:

* R_{m,k} cannot be a nonzero constant unless S={x=0};
* on S={x=0}, nonzero constant Jacobian occurs precisely when the target
  projection is nondegenerate on the first two target coordinates;
* every such restriction is a linear target change of
      (y,z) -&gt; (z+4y^2,y),
  hence a polynomial automorphism.

Therefore this entire descent class contains no planar counterexample.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x*y
F1 = sp.expand(u**3*z + y**2*u*(4+3*x*y))
F2 = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4+3*x*y))
F3 = sp.expand(2*x - 3*x**2*y - x**3*z)
F = (F1,F2,F3)
JF = sp.Matrix(&#91;&#91;sp.diff(fi,v) for v in (x,y,z)&#93; for fi in F&#93;)
assert sp.factor(JF.det()) == -2
Adj = JF.adjugate()
k1,k2,k3 = sp.symbols("k1 k2 k3")
k = sp.Matrix(&#91;k1,k2,k3&#93;)

# Case I: m3 != 0.  Normalize m=(a,b,1), z=d-a*x-b*y.
a,b,d = sp.symbols("a b d")
m = sp.Matrix(&#91;&#91;a,b,1&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(z,d-a*x-b*y))
P = sp.Poly(R,x,y)
assert P.coeff_monomial(y**3) == -89*k3
assert sp.expand(P.coeff_monomial(x*y**2).subs(k3,0)) == -6*k2
assert sp.expand(P.coeff_monomial(x*y).subs({k3:0,k2:0})) == -42*k1

# Case II: m3=0,m2 != 0. Normalize m=(a,1,0), y=d-a*x.
a,d = sp.symbols("a d")
m = sp.Matrix(&#91;&#91;a,1,0&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(y,d-a*x))
P = sp.Poly(R,x,z)
assert P.coeff_monomial(z) == 3*k3
assert sp.expand(P.coeff_monomial(x**2*z).subs(k3,0)) == 3*k2
assert sp.expand(P.coeff_monomial(x).subs({k3:0,k2:0})) == 6*k1

# Case III: m3=m2=0. Normalize m=(1,0,0), x=d.
d = sp.symbols("d")
m = sp.Matrix(&#91;&#91;1,0,0&#93;&#93;)
R = sp.expand((m*Adj*k)&#91;0&#93;.subs(x,d))
P = sp.Poly(R,y,z)
assert P.coeff_monomial(y**3*z) == 12*d**5*k3
assert sp.expand(P.coeff_monomial(y**3).subs(k3,0)) == 9*d**5*k2
assert sp.expand(P.coeff_monomial(y).subs({k3:0,k2:0})) == -6*d**4*k1
# At d=0 every nonconstant coefficient vanishes, and the constant is -k3.
for mon,coeff in P.terms():
    if mon != (0,0):
        assert sp.expand(coeff.subs(d,0)) == 0
assert sp.expand(P.coeff_monomial(1).subs(d,0)) == -k3

# The exceptional restriction is triangular.
assert sp.expand(F1.subs(x,0) - (z+4*y**2)) == 0
assert F2.subs(x,0) == y
assert F3.subs(x,0) == 0
assert sp.det(sp.Matrix(&#91;
    &#91;sp.diff(F1.subs(x,0),y),sp.diff(F1.subs(x,0),z)&#93;,
    &#91;sp.diff(F2.subs(x,0),y),sp.diff(F2.subs(x,0),z)&#93;,
&#93;)) == -1

print("Case m3!=0: y^3, x*y^2, x*y force k3=k2=k1=0")
print("Case m3=0,m2!=0: z, x^2*z, x force k3=k2=k1=0")
print("Case m=(1,0,0), d!=0: y^3*z, y^3, y force k3=k2=k1=0")
print("Exceptional plane x=0: restriction (z+4*y^2,y,0), triangular automorphism")
</code></pre>

<a id="source-f7cb2b829210956c"></a>

## `research-notes/planar-descent-no-go-20260802-v1/hc4_linear_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact no-go checks for descending the 5-variable Hessian counterexample to HC_4.

The five-variable potential is the Meng--Yang 2026 counterexample

    Psi = A^2 + 13 A + 2 B.

This script verifies three sharply scoped statements:

1. There is no nonzero constant linear direction c for which the second
   directional derivative c^T Hess(Psi)c is constant.  Hence the published
   one-variable Schur descent cannot simply be repeated after a linear change.
2. No affine linear hyperplane containing the two known collision points
   carries a four-variable restriction with nonzero constant Hessian
   determinant.  The four projective cases are exhausted exactly.
3. A birational partial Schur reduction does produce a polynomial
   four-variable near-example with a two-point gradient collision, but its
   Hessian determinant is 64*s^2.  After a linear change this is just the
   doubled planar fold (s,u)-&gt;((u^2-s^2)/2,4u); the missing constant-Jacobian
   condition is precisely the remaining planar obstruction.

All calculations are exact over Q.  This does not prove HC_4 or JC_2; it rules
out the most direct linear restriction/second-Schur descent of this particular
HC_5 counterexample.
"""
from __future__ import annotations

import itertools
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

# ---------------------------------------------------------------------------
# Source potential and collision.
# ---------------------------------------------------------------------------
x1, x2, y1, y2, y3 = sp.symbols("x1 x2 y1 y2 y3")
u = 1 + x1 * x2
A = y1 * u**3 + 3 * x1 * y2 * u**2 - x1**3 * y3
B = (
    y1 * x2**2 * u * (4 + 3 * x1 * x2)
    + y2 * (x2 + 3 * x1 * x2**2 * (4 + 3 * x1 * x2))
    + y3 * (2 * x1 - 3 * x1**2 * x2)
)
Psi = sp.expand(A**2 + 13 * A + 2 * B)
vars5 = (x1, x2, y1, y2, y3)
P_plus = {x1: 1, x2: -sp.Rational(3, 2), y1: 0, y2: 0, y3: 0}
P_minus = {x1: -1, x2: sp.Rational(3, 2), y1: 0, y2: 0, y3: 0}
grad = &#91;sp.diff(Psi, v) for v in vars5&#93;
assert &#91;g.subs(P_plus) for g in grad&#93; == &#91;g.subs(P_minus) for g in grad&#93;

# ---------------------------------------------------------------------------
# 1. No second constant linear Schur direction.
# ---------------------------------------------------------------------------
H5 = sp.hessian(Psi, vars5)
columns: list&#91;sp.Poly&#93; = &#91;&#93;
for i in range(5):
    for j in range(i, 5):
        entry = H5&#91;i, j&#93; if i == j else 2 * H5&#91;i, j&#93;
        columns.append(sp.Poly(entry, *vars5))
all_monomials = sorted(set().union(*(set(p.monoms()) for p in columns)))
nonconstant_monomials = &#91;m for m in all_monomials if any(m)&#93;
coefficient_matrix = sp.Matrix(&#91;
    &#91;p.coeff_monomial(m) for p in columns&#93;
    for m in nonconstant_monomials
&#93;)
assert coefficient_matrix.shape == (158, 15)
assert coefficient_matrix.rank() == 15

# ---------------------------------------------------------------------------
# Sparse exact determinant helper.
# ---------------------------------------------------------------------------
def permutation_sign(perm: tuple&#91;int, ...&#93;) -&gt; int:
    inversions = sum(
        perm&#91;i&#93; &gt; perm&#91;j&#93;
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def determinant4(R, matrix):
    value = R.zero
    for perm in itertools.permutations(range(4)):
        term = R.one
        for i in range(4):
            term *= matrix&#91;i&#93;&#91;perm&#91;i&#93;&#93;
        value += permutation_sign(perm) * term
    return value

# Every affine hyperplane through P_+ and P_- has equation
#   3*s*x1 + 2*s*x2 + n3*y1+n4*y2+n5*y3=0.
# The four cases below cover projective &#91;s:n3:n4:n5&#93;.

# Case 1: n5 != 0, normalize n5=1.
R1, X1, X2, Y1, Y2, S, aa, bb = ring(
    "x1,x2,y1,y2,s,a,b", QQ
)
Y3 = -(3 * S * X1 + 2 * S * X2 + aa * Y1 + bb * Y2)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y1, Y2)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det1 = determinant4(R1, HH)
assert len(det1.terms()) == 9397
assert det1&#91;(0, 0, 1, 0, 0, 0, 0)&#93; == -36504

# Case 2: n5=0, n4 != 0, normalize n4=1.
R2, X1, X2, Y1, Y3, S, aa = ring("x1,x2,y1,y3,s,a", QQ)
Y2 = -(3 * S * X1 + 2 * S * X2 + aa * Y1)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y1, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det2 = determinant4(R2, HH)
assert len(det2.terms()) == 3710
assert det2&#91;(0, 0, 1, 0, 0, 0)&#93; == -512

# Case 3: n5=n4=0, n3 != 0, normalize n3=1.
R3, X1, X2, Y2, Y3, S = ring("x1,x2,y2,y3,s", QQ)
Y1 = -(3 * S * X1 + 2 * S * X2)
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, X2, Y2, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det3 = determinant4(R3, HH)
assert len(det3.terms()) == 950
assert det3&#91;(1, 1, 0, 0, 0)&#93; == 2688

# Case 4: n3=n4=n5=0, hence s != 0; set 3*x1+2*x2=0.
R4, X1, Y1, Y2, Y3 = ring("x1,y1,y2,y3", QQ)
X2 = -QQ(3, 2) * X1
U = 1 + X1 * X2
AA = Y1 * U**3 + 3 * X1 * Y2 * U**2 - X1**3 * Y3
BB = (
    Y1 * X2**2 * U * (4 + 3 * X1 * X2)
    + Y2 * (X2 + 3 * X1 * X2**2 * (4 + 3 * X1 * X2))
    + Y3 * (2 * X1 - 3 * X1**2 * X2)
)
PP = AA**2 + 13 * AA + 2 * BB
V = (X1, Y1, Y2, Y3)
HH = &#91;&#91;PP.diff(vi).diff(vj) for vj in V&#93; for vi in V&#93;
det4 = determinant4(R4, HH)
assert det4 == R4.zero

# ---------------------------------------------------------------------------
# 3. Birational Schur near-descent: a polynomial four-variable fold.
# ---------------------------------------------------------------------------
s, xx, yy, zz = sp.symbols("s x y z")
Phi = sp.expand(
    (
        -16 * s**4 + 48 * s**3 * xx - 36 * s**2 * xx**2
        + 16 * s**2 * yy + 104 * s**2 + 24 * s * xx * yy
        - 156 * s * xx + 48 * s * zz + 8 * xx**2 * yy
        + 32 * xx * zz - 169
    ) / 4
)
vars4 = (s, xx, yy, zz)
assert sp.factor(sp.hessian(Phi, vars4).det()) == 64 * s**2
q_plus = {s: 1, xx: -sp.Rational(3, 2), yy: 0, zz: 0}
q_minus = {s: -1, xx: sp.Rational(3, 2), yy: 0, zz: 0}
grad4 = &#91;sp.diff(Phi, v) for v in vars4&#93;
assert &#91;g.subs(q_plus) for g in grad4&#93; == &#91;g.subs(q_minus) for g in grad4&#93;

# Phi=phi0(s,x)+y*f(s,x)+z*g(s,x).  Its Hessian determinant is the square
# of the planar Jacobian of (f,g).
f = sp.diff(Phi, yy)
g = sp.diff(Phi, zz)
Jfg = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(f, s), sp.diff(f, xx)&#93;,
    &#91;sp.diff(g, s), sp.diff(g, xx)&#93;,
&#93;)))
assert Jfg == -8 * s
assert sp.expand(sp.hessian(Phi, vars4).det() - Jfg**2) == 0
new_u = sp.symbols("u")
assert sp.expand(f.subs(xx, (new_u - 3 * s) / 2) - (new_u**2 - s**2) / 2) == 0
assert sp.expand(g.subs(xx, (new_u - 3 * s) / 2) - 4 * new_u) == 0

print("Directional-second-derivative coefficient matrix: 158 x 15, rank 15")
print("Hyperplane cases: coefficients -36504, -512, 2688; final case determinant 0")
print("No linear hyperplane through the collision yields nonzero constant Hessian")
print("Birational four-variable near-descent: det Hess = 64*s^2")
print("Underlying planar fold: ((u^2-s^2)/2, 4u), Jacobian -8s")
</code></pre>

<a id="source-9e967fdeb2921c93"></a>

## `research-notes/planar-descent-no-go-20260802-v1/hc4_square_correction_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact no-go for the first natural quadratic correction of the HC4 fold.

In coordinates (s,u,y,z), the polynomial four-variable near-descent is

    Phi = -(13*s^2 - 3*s*u - 13)^2/4
          + (u^2-s^2)*y/2 + 4*u*z,

and det Hess(Phi)=16*s^2.  This script proves that adding

    w^2,  w=(a0+a1*s+a2*u)*y + (b0+b1*s+b2*u)*z,

cannot make the Hessian determinant a nonzero constant.  It is enough to
restrict the Hessian determinant to y=z=0; the displayed coefficient
conditions give a contradiction over every characteristic-zero field.
"""
from __future__ import annotations

import sympy as sp

s, u, y, z = sp.symbols("s u y z")
a0, a1, a2, b0, b1, b2 = sp.symbols("a0 a1 a2 b0 b1 b2")
q = 13 * s**2 - 3 * s * u - 13
Phi = -q**2 / 4 + (u**2 - s**2) * y / 2 + 4 * u * z
assert sp.factor(sp.hessian(Phi, (s, u, y, z)).det()) == 16 * s**2

A = a0 + a1 * s + a2 * u
B = b0 + b1 * s + b2 * u
w = A * y + B * z
F = sp.expand(Phi + w**2)

# At y=z=0, the base-base and mixed corrections from w^2 vanish; only the
# rank-one fibre Hessian 2(A,B)^T(A,B) remains.  Computing this specialization
# is much smaller than expanding the full four-variable determinant.
H = sp.hessian(F, (s, u, y, z)).subs({y: 0, z: 0})
D = sp.Poly(sp.expand(H.det()), s, u)

assert sp.factor(D.coeff_monomial(s**6)) == 9 * b1**2
assert sp.factor(D.coeff_monomial(u**6)) == 9 * b2**2
assert sp.factor(D.coeff_monomial(s)) == -104 * a0 * (104 * a1 + 3 * b0)
assert sp.factor(D.coeff_monomial(u)) == -2704 * a0 * (4 * a2 - b0)
assert D.coeff_monomial(1) == -5408 * a0**2

# If D were a nonzero constant, b1=b2=0 and a0!=0.  The coefficients of s
# and u then force b0=-104*a1/3=4*a2.  Under these relations the u^2
# coefficient is 144*a0^2, a contradiction.
u2_reduced = sp.factor(
    D.coeff_monomial(u**2).subs({b1: 0, b2: 0, b0: 4 * a2})
)
assert u2_reduced == 144 * a0**2

print("det Hess(Phi) = 16*s^2")
print("s^6 and u^6 coefficients force b1=b2=0")
print("nonzero constant term forces a0!=0")
print("s,u coefficients force 104*a1+3*b0=0 and 4*a2-b0=0")
print("then the u^2 coefficient is 144*a0^2: contradiction")
</code></pre>

<a id="source-6f882ea3f01158fb"></a>

## `research-notes/planar-descent-no-go-20260802-v1/linear_target_coordinate_fibres.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Structure of generic fibres of every linear target coordinate.

For H=alpha*F1+beta*F2+gamma*F3 of the 2026 three-dimensional Keller map,
write H=A(x,y)z+B(x,y), and put t=1+xy.  The script verifies

    A = alpha*t^3 + 3*beta*x*t^2 - gamma*x^3,

and, on each hyperbola t=rho*x satisfying

    alpha*rho^3 + 3*beta*rho^2 - gamma = 0,

the restriction

    B = alpha*rho^2 + 4*beta*rho + (alpha*rho+2*beta)/x.

These formulas give a short Euler-characteristic proof that no nonzero
linear combination of F1,F2,F3 is a coordinate polynomial.  The one case
whose generic Euler characteristic is 1 is F1 itself; its generic fibre is
A^2 minus the hyperbola 1+xy=0 and has the nonconstant unit 1+xy.
"""
from __future__ import annotations

import sympy as sp

x, y, z, t, rho = sp.symbols("x y z t rho")
alpha, beta, gamma = sp.symbols("alpha beta gamma")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)
H = sp.expand(alpha * F1 + beta * F2 + gamma * F3)
A = sp.expand(sp.diff(H, z))
B = sp.expand(H - A * z)

A_t = sp.factor(A.subs(y, (t - 1) / x))
B_t = sp.factor(sp.together(B.subs(y, (t - 1) / x)))
assert A_t == alpha * t**3 + 3 * beta * x * t**2 - gamma * x**3

root_relation = {gamma: alpha * rho**3 + 3 * beta * rho**2}
B_on_component = sp.factor(
    sp.together(B_t.subs(t, rho * x).subs(root_relation))
)
expected = alpha * rho**2 + 4 * beta * rho + (alpha * rho + 2 * beta) / x
assert sp.factor(B_on_component - expected) == 0

# A root component is constant for B exactly when alpha*rho+2*beta=0.
# Such a root is repeated because the derivative of the cubic is
# 3*rho*(alpha*rho+2*beta).
R = alpha * rho**3 + 3 * beta * rho**2 - gamma
assert sp.factor(sp.diff(R, rho)) == 3 * rho * (alpha * rho + 2 * beta)

# Special repeated-root factorizations used in the case split.
b = sp.symbols("b")
assert sp.expand((rho + 2 * b) ** 2 * (rho - b)) == rho**3 + 3 * b * rho**2 - 4 * b**3
assert sp.expand(rho**2 * (rho + 3 * b)) == rho**3 + 3 * b * rho**2

print("A(x,t) = alpha*t^3 + 3*beta*x*t^2 - gamma*x^3")
print("On t=rho*x: B = alpha*rho^2+4*beta*rho+(alpha*rho+2*beta)/x")
print("alpha!=0, not F1: at least one nonconstant G_m component, so chi(generic fibre)&gt;=2")
print("alpha=0,beta!=0: line plus one/two G_m components, so chi(generic fibre)&gt;=2")
print("H=gamma*F3: generic fibre is G_m x A^1")
print("H=alpha*F1: generic fibre has the nonconstant unit 1+x*y")
print("Therefore no nonzero linear target coordinate pulls back to a source coordinate")
</code></pre>

<a id="source-e5a22357febe952a"></a>

## `research-notes/planar-descent-no-go-20260802-v1/three_dimensional_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for simple planar descents of the 2026 three-dimensional Keller map.

This script proves/checks three sharply scoped statements.

1. The G_m-invariant quotient is a polynomial map A^2 -&gt; A^2 whose
   Jacobian is -2 times the square of the contracted invariant.
2. After a birational monomial simplification it is the cubic cover
       s^3 - 2 s^2 + P s - 2 Q = 0,
   but its planar Jacobian still has the unavoidable branch factor.
3. For every polynomial graph z=h(x,y), and every rank-two linear target
   projection, the induced map A^2 -&gt; A^2 cannot have nonzero constant
   Jacobian.  The proof is degree-theoretic and valid for arbitrary degree h.

The script uses exact symbolic arithmetic only.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)

# ---------------------------------------------------------------------------
# 1. Coarse G_m quotient.
# ---------------------------------------------------------------------------
a, b = sp.symbols("a b")
uq = 1 + a
X = sp.expand(uq**3 * b + a**2 * uq * (4 + 3 * a))
C = 2 - 3 * a - b
D = sp.expand(a + 3 * uq**2 * b + 3 * a**2 * (4 + 3 * a))
P = sp.expand(X * C**2)
Q = sp.expand(D * C)
Jquot = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(P, a), sp.diff(P, b)&#93;,
    &#91;sp.diff(Q, a), sp.diff(Q, b)&#93;,
&#93;)))
assert sp.expand(Jquot + 2 * C**2) == 0

# A useful affine-modification coordinate.  Set r=a+1 and p=C*r.
r, c, p = sp.symbols("r c p")
Xrc = sp.expand(-c * r**3 + r**2 + r)
Drc = sp.expand(-3 * c * r**2 + 4 * r + 2)
Ppc = sp.expand((c**2 * Xrc).subs(r, p / c))
Qpc = sp.expand((c * Drc).subs(r, p / c))
assert Ppc == -p**3 + p**2 + c * p
assert Qpc == -3 * p**2 + 4 * p + 2 * c
Jpc = sp.factor(sp.det(sp.Matrix(&#91;
    &#91;sp.diff(Ppc, p), sp.diff(Ppc, c)&#93;,
    &#91;sp.diff(Qpc, p), sp.diff(Qpc, c)&#93;,
&#93;)))
assert Jpc == 2 * c
s = sp.symbols("s")
c_from_Q = sp.expand((Qpc + 3 * p**2 - 4 * p) / 2)
cubic = sp.expand(p**3 - 2 * p**2 + Qpc * p - 2 * Ppc)
assert cubic == 0

# ---------------------------------------------------------------------------
# 2. Polynomial graph z=h(x,y), arbitrary linear target projection.
# ---------------------------------------------------------------------------
H, Hx, Hy = sp.symbols("H Hx Hy")
hfun = sp.Function("h")(x, y)
Fs = &#91;F1, F2, F3&#93;


def graph_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(z, hfun)
    fj = Fs&#91;j&#93;.subs(z, hfun)
    jac = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, x), sp.diff(fi, y)&#93;,
        &#91;sp.diff(fj, x), sp.diff(fj, y)&#93;,
    &#93;))
    return sp.expand(jac.subs({
        hfun: H,
        sp.diff(hfun, x): Hx,
        sp.diff(hfun, y): Hy,
    }))


J12 = graph_jacobian(0, 1)
J13 = graph_jacobian(0, 2)
J23 = graph_jacobian(1, 2)

# The unique top-degree quadratic-in-h pieces.  If h_d is the leading
# homogeneous form of a nonconstant h, these become the leading homogeneous
# terms of the restricted Jacobians.
expected_top_12 = -3 * x * (x * y) ** 4 * H * (3 * H + x * Hx)
expected_top_13 = 3 * x**3 * (x * y) ** 2 * H * (3 * H + x * Hx)
expected_top_23 = 6 * x**4 * (x * y) * H * (3 * H + x * Hx)


def quadratic_part(expr: sp.Expr) -&gt; sp.Expr:
    # Degree two when H and either derivative are assigned degree one.
    poly = sp.Poly(expr, H, Hx, Hy)
    out = 0
    for (e_h, e_hx, e_hy), coeff in poly.terms():
        if e_h + e_hx + e_hy == 2:
            out += coeff * H**e_h * Hx**e_hx * Hy**e_hy
    return sp.expand(out)


q12 = quadratic_part(J12)
q13 = quadratic_part(J13)
q23 = quadratic_part(J23)

# Each quadratic part also has lower total (x,y)-degree terms involving Hy;
# extract the highest x,y-degree coefficient to verify the formulas above.
def leading_after_homogeneous_substitution(expr: sp.Expr) -&gt; sp.Expr:
    """Terms of maximal total degree after H-&gt;h_d and dH-&gt;degree d-1."""
    poly = sp.Poly(expr, x, y, H, Hx, Hy)
    score = lambda mon: mon&#91;0&#93; + mon&#91;1&#93; - mon&#91;3&#93; - mon&#91;4&#93;
    max_score = max(score(mon) for mon, _ in poly.terms())
    out = 0
    for mon, coeff in poly.terms():
        ex, ey, e_h, e_hx, e_hy = mon
        if score(mon) == max_score:
            out += coeff * x**ex * y**ey * H**e_h * Hx**e_hx * Hy**e_hy
    return sp.expand(out)


assert sp.expand(leading_after_homogeneous_substitution(q12) - expected_top_12) == 0
assert sp.expand(leading_after_homogeneous_substitution(q13) - expected_top_13) == 0
assert sp.expand(leading_after_homogeneous_substitution(q23) - expected_top_23) == 0

# Explanation encoded as a check: if h_d=sum c_i x^i y^(d-i), the equation
# x*d_x h_d=-3 h_d has no nonzero polynomial solution because every exponent
# i is a nonnegative integer.  We verify this coefficientwise for a symbolic
# generic degree d up to a representative range; the written proof is uniform.
for degree in range(1, 13):
    coeffs = sp.symbols(f"t0:{degree + 1}")
    hd = sum(coeffs&#91;i&#93; * x**i * y**(degree - i) for i in range(degree + 1))
    relation = sp.Poly(sp.expand(x * sp.diff(hd, x) + 3 * hd), x, y)
    for i in range(degree + 1):
        assert relation.coeff_monomial(x**i * y**(degree-i)) == (i+3)*coeffs&#91;i&#93;
    # Solving the diagonal equations gives all zero.
    diagonal = &#91;sp.expand((i + 3) * coeffs&#91;i&#93;) for i in range(degree + 1)&#93;
    assert sp.solve(diagonal, coeffs, dict=True) == &#91;dict(zip(coeffs, &#91;0&#93; * len(coeffs)))&#93;

# Constant h cannot work either.  The coefficients x^3 y^6, x^3 y^4,
# and x^3 y^3 successively kill the three Pluecker coordinates.
h0, lam12, lam13, lam23, kappa = sp.symbols(
    "h0 lam12 lam13 lam23 kappa"
)
const_combination = sp.Poly(
    sp.expand(
        lam12 * J12.subs({H: h0, Hx: 0, Hy: 0})
        + lam13 * J13.subs({H: h0, Hx: 0, Hy: 0})
        + lam23 * J23.subs({H: h0, Hx: 0, Hy: 0})
        - kappa
    ),
    x,
    y,
)
assert const_combination.coeff_monomial(x**3 * y**6) == -54 * lam12
assert sp.expand(
    const_combination.coeff_monomial(x**3 * y**4).subs(lam12, 0)
) == 54 * lam13
assert sp.expand(
    const_combination.coeff_monomial(x**3 * y**3).subs({lam12: 0, lam13: 0})
) == 108 * lam23

print("3D Keller map determinant: -2 (source formula imported from the paper)")
print(f"Coarse quotient Jacobian: {Jquot}")
print(f"Affine-modification quotient Jacobian: {Jpc}")
print("Fiber cubic: p^3 - 2 p^2 + Q p - 2 P = 0")
print("Polynomial z-graph + linear target projection: NO Keller descent")

# ---------------------------------------------------------------------------
# 3. Polynomial graph x=g(y,z), arbitrary linear target projection.
#    The only Keller case is the trivial plane x=0, where the restriction is
#    the triangular automorphism (y,z)-&gt;(z+4y^2,y) up to a linear target map.
# ---------------------------------------------------------------------------
G, Gy, Gz = sp.symbols("G Gy Gz")
gfun = sp.Function("g")(y, z)


def x_graph_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(x, gfun)
    fj = Fs&#91;j&#93;.subs(x, gfun)
    jac = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, y), sp.diff(fi, z)&#93;,
        &#91;sp.diff(fj, y), sp.diff(fj, z)&#93;,
    &#93;))
    return sp.expand(jac.subs({
        gfun: G,
        sp.diff(gfun, y): Gy,
        sp.diff(gfun, z): Gz,
    }))


K12 = x_graph_jacobian(0, 1)
K13 = x_graph_jacobian(0, 2)
K23 = x_graph_jacobian(1, 2)
expected_k12 = 3 * G**5 * y**4 * z * (G + 3 * z * Gz)
expected_k13 = -3 * G**5 * y**2 * z * (G + 3 * z * Gz)
expected_k23 = -6 * G**5 * y * z * (G + 3 * z * Gz)


def leading_g_degree(expr: sp.Expr) -&gt; sp.Expr:
    """Highest degree after G-&gt;g_d, dG-&gt;degree d-1, for any d&gt;=1."""
    poly = sp.Poly(expr, y, z, G, Gy, Gz)
    # total after substitution is d*(eG+eGy+eGz)+base-eGy-eGz.
    # Lexicographically maximize slope then intercept, valid uniformly d&gt;=1
    # here because the unique slope-six block also has maximal intercept.
    data = &#91;&#93;
    for mon, coeff in poly.terms():
        ey, ez, eG, eGy, eGz = mon
        slope = eG + eGy + eGz
        intercept = ey + ez - eGy - eGz
        data.append((slope, intercept, mon, coeff))
    max_slope = max(item&#91;0&#93; for item in data)
    max_intercept = max(item&#91;1&#93; for item in data if item&#91;0&#93; == max_slope)
    out = 0
    for slope, intercept, mon, coeff in data:
        if slope == max_slope and intercept == max_intercept:
            ey, ez, eG, eGy, eGz = mon
            out += coeff * y**ey * z**ez * G**eG * Gy**eGy * Gz**eGz
    return sp.expand(out)


assert sp.expand(leading_g_degree(K12) - expected_k12) == 0
assert sp.expand(leading_g_degree(K13) - expected_k13) == 0
assert sp.expand(leading_g_degree(K23) - expected_k23) == 0

# The equation g_d+3 z*d_z g_d=0 has no nonzero homogeneous polynomial
# solution: the coefficient of y^(d-j)z^j is multiplied by 1+3j.
for degree in range(1, 13):
    coeffs = sp.symbols(f"q0:{degree + 1}")
    gd = sum(coeffs&#91;j&#93; * y**(degree-j) * z**j for j in range(degree + 1))
    relation = sp.Poly(sp.expand(gd + 3*z*sp.diff(gd,z)), y, z)
    for j in range(degree+1):
        assert relation.coeff_monomial(y**(degree-j)*z**j) == (1+3*j)*coeffs&#91;j&#93;

# Constants: c!=0 is killed successively by y^4 z, y^2 z, yz; c=0
# leaves K12=-1 and K13=K23=0.
g0 = sp.symbols("g0")
assert sp.Poly(K12.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y**4*z) == 3*g0**6
assert sp.Poly(K13.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y**2*z) == -3*g0**6
assert sp.Poly(K23.subs({G:g0,Gy:0,Gz:0}),y,z).coeff_monomial(y*z) == -6*g0**6
assert K12.subs({G:0,Gy:0,Gz:0}) == -1
assert K13.subs({G:0,Gy:0,Gz:0}) == 0
assert K23.subs({G:0,Gy:0,Gz:0}) == 0
print("Polynomial x-graph + linear target projection: only x=0, a triangular automorphism")
</code></pre>

<a id="source-3b8a058f37f1b009"></a>

## `research-notes/planar-descent-no-go-20260802-v1/y_graph_descent_no_go.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""No planar Keller descent from a polynomial graph y=h(x,z).

For the 2026 three-dimensional Keller counterexample F=(F1,F2,F3), this
script computes the three restricted 2x2 Jacobians on y=h(x,z).  It verifies
the degree argument proving that no nonzero Pluecker combination can be a
nonzero constant, for any polynomial h and any rank-two linear target
projection.

Together with three_dimensional_descent_no_go.py, this covers polynomial
graphs over each of the three coordinate planes.
"""
from __future__ import annotations

import sympy as sp

x, y, z = sp.symbols("x y z")
u = 1 + x * y
F1 = sp.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
F2 = sp.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
F3 = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)
Fs = (F1, F2, F3)

G, Gx, Gz = sp.symbols("G Gx Gz")
gfun = sp.Function("g")(x, z)


def restricted_jacobian(i: int, j: int) -&gt; sp.Expr:
    fi = Fs&#91;i&#93;.subs(y, gfun)
    fj = Fs&#91;j&#93;.subs(y, gfun)
    value = sp.det(sp.Matrix(&#91;
        &#91;sp.diff(fi, x), sp.diff(fi, z)&#93;,
        &#91;sp.diff(fj, x), sp.diff(fj, z)&#93;,
    &#93;))
    return sp.expand(value.subs({
        gfun: G,
        sp.diff(gfun, x): Gx,
        sp.diff(gfun, z): Gz,
    }))


J12 = restricted_jacobian(0, 1)
J13 = restricted_jacobian(0, 2)
J23 = restricted_jacobian(1, 2)


def highest_g_slope(expr: sp.Expr) -&gt; sp.Expr:
    """Highest degree in G,Gx,Gz; ties by actual base-degree intercept."""
    poly = sp.Poly(expr, x, z, G, Gx, Gz)
    data = &#91;&#93;
    for mon, coeff in poly.terms():
        ex, ez, e_g, e_gx, e_gz = mon
        slope = e_g + e_gx + e_gz
        intercept = ex + ez - e_gx - e_gz
        data.append((slope, intercept, mon, coeff))
    max_slope = max(item&#91;0&#93; for item in data)
    max_intercept = max(item&#91;1&#93; for item in data if item&#91;0&#93; == max_slope)
    out = 0
    for slope, intercept, mon, coeff in data:
        if slope == max_slope and intercept == max_intercept:
            ex, ez, e_g, e_gx, e_gz = mon
            out += coeff * x**ex * z**ez * G**e_g * Gx**e_gx * Gz**e_gz
    return sp.expand(out)


assert sp.factor(highest_g_slope(J12)) == -54 * G**6 * Gz * x**3
assert sp.factor(highest_g_slope(J13)) == 54 * G**4 * Gz * x**3
assert sp.factor(highest_g_slope(J23)) == 108 * G**3 * Gz * x**3

# Hence the leading homogeneous form h_d must satisfy d_z h_d=0 whenever
# the corresponding Pluecker coefficient is the first nonzero one.  Thus
# h_d=c*x^d.  Direct substitution gives a nonzero next leading term.  The
# d=1,2 cases are exceptional only in which equal-degree terms tie; d&gt;=3 has
# the uniform monomial listed below.
c = sp.symbols("c", nonzero=True)
expected = {
    1: (
        3 * c**5 * x**10 * z,
        -3 * c**3 * x**8 * z,
        -6 * c**2 * x**7 * z,
    ),
    2: (
        6 * c**5 * x**15 * (3 * c * x + z),
        -6 * c**3 * x**11 * (3 * c * x + z),
        -12 * c**2 * x**9 * (3 * c * x + z),
    ),
}
for degree in (1, 2):
    for expr, target in zip((J12, J13, J23), expected&#91;degree&#93;):
        specialized = sp.Poly(
            sp.expand(expr.subs({
                G: c * x**degree,
                Gx: c * degree * x**(degree - 1),
                Gz: 0,
            })),
            x,
            z,
        )
        top_degree = max(sum(mon) for mon, _ in specialized.terms())
        top = sum(
            coeff * x**mon&#91;0&#93; * z**mon&#91;1&#93;
            for mon, coeff in specialized.terms()
            if sum(mon) == top_degree
        )
        assert sp.expand(top - target) == 0

for degree in range(3, 10):
    targets = (
        9 * degree * c**6 * x**(6 * degree + 4),
        -9 * degree * c**4 * x**(4 * degree + 4),
        -18 * degree * c**3 * x**(3 * degree + 4),
    )
    for expr, target in zip((J12, J13, J23), targets):
        specialized = sp.Poly(
            sp.expand(expr.subs({
                G: c * x**degree,
                Gx: c * degree * x**(degree - 1),
                Gz: 0,
            })),
            x,
            z,
        )
        top_degree = max(sum(mon) for mon, _ in specialized.terms())
        top = sum(
            coeff * x**mon&#91;0&#93; * z**mon&#91;1&#93;
            for mon, coeff in specialized.terms()
            if sum(mon) == top_degree
        )
        assert sp.expand(top - target) == 0

# Constant h: coefficients z, x, and x^2*z successively kill the three
# Pluecker coordinates (the target constant is allowed in the (0,0) term).
h0, l12, l13, l23 = sp.symbols("h0 l12 l13 l23")
combination = sp.Poly(sp.expand(
    l12 * J12.subs({G: h0, Gx: 0, Gz: 0})
    + l13 * J13.subs({G: h0, Gx: 0, Gz: 0})
    + l23 * J23.subs({G: h0, Gx: 0, Gz: 0})
), x, z)
assert combination.coeff_monomial(z) == -3 * l12
assert sp.factor(combination.coeff_monomial(x).subs(l12, 0)) == -6 * l23
assert sp.factor(
    combination.coeff_monomial(x**2 * z).subs({l12: 0, l23: 0})
) == 3 * l13

print("y=h(x,z): every nonconstant leading form is excluded by degree")
print("constant h: z, x, x^2*z coefficients force all Pluecker coordinates zero")
print("No polynomial y-graph with a rank-two linear target projection is Keller")
</code></pre>

[Back to Lane 8](plane-newton-queue-terminal-certificates.md)
