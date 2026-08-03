import json
import re
from datetime import datetime, timezone

from src.config import GRAPH_PATH

SYMMETRIC_TYPES = {"partnership", "competition"}

_SUFFIX_RE = re.compile(
    r"\b(inc\.?|corp\.?|corporation|ltd\.?|llc|co\.?|company|group|holdings|"
    r"technologies|technology|robotics)\b\.?",
    re.IGNORECASE,
)


def normalize(name: str) -> str:
    n = name.strip().lower()
    n = _SUFFIX_RE.sub("", n)
    n = re.sub(r"[^\w\s]", "", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n or name.strip().lower()


def _empty_graph() -> dict:
    return {"nodes": {}, "edges": []}


def load() -> dict:
    if not GRAPH_PATH.exists():
        return _empty_graph()
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save(graph: dict) -> None:
    with open(GRAPH_PATH, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)


def _upsert_node(graph: dict, name: str, node_type: str, sector: str, now: str) -> str:
    key = normalize(name)
    node = graph["nodes"].get(key)
    if node is None:
        graph["nodes"][key] = {
            "name": name.strip(),
            "type": node_type,
            "sectors": [sector] if sector else [],
            "mentions": 1,
            "first_seen": now,
            "last_seen": now,
        }
    else:
        node["mentions"] += 1
        node["last_seen"] = now
        if sector and sector not in node["sectors"]:
            node["sectors"].append(sector)
    return key


def _find_edge(graph: dict, source_key: str, target_key: str, edge_type: str):
    for edge in graph["edges"]:
        if edge["type"] != edge_type:
            continue
        same_order = edge["source"] == source_key and edge["target"] == target_key
        reverse_order = (
            edge_type in SYMMETRIC_TYPES
            and edge["source"] == target_key
            and edge["target"] == source_key
        )
        if same_order or reverse_order:
            return edge
    return None


def merge(extraction: dict, article: dict) -> dict:
    graph = load()
    now = datetime.now(timezone.utc).isoformat()

    name_to_key = {}
    for ent in extraction.get("entities", []):
        name = ent.get("name", "").strip()
        if not name:
            continue
        key = _upsert_node(graph, name, ent.get("type", "company"), ent.get("sector", ""), now)
        name_to_key[normalize(name)] = key

    evidence = {
        "description": None,
        "article_title": article["title"],
        "article_url": article["link"],
        "source_name": article.get("source_name", ""),
        "published": article.get("published", ""),
        "added_at": now,
    }

    for rel in extraction.get("relationships", []):
        src_name = rel.get("source", "").strip()
        tgt_name = rel.get("target", "").strip()
        edge_type = rel.get("type", "")
        if not src_name or not tgt_name or not edge_type:
            continue

        src_key = normalize(src_name)
        tgt_key = normalize(tgt_name)

        # entities referenced in relationships but not in the entities list
        if src_key not in graph["nodes"]:
            src_key = _upsert_node(graph, src_name, "company", "", now)
        if tgt_key not in graph["nodes"]:
            tgt_key = _upsert_node(graph, tgt_name, "company", "", now)

        rel_evidence = dict(evidence, description=rel.get("description", ""))

        edge = _find_edge(graph, src_key, tgt_key, edge_type)
        if edge is None:
            graph["edges"].append(
                {
                    "source": src_key,
                    "target": tgt_key,
                    "type": edge_type,
                    "evidence": [rel_evidence],
                }
            )
        else:
            urls = {e["article_url"] for e in edge["evidence"]}
            if rel_evidence["article_url"] not in urls:
                edge["evidence"].append(rel_evidence)

    save(graph)
    return graph
