import json
import re
from datetime import datetime, timezone

from src.config import GRAPH_PATH

SYMMETRIC_TYPES = {"partnership", "competition"}

# the six sectors the user tracks for investment purposes -- entities and
# article signals should tag onto these where relevant, not free-text sectors
CANONICAL_SECTORS = [
    "机器人板块",
    "AI板块",
    "能源板块",
    "量子计算板块",
    "太空经济板块",
    "edge AI板块",
]

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
    return {"nodes": {}, "edges": [], "sector_signals": []}


def load() -> dict:
    if not GRAPH_PATH.exists():
        return _empty_graph()
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        graph = json.load(f)
    graph.setdefault("sector_signals", [])
    return graph


def save(graph: dict) -> None:
    with open(GRAPH_PATH, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)


def _upsert_node(
    graph: dict,
    name: str,
    node_type: str,
    sector: str,
    now: str,
    sector_tags: list | None = None,
    hot: str | None = None,
    ticker: str | None = None,
) -> str:
    key = normalize(name)
    node = graph["nodes"].get(key)
    if node is None:
        node = {
            "name": name.strip(),
            "type": node_type,
            "sectors": [sector] if sector else [],
            "sector_tags": [],
            "hot": None,
            "ticker": None,
            "mentions": 1,
            "first_seen": now,
            "last_seen": now,
        }
        graph["nodes"][key] = node
    else:
        node["mentions"] += 1
        node["last_seen"] = now
        node.setdefault("sector_tags", [])
        if sector and sector not in node["sectors"]:
            node["sectors"].append(sector)

    for tag in sector_tags or []:
        if tag in CANONICAL_SECTORS and tag not in node["sector_tags"]:
            node["sector_tags"].append(tag)
    if hot in ("hot", "cold"):
        node["hot"] = hot
    if ticker:
        node["ticker"] = ticker

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

    for ent in extraction.get("entities", []):
        name = ent.get("name", "").strip()
        if not name:
            continue
        _upsert_node(
            graph,
            name,
            ent.get("type", "company"),
            ent.get("sector", ""),
            now,
            sector_tags=ent.get("sector_tags"),
            hot=ent.get("hot"),
            ticker=ent.get("ticker"),
        )

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

        rel_evidence = dict(
            evidence,
            description=rel.get("description", ""),
            article_title=rel.get("source_title") or evidence["article_title"],
            article_url=rel.get("source_url") or evidence["article_url"],
            source_name=rel.get("source_name") or evidence["source_name"],
            published=rel.get("published") or evidence["published"],
        )

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


def record_signal(sector: str, description: str, article: dict) -> dict:
    """Record that an article is a bullish/bearish signal for one of the six
    tracked sectors, independent of any specific company relationship."""
    graph = load()
    now = datetime.now(timezone.utc).isoformat()

    existing = [
        s
        for s in graph["sector_signals"]
        if s["sector"] == sector and s["article_url"] == article["link"]
    ]
    if not existing:
        graph["sector_signals"].append(
            {
                "sector": sector,
                "description": description,
                "article_title": article["title"],
                "article_url": article["link"],
                "source_name": article.get("source_name", ""),
                "published": article.get("published", ""),
                "added_at": now,
            }
        )
    save(graph)
    return graph
