"""
Fetch bibtex from top results in dblp.
"""

from lxml import etree
from .paper import Paper
from .utils import _request_content
from urllib import parse
from typing import Optional, List, Any


__all__ = ["fetch_dblp_bibtex"]

DBLP_BASE_URL = "http://dblp.uni-trier.de/"
DBLP_PUB_SEARCH_URL = DBLP_BASE_URL + "search/api/publ?q={title}&h={num_results}"
DBLP_BIBTEX_URL = DBLP_BASE_URL + "rec/bib/{key}.bib"


def _get_item_text(elem: Any, xpath: str) -> Optional[str]:
    try:
        return elem.xpath(xpath)[0].text
    except IndexError:
        return None


def fetch_dblp_bibtex(title: str, max_num_search_results: int = 10, **kwargs):
    search_url = DBLP_PUB_SEARCH_URL.format(
        title=parse.quote(title), num_results=max_num_search_results
    )
    root = etree.fromstring(_request_content(search_url))
    results = root.xpath("/result/hits/hit/info")
    papers = []
    for elem in results:
        authors = elem.xpath("authors/author/text()")
        title = _get_item_text(elem, "title")
        year = int(_get_item_text(elem, "year"))
        venue = _get_item_text(elem, "venue")
        key = _get_item_text(elem, "key")
        if key is None:
            raise RuntimeError(
                "No key found for paper: {}, failed to download bibtex.".format(title)
            )
        bibtex_url = DBLP_BIBTEX_URL.format(key=key)
        bibtex = _request_content(bibtex_url, decode=True)
        papers.append(Paper(title, authors, year, venue, bibtex))
    return papers
