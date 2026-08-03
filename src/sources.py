from dataclasses import dataclass, field

import feedparser
import requests

from src.config import USER_AGENT

REQUEST_TIMEOUT = 20


@dataclass
class Source:
    id: str
    name: str
    feed_url: str
    category_filter: str | None = None  # substring match against entry categories
    headers: dict = field(default_factory=dict)


SOURCES: list[Source] = [
    Source(
        id="robotreport_haptics",
        name="The Robot Report - Haptics",
        feed_url="https://www.therobotreport.com/feed/",
        category_filter="haptic",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="sciencedaily_robotics",
        name="ScienceDaily - Robotics",
        feed_url="https://www.sciencedaily.com/rss/computers_math/robotics.xml",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="ieee_spectrum_robotics",
        name="IEEE Spectrum - Robotics",
        feed_url="https://spectrum.ieee.org/feeds/topic/robotics.rss",
        headers={"User-Agent": USER_AGENT},
    ),
]


def _entry_categories(entry) -> list[str]:
    tags = entry.get("tags", [])
    return [t.get("term", "") for t in tags if t.get("term")]


def _entry_content(entry) -> str:
    content = entry.get("content")
    if content:
        return content[0].get("value", "")
    return entry.get("summary", "")


def fetch_items(source: Source) -> list[dict]:
    resp = requests.get(source.feed_url, headers=source.headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    parsed = feedparser.parse(resp.content)

    items = []
    for entry in parsed.entries:
        categories = _entry_categories(entry)
        if source.category_filter:
            haystack = " ".join(categories).lower()
            if source.category_filter.lower() not in haystack:
                continue
        items.append(
            {
                "source_id": source.id,
                "source_name": source.name,
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", "").strip(),
                "published": entry.get("published", ""),
                "categories": categories,
                "rss_content": _entry_content(entry),
            }
        )
    return items


def fetch_all_new_items() -> list[dict]:
    all_items = []
    for source in SOURCES:
        try:
            all_items.extend(fetch_items(source))
        except Exception as exc:  # noqa: BLE001
            print(f"[sources] failed to fetch {source.name}: {exc}")
    return all_items
