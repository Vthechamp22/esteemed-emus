'''Prompt toolkit is the main framework for the TUI
'''
import os

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import (
    focus_next, focus_previous
)
from prompt_toolkit.layout.containers import (
    HSplit, VerticalAlign, VSplit, Window
)
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button

from myoure.functions import list_content

kb = KeyBindings()


@kb.add('c-c')
def exit_(event):
    '''Allows user to exit the app by using Ctrl-C
    '''
    event.app.exit()


kb.add("down")(focus_next)
kb.add("up")(focus_previous)


# Not yet figured out, hopefully will recieve params from button
def choice():
    '''Returns what the user has chosen from the button
    '''


start = list_content(os.getcwd())

# Creates left column with contents of cwd
maxleft = len(max(start, key=len))
left_buttons = [
    Button(text, handler=choice, left_symbol="", right_symbol="", width=maxleft) for text in start
]
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

style = Style([
    ("pane", "bg:#000000 #000000"),
    ("button", "#00FF00"),
    ("button.focused", "bg:#696969"),
])
