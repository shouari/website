import reflex as rx
from website.theme import *

def footer() -> rx.Component:
    return rx.box(
        # Version desktop et tablette
        rx.tablet_and_desktop(
            rx.hstack(
                rx.text("© Salim Houari", font_size="1rem"),
                rx.spacer(),
                rx.text("Clarifier - Simplifier - Automatiser", font_size="1rem"),
                rx.spacer(),
                rx.link(
                    rx.icon("linkedin", size=18),
                    href="https://www.linkedin.com/in/salim-houari/",
                    is_external=True,
                    margin_left="0.5rem",
                ),
                align="center",
                justify="between",
                wrap="wrap",
                width="100%",
            )
        ),
        # Version mobile
        rx.mobile_only(
            rx.vstack(
                rx.text("© Salim Houari", font_size="0.95rem"),
                rx.text("Clarifier - Simplifier - Automatiser", font_size="0.95rem"),
                rx.link(
                    rx.icon("linkedin", size=20),
                    href="https://www.linkedin.com/in/salim-houari/",
                    is_external=True,
                    margin_top="0.5rem",
                ),
                spacing="1",
                align="center",
            )
        ),
        **container_style,
        width="100%",
        padding_y="1rem",
        border_top="1px solid rgba(0,0,0,0.06)",
        bg=CALYPSO_TRANSPARENT_20,
        backdrop_filter="blur(10px)",
    )
