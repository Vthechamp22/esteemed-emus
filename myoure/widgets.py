from pathlib import Path
from typing import Callable

from prompt_toolkit.application.current import get_app
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
from prompt_toolkit.layout.containers import WindowAlign
from prompt_toolkit.widgets import Button


class MyoureButton(Button):
    """Custom button widget for handling the file display."""

    def __init__(self, path: Path, handler: Callable, width: int):
        self.path = path
        self.style = ""
        super().__init__(
            text=path.name,
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
