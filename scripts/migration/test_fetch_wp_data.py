import json
import urllib.error
import urllib.request
from urllib.parse import urlparse, parse_qs
from unittest.mock import patch, MagicMock

from fetch_wp_data import fetch_all


def _page_of(request):
    """Extract the page query param from a urlopen call argument, which is
    a urllib.request.Request object (fetch_all always passes one so it can
    attach a User-Agent header)."""
    url = request.full_url if isinstance(request, urllib.request.Request) else request
    query = parse_qs(urlparse(url).query)
    return query["page"][0]


def test_fetch_all_stops_on_400_last_page():
    """WP returns HTTP 400 rest_post_invalid_page_number once you page
    past the last page - that's the normal end-of-results signal, not
    an error, and must not raise."""
    page1 = [{"id": i} for i in range(100)]
    page2 = [{"id": i} for i in range(100, 113)]

    def fake_urlopen(request):
        cm = MagicMock()
        page = _page_of(request)
        if page == "1":
            cm.__enter__.return_value.read.return_value = json.dumps(page1).encode()
        elif page == "2":
            cm.__enter__.return_value.read.return_value = json.dumps(page2).encode()
        else:
            raise urllib.error.HTTPError(request.full_url, 400, "Bad Request", {}, None)
        return cm

    with patch("fetch_wp_data.urllib.request.urlopen", side_effect=fake_urlopen), \
         patch("fetch_wp_data.time.sleep"):
        result = fetch_all("posts")

    assert len(result) == 113
    assert result[0]["id"] == 0
    assert result[-1]["id"] == 112


def test_fetch_all_empty_batch_stops_pagination():
    def fake_urlopen(request):
        cm = MagicMock()
        cm.__enter__.return_value.read.return_value = b"[]"
        return cm

    with patch("fetch_wp_data.urllib.request.urlopen", side_effect=fake_urlopen), \
         patch("fetch_wp_data.time.sleep"):
        result = fetch_all("posts")

    assert result == []
