import json
from datetime import datetime, timezone
from pathlib import Path

from src.config import GRAPH_HTML_PATH
from src.graph_store import load

TEMPLATE_PATH = Path(__file__).resolve().parent / "graph_template.html"


def render() -> Path:
    graph = load()
    graph_with_meta = dict(graph, generated_at=datetime.now(timezone.utc).isoformat())

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__GRAPH_DATA__", json.dumps(graph_with_meta, ensure_ascii=False))

    GRAPH_HTML_PATH.write_text(html, encoding="utf-8")
    return GRAPH_HTML_PATH
