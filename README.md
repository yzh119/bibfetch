# bibfetch
Fetch bibtex information in command line interface/vscode from academic search engines like dblp.

## Installation

Install the python package from pypi:

```bash
pip install bibfetch
```

User can also clone the github repository and install from source:

```bash
git clone git@github.com:yzh119/bibfetch.git
cd bibfetch/python
pip3 install .
```

### VSCode

See [vscode-extension](vscode-extension/README.md).

## CLI Usage

```
usage: Bibtex fetcher command line interface. [-h] [--backend BACKEND] [--title TITLE] [--number NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  --backend BACKEND, -b BACKEND
                        Backend to use for fetching bibtex, supported backends: dblp/semanticscholar.
  --title TITLE, -t TITLE
                        Title of the paper to fetch.
  --number NUMBER, -n NUMBER
                        Maximum number of search results to fetch, defaults to 10.
```

Example
```
bibfetch -t "Discerning the dominant out-of-order performance advantage"
```

## VSCode Demo

Search for bibtext from selected text:
![](https://github.com/yzh119/web-data/blob/main/bibfetch/search-for-selected-text.gif)

Search for bibtex from input box:
![](https://github.com/yzh119/web-data/blob/main/bibfetch/search-from-input-box.gif)

### Usage

1. Enter command palatte and type "bibfetch: Search BibTex".
  - User will be prompt to enter paper title and bibfetch would search bibtex using default configuration.
2. Enter command palatte and type "bibfetch: Search BibTex With..."
  - User will be prompt to enter paper title, backend, and number of entries to fetch, and bibfetch would search bibtex using the configuration.
3. Select text then right click and select "Search BibTex".
  - bibfetch would search bibtex of selected text using default configuration.
