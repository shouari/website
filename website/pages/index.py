import reflex as rx
from website.components.layout import base_page
from website.theme import (
    BG_MAIN, BG_CARD, MARINE_MID, VERT_TERRAIN, VERT_CLAIR, BLEU_ACCENT,
    TEXT_MAIN, TEXT_MUTED, TEXT_DIM, BORDER, BORDER_VERT, WHITE,
)

# ── Static data ────────────────────────────────────────────────────────────────

METRICS = [
    {"value": "12",   "label": "Techniciens briefés", "sub": "la veille de chaque intervention"},
    {"value": "712",  "label": "Appels coordonnés",   "sub": "par année"},
    {"value": "342k$","label": "Revenus pilotés",     "sub": "activité SAV"},
    {"value": "5",    "label": "Outils en production","sub": "déployés"},
]

# ── Shared micro-components ────────────────────────────────────────────────────

def pill(text: str) -> rx.Component:
    return rx.box(
        rx.text(text, color=VERT_CLAIR, size="2", weight="medium"),
        padding_x="0.875rem",
        padding_y="0.375rem",
        background="rgba(39,165,103,0.07)",
        border=f"1px solid {BORDER_VERT}",
        border_radius="999px",
        display="inline-block",
    )


def tag(text: str, color: str, bg: str, border_color: str) -> rx.Component:
    return rx.box(
        rx.text(text, size="1", color=color, weight="medium"),
        padding_x="0.5rem",
        padding_y="0.2rem",
        background=bg,
        border=f"1px solid {border_color}",
        border_radius="6px",
        display="inline-block",
    )


def label_upper(text: str) -> rx.Component:
    return rx.text(
        text, color=VERT_CLAIR, size="1", weight="bold", letter_spacing="0.1em"
    )


# ── HERO ──────────────────────────────────────────────────────────────────────

# CSS keyframe animation — rotates active state across 4 cards every 2.5s (cycle=10s)
_METRICS_CSS = """
<style>
@keyframes mcBg{
  0%,25%{background:rgba(39,165,103,0.08);border-color:rgba(39,165,103,0.25);}
  26%,100%{background:#111827;border-color:rgba(255,255,255,0.07);}
}
@keyframes mcTxt{0%,25%{color:#27A567;}26%,100%{color:#F0F4F8;}}
.mc{animation:mcBg 10s infinite;border:1px solid transparent;border-radius:12px;transition:background .3s,border-color .3s;}
.mc0{animation-delay:0s;}.mc1{animation-delay:-7.5s;}.mc2{animation-delay:-5s;}.mc3{animation-delay:-2.5s;}
.mv{animation:mcTxt 10s infinite;font-size:1.75rem;font-weight:800;line-height:1;}
.mv0{animation-delay:0s;}.mv1{animation-delay:-7.5s;}.mv2{animation-delay:-5s;}.mv3{animation-delay:-2.5s;}
</style>
"""


def metric_card(data: dict, index: int) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(data["value"], class_name=f"mv mv{index}"),
            rx.text(data["label"], size="2", color=TEXT_MAIN, text_align="center"),
            rx.text(data["sub"],   size="1", color=TEXT_MUTED, text_align="center"),
            spacing="1",
            align="center",
        ),
        class_name=f"mc mc{index}",
        padding="1rem 1.25rem",
        flex="1",
        min_width="130px",
        text_align="center",
    )


