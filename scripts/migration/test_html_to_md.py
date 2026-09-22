from html_to_md import (
    brush_language,
    extract_uploads_path,
    html_to_markdown,
    media_asset_path,
    rewrite_image_srcs,
    rewrite_download_links,
    normalize_enlighter_blocks,
    normalize_syntaxhighlighter_blocks,
    convert_post_content,
    unwrap_photon_url,
)


def test_extract_uploads_path_bare_url():
    url = "https://marduc812.com/wp-content/uploads/2020/05/photo.jpg"
    assert extract_uploads_path(url) == "/assets/uploads/2020/05/photo.jpg"


def test_extract_uploads_path_photon_proxied():
    url = "https://i0.wp.com/marduc812.com/wp-content/uploads/2020/05/photo.jpg?resize=300%2C200&ssl=1"
    assert extract_uploads_path(url) == "/assets/uploads/2020/05/photo.jpg"


def test_extract_uploads_path_no_match():
    assert extract_uploads_path("https://example.com/foo.jpg") is None


def test_media_asset_path():
    media_obj = {"source_url": "https://marduc812.com/wp-content/uploads/2019/01/cover.png"}
    assert media_asset_path(media_obj) == "/assets/uploads/2019/01/cover.png"


def test_rewrite_image_srcs_resolves_by_wp_image_id():
    media_by_id = {
        42: {"source_url": "https://marduc812.com/wp-content/uploads/2021/03/original.png"}
    }
    html = (
        '<img class="wp-image-42 size-large" '
        'src="https://i0.wp.com/marduc812.com/wp-content/uploads/2021/03/original.png?resize=300%2C200&ssl=1" '
        'srcset="a.jpg 300w, b.jpg 600w" sizes="(max-width: 300px) 100vw">'
    )
    result = rewrite_image_srcs(html, media_by_id)
    assert 'src="/assets/uploads/2021/03/original.png"' in result
    assert "srcset" not in result
    assert "sizes" not in result


def test_rewrite_image_srcs_falls_back_to_path_parsing():
    html = (
        '<img class="alignnone" '
        'src="https://i0.wp.com/marduc812.com/wp-content/uploads/2018/07/untagged.jpg?ssl=1">'
    )
    result = rewrite_image_srcs(html, media_by_id={})
    assert 'src="/assets/uploads/2018/07/untagged.jpg"' in result


def test_unwrap_photon_url_external_host():
    url = "https://i0.wp.com/lh5.googleusercontent.com/foo/bar/Screenshot.png?w=1200&ssl=1"
    assert unwrap_photon_url(url) == "https://lh5.googleusercontent.com/foo/bar/Screenshot.png"


def test_unwrap_photon_url_not_photon():
    assert unwrap_photon_url("https://example.com/foo.jpg") is None


def test_rewrite_image_srcs_unwraps_photon_for_external_host():
    html = (
        '<img class="alignnone" '
        'src="https://i0.wp.com/i.imgur.com/A8Ts3kA.png?w=1200">'
    )
    result = rewrite_image_srcs(html, media_by_id={})
    assert 'src="https://i.imgur.com/A8Ts3kA.png"' in result
    assert "i0.wp.com" not in result


def test_rewrite_download_links_rewrites_href_and_video_src():
    html = (
        '<a href="https://marduc812.com/wp-content/uploads/2016/02/tool.zip">download</a>'
        '<video src="https://marduc812.com/wp-content/uploads/2016/03/demo.mp4"></video>'
    )
    result = rewrite_download_links(html)
    assert '/assets/uploads/2016/02/tool.zip' in result
    assert '/assets/uploads/2016/03/demo.mp4' in result


def test_normalize_enlighter_blocks():
    html = (
        '<pre class="EnlighterJSRAW" data-enlighter-language="js">'
        'console.log("hi");'
        '</pre>'
    )
    result = normalize_enlighter_blocks(html)
    assert 'class="language-js"' in result
    assert 'console.log("hi");' in result
    assert "EnlighterJSRAW" not in result


def test_brush_language_parses_and_maps():
    assert brush_language("brush: bash; title: ; notranslate") == "bash"
    assert brush_language("brush: jscript; title: ; notranslate") == "js"
    assert brush_language("brush: plain; title: ; notranslate") == "text"
    # BeautifulSoup splits class on whitespace, so this is the shape
    # pre.get("class") actually hands us.
    assert brush_language(["brush:", "xml;", "title:", ";", "notranslate"]) == "xml"
    assert brush_language("EnlighterJSRAW") is None
    assert brush_language(["EnlighterJSRAW"]) is None
    assert brush_language(None) is None


