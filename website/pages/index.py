# website/pages/index.py
# Index page for the Reflex application
# This file defines the main content of the homepage with sections and components.

import reflex as rx
from website.components.layout import base_page
from website.components.sections import section_container
from website.theme import PRIMARY_BG, TEXT_MAIN, ACCENT, ACCENT_2, WHITE, container_style, heading_style, text_style, container_box_style


def hero() -> rx.Component:
    return rx.box(
        
        rx.box(
            rx.vstack(
                rx.heading("Clarifier. Simplifier. Automatiser.", font_size=["2rem","2.4rem","3rem"], **heading_style),
                rx.text(
                    "Des solutions concrètes pour que gagner en efficacité et en sérénité.",
                    font_size=["1rem","1.05rem","1.1rem"],
                    **text_style,
                ),
                # rx.hstack(
                #     rx.link(
                #         rx.button("Prendre rendez-vous", bg=ACCENT, color=WHITE, size="4", _hover={"opacity":0.9}),
                #         href="/contact",
                #         aria_label="Prendre rendez-vous",
                #     ),
                #     rx.link(
                #         rx.button("Lire le manifeste", variant="outline", border_color=ACCENT, color=TEXT_MAIN, size="4", _hover={"bg":"rgba(37,99,235,0.06)"}),
                #         href="/manifeste",
                #         aria_label="Lire le manifeste",
                #     ),
                #     spacing="4",
                # ),
                spacing="4",
                align="center",
                padding_y="5rem",
            ),
        ),
        # **section_style,
        bg=PRIMARY_BG,
        width="100%",
    )

def intro_section() -> rx.Component:
    with open("website\content\intro.md", "r", encoding="utf-8") as f:
        markdown_text = f.read()
    
    return  rx.box(
            rx.image(
            src="/smoke.svg",
            position="absolute",
            top="0%",
            left="0",
            # transform="translate(-50%, -50%)",
            width="100%",
            height="auto",
            opacity=0.1,
            z_index=0,
            style={"pointer-events": "none"},
        ),


            rx.center(
                section_container(
                    rx.markdown(markdown_text,
                                **text_style,
                                font_size=["1rem","1.05rem","1.1rem"],
                                text_align="center",
                                max_width="850px",
                                
                                ),
            ),
            ),
        bg= PRIMARY_BG,
        )
   

def three_pillars() -> rx.Component:

    with open("website\content\card_clarifier.md", "r", encoding="utf-8") as f:
        card_clarifier_text = f.read()

    with open("website\content\card_simplifier.md", "r", encoding="utf-8") as f:
        card_simplifier_text = f.read()
    with open("website\content\card_automatiser.md", "r", encoding="utf-8") as f:
        card_automatiser_text = f.read()

    card_style = dict(
        
        border="1px solid rgba(0,0,0,0.06)",
        padding="2rem",
        border_radius="12px",
        width="100%",
        height="100%",
    )
    return section_container(
        
        rx.heading("Une méthode en 3 étapes: CSA", font_size=["1.4rem","1.6rem","1.8rem"],
                    **heading_style ,                  
                    text_align="center",
                    width="100%",
                    margin_top="2rem",
                    ),
        rx.grid(
            rx.box(
                rx.markdown(card_clarifier_text,
                            **text_style,
                            font_size="1rem",
                            ),
               
                **card_style,
                bg="rgba(0,66,95,0.1)",  # dark semi-transparent
                backdrop_filter="blur(9px)",
                _hover={
                    "bg" : "#442F9445"},
            ),
            rx.box(
                rx.markdown(card_simplifier_text,
                            **text_style,
                            font_size="1rem",
                            ),
                **card_style,
                bg="rgba(0,66,95,0.1)",  # dark semi-transparent
                backdrop_filter="blur(9px)",
                _hover={
                    "bg" : "#442F9445"},
            ),
            rx.box(
                rx.markdown(card_automatiser_text,
                            **text_style,
                            font_size="1rem",
                            ),
                **card_style,
                bg="rgba(0,66,95,0.1)",  # dark semi-transparent
                backdrop_filter="blur(9px)",
                _hover={
                    "bg" : "#442F9445"},
            ),
            columns=rx.breakpoints(xs="1fr", md=" repeat(3, 1fr)"),
            gap="1rem",
            width="100%",
            padding_y="2rem",
        ),
      bg= PRIMARY_BG,  
    )

def cta_banner() -> rx.Component:
    return rx.box(
        rx.center(  # ✅ Centrage horizontal du contenu
            rx.vstack(
                rx.text(
                    "Et si on voyait ensemble comment gagner en efficacité ?",
                    font_size=["1.4rem", "1.6rem", "1.8rem"],
                    font_weight="800",
                    color="white",
                    text_align="center",
                ),
                rx.text(
                    "Prenons un moment pour explorer vos défis opérationnels. Sans engagement.",
                    font_size="md",
                    color="white",
                    opacity="0.9",
                    text_align="center",
                    max_width="600px",   # ✅ évite une ligne trop longue
                ),
                rx.link(
                    rx.button(
                        "Réserver un appel gratuit",
                        size="4",
                        color=ACCENT,
                        bg="white",
                        _hover={"opacity": 0.9}
                    ),
                    href="/contact",
                ),
                spacing="3",
                align="center",
                width="100%",
                padding_x="1rem",       # ✅ ajout pour petits écrans
            ),
            max_width="auto",
            width="100%",
                   ),
        bg="linear-gradient(180deg, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.3))",
        padding_y="1rem",  # ✅ un peu plus d’air
        width="100%",
        backdrop_filter="blur(10px)"

        
    )



@rx.page(route="/home")
def index() -> rx.Component:
    return base_page(
        hero(),
        intro_section(),
        three_pillars(),
        cta_banner(),
    )




