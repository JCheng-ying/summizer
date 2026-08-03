import re

import requests
import trafilatura

from src.config import USER_AGENT

MIN_TEXT_LENGTH = 300
REQUEST_TIMEOUT = 20


def _strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_full_text(item: dict) -> str:
    """Best-effort full article text. Falls back to the RSS content if the
    live page can't be fetched or extracted (paywall, bot-blocking, etc.)."""
    url = item["link"]
    try:
        resp = requests.get(
            url, headers={"User-Agent": USER_AGENT}, timeout=REQUEST_TIMEOUT
        )
        resp.raise_for_status()
        extracted = trafilatura.extract(
            resp.text,
            url=url,
            include_comments=False,
            include_tables=True,
            favor_recall=True,
        )
        if extracted and len(extracted) >= MIN_TEXT_LENGTH:
            return extracted.strip()
    except Exception as exc:  # noqa: BLE001
        print(f"[fetch_article] live fetch failed for {url}: {exc}")

    fallback = _strip_html(item.get("rss_content", ""))
    return fallback