def hero_section() -> rx.Component:
    return rx.box(
        rx.html(_METRICS_CSS),
        rx.center(
            rx.vstack(
                pill("Adm.A. · M.Sc. · Membre ISO TC279"),
                rx.vstack(
                    rx.heading(
                        "J'améliore les opérations.",
                        font_size="clamp(1.8rem, 4vw, 3.25rem)",
                        font_weight="800",
                        letter_spacing="-0.03em",
                        color=TEXT_MAIN,
                        text_align="center",
                        line_height="1.15",
                    ),
                    rx.heading(
                        "Je construis les outils.",
                        font_size="clamp(1.8rem, 4vw, 3.25rem)",
                        font_weight="800",
                        letter_spacing="-0.03em",
                        color=BLEU_ACCENT,
                        text_align="center",
                        line_height="1.15",
                    ),
                    rx.heading(
                        "Je mesure les résultats.",
                        font_size="clamp(1.8rem, 4vw, 3.25rem)",
                        font_weight="800",
                        letter_spacing="-0.03em",
                        color=TEXT_MAIN,
                        text_align="center",
                        line_height="1.15",
                    ),
                    spacing="1",
                    align="center",
                ),
                rx.vstack(
                    rx.text(
                        "Amélioration continue & Automatisation — Laval, QC.",
                        color=TEXT_MUTED, size="3", text_align="center",
                    ),
                    rx.text(
                        "15 ans d'opérations réelles. 5 outils en production.",
                        color=TEXT_MUTED, size="3", text_align="center",
                    ),
                    spacing="1",
                    align="center",
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            "Voir les projets ↓",
                            background=VERT_CLAIR,
                            color=WHITE,
                            size="3",
                            border_radius="8px",
                            cursor="pointer",
                            _hover={"opacity": "0.85"},
                            transition="all 0.2s ease",
                        ),
                        href="#projets",
                    ),
                    rx.link(
                        rx.button(
                            "Discutons →",
                            color=TEXT_MAIN,
                            size="3",
                            border_radius="8px",
                            background="transparent",
                            border=f"1px solid {BORDER_VERT}",
                            cursor="pointer",
                            _hover={"background": "rgba(39,165,103,0.07)"},
                            transition="all 0.2s ease",
                        ),
                        href="mailto:salim@salimhouari.com",
                    ),
                    gap="1rem",
                    wrap="wrap",
                    justify="center",
                ),
                rx.flex(
                    metric_card(METRICS[0], 0),
                    metric_card(METRICS[1], 1),
                    metric_card(METRICS[2], 2),
                    metric_card(METRICS[3], 3),
                    gap="0.75rem",
                    wrap="wrap",
                    justify="center",
                    width="100%",
                    margin_top="0.5rem",
                ),
                spacing="6",
                align="center",
                max_width="820px",
                width="100%",
                padding_x=["1rem", "1.5rem", "2rem"],
            ),
        ),
        background=BG_MAIN,
        padding_y=["4rem", "5rem", "7rem"],
        width="100%",
    )


# ── CE QUI ME DISTINGUE ───────────────────────────────────────────────────────

def distinction_card(icon: str, title: str, text: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(icon, font_size="1.25rem"),
            rx.text(title, color=TEXT_MAIN, weight="bold", size="3"),
            rx.text(text, color=TEXT_MUTED, size="2", line_height="1.6"),
            spacing="2",
            align="start",
        ),
        padding="1.25rem",
        border_radius="12px",
        background=BG_CARD,
        border=f"1px solid {BORDER}",
        width="100%",
        transition="all 0.2s ease",
        _hover={"border_color": BORDER_VERT, "transform": "translateY(-2px)"},
    )


def distinction_section() -> rx.Component:
    return rx.box(
        rx.center(
            rx.grid(
                rx.vstack(
                    label_upper("CE QUI ME DISTINGUE"),
                    rx.vstack(
                        rx.text(
                            "La plupart font l'un ou l'autre.",
                            font_size=["1.5rem", "1.75rem", "2rem"],
                            font_weight="700",
                            color=TEXT_MAIN,
                            line_height="1.2",
                        ),
                        rx.text(
                            "Je fais les trois.",
                            font_size=["1.5rem", "1.75rem", "2rem"],
                            font_weight="700",
                            color=TEXT_MUTED,
                            line_height="1.2",
                        ),
                        spacing="0",
                    ),
                    rx.text(
                        "Comprendre les opérations terrain. Construire les outils qui les améliorent. "
                        "Mesurer l'impact en chiffres réels. Ces trois compétences dans un même profil — "
                        "c'est rare. C'est ce que je livre.",
                        color=TEXT_MUTED,
                        size="3",
                        line_height="1.75",
                    ),
                    rx.link(
                        "Discutons de votre situation →",
                        href="mailto:salim@salimhouari.com",
                        color=VERT_CLAIR,
                        size="3",
                        _hover={"opacity": "0.8"},
                        transition="opacity 0.2s ease",
                    ),
                    spacing="5",
                    align="start",
                ),
                rx.vstack(
                    rx.grid(
                        distinction_card("⊙", "Terrain",
                                         "Opérations réelles — pas les procédures idéales"),
                        distinction_card("⚡", "Outils",
                                         "Solutions qui tiennent sans surveillance constante"),
                        columns="2",
                        gap="0.75rem",
                        width="100%",
                    ),
                    distinction_card("◈", "Résultats mesurables",
                                     "Chaque intervention traduite en chiffres défendables"),
                    spacing="3",
                    width="100%",
                ),
                columns=rx.breakpoints(xs="1", md="2"),
                gap=["2rem", "2.5rem", "3rem"],
                max_width="1100px",
                width="100%",
                align_items="start",
            ),
            width="100%",
            padding_x=["1.5rem", "2rem", "3rem"],
        ),
        background=BG_MAIN,
        padding_y=["4rem", "5rem", "6rem"],
        width="100%",
    )


# ── PROJETS BENTO GRID ────────────────────────────────────────────────────────

