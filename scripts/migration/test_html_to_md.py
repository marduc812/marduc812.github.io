from html_to_md import (
    extract_uploads_path,
    media_asset_path,
    rewrite_image_srcs,
    rewrite_download_links,
    normalize_enlighter_blocks,
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
