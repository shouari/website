import reflex as rx
from website.components.layout import base_page
from website.theme import (
    BG_MAIN, BG_CARD, TEXT_MAIN, TEXT_MUTED, TEXT_DIM, VERT_CLAIR, BORDER, BORDER_VERT,
)

# ── Data ─────────────────────────────────────────────────────────────────────
# Une liste de dossiers. Chaque dossier regroupe une ou plusieurs publications
# sur un même sujet ; "chapeau" est optionnel (un dossier à une seule entrée
# n'en a pas besoin). Ajouter une publication = ajouter une entrée ici.

PUBLICATIONS = [
    {
        "titre": "Les irritants opérationnels — article et balado",
        "chapeau": (
            "Deux formats, un même sujet, publiés par l'Ordre des administrateurs "
            "agréés du Québec : ce qui rend une friction organisationnelle invisible, "
            "et comment un gestionnaire apprend à la repérer."
        ),
        "items": [
            {
                "format": "Article",
                "format_color": "blue",
                "titre": "Irritants opérationnels et sources de friction organisationnelle",
                "editeur": "Ordre des administrateurs agréés du Québec",
                "resume": (
                    "Pourquoi la performance stagne malgré l'engagement des équipes : "
                    "le travail prescrit et le travail réel divergent, et personne ne "
                    "prend le temps d'observer l'écart. L'article définit l'irritant "
                    "opérationnel et explique pourquoi l'identifier relève de la gestion, "
                    "pas du détail."
                ),
                "url": "https://www.adma.qc.ca/outils/articles/gestion/irritants-operationnels-et-sources-de-friction-organisationnelle/",
                "cta": "Lire l'article",
            },
            {
                "format": "Balado",
                "format_color": "green",
                "titre": "S8E13 — Les irritants opérationnels : ces frictions invisibles qui freinent la performance",
                "editeur": "Ordre des administrateurs agréés du Québec",
                "emission": "Profession gestionnaire, saison 2025-2026",
                "resume": (
                    "Entrevue avec Béatrice Aubry sur les frictions invisibles qui "
                    "ralentissent les organisations en changement continu, et sur "
                    "pourquoi clarifier les rôles et responsabilités doit précéder une "
                    "transformation, pas la suivre."
                ),
                "url": "https://www.adma.qc.ca/outils/baladodiffusion/saison-2025-2026/s8e13-les-irritants-operationnels-ces-frictions-invisibles-qui-freinent-la-performance/",
                "cta": "Écouter le balado",
            },
        ],
    },
]

AUTEUR_URL = "https://www.adma.qc.ca/auteurs/salim-houari/"


# ── Rendering ────────────────────────────────────────────────────────────────

def _outbound_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(f"{text} ↗", color=VERT_CLAIR, size="2", weight="medium"),
        href=url,
        target="_blank",
        rel="noopener",
        _hover={"opacity": "0.8"},
        transition="opacity 0.2s ease",
    )


def _publication_card(item: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.badge(item["format"], color_scheme=item["format_color"], variant="soft", size="1"),
            rx.heading(item["titre"], size="4", weight="bold", color=TEXT_MAIN, line_height="1.35"),
            rx.text(item["editeur"], color=VERT_CLAIR, size="2", weight="medium"),
            rx.text(item["emission"], color=TEXT_DIM, size="1") if "emission" in item else rx.fragment(),
            rx.text(item["resume"], color=TEXT_MUTED, size="2", line_height="1.7"),
            _outbound_link(item["cta"], item["url"]),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding="1.5rem",
        border_radius="12px",
        border=f"1px solid {BORDER}",
        background=BG_CARD,
        height="100%",
        _hover={"border_color": BORDER_VERT},
        transition="border-color 0.2s ease",
    )


def _dossier(dossier: dict) -> rx.Component:
    header = [
        rx.heading(dossier["titre"], size="5", weight="bold", color=TEXT_MAIN),
    ]
    if dossier.get("chapeau"):
        header.append(rx.text(dossier["chapeau"], color=TEXT_MUTED, size="3", line_height="1.7"))

    return rx.vstack(
        *header,
        rx.grid(
            *[_publication_card(item) for item in dossier["items"]],
            columns=rx.breakpoints(xs="1", md=str(min(len(dossier["items"]), 2))),
            gap="1.25rem",
            width="100%",
        ),
        spacing="4",
        align="start",
        width="100%",
    )


def publications_content() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "Publications",
                        font_size=["1.75rem", "2rem", "2.25rem"],
                        font_weight="700",
                        color=TEXT_MAIN,
                    ),
                    rx.text(
                        "Textes et entrevues publiés par des tiers — pas produits par moi, "
                        "pas hébergés ici.",
                        color=TEXT_MUTED,
                        size="3",
                    ),
                    spacing="2",
                    align="start",
                    width="100%",
                ),
                *[_dossier(d) for d in PUBLICATIONS],
                rx.box(
                    _outbound_link("Tous mes textes sur le site de l'Ordre", AUTEUR_URL),
                    padding_top="1rem",
                    border_top=f"1px solid {BORDER}",
                    width="100%",
                ),
                spacing="6",
                align="start",
                max_width="900px",
                width="100%",
            ),
            width="100%",
            padding_x=["1rem", "1.5rem", "2rem"],
        ),
        background=BG_MAIN,
        padding_y=["2.5rem", "3rem", "4rem"],
        width="100%",
    )


def publications() -> rx.Component:
    return base_page(publications_content())
