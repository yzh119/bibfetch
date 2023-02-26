# bibfetch
Fetch bibtex information in command line interface/vscode from academic search engines like dblp.

## Installation

To install the python package, run the following command in the root directory of the project.

```bash
cd python
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

## VSCode Usage

TODO