"""Class for storing paper information.
"""


class Paper(object):
    def __init__(
        self, title: str, authors: str, year: int, venue: str, bibtex: str
    ) -> None:
        self.title = title
        self.authors = authors
        self.year = year
        self.venue = venue
        self.bibtex = bibtex

    def pretty_print(self):
        ret = "=" * 80 + "\n"
        ret += "Title:   {}\n".format(self.title)
        ret += "Authors: {}\n".format(", ".join(self.authors))
        ret += "Year:    {}\n".format(self.year)
        ret += "Venue:   {}\n".format(self.venue)
        ret += "Bibtex:\n\n{}\n".format(self.bibtex)
        return ret
