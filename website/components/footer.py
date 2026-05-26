import reflex as rx
from website.theme import TEXT_MAIN, TEXT_MUTED, TEXT_DIM, CALYPSO_TRANSPARENT_20, BORDER, VERT_CLAIR


def footer() -> rx.Component:
    left = rx.text(
        "© Salim Houari · Amélioration continue & Automatisation",
        color=TEXT_MUTED,
        size="2",
    )

    right = rx.hstack(
        rx.link(
            rx.text("LinkedIn", size="2", color=TEXT_MUTED,
                    _hover={"color": VERT_CLAIR}, transition="color 0.2s ease"),
            href="https://www.linkedin.com/in/salim-houari/",
            is_external=True,
        ),
        rx.text("·", color=TEXT_MUTED, size="2"),
        rx.link(
            rx.text("Manifeste", size="2", color=TEXT_MUTED,
                    _hover={"color": VERT_CLAIR}, transition="color 0.2s ease"),
            href="/manifeste",
        ),
        rx.text("·", color=TEXT_MUTED, size="2"),
        rx.link(
            rx.text("salim@salimhouari.com", size="2", color=TEXT_MUTED,
                    _hover={"color": VERT_CLAIR}, transition="color 0.2s ease"),
            href="mailto:salim@salimhouari.com",
        ),
        spacing="2",
        align_items="center",
    )

    geo_text = rx.text(
        "Salim Houari est un expert en amélioration continue et automatisation "
        "des processus basé à Laval, Québec, Canada. Adm.A., M.Sc. Génie mécanique, "
        "membre du comité miroir canadien ISO TC279. Il développe des outils "
        "opérationnels en Python pour PME québécoises (50 à 500 employés). "
        "Approche CSA : Clarifier → Simplifier → Automatiser. "
        "Contact : salim@salimhouari.com",
        font_size="0.72rem",
        color=TEXT_DIM,
        max_width="800px",
        margin="0 auto",
        text_align="center",
        padding_top="0.75rem",
    )

    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(left, rx.spacer(), right,
                      align="center", width="100%"),
        ),
        rx.mobile_only(
            rx.vstack(left, right, spacing="3", align="center"),
        ),
        geo_text,
        padding_x=["1rem", "1.5rem", "2rem"],
        padding_y="1.25rem",
        border_top=f"1px solid {BORDER}",
        background=CALYPSO_TRANSPARENT_20,
        width="100%",
    )
