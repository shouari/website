import reflex as rx
from website.state import CTA_State
from website.components.layout import base_page
from website.components.sections import section_container
from website.theme import PRIMARY_BG, TEXT_MAIN, ACCENT, ACCENT_2, WHITE, container_style, heading_style, text_style, container_box_style, CTA_COLOR

card_style = dict(
    border="1px solid rgba(0,0,0,0.06)",
    padding="2rem",
    border_radius="12px",
    width="100%",
    height="100%",
)

def hero() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Clarifier. Simplifier. Automatiser.", 
                    font_size=["2rem", "2.4rem", "3rem"], 
                    text_align="center",
                    **heading_style
                ),
                rx.text(
                    "Des solutions concrètes pour gagner en efficacité et en sérénité.",
                    font_size=["1rem", "1.05rem", "1.1rem"],
                    text_align="center",
                    **text_style,
                ),
                spacing="4",
                align="center",
                padding_y=["3rem", "4rem", "5rem"],
            ),
        ),
        bg=PRIMARY_BG,
        width="100%",
    )

def intro_section() -> rx.Component:
    with open("website/content/intro.md", "r", encoding="utf-8") as f:
        markdown_text = f.read()

    return rx.box(
        rx.center(
            section_container(
                rx.markdown(
                    markdown_text,
                    **text_style,
                    font_size=["1rem", "1.05rem", "1.1rem"],
                    text_align="center",
                    max_width="850px",
                    width="100%"
                )
            )
        ),
        bg=PRIMARY_BG,
        padding_y=["3rem", "4rem", "5rem"]
    )

def three_pillars() -> rx.Component:
    with open("website/content/card_clarifier.md", "r", encoding="utf-8") as f:
        card_clarifier_text = f.read()
    with open("website/content/card_simplifier.md", "r", encoding="utf-8") as f:
        card_simplifier_text = f.read()
    with open("website/content/card_automatiser.md", "r", encoding="utf-8") as f:
        card_automatiser_text = f.read()

    return section_container(
        rx.heading(
            rx.text("Une méthode en 3 étapes: ", display="inline"),
            rx.text("CSA", color="#C83541", display="inline"),
            **heading_style,
            text_align="center",
            width="100%",
            margin_top="2rem",
        ),
        rx.grid(
            rx.box(
                rx.markdown(card_clarifier_text, **text_style, font_size="1rem"),
                **card_style,
                bg="#00425f10",
                backdrop_filter="blur(5px)",
                _hover={"bg": "#442F9445"},
            ),
            rx.box(
                rx.markdown(card_simplifier_text, **text_style, font_size="1rem"),
                **card_style,
                bg="#00425f10",
                backdrop_filter="blur(5px)",
                _hover={"bg": "#442F9445"},
            ),
            rx.box(
                rx.markdown(card_automatiser_text, **text_style, font_size="1rem"),
                **card_style,
                bg="#00435F10",
                backdrop_filter="blur(5px)",
                _hover={"bg": "#442F9445"},
            ),
            columns=rx.breakpoints(xs="1fr", md="repeat(3, 1fr)"),
            gap="1rem",
            width="100%",
            padding_y=["3rem", "4rem", "5rem"]
        ),
    )

def goals() -> rx.Component:
    with open("website/content/goals_left.md", "r", encoding="utf-8") as f:
        goals_left_text = f.read()
    with open("website/content/goals_right.md", "r", encoding="utf-8") as f:
        goals_right_text = f.read()
    with open("website/content/forwho.md", "r", encoding="utf-8") as f:
        forwho_text = f.read()

    return section_container(
        rx.heading(
            rx.text("🎯 Ce que je fais (concrètement) ", display="inline"),
            **heading_style,
            text_align="center",
            width="100%",
            margin_top="2rem",
        ),
        rx.grid(
            rx.box(
                rx.markdown(goals_left_text, **text_style, font_size="1rem", link_target="_blank"),
                **card_style,
                backdrop_filter="blur(5px)",
            ),
            rx.box(
                rx.markdown(goals_right_text, **text_style, font_size="1rem"),
                **card_style,
                backdrop_filter="blur(5px)",
            ),
            columns=rx.breakpoints(xs="1fr", md="repeat(2, 1fr)"),
            gap="1rem",
            width="100%",
        ),
        rx.center(
            rx.markdown(
                forwho_text,
                **text_style,
                font_size=["1rem", "1.05rem", "1.1rem"],
                text_align="center",
                max_width="850px",
                width="100%"
            ),
            justify="center",
            **card_style,
            backdrop_filter="blur(5px)",
        ),
        bg="#00425f10",
        backdrop_filter="blur(5px)",
        border="1px solid rgba(0,0,0,0.06)",
        padding="2rem",
        border_radius="12px",
    )

def cta_banner() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Envie d’aller plus loin ?",
                    **heading_style,
                    padding_bottom="1rem",
                    text_align="center",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "📖 Lire mon manifeste",
                            size="2",
                            color=WHITE,
                            bg=CTA_COLOR,
                            _hover={"opacity": 0.7},
                        ),
                        href="/manifeste",
                    ),
                    rx.button(
                        "🗓️ Échanger avec moi",
                        on_click=CTA_State.open_dialog,
                        size="2",
                        color=WHITE,
                        bg=CTA_COLOR,
                        _hover={"opacity": 0.7},
                    ),
                    spacing="6",
                    justify="center",
                    wrap="wrap"
                ),
                rx.dialog.root(
                    rx.dialog.content(
                        rx.vstack(
                            rx.dialog.title("Me contacter", text_align="center", color=TEXT_MAIN),
                            rx.link(
                                "📧 salim@salimhouari.com",
                                href="mailto:salim@salimhouari.com?subject=Demande%20de%20contact&body=Bonjour%20Salim%2C%0A%0AJe%20souhaiterais%20prendre%20contact%20avec%20vous.%0A%0ACordialement%2C",
                                color=TEXT_MAIN,
                                font_size="1.1rem",
                                _hover={"text_decoration": "underline"},
                            ),
                            rx.hstack(
                                rx.spacer(),
                                rx.dialog.close(
                                    rx.button(
                                        "Fermer",
                                        on_click=CTA_State.close_dialog,
                                        bg=CTA_COLOR,
                                        size="2",
                                        border_radius="8px",
                                        _hover={"bg": "#bbb"},
                                    )
                                ),
                            ),
                            spacing="4",
                            align="stretch",
                            padding="1rem",
                        ),
                        **card_style,
                        bg="#13223885",
                        backdrop_filter="blur(5px)",
                    ),
                    open=CTA_State.dialog_open,
                    modal=False,
                    on_open_change=CTA_State.close_dialog,
                ),
                spacing="1",
                align="center",
                width="100%",
                padding_x="1rem",
            ),
            max_width="auto",
            width="100%",
        ),
        bg="#00435f20",
        backdrop_filter="blur(5px)",
        padding_y="1.5rem",
        margin_bottom="2rem",
    )

@rx.page(route="/home")
def index() -> rx.Component:
    return base_page(
        hero(),
        intro_section(),
        three_pillars(),
        goals(),
        cta_banner(),
    )
