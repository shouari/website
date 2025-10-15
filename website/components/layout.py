
import reflex as rx
from website.components.navbar import navbar
from website.components.footer import footer
from website.components.sections import section_container, container_style
from website.theme import PRIMARY_BG


def base_page(*children: rx.Component) -> rx.Component:
    return rx.box(
        rx.image(
            src="/bg_svg.svg",
            position="fixed",
            top="7%",
            left="0",
            # transform="translate(-50%, -50%)",
            width="100%",
            height="auto",
            opacity=0.2,
            
            z_index=0,
            style={"pointer-events": "none"},
        ),
        rx.vstack(
            navbar(),
            rx.box(*children, width="100%", flex="1"),  # ← contenu extensible
            footer(),  # ← collera en bas
            spacing="0",
            align="stretch",
            flex = "1",  # ← prend toute la hauteur de la fenêtre
        ),
        width="100%",
        min_height="100vh",  # ← prend toute la hauteur de la fenêtre
        bg=PRIMARY_BG,
        display="flex",
        flex_direction="column",
        justify_content="space-between",  # ← espace entre le contenu et le footer
    )