import reflex as rx
from markdown_it import MarkdownIt
from website.components.layout import base_page
from website.theme import BG_MAIN, BG_CARD, VERT_CLAIR, TEXT_MAIN, TEXT_MUTED, BORDER, WHITE

with open("website/content/about.md", "r", encoding="utf-8") as f:
    _about_text = f.read()

_about_html = MarkdownIt("commonmark").render(_about_text)

_ABOUT_CSS = (
    f"<style>"
    f".about-md{{color:{TEXT_MAIN};font-size:1.05rem;line-height:1.75;max-width:750px;width:100%;text-align:justify;}}"
    f".about-md h1{{font-size:2rem;font-weight:700;margin:0 0 0.75rem;color:{TEXT_MAIN};}}"
    f".about-md h2{{font-size:1.35rem;font-weight:600;margin:1.75rem 0 0.5rem;color:{TEXT_MAIN};}}"
    f".about-md p{{margin:0.75rem 0;}}"
    f".about-md strong{{font-weight:700;color:{TEXT_MAIN};}}"
    f"</style>"
    f'<div class="about-md">{_about_html}</div>'
)


def about_section() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.html(_ABOUT_CSS),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "Prêt à améliorer vos opérations ?",
                            color=TEXT_MUTED,
                            size="2",
                            text_align="center",
                        ),
                        rx.link(
                            rx.button(
                                "📅 Discutons de votre situation",
                                size="3",
                                background=VERT_CLAIR,
                                color=WHITE,
                                border_radius="8px",
                                cursor="pointer",
                                _hover={"opacity": "0.85"},
                                transition="all 0.2s ease",
                            ),
                            href="mailto:salim@salimhouari.com?subject=Contact%20via%20salimhouari.com",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="2rem",
                    border_radius="16px",
                    background=BG_CARD,
                    border=f"1px solid {BORDER}",
                    width="100%",
                    max_width="750px",
                    text_align="center",
                ),
                spacing="8",
                align="center",
                max_width="750px",
                width="100%",
            ),
        ),
        background=BG_MAIN,
        padding_y=["2.5rem", "3rem", "4rem"],
        padding_x=["1rem", "1.5rem", "2rem"],
        width="100%",
    )


@rx.page(route="/about")
def about() -> rx.Component:
    return base_page(about_section())