def project_card(
    tag: str, tag_color: str,
    title: str,
    accroche: str,
    preuve: str,
    stack: str,
    statut: str,
    slug: str,
    class_name: str = "",
    gradient: str = BG_CARD,
) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.badge(tag, color_scheme=tag_color, variant="soft", size="1"),
            rx.heading(title, size="4", weight="bold", color=TEXT_MAIN),
            rx.text(accroche, color=TEXT_MUTED, size="2", line_height="1.7"),
            rx.text(preuve, color=VERT_CLAIR, size="1", weight="medium"),
            rx.hstack(
                rx.text(stack, color=TEXT_DIM, size="1", font_family="monospace"),
                rx.spacer(),
                rx.badge(statut, variant="outline", size="1"),
                width="100%",
                align="center",
            ),
            spacing="3",
            align="start",
            width="100%",
        ),
        padding="1.5rem",
        border_radius="12px",
        border=f"1px solid {BORDER}",
        background=gradient,
        cursor="pointer",
        height="100%",
        class_name=class_name,
        _hover={"border_color": BORDER_VERT, "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
        on_click=rx.redirect(f"/projets/{slug}"),
    )


def projets_section() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.text(
                    "PME intégration AV · Laval, QC · 2023–2026",
                    color=TEXT_MUTED, size="1", weight="medium", letter_spacing="0.08em",
                ),
                rx.heading(
                    "Pas des concepts. Des outils en production.",
                    font_size=["1.75rem", "2rem", "2.25rem"],
                    font_weight="700",
                    color=TEXT_MAIN,
                    text_align="center",
                    line_height="1.2",
                ),
                rx.text(
                    "5 outils développés en contexte réel. Chacun répond à un problème précis.",
                    color=TEXT_MUTED, size="3", text_align="center",
                ),
                rx.box(
                    # ── Row 1 ──
                    project_card(
                        tag="Intégration AV", tag_color="blue",
                        title="Interfaces de contrôle AV — Q-SYS",
                        accroche="Chaque projet réinventait ses interfaces de zéro. J'ai construit le framework pour ne plus jamais repartir de zéro.",
                        preuve="3 interfaces · 1 protocole · 0 dépendance externe",
                        stack="HTML · JS · QSC Q-SYS · QRC",
                        statut="Bêta fonctionnelle",
                        slug="qsys",
                        gradient=f"linear-gradient(135deg, {MARINE_MID}22, {BG_CARD})",
                        class_name="sm:col-span-2 md:col-span-2",
                    ),
                    project_card(
                        tag="Gestion des retours", tag_color="green",
                        title="App RMA — Suivi des retours produits",
                        accroche="Des retours gérés par email et Excel. Aucun dossier ne tombait dans les mailles — par chance.",
                        preuve="Relances automatiques · historique complet · zéro oubli",
                        stack="Python · Streamlit · PostgreSQL · Brevo",
                        statut="Déploiement en cours",
                        slug="rma",
                        gradient=f"linear-gradient(135deg, {VERT_TERRAIN}22, {BG_CARD})",
                    ),
                    # ── Row 2 ──
                    project_card(
                        tag="IA terrain", tag_color="blue",
                        title="Préparateur d'intervention",
                        accroche="La préparation d'un appel complexe prenait 1 à 2 heures. Elle en prend maintenant quelques minutes.",
                        preuve="12 techniciens · dispatch automatique · 16h30 la veille",
                        stack="Python · Streamlit · OpenAI API · Brevo",
                        statut="En production",
                        slug="preparateur",
                        gradient=f"linear-gradient(135deg, {MARINE_MID}22, {BG_CARD})",
                    ),
                    project_card(
                        tag="Pilotage opérationnel", tag_color="green",
                        title="Dashboard KPI SAV",
                        accroche="Les données existaient dans le système. Personne ne les lisait. Le dashboard a changé ça.",
                        preuve="2 ans d'historique · rapport mensuel automatisé · KPI validés direction",
                        stack="Python · Streamlit · Pandas · Plotly · OpenAI API",
                        statut="En production",
                        slug="kpi-dashboard",
                    ),
                    project_card(
                        tag="Qualification d'appels", tag_color="blue",
                        title="Qualification d'appel SAV",
                        accroche="Chacun notait ce qu'il voulait, comme il voulait. J'ai codifié les bonnes questions — celles qu'on pose toujours.",
                        preuve="Ouverture automatique à la sonnerie 3CX · 100% des appels structurés",
                        stack="Python · Streamlit · OpenStreetMap · 3CX",
                        statut="En production",
                        slug="call-logger",
                    ),
                    class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-5",
                    width="100%",
                ),
                spacing="6",
                align="center",
                max_width="1100px",
                width="100%",
            ),
            width="100%",
            padding_x=["1.5rem", "2rem", "3rem"],
        ),
        id="projets",
        background=BG_MAIN,
        padding_y=["4rem", "5rem", "6rem"],
        width="100%",
    )


