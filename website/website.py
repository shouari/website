"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from website.pages.index import index
from rxconfig import config


class BaseState(rx.State):
    """The app state."""
    pass


app = rx.App()
app.add_page(index)
