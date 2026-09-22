# scripts/migration/verify_urls.py
import json
import os
import re
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
SITE_DIR = os.path.join(REPO_ROOT, "_site")

# /_site/YYYY/MM/DD/slug/index.html - the shape _config.yml's
# permalink: /:year/:month/:day/:title/ produces.
BUILT_PATH_RE = re.compile(r"^/(\d{4})/(\d{2})/(\d{2})/([^/]+)/$")


def wp_permalink_paths() -> set[str]:
    with open(os.path.join(DATA_DIR, "posts.json")) as f:
        posts = json.load(f)
    paths = set()
    for post in posts:
        # post["link"] e.g. "https://marduc812.com/2021/03/15/example-post/"
        path = post["link"].split("marduc812.com", 1)[1]
        paths.add(path)
    return paths


def built_post_paths(site_dir: str = SITE_DIR) -> set[str]:
    """Walk the BUILT site for dated post URLs.

    Deliberately reads _site/ and not _posts/: a source filename only says
    what date the post claims, while the built path is what Jekyll actually
    resolved that date to (and therefore what the live URL will be). Checking
    filenames hides date-parsing bugs such as timezone-shifted permalinks.
    """
    if not os.path.isdir(site_dir):
        raise FileNotFoundError(
            f"{site_dir} not found - run `bundle exec jekyll build` before verifying"
        )
    paths = set()
    for dirpath, _dirnames, filenames in os.walk(site_dir):
        if "index.html" not in filenames:
            continue
        rel = os.path.relpath(dirpath, site_dir)
        if rel == ".":
            continue
        candidate = "/" + rel.replace(os.sep, "/") + "/"
        if BUILT_PATH_RE.match(candidate):
            paths.add(candidate)
    return paths


def main() -> int:
    wp_paths = wp_permalink_paths()
    try:
        built_paths = built_post_paths()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 2
    missing = wp_paths - built_paths
    extra = built_paths - wp_paths
    if missing or extra:
        print(f"MISMATCH: {len(missing)} missing, {len(extra)} extra")
        for p in sorted(missing)[:10]:
            print(f"  missing: {p}")
        for p in sorted(extra)[:10]:
            print(f"  extra: {p}")
        return 1
    print(f"OK: all {len(wp_paths)} permalinks match the built site in {SITE_DIR}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
