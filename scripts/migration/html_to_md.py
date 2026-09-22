import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

UPLOADS_RE = re.compile(r'/wp-content/uploads/(\d{4}/\d{2}/[^\s"\'<>)?]+)')
PHOTON_HOST_RE = re.compile(r'^https?://i[0-2]\.wp\.com/(.+)$')
PHOTON_QUERY_KEYS = {"w", "h", "resize", "ssl", "quality", "crop", "fit", "zoom", "strip"}


def extract_uploads_path(url: str) -> str | None:
    """Extract the '/wp-content/uploads/YYYY/MM/file.ext' segment from any
    URL, whether it's a bare marduc812.com URL or a Jetpack Photon-proxied
    i0.wp.com URL - the segment and its query-string boundary are the same
    in both forms, only the host and query string differ."""
    match = UPLOADS_RE.search(url)
    if not match:
        return None
    return f"/assets/uploads/{match.group(1)}"


def media_asset_path(media_obj: dict) -> str:
    """Given a WP REST API media object (has 'source_url'), return its
    rewritten local asset path."""
    path = extract_uploads_path(media_obj["source_url"])
    if path is None:
        raise ValueError(f"no uploads path in {media_obj['source_url']!r}")
    return path


def unwrap_photon_url(url: str) -> str | None:
    """Given a Jetpack Photon-proxied URL (https://i0.wp.com/<original>),
    return the original external URL with Photon's own resize/ssl query
    params stripped. Handles images that Photon proxies from a host other
    than this site's own uploads - e.g. old posts hotlinking Google Photos
    or Imgur - which never appear in the WP media library and so can't be
    resolved to a local asset path. Returns None if url isn't a Photon
    URL."""
    match = PHOTON_HOST_RE.match(url)
    if not match:
        return None
    parsed = urlsplit("https://" + match.group(1))
    kept_query = [
        (k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True)
        if k not in PHOTON_QUERY_KEYS
    ]
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(kept_query), ""))


def rewrite_image_srcs(html: str, media_by_id: dict) -> str:
    """Rewrite every <img> tag's src to its local asset path. Prefers
    resolving via the wp-image-{ID} class against media_by_id (gets the
    true full-resolution original, not a Photon-resized variant); falls
    back to parsing the uploads path directly out of src when no ID class
    is present or the ID isn't in the media library. Drops srcset/sizes
    since there's only one resolution locally."""
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        target = None
        for c in img.get("class", []):
            if c.startswith("wp-image-"):
                media_obj = media_by_id.get(int(c.removeprefix("wp-image-")))
                if media_obj is not None:
                    target = media_asset_path(media_obj)
                break
        if target is None and img.get("src"):
            target = extract_uploads_path(img["src"])
        if target is None and img.get("src"):
            target = unwrap_photon_url(img["src"])
        if target is not None:
            img["src"] = target
        if img.has_attr("srcset"):
            del img["srcset"]
        if img.has_attr("sizes"):
            del img["sizes"]
    return str(soup)


def rewrite_download_links(html: str) -> str:
    """Rewrite <a href> and <video>/<source> src attributes that point at
    wp-content/uploads (zips, mp4s, movs) to their local asset path."""
    soup = BeautifulSoup(html, "html.parser")
    for tag, attr in (("a", "href"), ("video", "src"), ("source", "src")):
        for el in soup.find_all(tag):
            url = el.get(attr)
            if not url:
                continue
            target = extract_uploads_path(url)
            if target is None:
                target = unwrap_photon_url(url)
            if target is not None:
                el[attr] = target
    return str(soup)


def normalize_enlighter_blocks(html: str) -> str:
    """Convert Enlighter's <pre class="EnlighterJSRAW"
    data-enlighter-language="LANG">CODE</pre> into standard
    <pre><code class="language-LANG">CODE</code></pre> so the generic
    HTML-to-Markdown pass emits a fenced block with the right language."""
    soup = BeautifulSoup(html, "html.parser")
    for pre in soup.find_all("pre", class_="EnlighterJSRAW"):
        lang = pre.get("data-enlighter-language", "text")
        code_text = pre.get_text()
        new_pre = soup.new_tag("pre")
        new_code = soup.new_tag("code")
        new_code["class"] = f"language-{lang}"
        new_code.string = code_text
        new_pre.append(new_code)
        pre.replace_with(new_pre)
    return str(soup)


def _code_language_callback(el):
    """markdownify calls this with the <pre> element itself (not the inner
    <code>), so look at the <pre>'s child <code> tag for the
    'language-LANG' class that normalize_enlighter_blocks put there."""
    code = el.find("code")
    if code is None:
        return ""
    for c in code.get("class", []) or []:
        if c.startswith("language-"):
            return c.removeprefix("language-")
    return ""


def html_to_markdown(html: str) -> str:
    """Convert normalized post-body HTML to Markdown: ATX headings, '-'
    bullets, fenced code blocks with a language tag pulled from the code
    element's class."""
    converter = MarkdownConverter(
        heading_style="ATX",
        bullets="-",
        code_language_callback=_code_language_callback,
    )
    return converter.convert(html).strip() + "\n"


def convert_post_content(raw_html: str, media_by_id: dict) -> str:
    """Full per-post pipeline: Enlighter code blocks -> standard code
    blocks, image srcs -> local asset paths, download links -> local asset
    paths, then HTML -> Markdown."""
    html = normalize_enlighter_blocks(raw_html)
    html = rewrite_image_srcs(html, media_by_id)
    html = rewrite_download_links(html)
    return html_to_markdown(html)
