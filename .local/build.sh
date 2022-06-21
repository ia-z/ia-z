# Should be called only from root `bash .local/build.sh`

# Declare the source of venv for Linux/Windows (Fuck Mac =))
python_source_activate=.venv/Scripts/activate
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ];
then
    python_source_activate=.venv/bin/activate
fi

if [ -d "$(pwd)/.local" ]
then
    rm -rf _build/
    if [ ! -d "$(pwd)/.venv" ]
    then
        python -m venv .venv
    fi
    source python_source_activate
    pip install -r requirements.txt
    python .local/manage_iframes.py delete ./docs/
    jupyter-book build .
    python .local/manage_iframes.py copy ./docs/ .
    exit 0
else
    echo "Launch the script at root please !"
    exit 1
fi