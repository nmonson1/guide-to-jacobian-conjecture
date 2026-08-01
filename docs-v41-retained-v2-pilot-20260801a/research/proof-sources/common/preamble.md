---
title: "Text proof source — common/preamble.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/common/preamble.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `a0a994251bdf20e13e53d2339df3ed2ebf83870ec74ff9afeca5a96f7d463be6` · 1,848 bytes

## Complete source

~~~tex
\usepackage[T1]{fontenc}
\usepackage{iftex}
\ifPDFTeX
  \usepackage[utf8]{inputenc}
\fi
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage[hidelinks]{hyperref}
\usepackage[nameinlink,noabbrev]{cleveref}

\numberwithin{equation}{section}
\raggedbottom

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{question}[theorem]{Question}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\A}{\mathbb A}
\newcommand{\C}{\mathbb C}
\newcommand{\F}{\mathbb F}
\newcommand{\Gm}{\mathbb G_{\mathrm m}}
\newcommand{\Lef}{\mathbb L}
\newcommand{\PP}{\mathbb P}
\newcommand{\Cl}{\operatorname{Cl}}
\newcommand{\Disc}{\operatorname{Disc}}
\newcommand{\Res}{\operatorname{Res}}
\newcommand{\Sing}{\operatorname{Sing}}
\newcommand{\Sym}{\operatorname{Sym}}
\newcommand{\Spec}{\operatorname{Spec}}
\newcommand{\ord}{\operatorname{ord}}
\newcommand{\id}{\operatorname{id}}
\newcommand{\cE}{E_{\mathrm c}}
\newcommand{\cchi}{\chi_{\mathrm c}}
\newcommand{\set}[1]{\left\{#1\right\}}
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\angles}[1]{\left\langle#1\right\rangle}

\crefname{theorem}{theorem}{theorems}
\Crefname{theorem}{Theorem}{Theorems}
\crefname{proposition}{proposition}{propositions}
\Crefname{proposition}{Proposition}{Propositions}
\crefname{lemma}{lemma}{lemmas}
\Crefname{lemma}{Lemma}{Lemmas}
\crefname{corollary}{corollary}{corollaries}
\Crefname{corollary}{Corollary}{Corollaries}
\crefname{question}{question}{questions}
\Crefname{question}{Question}{Questions}
~~~

[Back to the text-source index](../index.md)
