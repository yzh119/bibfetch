from distutils.core import setup

import os

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + "/requirements.txt"
requirements = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        requirements = f.read().splitlines()
setup(
    name="bibfetch",
    version="0.0.1",
    description="Fetch bibtex information from academic search engines.",
    author="Zihao Ye",
    author_email="expye@outlook.com",
    url="https://github.com/yzh119/bibfetch",
    packages=["bibfetch"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "bibfetch = bibfetch.__main__:main",
        ]
    },
)
