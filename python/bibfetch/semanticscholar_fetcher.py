"""
Fetch bibtex from top results in dblp.
"""

from urllib import parse
import json
from .paper import Paper
from .utils import _request_content
from typing import List


__all__ = ["fetch_semanticscholar_bibtex"]

SEMANTICSCHOLAR_API_URL = "https://api.semanticscholar.org/graph/v1/"
SEMANTICSCHOLAR_SEARCH_PAPER = (
    SEMANTICSCHOLAR_API_URL + "paper/search?query={title}&offset=0&limit={num_results}"
)
SEMANTICSCHOLAR_PAPER_SINGLE = (
    SEMANTICSCHOLAR_API_URL
    + "paper/{paper_id}?fields=title,authors,venue,year,citationStyles"
)
SEMANTICSCHOLAR_PAPER_BATCH = (
    SEMANTICSCHOLAR_API_URL
    + "paper/batch?fields=title,authors,venue,year,citationStyles"
)


def _cleanup_bibtex(
    raw_bibtex: str,
) -> str:
    first_para_idx = raw_bibtex.find("{")
    return "@inproceedings" + raw_bibtex[first_para_idx:]


def fetch_semanticscholar_bibtex(
    title: str, max_num_search_results: int = 10, batch_mode: bool = True, **kwargs
) -> List[Paper]:
    search_url = SEMANTICSCHOLAR_SEARCH_PAPER.format(
        title=parse.quote(title), num_results=max_num_search_results
    )

    search_results = json.loads(_request_content(search_url, decode=True))
    paper_ids = [elem["paperId"] for elem in search_results["data"]]
    papers = []
    if batch_mode:
        paper_details = json.loads(
            _request_content(
                SEMANTICSCHOLAR_PAPER_BATCH,
                data=json.dumps({"ids": paper_ids}).encode("utf-8"),
                decode=True,
            )
        )
        for paper_detail in paper_details:
            authors = [author["name"] for author in paper_detail["authors"]]
            title = paper_detail["title"]
            year = int(paper_detail["year"])
            venue = paper_detail["venue"]
            bibtex = _cleanup_bibtex(paper_detail["citationStyles"]["bibtex"])
            papers.append(Paper(title, authors, year, venue, bibtex))
    else:
        for paper_id in paper_ids:
            paper_detail = json.loads(
                _request_content(
                    SEMANTICSCHOLAR_PAPER_SINGLE.format(paper_id=paper_id), decode=True
                )
            )
            authors = [author["name"] for author in paper_detail["authors"]]
            title = paper_detail["title"]
            year = int(paper_detail["year"])
            venue = paper_detail["venue"]
            bibtex = _cleanup_bibtex(paper_detail["citationStyles"]["bibtex"])
            papers.append(Paper(title, authors, year, venue, bibtex))

    return papers
