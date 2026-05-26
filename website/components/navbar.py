import reflex as rx
from website.theme import TEXT_MAIN, CALYPSO_TRANSPARENT_20, VERT_CLAIR, BORDER
from reflex.state import State


def navbar_link(text, url: str) -> rx.Component:
    is_active = State.router.page.path == url
    return rx.link(
        rx.text(
            text,
            size="3",
            weight=rx.cond(is_active, "bold", "medium"),
            color=rx.cond(is_active, VERT_CLAIR, TEXT_MAIN),
            _hover={"color": VERT_CLAIR},
            transition="color 0.2s ease",
        ),
        href=url,
    )


def navbar() -> rx.Component:
    logo = rx.hstack(
        rx.image(src="/Logo.png", width="1.5em", height="auto", border_radius="25%"),
        rx.heading("Salim Houari", size="4", weight="bold", color=TEXT_MAIN),
        align_items="center",
    )

    desktop_links = rx.hstack(
        navbar_link("Accueil", "/home"),
        navbar_link("Projets", "/home#projets"),
        navbar_link("Méthode", "/home#methode"),
        navbar_link("À propos", "/about"),
        navbar_link("Manifeste", "/manifeste"),
        spacing="6",
        align_items="center",
    )

    mobile_menu = rx.menu.root(
        rx.menu.trigger(rx.icon("menu", size=28, color=TEXT_MAIN)),
        rx.menu.content(
            rx.menu.item(navbar_link("Accueil", "/home")),
            rx.menu.item(navbar_link("Projets", "/home#projets")),
            rx.menu.item(navbar_link("Méthode", "/home#methode")),
            rx.menu.item(navbar_link("À propos", "/about")),
            rx.menu.item(navbar_link("Manifeste", "/manifeste")),
            background=CALYPSO_TRANSPARENT_20,
            border=f"1px solid {BORDER}",
        ),
    )

    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(logo, href="/home"),
                desktop_links,
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.link(logo, href="/home"),
                mobile_menu,
                justify="between",
                align_items="center",
                width="100%",
            ),
        ),
        bg=CALYPSO_TRANSPARENT_20,
        padding="1em 1.5em",
        width="100%",
        position="sticky",
        top="0px",
        z_index="10",
        border_bottom=f"1px solid {BORDER}",
    )
