import reflex as rx
from website.theme import TEXT_MAIN, TEXT_MUTED, BG_CARD, BORDER


def step3_process() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Cartographie du processus", size="5", color=TEXT_MAIN),
            rx.text(
                "Cette étape est en cours de développement.",
                color=TEXT_MUTED,
                size="3",
            ),
            spacing="4",
            align="center",
            padding="3rem",
        ),
        background=BG_CARD,
        border=f"1px solid {BORDER}",
        border_radius="12px",
        width="100%",
    )
