# bibfetch
Fetch bibtex info in command line interface from academic search engines like dblp.

## Installation

```bash
cd python
pip3 install -e .
```

## Usage

```
usage: Bibtex fetcher command line interface. [-h] [--backend BACKEND] [--title TITLE] [--number NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  --backend BACKEND, -b BACKEND
                        Backend to use for fetching bibtex, only dblp is supported up to now.
  --title TITLE, -t TITLE
                        Title of the paper to fetch.
  --number NUMBER, -n NUMBER
                        Maximum number of search results to fetch, defaults to 10.
```

Example
```
bibfetch -t "Discerning the dominant out-of-order performance advantage"
```
