import os
from functools import partial
from pathlib import Path
from typing import Callable, NoReturn

from prompt_toolkit.application.current import get_app
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
from prompt_toolkit.layout.containers import HSplit, VerticalAlign, WindowAlign
from prompt_toolkit.widgets import Box, Button

from myoure.functions import list_content, open_file

# linting fix


class MyoureButton(Button):
    """Custom button widget for handling the file display."""

    def __init__(self, path: Path, handler: Callable, width: int = 12):
        self.path = path
        self.style = ""
        super().__init__(
            text=f"{path.name}",
            handler=handler,
            left_symbol="",
            right_symbol="",
            width=width,
        )
        if self.path.is_dir():
            self.style = "class:file.dir-button"
        elif self.path.is_symlink():
            self.style = "class:file.symlink-button"
        elif self.path.is_file():
            self.style = "class:file.file-button"

        if get_app().layout.has_focus(self):
            self.style += ".focused"

        self.window.align = WindowAlign.LEFT  # Set align to left

    def _get_text_fragments(self) -> StyleAndTextTuples:
        frags = super()._get_text_fragments()
        _old_style, _, handler = frags[2]
        frags[2] = (self.style, self.text, handler)  # Just pass in un-padded text
        return frags


class Folder:
    """Represents a columnar box."""

    def __init__(self, column_no: int, path: str = None) -> None:
        self.column_no = column_no
        self.buttons = []
        self.files = []
        max_len = 12
        if column_no == 0:
            self.files = list_content(os.getcwd())
        elif path:
            self.files = list_content(path)

        if self.files != []:
            max_len = max(len(x.name) for x in self.files) + 1

        self.buttons = [
            MyoureButton(file, partial(self._handler, file), max_len)
            for file in self.files
        ]

        self.layout = Box(
            body=HSplit(
                self.buttons, padding=0, align=VerticalAlign.TOP, style="class:pane"
            ),
            padding=1,
            style="class:pane",
        )

    def _handler(self, file: str) -> NoReturn:
        path = Path(file)
        if path.exists():
            if path.is_file():
                open_file(path)
            elif path.is_dir():
                self.cd_dir(str(path.absolute()))

    def cd_dir(self, dir: str) -> NoReturn:
        """Fills or shifts columns to depict opening the folder."""
        app = get_app()
        columns = app.layout.container.get_children()
        if self.column_no == 0:  # First column
            columns[2] = Folder(1, dir).layout.body
        if self.column_no == 1:  # second column
            columns[4] = Folder(2, dir).layout.body

    def is_empty(self) -> bool:
        """Returns whether this column is empty"""
        return len(self.buttons) == 0

    def __pt_container__(self) -> Box:
        return self.layout
