#! /usr/bin/bash
rm -rf ./_build
jupyter-book build .
python3 copy_iframes.py ./docs/ .
