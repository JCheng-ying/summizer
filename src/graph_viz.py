import json
import warnings
from datetime import datetime, timezone
from pathlib import Path

from dateutil import parser as dateutil_parser

from src.config import ARTICLES_DIR, GRAPH_HTML_PATH, SEEN_URLS_PATH
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


def _published_sort_key(published: str) -> str:
    """Sources hand us `published` in a mix of formats (RFC 822 with or
    without a time component, RFC 822 with a named timezone like EDT, ISO
    8601 with an offset...). Comparing those strings directly sorts them
    essentially at random. Normalize to a UTC ISO 8601 string, which *is*
    safe to compare lexicographically, and sort on that instead."""
    if not published:
        return ""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # unknown tz abbreviations (e.g. EDT)
            dt = dateutil_parser.parse(published)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except (ValueError, OverflowError):
        return ""


def _load_seen_urls() -> dict:
    if not SEEN_URLS_PATH.exists():
        return {}
    with open(SEEN_URLS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _latest_update_date(graph: dict, seen: dict) -> str:
    """The pipeline doesn't run at a fixed time, and `graph` render() can be
    invoked again later without new data, so "today" for the purposes of the
    UI is defined as the most recent date any timestamp in the data actually
    advanced to -- not wall-clock today. All our own timestamps are UTC
    isoformat, so the date is just the first 10 characters."""
    dates = [info.get("seen_at", "")[:10] for info in seen.values() if info.get("seen_at")]
    dates += [n.get("first_seen", "")[:10] for n in graph.get("nodes", {}).values() if n.get("first_seen")]
    dates += [
        ev.get("added_at", "")[:10]
        for e in graph.get("edges", [])
        for ev in e.get("evidence", [])
        if ev.get("added_at")
    ]
    dates += [s.get("added_at", "")[:10] for s in graph.get("sector_signals", []) if s.get("added_at")]
    dates = [d for d in dates if d]
    return max(dates) if dates else ""


def render() -> Path:
    graph = load()
    articles_by_url = _load_articles_by_url()
    seen = _load_seen_urls()

    latest_date = _latest_update_date(graph, seen)

    for signal in graph.get("sector_signals", []):
        article = articles_by_url.get(signal.get("article_url", ""))
        if article:
            signal["article_body"] = article["body"]
        signal["published_ts"] = _published_sort_key(signal.get("published", ""))
        signal["is_new"] = bool(latest_date) and signal.get("added_at", "")[:10] == latest_date

    for node in graph.get("nodes", {}).values():
        node["is_new"] = bool(latest_date) and node.get("first_seen", "")[:10] == latest_date

    for edge in graph.get("edges", []):
        edge["is_new"] = False
        for ev in edge.get("evidence", []):
            ev["published_ts"] = _published_sort_key(ev.get("published", ""))
            if bool(latest_date) and ev.get("added_at", "")[:10] == latest_date:
                edge["is_new"] = True

    # articles processed in the most recent pipeline run, regardless of
    # whether they produced graph entities/relationships or a sector signal --
    # this is what backs the "今日更新" banner in the UI.
    signals_by_url: dict[str, list[str]] = {}
    for signal in graph.get("sector_signals", []):
        signals_by_url.setdefault(signal.get("article_url", ""), []).append(signal["sector"])

    today_articles = []
    if latest_date:
        for url, info in seen.items():
            if info.get("seen_at", "")[:10] != latest_date:
                continue
            article = articles_by_url.get(url)
            today_articles.append(
                {
                    "title": info.get("title", ""),
                    "url": url,
                    "seen_at": info.get("seen_at", ""),
                    "sectors": signals_by_url.get(url, []),
                    "article_body": article["body"] if article else None,
                }
            )
        today_articles.sort(key=lambda a: a["seen_at"], reverse=True)

    graph_with_meta = dict(
        graph,
        generated_at=datetime.now(timezone.utc).isoformat(),
        latest_update_date=latest_date,
        today_articles=today_articles,
    )

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__GRAPH_DATA__", json.dumps(graph_with_meta, ensure_ascii=False))

    GRAPH_HTML_PATH.write_text(html, encoding="utf-8")
    return GRAPH_HTML_PATH
