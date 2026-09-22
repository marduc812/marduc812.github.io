import html
import json
import os

from html_to_md import convert_post_content, media_asset_path

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
POSTS_DIR = os.path.join(REPO_ROOT, "_posts")


def load_json(name):
    with open(os.path.join(DATA_DIR, name)) as f:
        return json.load(f)


def build_id_maps():
    media_by_id = {m["id"]: m for m in load_json("media.json")}
    category_by_id = {c["id"]: c["name"] for c in load_json("categories.json")}
    tag_by_id = {t["id"]: t["name"] for t in load_json("tags.json")}
    return media_by_id, category_by_id, tag_by_id


def yaml_escape(value: str) -> str:
    # Backslashes first: escaping quotes inserts backslashes of its own,
    # and doing it the other way round would double-escape those.
    return value.replace("\\", "\\\\").replace('"', '\\"')


def front_matter(post, media_by_id, category_by_id, tag_by_id) -> str:
    # WP returns the title as rendered HTML, so it carries entities like
    # &#8217; for a curly apostrophe. Left as-is they reach the layout's
    # Liquid `escape` filter, which escapes the ampersand again and puts a
    # literal "&amp;#8217;" on the page.
    title = yaml_escape(html.unescape(post["title"]["rendered"]))
    lines = [
        "---",
        f'title: "{title}"',
        f"date: {post['date']}",
    ]
    categories = [category_by_id[c] for c in post["categories"] if c in category_by_id]
    if categories:
        lines.append("categories: [" + ", ".join(f'"{yaml_escape(c)}"' for c in categories) + "]")
    tags = [tag_by_id[t] for t in post["tags"] if t in tag_by_id]
    if tags:
        lines.append("tags: [" + ", ".join(f'"{yaml_escape(t)}"' for t in tags) + "]")
    featured_id = post.get("featured_media")
    if featured_id and featured_id in media_by_id:
        lines.append(f"image: {media_asset_path(media_by_id[featured_id])}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def post_filename(post) -> str:
    date_part = post["date"][:10]  # "YYYY-MM-DD"
    return f"{date_part}-{post['slug']}.md"


def convert_all_posts() -> int:
    posts = load_json("posts.json")
    media_by_id, category_by_id, tag_by_id = build_id_maps()
    os.makedirs(POSTS_DIR, exist_ok=True)

    for post in posts:
        fm = front_matter(post, media_by_id, category_by_id, tag_by_id)
        body = convert_post_content(post["content"]["rendered"], media_by_id)
        with open(os.path.join(POSTS_DIR, post_filename(post)), "w") as f:
            f.write(fm + body)

    return len(posts)


if __name__ == "__main__":
    count = convert_all_posts()
    print(f"wrote {count} posts to {POSTS_DIR}/")
