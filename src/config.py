from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
ARTICLES_DIR = DATA_DIR / "articles"
WEB_DIR = ROOT_DIR / "web"

SEEN_URLS_PATH = DATA_DIR / "seen_urls.json"
GRAPH_PATH = DATA_DIR / "graph.json"
GRAPH_HTML_PATH = WEB_DIR / "graph.html"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

for d in (DATA_DIR, ARTICLES_DIR, WEB_DIR):
    d.mkdir(parents=True, exist_ok=True)
