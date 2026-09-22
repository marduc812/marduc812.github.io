from convert_posts import front_matter, post_filename

SAMPLE_POST = {
    "date": "2021-03-15T10:30:00",
    "slug": "example-post",
    "title": {"rendered": "An \"Example\" Post"},
    "categories": [3],
    "tags": [5, 9],
    "featured_media": 42,
}

MEDIA_BY_ID = {
    42: {"source_url": "https://marduc812.com/wp-content/uploads/2021/03/cover.jpg"}
}
CATEGORY_BY_ID = {3: "Security"}
TAG_BY_ID = {5: "android", 9: "rooting"}


def test_post_filename():
    assert post_filename(SAMPLE_POST) == "2021-03-15-example-post.md"


def test_front_matter_contains_expected_fields():
    fm = front_matter(SAMPLE_POST, MEDIA_BY_ID, CATEGORY_BY_ID, TAG_BY_ID)
    assert 'title: "An \\"Example\\" Post"' in fm
    assert "date: 2021-03-15T10:30:00" in fm
    assert 'categories: ["Security"]' in fm
    assert 'tags: ["android", "rooting"]' in fm
    assert "image: /assets/uploads/2021/03/cover.jpg" in fm
    assert fm.startswith("---\n")
    assert fm.endswith("---\n\n")  # ends with blank line after closing ---


def test_front_matter_skips_missing_featured_media():
    post = dict(SAMPLE_POST, featured_media=999)
    fm = front_matter(post, MEDIA_BY_ID, CATEGORY_BY_ID, TAG_BY_ID)
    assert "image:" not in fm
