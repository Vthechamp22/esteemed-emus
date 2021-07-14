from pathlib import Path


def list_content(path):
    entries = Path(path)
    content_list = [i.name for i in entries.iterdir()]
    return content_list


def mkdir(path, name=None):
    index = 0
    while True:
        try:
            dir = Path(path) / ('New Folder' if index == 0 else f"New Folder{index}") if name is None else name
            dir.mkdir()
            break
        except FileExistsError:
            index += 1

def rmdir(path):
    path = Path(path)
    try:
        path.rmdir()
    except NotADirectoryError:
        print(f"{path} is not a directory")

