import json
from datetime import datetime, timezone
from pathlib import Path

from src.config import ARTICLES_DIR, GRAPH_HTML_PATH
from src.graph_store import load

TEMPLATE_PATH = Path(__file__).resolve().parent / "graph_template.html"


def _load_articles_by_url() -> dict:
    """Parse data/articles/*.md into a {url: {title, body}} lookup so the
    viz can embed the full generated analysis alongside each sector signal,
    not just a link out to the original news URL."""
    articles = {}
    for path in sorted(ARTICLES_DIR.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) < 2:
            continue
        title = lines[0].lstrip("#").strip()
        url = ""
        body_start = 1
        for i in range(1, min(len(lines), 4)):
            candidate = lines[i].strip()
            if candidate.startswith("http"):
                url = candidate
                body_start = i + 1
                break
        if not url:
            continue
        body = "\n".join(lines[body_start:]).strip()
        articles[url] = {"title": title, "body": body}
    return articles


def render() -> Path:
    graph = load()
    articles_by_url = _load_articles_by_url()

    for signal in graph.get("sector_signals", []):
        article = articles_by_url.get(signal.get("article_url", ""))
        if article:
            signal["article_body"] = article["body"]

    graph_with_meta = dict(graph, generated_at=datetime.now(timezone.utc).isoformat())

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__GRAPH_DATA__", json.dumps(graph_with_meta, ensure_ascii=False))

    GRAPH_HTML_PATH.write_text(html, encoding="utf-8")
    return GRAPH_HTML_PATH
