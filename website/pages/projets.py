import reflex as rx
from markdown_it import MarkdownIt
from website.components.layout import base_page
from website.theme import BG_MAIN, TEXT_MAIN, TEXT_MUTED, VERT_CLAIR, BORDER

_md = MarkdownIt("commonmark")

_STYLE = (
    f"<style>"
    f".projet-md{{color:{TEXT_MAIN};font-size:1.05rem;line-height:1.75;max-width:750px;width:100%;}}"
    f".projet-md h1{{font-size:1.75rem;font-weight:700;margin:0 0 1.25rem;color:{TEXT_MAIN};}}"
    f".projet-md h2{{font-size:1.15rem;font-weight:600;margin:2rem 0 0.5rem;color:{TEXT_MAIN};}}"
    f".projet-md p{{margin:0.75rem 0;color:{TEXT_MUTED};}}"
    f".projet-md p strong{{font-weight:700;color:{TEXT_MAIN};}}"
    f".projet-md ul{{margin:0.5rem 0 0.75rem 1.5rem;padding:0;}}"
    f".projet-md li{{margin:0.35rem 0;color:{TEXT_MUTED};}}"
    f".projet-md hr{{border:none;border-top:1px solid {BORDER};margin:2rem 0;}}"
    f"</style>"
)


def _load(slug: str) -> str:
    with open(f"website/content/projets/{slug}.md", "r", encoding="utf-8") as f:
        return _STYLE + f'<div class="projet-md">{_md.render(f.read())}</div>'


_HTML = {
    "preparateur":  _load("preparateur"),
    "kpi-dashboard": _load("kpi-dashboard"),
    "rma":          _load("rma"),
    "call-logger":  _load("call-logger"),
    "qsys":         _load("qsys"),
}


def _page(slug: str) -> rx.Component:
    return base_page(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.link(
                        "← Retour aux projets",
                        href="/home#projets",
                        color=VERT_CLAIR,
                        size="2",
                        _hover={"opacity": "0.8"},
                        transition="opacity 0.2s ease",
                    ),
                    rx.html(_HTML[slug]),
                    spacing="5",
                    align="start",
                    max_width="750px",
                    width="100%",
                ),
                width="100%",
                padding_x=["1rem", "1.5rem", "2rem"],
            ),
            background=BG_MAIN,
            padding_y=["2.5rem", "3rem", "4rem"],
            width="100%",
        )
    )


def projet_preparateur() -> rx.Component:
    return _page("preparateur")


def projet_kpi_dashboard() -> rx.Component:
    return _page("kpi-dashboard")


def projet_rma() -> rx.Component:
    return _page("rma")


def projet_call_logger() -> rx.Component:
    return _page("call-logger")


def projet_qsys() -> rx.Component:
    return _page("qsys")
