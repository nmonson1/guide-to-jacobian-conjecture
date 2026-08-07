---
title: "Unlisted review workspace"
description: "A public but unlisted index of guide pages and their exact-version editorial states."
---

# Unlisted review workspace

This page lets invited readers reach every draft before it enters the guide's
ordinary navigation. The pages are public; the distinction is editorial, not
a privacy boundary.

- **Unread:** the owner has not yet reviewed this version.
- **Needs revision:** the owner has reviewed it and requested changes.
- **Changed since review:** a previously approved file has changed.
- **Approved:** this exact file version is eligible for navigation, search,
  and the sitemap.

Approval here is not mathematical peer review. It means only that the guide's
owner has looked over this exact version and wants it listed.

<label class="review-filter-label" for="review-filter">Filter by title, path, or status</label>
<input id="review-filter" class="review-filter" type="search" placeholder="Try: counterexample or unread" autocomplete="off">

<p id="review-count" class="review-count" aria-live="polite">Showing all draft pages.</p>

<div id="review-pages" aria-describedby="review-count">Loading the review index…</div>

<script src="../assets/javascripts/review-index.js"></script>
