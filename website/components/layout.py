
import reflex as rx
from website.components.navbar import navbar
from website.components.footer import footer
from website.components.sections import section_container, container_style
from website.theme import PRIMARY_BG


def base_page(*children: rx.Component) -> rx.Component:
    return rx.flex(
        rx.vstack(
            navbar(),
            rx.box(*children, flex="1", width="100%"),
            footer(),
            spacing="0",
        ),
        direction="column",
        min_height="100vh",  # occupe toute la hauteur de l’écran
        width="100%",
       
        bg=PRIMARY_BG,
    )

