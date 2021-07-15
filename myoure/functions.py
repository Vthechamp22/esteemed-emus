"""Functions of the application"""
from pathlib import Path
from typing import List, NoReturn


def list_content(path: str) -> List:
    """Lists the files and directories in the given path.

    :param path: The path to list folders and files from.
    """
    entries = Path(path)
    content_list = [i for i in entries.iterdir()]
    return content_list


def mkdir(path: str, name: str = None) -> NoReturn:
    """Makes a directory in the given path with the given name

    :param path: The path to the parent directory of the new folder
    :param name: The name of the new folder, None by default.
    """
    index = 0
    while True:
        try:
            dir = Path(path) / ('New Folder' if index == 0 else f"New Folder{index}") if name is None else name
            dir.mkdir()
            break
        except FileExistsError:
            index += 1


def rmdir(path: str) -> NoReturn:
    """Removes the given directory

    :param path: Path to the directory
    """
    path = Path(path)
    try:
        path.rmdir()
    except NotADirectoryError:
        raise Exception(f"{path} is not a directory")


def get_extension(path):
    file = Path(path)
    if file.is_file():
        return file.suffix
    if file.is_dir():
        return [i.suffix for i in file.iterdir()]

