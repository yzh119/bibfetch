from .dblp_fetcher import fetch_dblp_bibtex
from .semanticscholar_fetcher import fetch_semanticscholar_bibtex


def get_fetcher(backend: str):
    if backend == "dblp":
        return fetch_dblp_bibtex
    elif backend == "semanticscholar":
        return fetch_semanticscholar_bibtex
    else:
        raise KeyError("Unknown backend: {}".format(backend))
