import json
import os
import time
import urllib.error
import urllib.request

BASE = "https://marduc812.com/wp-json/wp/v2"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# Install a custom opener that sends User-Agent to avoid 403 Forbidden from servers
# that reject requests without one. This is transparent to mocked tests which patch
# urllib.request.urlopen directly.
_handler = urllib.request.HTTPSHandler()
_opener = urllib.request.build_opener(_handler)
_opener.addheaders = [("User-Agent", "Mozilla/5.0 (compatible; WordPress-Data-Migration)")]
_urlopen_impl = urllib.request.urlopen

def urlopen(url, *args, **kwargs):
    """Wrapper around urlopen that adds User-Agent header."""
    if not isinstance(url, urllib.request.Request):
        url = urllib.request.Request(url)
    if not url.has_header("User-Agent"):
        url.add_unredirected_header("User-Agent", "Mozilla/5.0 (compatible; WordPress-Data-Migration)")
    return _urlopen_impl(url, *args, **kwargs)

# Replace urllib.request.urlopen with our wrapper
urllib.request.urlopen = urlopen


def fetch_all(endpoint: str, per_page: int = 99) -> list[dict]:
    """Fetch every item from a paginated WP REST API collection endpoint.
    Stops when the API returns HTTP 400 (rest_post_invalid_page_number),
    which is WordPress's normal way of saying "no more pages" once you
    page past the end, not an error condition."""
    items = []
    page = 1
    while True:
        url = f"{BASE}/{endpoint}?page={page}&per_page={per_page}"
        try:
            with urllib.request.urlopen(url) as resp:
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


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    for endpoint, filename in [
        ("posts", "posts.json"),
        ("media", "media.json"),
        ("categories", "categories.json"),
        ("tags", "tags.json"),
    ]:
        items = fetch_all(endpoint)
        with open(os.path.join(DATA_DIR, filename), "w") as f:
            json.dump(items, f)
        print(f"{endpoint}: {len(items)} items")


if __name__ == "__main__":
    main()
