"""The base layout and style for the application"""
import os
from typing import NoReturn

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next, focus_previous
)
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout.containers import (
    HSplit, VerticalAlign, VSplit, Window
)
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box

from myoure.functions import list_content
from myoure.widgets import MyoureButton

kb = KeyBindings()


@kb.add('q')
def exit_(event: KeyPressEvent) -> NoReturn:
    """Allows user to exit the app by using Q"""
    event.app.exit()


kb.add("down")(focus_next)
kb.add("up")(focus_previous)


# Not yet figured out, hopefully will recieve params from button
def choice() -> NoReturn:
    """Returns what the user has chosen from the button"""


start = list_content(os.getcwd())

# Creates left column with contents of cwd
maxleft = max(len(x.name) for x in start)
left_buttons = [MyoureButton(file, choice, maxleft) for file in start]
leftWin = Box(
    body=HSplit(left_buttons, padding=0, align=VerticalAlign.TOP),
    padding=1,
    style="class:pane",
)

midWin = Box(
    body=HSplit("", padding=0, align=VerticalAlign.TOP),
    padding=1,
    style="class:pane"
)
rightWin = Box(
    body=HSplit("", padding=0, align=VerticalAlign.TOP),
    padding=1,
    style="class:pane"
)

root_cont = Box(
    body=VSplit(
        children=[
            leftWin,
            Window(width=1, char=' '),
            midWin,
            Window(width=1, char=' '),
            rightWin,
        ]
    ),
    padding_left=0,
    padding_right=0,
    padding_bottom=0,
    padding_top=0,
)

layout = Layout(container=root_cont)

style = Style(
    [
        ("pane", "bg:#000000 #000000"),
        ("button", "#00FF00"),
        ("button.focused", "bg:#696969"),
        ("file.dir-button", "#BBCCDD"),
        ("file.file-button", "#AABBCC"),
        ("file.symlink-button", "#CCDDEE"),
    ]
)
