"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from website.pages.index import index
from website.pages.about import about
from rxconfig import config


meta = [
    {"name": "theme_color", "content": "#2563EB"},
    {"char_set": "UTF-8"},
    {"property": "og:url", "content": "url"},
]

class BaseState(rx.State):
    """The app state."""
    pass


app = rx.App()
app.add_page(index,
             title="Salim Houari - Consultant en optimisation des opérations",
             description="Clarifier, Simplifier, Automatiser les opérations de votre entreprise.",
             image="/Logo.png",
             meta=meta)
app.add_page(about,
             title="À propos - Salim Houari",
             description="Découvrez mon parcours et ma mission pour aider les entreprises à optimiser leurs opérations.",
             image="/Logo.png",
             meta=meta)
