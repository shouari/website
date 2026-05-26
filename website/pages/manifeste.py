import reflex as rx
from markdown_it import MarkdownIt
from website.components.layout import base_page
from website.theme import BG_MAIN, TEXT_MAIN, TEXT_MUTED, VERT_CLAIR, BORDER

with open("website/content/manifeste.md", "r", encoding="utf-8") as f:
    _manifeste_text = f.read()

_manifeste_html = MarkdownIt("commonmark").render(_manifeste_text)

_MANIFESTE_CSS = (
    f"<style>"
    f".manifeste-md{{color:{TEXT_MAIN};font-size:1.05rem;line-height:1.75;max-width:750px;width:100%;text-align:justify;}}"
    f".manifeste-md h1{{font-size:1.75rem;font-weight:700;margin:0 0 0.5rem;color:{TEXT_MAIN};}}"
    f".manifeste-md h2,.manifeste-md h3{{font-size:1.2rem;font-weight:600;margin:1.5rem 0 0.4rem;color:{TEXT_MAIN};}}"
    f".manifeste-md p{{margin:0.75rem 0;color:{TEXT_MAIN};}}"
    f".manifeste-md strong{{font-weight:700;color:{TEXT_MAIN};}}"
    f".manifeste-md em{{font-style:italic;}}"
    f".manifeste-md blockquote{{border-left:3px solid {VERT_CLAIR};padding:0.5rem 1rem;margin:1rem 0;color:{TEXT_MUTED};font-style:italic;}}"
    f".manifeste-md hr{{border:none;border-top:1px solid {BORDER};margin:1.5rem 0;}}"
    f".manifeste-md a{{color:{VERT_CLAIR};}}"
    f"</style>"
    f'<div class="manifeste-md">{_manifeste_html}</div>'
)


def manifeste_content() -> rx.Component:
    return rx.box(
        rx.center(
            rx.html(_MANIFESTE_CSS),
            width="100%",
            padding_x=["1rem", "1.5rem", "2rem"],
        ),
        background=BG_MAIN,
        padding_y=["2.5rem", "3rem", "4rem"],
        width="100%",
    )


@rx.page(route="/manifeste", title="Manifeste — Clarifier, Simplifier, Automatiser")
def manifeste() -> rx.Component:
    return base_page(manifeste_content())
