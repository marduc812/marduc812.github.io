# scripts/migration/verify_urls.py
import json
import os
import re
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
POSTS_DIR = os.path.join(REPO_ROOT, "_posts")

FILENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")


def wp_permalink_paths() -> set[str]:
    with open(os.path.join(DATA_DIR, "posts.json")) as f:
        posts = json.load(f)
    paths = set()
    for post in posts:
        # post["link"] e.g. "https://marduc812.com/2021/03/15/example-post/"
        path = post["link"].split("marduc812.com", 1)[1]
        paths.add(path)
    return paths


def local_post_paths() -> set[str]:
    paths = set()
    for filename in os.listdir(POSTS_DIR):
        m = FILENAME_RE.match(filename)
        if not m:
            continue
        year, month, day, slug = m.groups()
        paths.add(f"/{year}/{month}/{day}/{slug}/")
    return paths


def main() -> int:
    wp_paths = wp_permalink_paths()
    local_paths = local_post_paths()
    missing = wp_paths - local_paths
    extra = local_paths - wp_paths
    if missing or extra:
        print(f"MISMATCH: {len(missing)} missing, {len(extra)} extra")
        for p in sorted(missing)[:10]:
            print(f"  missing: {p}")
        for p in sorted(extra)[:10]:
            print(f"  extra: {p}")
        return 1
    print(f"OK: all {len(wp_paths)} permalinks match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
