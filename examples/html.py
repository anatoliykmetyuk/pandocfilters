#!/usr/bin/env python

"""
Pandoc filter to process code blocks with class "html" into
raw html code.
"""

import os
import sys

import pygraphviz

from pandocfilters import toJSONFilter, RawBlock

def html(key, value, format, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if "html" in classes:
            return RawBlock("html", code)

if __name__ == "__main__":
    toJSONFilter(html)
