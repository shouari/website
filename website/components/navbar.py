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
                text_decoration=rx.cond(is_active, "underline", "none"),
                color=rx.cond(is_active, "#F1F5F950", TEXT_MAIN), 
                _hover={"color": "#F1F5F990", "text_decoration": "underline"},
            
                ), 
                href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="\Logo.png",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Salim Houari", size="4", weight="bold", color=TEXT_MAIN
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Accueil", "/home"),
                    # rx.menu.root(
                    #     rx.menu.trigger(
                    #         rx.button(
                    #             rx.text(
                    #                 "A propos",
                    #                 size="4",
                    #                 weight="medium",
                    #             ),
                    #             rx.icon("chevron-down"),
                    #             weight="medium",
                    #             variant="ghost",
                    #             size="3",
                    #         ),
                    #     ),
                    #     rx.menu.content(
                    #         rx.menu.item("A propos de moi"),
                    #         rx.menu.item("Manifeste"),
                    #         rx.menu.item("Service 3"),
                    #     ),
                    # ),
                    navbar_link("A Propos", "/about"),
                    navbar_link("Blog", "/blog"),
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
                    rx.image(
                        src="\Logo.png",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Salim Houari", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("Services"),
                            rx.menu.sub_content(
                                rx.menu.item("Service 1"),
                                rx.menu.item("Service 2"),
                                rx.menu.item("Service 3"),
                            ),
                        ),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
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
        
    )
