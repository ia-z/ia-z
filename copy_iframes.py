import os
import shutil
import copy


def copy_iframes(current_dir: str, root_dir: str):
    """Copy the iframes of the current directory pointed by `current_dir`.
    There should be a subdirectory named `iframe_figures`.

    Input
    -----
        current_dir: Path of the directory which contains a subdir `iframe_figures`.
        root_dir: Path of the root directory, where the website is build.
    """
    assert 'iframe_figures' in os.listdir(current_dir), f"No subdir 'iframe_figures' found inside '{current_dir}'!"

    current_dir = os.path.abspath(current_dir)
    current_dir = os.path.join(current_dir, 'iframe_figures')

    root_dir = os.path.abspath(root_dir)

    common_path = os.path.commonpath([current_dir, root_dir])
    complete_path = current_dir.split(common_path)[1]
    website_path = os.path.join(
        root_dir,
        '_build/html',
    ) + complete_path

    shutil.copytree(current_dir, website_path)


def copy_recursive(current_dir: str, root_dir: str):
    """Check if 'iframe_figures' is in the 'current_dir'.
    If so it copies the iframe directory.

    Recursively calls this function to all subdirectories.
    """
    directories = [
        dirname
        for dirname in os.listdir(current_dir)
        if os.path.isdir(os.path.join(current_dir, dirname))
    ]

    for dirname in directories:
        if dirname == 'iframe_figures':
            copy_iframes(current_dir, root_dir)
        else:
            copy_recursive(os.path.join(current_dir, dirname), root_dir)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} [docs_path] [root_path]')
        sys.exit(0)

    current_dir = sys.argv[1]
    root_dir = sys.argv[2]

    copy_recursive(current_dir, root_dir)
