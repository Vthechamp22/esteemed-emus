from pathlib import Path
from typing import Callable, Optional
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
from prompt_toolkit.key_binding.key_bindings import KeyBindings
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.containers import Container, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.mouse_events import MouseEvent, MouseEventType

from prompt_toolkit.widgets import Button
from prompt_toolkit import HTML
from prompt_toolkit.application.current import get_app
from prompt_toolkit.utils import get_cwidth


class MyoureButton(Button):
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
            self.style = "class:dir-button"
        elif self.path.is_symlink():
            self.style = "class:symlink-button"
        elif self.path.is_file():
            self.style = "class:file-button"

        if get_app().layout.has_focus(self):
            self.style += ".focused"

    def _get_text_fragments(self) -> StyleAndTextTuples:
        frags = super()._get_text_fragments()
        _old_style, text, handler = frags[2]
        frags[2] = (self.style, text, handler)
        return frags
