import reflex as rx
from website.theme import PRIMARY_BG, container_style, heading_style, text_style, CTA_COLOR
from website.components.layout import base_page
from website.state import Blog_FormState

# Données fictives
dummy_articles = [
    {
        "title": "Pourquoi clarifier avant d'automatiser ?",
        "date": "2025-09-11",
        "summary": "Trop souvent, on automatise le chaos. Cet article explique pourquoi il faut d’abord comprendre, cartographier et simplifier.",
        "tag": "Clarifier",
        "slug": "clarifier-avant-automatiser"
    },
    {
        "title": "Simplifier : art ou science ?",
        "date": "2025-09-05",
        "summary": "Réduire, structurer, alléger. Une réflexion sur la simplification comme stratégie.",
        "tag": "Simplifier",
        "slug": "simplifier-art-science"
    },
    {
        "title": "Automatiser sans coder",
        "date": "2025-08-30",
        "summary": "Les outils no-code comme n8n permettent aux PME d'automatiser sans développeur.",
        "tag": "Automatiser",
        "slug": "automatiser-sans-code"
    }
]
card_style = dict(
    padding="2rem",
    border_radius="12px",
    background_color="#1F2937",
    box_shadow="lg",
    transition="all 0.2s",
    height="100%",  # ✅ force même taille
    width="100%",
    max_width="24rem",  # optionnel
    _hover={"box_shadow": "xl", "transform": "scale(1.02)"},
)



def blog_hero() -> rx.Component:
    return rx.box(
        rx.heading("Articles & réflexions", **heading_style, text_align="center", font_size=["2rem", "2.4rem", "3rem"]),
        rx.center(
            rx.markdown(
                "Bienvenue sur mon blog. J'y partage des conseils concrets, des cas réels, et des réflexions autour de la méthode **CSA** : Clarifier, Simplifier, Automatiser.",
                font_size=["1rem", "1.05rem", "1.1rem"],
                text_align="justify",
                max_width="800px",
            )
        ),
        padding_y=["2.5rem", "3rem", "3.5rem"],
    )

def article_card(article: dict) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.text(article["title"], weight="bold", size="5"),
                rx.text(article["date"], size="2", color="gray"),
                rx.text(article["summary"], size="3", margin_top="0.5rem"),
                rx.badge(article["tag"], variant="soft", margin_top="0.5rem"),
                rx.spacer(),  # pousse le bouton vers le bas
                rx.flex(
                    rx.button(
                        "Lire l'article",
                        bg=CTA_COLOR,
                        color="white",
                        _hover={"opacity": 0.8},
                        size="2",
                    ),
                    justify="end",
                    width="100%",
                ),
                spacing="3",
                align="start",
                height="100%",
            ),
            **card_style,
        ),
        href=f"/article?slug={article['slug']}",  # ✅ nouveau lien simplifié
    )

def blog_grid() -> rx.Component:
    return rx.flex(
                *[article_card(article) for article in dummy_articles],
                wrap="wrap",
                justify="center",
                align="stretch",
                spacing="4",
)


def newsletter_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Restez informé", size="6", margin_bottom="1rem"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Prénom", name="first_name", required=True, width="100%"),
                    rx.input(placeholder="Nom", name="last_name", width="100%"),
                    rx.input(placeholder="Email", name="email", type="email", required=True, width="100%"),
                    rx.button(
                        "S'inscrire",
                        type="submit",
                        bg=CTA_COLOR,
                        color="white",
                        _hover={"opacity": 0.8},
                        align_self="center",
                        margin_top="1rem",
                    ),
                ),
                on_submit=Blog_FormState.handle_submit,
                reset_on_submit=True,
                width="100%",
            ),
        ),
        border="1px solid rgba(255,255,255,0.1)",
        border_radius="12px",
        padding="2rem",
        bg="#13223899",
        backdrop_filter="blur(6px)",
        width=["90%", "70%", "400px"],
    )

def blog_subscription() -> rx.Component:
    return rx.center(
        newsletter_form(),
        padding_y="3rem"
    )

@rx.page(route="/blog")
def blog() -> rx.Component:
    return base_page(
        rx.box(
            blog_hero(),
            blog_grid(),
            blog_subscription(),
            bg=PRIMARY_BG,
            padding_x=["1rem", "1.5rem", "2rem"],
            width="100%",
        )
    )
