
import reflex as rx
from website.components.navbar import navbar
from website.components.footer import footer
from website.components.sections import section_container, container_style
from website.theme import PRIMARY_BG


def base_page(*children: rx.Component) -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(*children, width="100%", flex="1"),  # ← contenu extensible
            footer(),  # ← collera en bas
            spacing="0",
            align="stretch",
            flex = "1",  # ← prend toute la hauteur de la fenêtre
        ),
        width="100%",
        height="100vh",  # ← prend toute la hauteur de la fenêtre
        bg=PRIMARY_BG,
        padding="0",  # ← important pour éviter les bandes
        margin="0",
    )