def test_normalize_syntaxhighlighter_blocks():
    html = (
        '<pre class="brush: bash; title: ; notranslate" title="">\n'
        "brew install subliminal\n"
        "</pre>"
    )
    result = normalize_syntaxhighlighter_blocks(html)
    assert 'class="language-bash"' in result
    assert "brew install subliminal" in result
    assert "brush:" not in result


def test_normalize_syntaxhighlighter_blocks_unwraps_stray_outer_pre():
    """Two posts wrap the real brush <pre> in a second bare <pre>, which
    otherwise nests one fenced block inside another."""
    html = (
        '<pre><pre class="brush: plain; title: ; notranslate">\nnpm -v\n</pre>'
        "<h3>More info</h3></pre>"
    )
    md = html_to_markdown(normalize_syntaxhighlighter_blocks(html))
    assert md.count("```") == 2
    assert "```text" in md
    assert "### More info" in md


def test_legacy_syntaxhighlighter_block_gets_language_fence():
    html = '<pre class="brush: java; title: ; notranslate">int x = 1;</pre>'
    md = convert_post_content(html, media_by_id={})
    assert "```java" in md
    assert "int x = 1;" in md


def test_iframe_embed_survives_as_raw_html():
    """Stock markdownify has no iframe converter and drops the embed."""
    html = (
        '<div class="wp-block-embed__wrapper">'
        '<iframe src="https://player.vimeo.com/video/70748579" width="640" '
        'height="360" allowfullscreen></iframe>'
        "</div>"
    )
    md = convert_post_content(html, media_by_id={})
    assert "<iframe" in md
    assert "https://player.vimeo.com/video/70748579" in md
    # kramdown only passes raw HTML through when it's a standalone block.
    assert "\n\n<iframe" in "\n\n" + md


def test_video_renders_as_player_not_empty_link():
    """WordPress emits attribute-only <video controls src=...></video> with
    no child nodes; markdownify turned that into an invisible '[](src)'."""
    html = (
        '<figure><video controls '
        'src="https://marduc812.com/wp-content/uploads/2023/12/demo.mov">'
        "</video></figure>"
    )
    md = convert_post_content(html, media_by_id={})
    assert "<video" in md
    assert "controls" in md
    assert "/assets/uploads/2023/12/demo.mov" in md
    assert "[](" not in md


def test_gist_script_embed_is_kept_but_other_scripts_dropped():
    gist = '<p><script src="https://gist.github.com/marduc812/42dc.js"></script></p>'
    assert "gist.github.com/marduc812/42dc.js" in convert_post_content(gist, {})
    widget = '<p><script async src="https://platform.twitter.com/widgets.js"></script></p>'
    assert "<script" not in convert_post_content(widget, {})


def test_heading_id_is_preserved_as_kramdown_ial():
    """An in-document link only resolves if the heading keeps its source id;
    kramdown otherwise invents a different one from the heading text."""
    html = (
        '<h3 id="#crawling">Crawling / File Enumeration</h3>'
        '<p><a href="#crawling">see above</a></p>'
    )
    md = convert_post_content(html, media_by_id={})
    assert "### Crawling / File Enumeration {#crawling}" in md


def test_heading_without_id_is_unchanged():
    md = convert_post_content("<h3>Plain Heading</h3>", media_by_id={})
    assert md.strip() == "### Plain Heading"


def test_convert_post_content_end_to_end():
    media_by_id = {
        7: {"source_url": "https://marduc812.com/wp-content/uploads/2022/01/pic.jpg"}
    }
    html = (
        "<p>Intro paragraph.</p>"
        '<img class="wp-image-7" src="https://i0.wp.com/marduc812.com/wp-content/uploads/2022/01/pic.jpg?resize=300%2C200&ssl=1">'
        '<pre class="EnlighterJSRAW" data-enlighter-language="python">print(1)</pre>'
    )
    md = convert_post_content(html, media_by_id)
    assert "Intro paragraph." in md
    assert "/assets/uploads/2022/01/pic.jpg" in md
    assert "```python" in md
    assert "print(1)" in md
