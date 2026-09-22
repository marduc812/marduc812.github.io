from convert_posts import front_matter, post_filename, yaml_escape

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


def test_front_matter_unescapes_html_entities_in_title():
    """WP returns titles as rendered HTML. Left escaped, the layout's Liquid
    `escape` filter escapes the ampersand again and the page shows a literal
    '&amp;#8217;'."""
    post = dict(SAMPLE_POST, title={"rendered": "Scheme is CSP&#8217;s Weakest Link"})
    fm = front_matter(post, MEDIA_BY_ID, CATEGORY_BY_ID, TAG_BY_ID)
    assert 'title: "Scheme is CSP\u2019s Weakest Link"' in fm
    assert "&#8217;" not in fm


def test_yaml_escape_escapes_backslash_before_quote():
    assert yaml_escape(r"C:\Windows") == r"C:\\Windows"
    # The backslash the quote-escape inserts must not itself be doubled.
    assert yaml_escape(r'say "hi"') == r"say \"hi\""
    assert yaml_escape(r'path\ and "quote"') == r"path\\ and \"quote\""
