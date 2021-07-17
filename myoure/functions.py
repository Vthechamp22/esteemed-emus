"""Functions of the application."""
import subprocess
from pathlib import Path
from platform import system
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
        print(f"{path} is not a directory")


def open_file(path: Path) -> NoReturn:
    """Opens the file using the system's default handler."""
    if system() == "Linux":
        err = subprocess.run(["xdg-open", str(path.resolve())], shell=False)
    elif system() == "Windows":
        err = subprocess.run(["start", str(path.resolve())], shell=False)
    elif system() == "Darwin":
        err = subprocess.run(["open", str(path.resolve())], shell=False)

    if err.stderr:
        raise Exception(err.stderr)
        raise Exception(f"{path} is not a directory")


def get_extension(path):
    file = Path(path)
    if file.is_file():
        return file.suffix
    if file.is_dir():
        return [i.suffix for i in file.iterdir()]


def mkfileutility(path: str):
    # utility function to make file, use mkfile function below
    absolute_path_file = Path(path).absolute()
    if absolute_path_file.exists():
        raise FileExistsError(f"{absolute_path_file} already exists")

    else:
        with absolute_path_file.open("w", encoding="utf-8") as f:
            f.close()


def mkfile(path: str, name: str = None):
    index = 0
    while True:
        try:
            file = Path(path).absolute() / (
                'New Empty File' if index == 0 else f"New Empty File {index}") if name is None else name
            mkfileutility(file)
            break
        except FileExistsError:
            index += 1


def rmfile(path: str):
    Path(path).unlink()
