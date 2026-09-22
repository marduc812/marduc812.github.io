import json
import os
import urllib.request

from html_to_md import media_asset_path

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
USER_AGENT = "Mozilla/5.0 (compatible; WordPress-Data-Migration)"


def download_all_media() -> tuple[int, int]:
    with open(os.path.join(DATA_DIR, "media.json")) as f:
        media_items = json.load(f)

    downloaded = 0
    for item in media_items:
        rel_path = media_asset_path(item)  # "/assets/uploads/YYYY/MM/file.ext"
        local_path = os.path.join(REPO_ROOT, rel_path.lstrip("/"))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        if os.path.exists(local_path):
            continue

        # Use Request with User-Agent header instead of urlretrieve
        # to avoid server rejecting bare urllib requests
        request = urllib.request.Request(
            item["source_url"],
            headers={"User-Agent": USER_AGENT}
        )
        with urllib.request.urlopen(request) as resp:
            with open(local_path, "wb") as f:
                f.write(resp.read())
        downloaded += 1

    return downloaded, len(media_items)


if __name__ == "__main__":
    downloaded, total = download_all_media()
    print(f"downloaded {downloaded} new files, {total} total in media library")
