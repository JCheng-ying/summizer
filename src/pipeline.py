import re

from src import fetch_article, graph_store, sources, state

MIN_ARTICLE_TEXT_LENGTH = 300


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip().lower()).strip("-")
    return slug[:80] or "article"


def seed_baseline() -> int:
    """Mark every article currently in the feeds as seen, without analyzing
    them. Run this once on first setup so `new-items` only surfaces articles
    published after that point."""
    items = sources.fetch_all_new_items()
    count = 0
    for item in items:
        if not state.is_seen(item["link"]):
            state.mark_seen(item["link"], item["title"])
            count += 1
    return count


def get_new_items(limit: int) -> list[dict]:
    """Unseen items across all sources, with full article text attached.
    Does NOT mark them as seen -- that happens once each item has actually
    been written up (see mark_seen / merge_graph)."""
    all_items = sources.fetch_all_new_items()
    new_items = [it for it in all_items if not state.is_seen(it["link"])]

    results = []
    for item in new_items[:limit]:
        full_text = fetch_article.get_full_text(item)
        if len(full_text) < MIN_ARTICLE_TEXT_LENGTH:
            state.mark_seen(item["link"], item["title"])  # not enough text, skip permanently
            continue
        results.append(dict(item, full_text=full_text))
    return results


def merge_graph(item: dict, extraction: dict) -> dict:
    graph = graph_store.merge(extraction, item)
    state.mark_seen(item["link"], item["title"])
    return graph
