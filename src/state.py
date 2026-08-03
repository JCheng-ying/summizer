import json
from datetime import datetime, timezone

from src.config import SEEN_URLS_PATH


def _load() -> dict:
    if not SEEN_URLS_PATH.exists():
        return {}
    with open(SEEN_URLS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data: dict) -> None:
    with open(SEEN_URLS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def is_seen(url: str) -> bool:
    return url in _load()


def mark_seen(url: str, title: str = "") -> None:
    data = _load()
    data[url] = {
        "title": title,
        "seen_at": datetime.now(timezone.utc).isoformat(),
    }
    _save(data)
