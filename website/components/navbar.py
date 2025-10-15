# website/components/navbar.py

import reflex as rx
from website.theme import *
from reflex.state import State

def navbar_link(text: str, url: str) -> rx.Component:
    
    is_active = State.router.page.path == url
    return rx.link(
        rx.text(text, 
                size="3", 
                
                weight=rx.cond(is_active, "bold", "medium"), 
                color=rx.cond(is_active, "#AC3640", TEXT_MAIN), 
                _hover={"color": "#B7303B"},
            
                ), 
                href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    navbar_link(
                    rx.image(
                        src="\Logo.png",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    "/home"),
                    navbar_link(
                    rx.heading(
                        "Salim Houari", size="4", weight="bold", color=TEXT_MAIN
                    ),
                    "/home"),

                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Accueil", "/home"),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.text("A propos", color=TEXT_MAIN),
                                rx.icon("chevron-down"),
                                weight="light",
                                variant="ghost",
                                size="3",
                                color=TEXT_MAIN,
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item(navbar_link("A Propos de moi", "/about")),
                            rx.menu.item(navbar_link("Manifeste", "/manifeste")),                        ),
                    ),
                    # navbar_link("Blog", "/blog"),
                    justify="end",
                    spacing="5",
                    
                    
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    navbar_link(
                    rx.image(
                        src="\Logo.png",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    "/home"),
                    navbar_link(
                    rx.heading(
                        "Salim Houari", size="4", weight="bold", color=TEXT_MAIN
                    ),
                    "/home"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(navbar_link("Accueil", "/home")),
                        rx.menu.sub(
                            rx.menu.sub_trigger("A Propos", color=TEXT_MAIN, size="3"),
                            rx.menu.sub_content(
                                rx.menu.item(navbar_link("A Propos de moi", "/about")),
                                rx.menu.item(navbar_link("Manifeste", "/manifeste")),
                                
                            ),
                        ),
                        # rx.menu.item(navbar_link("Blog", "/blog")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=CALYPSO_TRANSPARENT_20,
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        position="sticky",
        top="0px",
        z_index="10",
        
    )
