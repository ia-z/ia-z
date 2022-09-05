import os
import shutil


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

    print(f'Copying "{complete_path}".')
    shutil.copytree(current_dir, website_path)


def delete_iframes(current_dir: str):
    """Delete the 'iframe_figures' directory.
    Input
        current_dir: Path to a directory that contains the 'iframe_figures' subdirectory.
    """
    assert 'iframe_figures' in os.listdir(current_dir), f"No subdir 'iframe_figures' found inside '{current_dir}'!"

    iframe_path = os.path.join(current_dir, 'iframe_figures')
    print(f'Deleting "{iframe_path}".')
    shutil.rmtree(iframe_path)


def apply_recursive(current_dir: str, fn: callable):
    """Check if 'iframe_figures' is in the 'current_dir'.
    If so it calls the function `fn` passed by the argument.
    The function `fn` is called with the path of the directory containing
    the 'iframe_figures' directory.
    Recursively calls this function to all subdirectories.
    Input
    -----
        current_dir: Path of the directory where we look for an 'iframe_figures' subdirectory.
        fn: Function to call when we find an 'iframe_figures'.
    """
    directories = [
        dirname
        for dirname in os.listdir(current_dir)
        if os.path.isdir(os.path.join(current_dir, dirname))
    ]

    for dirname in directories:
        if dirname == 'iframe_figures':
            fn(current_dir)
        else:
            apply_recursive(os.path.join(current_dir, dirname), fn)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2 or sys.argv[1] not in {'copy', 'delete'}:
       print(f'Usage: {sys.argv[0]} [delete/copy]')
       sys.exit(0)

    if sys.argv[1] == 'copy' and len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} copy [docs_path] [root_path]')
        sys.exit(0)

    if sys.argv[1] == 'delete' and len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} delete [docs_path]')
        sys.exit(0)

    if sys.argv[1] == 'copy':
        current_dir = sys.argv[2]
        root_dir = sys.argv[3]
        fn = lambda d: copy_iframes(d, root_dir)
        apply_recursive(current_dir, fn)

    elif sys.argv[1] == 'delete':
        current_dir = sys.argv[2]
        apply_recursive(current_dir, delete_iframes)