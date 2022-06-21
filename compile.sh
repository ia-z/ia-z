#! /usr/bin/bash
rm -rf ./_build
python3 manage_iframes.py delete ./docs/
jupyter-book build .
python3 manage_iframes.py copy ./docs/ .
