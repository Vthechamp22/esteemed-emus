from typing import NoReturn

import cursor
from prompt_toolkit import Application

from myoure.layout import kb, layout, style


def start() -> NoReturn:
    """Start the application."""
    app = Application(layout=layout, full_screen=True, key_bindings=kb, style=style, refresh_interval=1)
    app.output.show_cursor = lambda: None  # Hide the cursor

    app.run()
    cursor.show()
