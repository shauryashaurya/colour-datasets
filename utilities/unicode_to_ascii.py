#!/usr/bin/env python
"""
Unicode to ASCII Utility
========================
"""

import codecs
import os
import unicodedata

__copyright__ = "Copyright (C) 2018-2021 - Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = ["SUBSTITUTIONS", "unicode_to_ascii"]

SUBSTITUTIONS = {
    "–": "-",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "′": "'",
}


def unicode_to_ascii(root_directory):
    """
    Recursively converts from unicode to ASCII *.py*, *.bib* and *.rst* files
    in given directory.

    Parameters
    ----------
    root_directory : unicode
        Directory to convert the files from unicode to ASCII.
    """

    for root, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if (
                not filename.endswith(".tex")
                and not filename.endswith(".py")
                and not filename.endswith(".bib")
                and not filename.endswith(".rst")
            ):
                continue

            if filename == "unicode_to_ascii.py":
                continue

            filename = os.path.join(root, filename)
            with codecs.open(filename, encoding="utf8") as file_handle:
                content = file_handle.read()

            with codecs.open(filename, "w", encoding="utf8") as file_handle:
                for key, value in SUBSTITUTIONS.items():
                    content = content.replace(key, value)

                content = unicodedata.normalize("NFD", content)

                file_handle.write(content)


if __name__ == "__main__":
    unicode_to_ascii(os.path.join("..", "colour_checker_detection"))
