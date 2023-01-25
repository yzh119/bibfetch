"""
Fetch bibtex from top results in dblp.
"""

import urllib
import urllib.request
import urllib.parse
from lxml import etree
from .paper import Paper


__all__ = ["fetch_dblp_bibtex"]

DBLP_BASE_URL = "http://dblp.uni-trier.de/"
DBLP_PUB_SEARCH_URL = DBLP_BASE_URL + "search/api/publ?q={title}&h={num_results}"
DBLP_BIBTEX_URL = DBLP_BASE_URL + "rec/bib/{key}.bib"


def _download_content(url: str, decode: bool = False):
    response = urllib.request.urlopen(url)
    data = response.read()
    if decode:
        text = data.decode("utf-8")
    else:
        text = data
    return text


def _get_item_text(elem, xpath):
    try:
        return elem.xpath(xpath)[0].text
    except IndexError:
        return None


def fetch_dblp_bibtex(title: str, max_num_search_results: int = 10):
    search_url = DBLP_PUB_SEARCH_URL.format(
        title=urllib.parse.quote(title), num_results=max_num_search_results
    )
    root = etree.fromstring(_download_content(search_url))
    results = root.xpath("/result/hits/hit/info")
    papers = []
    for elem in results:
        authors = elem.xpath("authors/author/text()")
        title = _get_item_text(elem, "title/text()")
        year = _get_item_text(elem, "year/text()")
        venue = _get_item_text(elem, "venue/text()")
        key = _get_item_text(elem, "venue/text()")
        if key is None:
            raise RuntimeError(
                "No key found for paper: {}, failed to download bibtex.".format(title)
            )
        bibtex_url = DBLP_BIBTEX_URL.format(key=key)
        bibtex = _download_content(bibtex_url, decode=True)
        papers.append(Paper(title, authors, year, venue, bibtex))
    return papers
