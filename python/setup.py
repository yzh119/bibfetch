from distutils.core import setup

setup(
    name="bibfetch",
    version="0.0.1",
    description="Fetch bibtex information from academic search engines.",
    author="Zihao Ye",
    author_email="expye@outlook.com",
    url="git@github.com:yzh119/bibfetch.git",
    packages=["bibfetch"],
    requires=["lxml", "urllib"],
    entry_points={
        'console_scripts': [
            'bibfetch = bibfetch.__main__:main',
        ]
    },
)
