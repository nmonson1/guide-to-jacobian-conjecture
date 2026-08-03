"""Proof-carrying queue validation."""
from __future__ import annotations

from typing import Any

from .common import require


def validate_queue(manifest: dict[str, Any]) -> None:
    queue = manifest["queue"]
    nodes, edges = queue["nodes"], queue["edges"]
    node_ids = [node["id"] for node in nodes]
    edge_ids = [edge["id"] for edge in edges]
    require(len(node_ids) == len(set(node_ids)), "duplicate queue node ID")
    require(len(edge_ids) == len(set(edge_ids)), "duplicate queue edge ID")
    node_map = {node["id"]: node for node in nodes}
    edge_map: dict[tuple[str, str], list[dict[str, Any]]] = {}
    adjacency: dict[str, list[str]] = {node_id: [] for node_id in node_ids}
    for edge in edges:
        require(edge["from"] in node_map, f"edge {edge['id']} has unknown parent")
        require(edge["to"] in node_map, f"edge {edge['id']} has unknown child")
        require(edge["from"] != edge["to"], f"edge {edge['id']} is a self-loop")
        edge_map.setdefault((edge["from"], edge["to"]), []).append(edge)
        adjacency[edge["from"]].append(edge["to"])

    state = {node_id: 0 for node_id in node_ids}
    def visit(node_id: str) -> None:
        require(state[node_id] != 1, f"cycle detected at {node_id}")
        if state[node_id] == 2:
            return
        state[node_id] = 1
        for child in adjacency[node_id]:
            visit(child)
        state[node_id] = 2
    for node_id in node_ids:
        visit(node_id)

    cover_ids: set[str] = set()
    for group in queue["cover_groups"]:
        require(group["id"] not in cover_ids, f"duplicate cover group {group['id']}")
        cover_ids.add(group["id"])
        require(group["parent"] in node_map, f"unknown cover parent {group['parent']}")
        require(len(group["children"]) >= 2, f"cover group {group['id']} is not a split")
        for child in group["children"]:
            candidates = edge_map.get((group["parent"], child), [])
            require(candidates, f"cover group {group['id']} lacks edge to {child}")
            require(any(edge.get("cover_group") == group["id"] and edge["covering"]
                        for edge in candidates), f"cover group {group['id']} edge to {child} is not covering")

    roots = {"truncated": "L8-T-ROOT", "full": "L8-F-ROOT"}
    closure_paths: dict[str, list[list[str]]] = {}
    for root_name in ("truncated", "full"):
        closure = queue["closure"][root_name]
        paths = [closure["path"]] if "path" in closure else closure["paths"]
        closure_paths[root_name] = paths
        for path in paths:
            require(path and path[0] == roots[root_name], f"bad closure root for {root_name}")
            for parent, child in zip(path, path[1:]):
                candidates = edge_map.get((parent, child), [])
                require(candidates, f"missing closure edge {parent}->{child}")
                require(any(edge["covering"] for edge in candidates),
                        f"closure uses noncovering edge {parent}->{child}")
            require(node_map[path[-1]]["status"].startswith("terminal_empty"),
                    f"closure path ends at nonempty node {path[-1]}")

    full_paths = closure_paths["full"]
    require(len(full_paths) == 2, "full closure must contain exactly two split-child paths")
    split_parent = "L8-F-SQUARE-RED"
    observed: set[str] = set()
    for path in full_paths:
        require(split_parent in path, f"full closure path omits {split_parent}")
        index = path.index(split_parent)
        require(index + 1 < len(path), "full closure stops before a split child")
        observed.add(path[index + 1])
        require("L8-ADJ-STORED" not in path, "full closure improperly uses adjacent terminal")
    require(observed == {"L8-F-T11-ZERO", "L8-F-T11-OPEN"},
            f"full closure does not cover both split children: {sorted(observed)}")
    require(queue["closure"]["full"]["noncovering_edges_used"] == [],
            "full closure records a noncovering edge")
    candidate = next(edge for edge in edges if edge["id"] == "E-F-ADJ-CANDIDATE")
    require(not candidate["covering"], "adjacent candidate was promoted without a theorem")
    require(node_map["L8-ADJ-STORED"]["status"] == "terminal_empty_unattached",
            "adjacent terminal boundary changed")

    certificate_ids = {certificate["id"] for certificate in manifest["terminal_certificates"]}
    for node in nodes:
        if node["status"].startswith("terminal_empty"):
            require(node.get("certificate") in certificate_ids,
                    f"terminal node {node['id']} lacks a certificate")
