(function () {
  "use strict";

  const target = document.getElementById("review-pages");
  const filter = document.getElementById("review-filter");
  const count = document.getElementById("review-count");
  if (!target || !filter || !count) return;

  const labels = {
    unread: "Unread",
    needs_revision: "Needs revision",
    changed_since_review: "Changed since review",
    approved: "Approved",
  };

  function render(pages) {
    const query = filter.value.trim().toLowerCase();
    target.replaceChildren();
    const visible = pages.filter((page) =>
      page.path !== "review/index.md" &&
      `${page.title} ${page.path} ${page.effective_status}`.toLowerCase().includes(query)
    );

    const list = document.createElement("ul");
    list.className = "review-list";
    for (const page of visible) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `../${page.url}`;
      link.textContent = page.title;
      const path = document.createElement("code");
      path.textContent = page.path;
      const status = document.createElement("span");
      status.className = `review-status review-status--${page.effective_status}`;
      status.textContent = labels[page.effective_status] || page.effective_status;
      item.append(link, path, status);
      list.append(item);
    }
    if (visible.length) {
      target.append(list);
      count.textContent = `${visible.length} ${visible.length === 1 ? "page" : "pages"} shown.`;
    } else {
      const empty = document.createElement("p");
      empty.textContent = "No pages match that filter.";
      target.append(empty);
      count.textContent = "No pages shown.";
    }
  }

  fetch("status.json")
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((payload) => {
      filter.addEventListener("input", () => render(payload.pages));
      render(payload.pages);
    })
    .catch(() => {
      count.textContent = "The live filter is unavailable; the complete static list remains below.";
    });
})();
