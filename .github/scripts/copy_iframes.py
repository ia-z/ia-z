import os
import shutil
from argparse import ArgumentParser
from typing import Callable

IFRAMES_FOLDER = "iframe_figures"

def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("root_directory", help="The root directory where '_build' folder exists as output from 'jupyter-book' build step.")
    parser.add_argument("current_directory", help=f"The current directory from where you want to search for '{IFRAMES_FOLDER}' folders recursively.")
    return parser

def copy_iframes(current_directory: str, root_directory: str, verbose: bool = True) -> None:
    """Copy iframes from 'current_directory' to build directory of 'jupyter-book' command.

    Args:
        current_directory (str): Path of the directory which contains a subdirectory `iframe_figures`.
        root_directory (str): Path of the root directory, where the website is build.
        verbose (bool, optional): Verbose of the function. Defaults to True.
    """
    # Let the function raise exceptions if no 'iframe_figures' directory found.
    assert IFRAMES_FOLDER in os.listdir(current_directory), f"No subdirectory '{IFRAMES_FOLDER}' found inside '{current_directory}'!"

    # Define absolute path of iframes folder as it should be
    absolute_current_directory = os.path.abspath(current_directory)
    absolute_iframes_folder = os.path.join(absolute_current_directory, IFRAMES_FOLDER)
    if verbose: print(f"Built iframes absolute path : '{absolute_iframes_folder}'.")
    # Define absolute root directory as it should be
    absolute_root_directory = os.path.abspath(root_directory)
    if verbose: print(f"Built root absolute path : '{absolute_iframes_folder}'.")
    # Find common path in absolute directories
    common_path = os.path.commonpath([absolute_iframes_folder, absolute_root_directory])
    complete_path = absolute_iframes_folder.split(common_path)[1]
    website_path = os.path.join(absolute_root_directory, '_build', 'html', complete_path)
    if verbose: print(f"Define website path where to make the copy : '{website_path}'.")
    print(f"Copying '{complete_path}'.")
    shutil.copytree(absolute_iframes_folder, website_path)
    print(f"Copied sucessfully '{complete_path}'.")

def apply_recursive(current_directory: str, applied_function: Callable[[str], None]):
    """Check recursively if 'iframe_figures' is in the 'current_directory'.
    If so, call the function `applied_function` with the path of the directory containing 'iframe_figures.
    If not, call this function recursively on all child directories.

    Args:
        current_directory (str): Path of the directory where we look for an 'iframe_figures' subdirectory.
        applied_function (Callable): Function to call when we find an 'iframe_figures'.
    """
    current_directory_subdirectories = [ dirname for dirname in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, dirname)) ]
    for directory_name in current_directory_subdirectories:
        if directory_name == IFRAMES_FOLDER: applied_function(directory_name)
        else: apply_recursive(os.path.join(current_directory, directory_name), applied_function)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    root_directory = args.root_directory
    current_directory = args.current_directory
    apply_recursive(current_directory, lambda walking_directory: copy_iframes(walking_directory, root_directory))

