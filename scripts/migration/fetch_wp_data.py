import json
import os
import time
import urllib.error
import urllib.request

BASE = "https://marduc812.com/wp-json/wp/v2"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
USER_AGENT = "Mozilla/5.0 (compatible; WordPress-Data-Migration)"


def fetch_all(endpoint: str, per_page: int = 100) -> list[dict]:
    """Fetch every item from a paginated WP REST API collection endpoint.
    Stops when the API returns HTTP 400 (rest_post_invalid_page_number),
    which is WordPress's normal way of saying "no more pages" once you
    page past the end, not an error condition."""
    items = []
    page = 1
    while True:
        url = f"{BASE}/{endpoint}?per_page={per_page}&page={page}"
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request) as resp:
                batch = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 400:
                break
            raise
        if not batch:
            break
        items.extend(batch)
        page += 1
        time.sleep(0.2)
    return items


def save_items(path: str, items: list[dict], label: str) -> None:
    """Write items to path, unless the fetch came back empty and an
    existing file already holds real data — a transient API hiccup (rate
    limit, timeout, WP returning a 200 with no body) must not truncate a
    good local copy to zero items."""
    if not items and os.path.exists(path) and os.path.getsize(path) > 2:
        print(f"{label}: fetch returned 0 items, keeping existing {os.path.basename(path)}")
        return
    with open(path, "w") as f:
        json.dump(items, f)
    print(f"{label}: {len(items)} items")


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    for endpoint, filename in [
        ("posts", "posts.json"),
        ("media", "media.json"),
        ("categories", "categories.json"),
        ("tags", "tags.json"),
    ]:
        items = fetch_all(endpoint)
        save_items(os.path.join(DATA_DIR, filename), items, endpoint)


if __name__ == "__main__":
    main()
