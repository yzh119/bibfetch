from .dblp_fetcher import fetch_dblp_bibtex


def get_fetcher(backend: str):
    if backend == "dblp":
        return fetch_dblp_bibtex
    else:
        raise KeyError("Unknown backend: {}".format(backend))
