"""The base layout and style for the application"""
from typing import NoReturn

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next, focus_previous
)
from prompt_toolkit.key_binding.key_processor import KeyPressEvent
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.styles import Style

from myoure.widgets import Folder

kb = KeyBindings()


@kb.add('q')
def exit_(event: KeyPressEvent) -> NoReturn:
    """Allows user to exit the app by using Q"""
    event.app.exit()


kb.add("down")(focus_next)
kb.add("up")(focus_previous)

leftWin, midWin, rightWin = [Folder(i) for i in range(3)]

root_cont = VSplit(
    children=[
        leftWin,
        Window(width=1, char='│'),
        midWin,
        Window(width=1, char='│'),
        rightWin,
    ])

layout = Layout(container=root_cont)


def get(x, a):
    return x[a].get_children()[0].get_children()[1].get_children()[1].get_children()[0].get_children()


@kb.add('right')
def right(event: KeyPressEvent) -> NoReturn:
    cont = event.app.layout.container.get_children()
    leftcol = cont[0].get_children()[1].get_children()[1].get_children()[0].get_children()
    midcol = cont[2].get_children()[0].get_children()
    rightcol = cont[4].get_children()[0].get_children()
    cur = event.app.layout.current_window

    if cur in leftcol:
        event.app.layout.focus(midcol[0])
    if cur in midcol:
        event.app.layout.focus(rightcol[0])


@kb.add('left')
def left(event: KeyPressEvent) -> NoReturn:
    cont = event.app.layout.container.get_children()
    leftcol = cont[0].get_children()[1].get_children()[1].get_children()[0].get_children()
    midcol = cont[2].get_children()[0].get_children()
    rightcol = cont[4].get_children()[0].get_children()
    cur = event.app.layout.current_window

    if cur in midcol:
        event.app.layout.focus(leftcol[0])
    if cur in rightcol:
        event.app.layout.focus(midcol[0])


style = Style(
    [
        ("pane", "bg:#000000 #ffffff"),
        ("button", "#00FF00"),
        ("button.focused", "bg:#696969"),
        ("file.dir-button", "#BBCCDD"),
        ("file.file-button", "#AABBCC"),
        ("file.symlink-button", "#CCDDEE"),
    ]
)
