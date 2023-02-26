# VSCode Extension for bibfetch

VSCode Extension for bibfetch.

## Demo

Search for bibtext from selected text:
![](https://github.com/yzh119/web-data/blob/main/bibfetch/search-for-selected-text.gif)

Search for bibtex from input box:
![](https://github.com/yzh119/web-data/blob/main/bibfetch/search-from-input-box.gif)

## Install the Extension to VSCode

### VSCode MarketPlace

You can get the extensions by searching `bibfetch` in the VSCode marketplace.

### Dependency

Before installing this extension, please make sure you have already installed python package `bibfetch`.

You can install the python package via:

```bash
pip install bibfetch
```

## Customize VSCode bibfetch extension

There are several settings that can be customized for bibfetch extension in VSCode:

- `bibfetch.pythonpath` : Set the interpreter path for the python environment where `bibfetch` is installed. If not set, the extension will use the default python3 interpreter.
- `bibfetch.defaultBackend` : Set the backend to use for fetching bibtex, supported backends: `dblp`/`semanticscholar`.
- `bibfetch.defaultNumEntries` : Set the default number of search results to fetch, defaults to 10.

User can go to VSCode settings UI and set these settings in `Extensions -> bibfetch`, or open `settings.json` and write the following lines:

```json
{
    "bibfetch.pythonpath": "/path/to/python3",
    "bibfetch.defaultBackend": "dblp",
    "bibfetch.defaultNumEntries": 10
}
```
