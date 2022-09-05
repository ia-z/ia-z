rm -rf _build/
jupyter-book build .
python3 .github/scripts/copy_iframes.py . docs/