# ── MÉTHODE CSA ───────────────────────────────────────────────────────────────

def methode_card(number: str, icon: str, title: str, text: str, badge_text: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(icon, font_size="1.5rem"),
                rx.spacer(),
                rx.text(number, font_size="2rem", font_weight="800",
                        color="rgba(255,255,255,0.08)", line_height="1"),
                align="center",
                width="100%",
            ),
            rx.text(title, color=TEXT_MAIN, weight="bold", size="4"),
            rx.text(text,  color=TEXT_MUTED, size="2", line_height="1.6"),
            tag(badge_text, TEXT_MUTED, "rgba(255,255,255,0.04)", BORDER),
            spacing="3",
            align="start",
        ),
        padding="1.5rem",
        border_radius="16px",
        background=BG_CARD,
        border=f"1px solid {BORDER}",
        transition="all 0.2s ease",
        _hover={"border_color": BORDER_VERT, "transform": "translateY(-3px)"},
    )


def methode_section() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                label_upper("APPROCHE DE TRAVAIL"),
                rx.heading(
                    "Le cadre CSA",
                    font_size=["1.75rem", "2rem", "2.25rem"],
                    font_weight="700",
                    color=TEXT_MAIN,
                    text_align="center",
                ),
                rx.grid(
                    methode_card("01", "◎", "Clarifier",
                                 "Observer les opérations réelles. Cartographier, mesurer, nommer ce qui coûte.",
                                 "Camunda · BPMN"),
                    methode_card("02", "⊘", "Simplifier",
                                 "Supprimer ce qui est inutile. Réduire les frictions avant d'outiller.",
                                 "Analyse · Redesign"),
                    methode_card("03", "⚙", "Automatiser",
                                 "Déployer les outils qui tiennent sans surveillance constante.",
                                 "n8n · Python · IA"),
                    columns=rx.breakpoints(xs="1", md="3"),
                    gap="1.25rem",
                    width="100%",
                ),
                spacing="6",
                align="center",
                max_width="1100px",
                width="100%",
            ),
            width="100%",
            padding_x=["1.5rem", "2rem", "3rem"],
        ),
        id="methode",
        background=BG_MAIN,
        padding_y=["4rem", "5rem", "6rem"],
        width="100%",
    )


# ── CTA FINAL ─────────────────────────────────────────────────────────────────

def cta_final_section() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                label_upper("PARLONS DE VOTRE SITUATION"),
                rx.vstack(
                    rx.text(
                        "Vous reconnaissez votre entreprise",
                        font_size=["1.75rem", "2rem", "2.25rem"],
                        font_weight="700",
                        color=TEXT_MAIN,
                        text_align="center",
                        line_height="1.2",
                    ),
                    rx.text(
                        "dans ce que je décris ?",
                        font_size=["1.75rem", "2rem", "2.25rem"],
                        font_weight="700",
                        color=TEXT_MUTED,
                        text_align="center",
                        line_height="1.2",
                    ),
                    spacing="0",
                    align="center",
                ),
                rx.text(
                    "Je travaille avec quelques organisations en mode exploratoire. "
                    "Si la conversation vaut la peine d'être eue, on le saura vite.",
                    color=TEXT_MUTED,
                    size="3",
                    text_align="center",
                    max_width="500px",
                    line_height="1.75",
                ),
                rx.link(
                    rx.button(
                        "Discutons →",
                        background=VERT_CLAIR,
                        color=WHITE,
                        size="3",
                        border_radius="8px",
                        cursor="pointer",
                        _hover={"opacity": "0.85"},
                        transition="all 0.2s ease",
                    ),
                    href="mailto:salim@salimhouari.com?subject=Prise%20de%20contact%20%E2%80%94%20CSA",
                ),
                spacing="6",
                align="center",
                max_width="700px",
                width="100%",
                padding_x=["1rem", "1.5rem", "2rem"],
            ),
            width="100%",
        ),
        background=(
            f"linear-gradient(135deg, {MARINE_MID}33 0%, {BG_MAIN} 50%, {VERT_TERRAIN}22 100%)"
        ),
        padding_y=["5rem", "6rem", "8rem"],
        width="100%",
    )


# ── PAGE ──────────────────────────────────────────────────────────────────────

@rx.page(route="/home")
def index() -> rx.Component:
    return base_page(
        hero_section(),
        distinction_section(),
        projets_section(),
        methode_section(),
        cta_final_section(),
    )
