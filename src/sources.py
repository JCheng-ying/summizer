import re
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
    kind: str = "rss"  # "rss" or "html_listing"
    category_filter: str | None = None  # substring match against entry categories (rss only)
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
    Source(
        id="importai_substack",
        name="Import AI (Substack)",
        feed_url="https://importai.substack.com/feed",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="deeplearning_the_batch_research",
        name="DeepLearning.AI - The Batch (Research)",
        feed_url="https://www.deeplearning.ai/the-batch/tag/research/",
        kind="html_listing",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="spacenews",
        name="SpaceNews",
        feed_url="https://spacenews.com/feed/",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="nasaspaceflight",
        name="NASASpaceFlight.com",
        feed_url="https://www.nasaspaceflight.com/feed/",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="the_quantum_insider",
        name="The Quantum Insider",
        feed_url="https://thequantuminsider.com/feed/",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="datacenterdynamics",
        name="DataCenterDynamics",
        feed_url="https://www.datacenterdynamics.com/en/rss/",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="techcrunch_ai",
        name="TechCrunch - AI",
        feed_url="https://techcrunch.com/category/artificial-intelligence/feed/",
        headers={"User-Agent": USER_AGENT},
    ),
    Source(
        id="siliconangle",
        name="SiliconANGLE",
        feed_url="https://siliconangle.com/feed/",
        headers={"User-Agent": USER_AGENT},
    ),
]

# path segments on a listing page that are never individual articles
_HTML_LISTING_EXCLUDE_SLUGS = {"about", "search", "tag", "contact", "issue"}


def _entry_categories(entry) -> list[str]:
    tags = entry.get("tags", [])
    return [t.get("term", "") for t in tags if t.get("term")]


def _entry_content(entry) -> str:
    content = entry.get("content")
    if content:
        return content[0].get("value", "")
    return entry.get("summary", "")


def _fetch_rss_items(source: Source) -> list[dict]:
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


def _extract_article_links(html: str, base_url: str) -> list[str]:
    from urllib.parse import urljoin

    paths = set(re.findall(r'href="(/the-batch/[a-z0-9][a-z0-9-]*)/?"', html, re.IGNORECASE))
    links = []
    for path in paths:
        slug = path.rsplit("/", 1)[-1]
        if slug in _HTML_LISTING_EXCLUDE_SLUGS:
            continue
        links.append(urljoin(base_url, path + "/"))
    return links


def _fetch_page_metadata(url: str, headers: dict) -> tuple[str, str]:
    resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    html = resp.text
    title_match = re.search(r"<title>([^<]*)</title>", html)
    title = title_match.group(1).split("|")[0].strip() if title_match else url
    pub_match = re.search(r'property="article:published_time" content="([^"]*)"', html)
    published = pub_match.group(1) if pub_match else ""
    return title, published


def _fetch_html_listing_items(source: Source) -> list[dict]:
    resp = requests.get(source.feed_url, headers=source.headers, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    links = _extract_article_links(resp.text, source.feed_url)

    items = []
    for link in links:
        try:
            title, published = _fetch_page_metadata(link, source.headers)
        except Exception as exc:  # noqa: BLE001
            print(f"[sources] failed to fetch metadata for {link}: {exc}")
            continue
        items.append(
            {
                "source_id": source.id,
                "source_name": source.name,
                "title": title,
                "link": link,
                "published": published,
                "categories": [],
                "rss_content": "",
            }
        )
    return items


def fetch_items(source: Source) -> list[dict]:
    if source.kind == "html_listing":
        return _fetch_html_listing_items(source)
    return _fetch_rss_items(source)


def fetch_all_new_items() -> list[dict]:
    all_items = []
    for source in SOURCES:
        try:
            all_items.extend(fetch_items(source))
        except Exception as exc:  # noqa: BLE001
            print(f"[sources] failed to fetch {source.name}: {exc}")
    return all_items
