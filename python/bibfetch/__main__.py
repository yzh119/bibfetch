import argparse
from . import get_fetcher


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Bibtex fetcher command line interface.")
    parser.add_argument(
        "--backend",
        "-b",
        type=str,
        default="dblp",
        help="Backend to use for fetching bibtex (choice: dblp).",
    )
    parser.add_argument("--title", "-t", type=str, help="Title of the paper to fetch.")
    parser.add_argument(
        "--number",
        "-n",
        type=int,
        default=10,
        help="Maximum number of search results to fetch.",
    )

    args = parser.parse_args()
    fetcher = get_fetcher(args.backend)
    for item in fetcher(args.title, args.number):
        print(item.pretty_print())
