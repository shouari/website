
import json
import reflex as rx

from website.pages.index import index
from website.pages.about import about
from website.pages.manifeste import manifeste
from website.pages.mapper_app.mapper import mapper
from website.pages.auth.login import login_page
from website.pages.contact import contact_page
from website.pages.projets import (
    projet_preparateur,
    projet_kpi_dashboard,
    projet_rma,
    projet_call_logger,
    projet_qsys,
)
from rxconfig import config

# ── Schema.org JSON-LD (GEO — IA indexing) ────────────────────────────────────

_SCHEMA_PERSON = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Salim Houari",
    "jobTitle": "Coordonnateur de service | Amélioration continue & Automatisation",
    "description": (
        "Expert en amélioration continue, automatisation des processus et "
        "transformation opérationnelle. Adm.A., M.Sc. Génie mécanique, "
        "membre du comité miroir canadien ISO TC279. Développe des outils "
        "opérationnels déployés en production pour PME québécoises."
    ),
    "url": "https://www.salimhouari.com",
    "email": "salim@salimhouari.com",
    "sameAs": ["https://www.linkedin.com/in/salim-houari"],
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Laval",
        "addressRegion": "QC",
        "addressCountry": "CA",
    },
    "knowsAbout": [
        "Amélioration continue", "Lean Management", "Kaizen",
        "Automatisation des processus", "BPMN", "Camunda",
        "ISO TC279", "Management de l'innovation", "Python",
        "Reflex.dev", "Transformation opérationnelle",
        "Intégration AV", "QSC Q-SYS", "KPI Dashboard",
    ],
    "hasCredential": [
        {
            "@type": "EducationalOccupationalCredential",
            "name": "Administrateur Agréé (Adm.A.)",
            "recognizedBy": {
                "@type": "Organization",
                "name": "Ordre des administrateurs agréés du Québec (OAAQ)",
            },
        },
        {
            "@type": "EducationalOccupationalCredential",
            "name": "Maîtrise ès sciences (M.Sc.) — Génie mécanique",
            "recognizedBy": {
                "@type": "Organization",
                "name": "École Nationale Polytechnique d'Alger",
            },
        },
    ],
    "memberOf": {
        "@type": "Organization",
        "name": "Comité miroir canadien ISO TC279 — Management de l'innovation",
    },
    "knowsLanguage": ["fr", "en", "ar"],
}

_SCHEMA_WEBSITE = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Salim Houari — Amélioration continue & Automatisation",
    "url": "https://www.salimhouari.com",
    "description": (
        "Site personnel de Salim Houari, expert en amélioration continue "
        "et automatisation des processus. Projets opérationnels déployés "
        "en production. Laval, Québec, Canada."
    ),
    "inLanguage": "fr-CA",
    "author": {"@type": "Person", "name": "Salim Houari"},
}

# ── Meta helpers ───────────────────────────────────────────────────────────────

_META_BASE = [
    {"charset": "UTF-8"},
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    {"name": "theme-color", "content": "#0D1B2A"},
    {"name": "author", "content": "Salim Houari"},
    {"name": "robots", "content": "index, follow"},
    {"name": "geo.region", "content": "CA-QC"},
    {"name": "geo.placename", "content": "Laval, Québec, Canada"},
    {"property": "og:type", "content": "website"},
    {"property": "og:site_name", "content": "Salim Houari"},
    {"property": "og:image", "content": "https://www.salimhouari.com/screenshot_home.png"},
    {"property": "og:locale", "content": "fr_CA"},
    {"name": "twitter:card", "content": "summary"},
]


def _meta(route: str, og_title: str, og_desc: str, keywords: str = "") -> list:
    m = _META_BASE + [
        {"property": "og:url", "content": f"https://www.salimhouari.com{route}"},
        {"property": "og:title", "content": og_title},
        {"property": "og:description", "content": og_desc},
    ]
    if keywords:
        m.append({"name": "keywords", "content": keywords})
    return m


# ── App ────────────────────────────────────────────────────────────────────────

app = rx.App(
    style={"font_family": "Inter, sans-serif"},
    head_components=[
        # Fonts
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
        ),
        # Google Analytics
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-N4RHF8WZ8J", async_=True),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-N4RHF8WZ8J');
            window.addEventListener('popstate', () => {
                gtag('event', 'page_view', {
                    page_path: window.location.pathname + window.location.search
                });
            });
            """
        ),
        # lang="fr-CA" on <html> (Reflex 0.9.x doesn't expose html_lang in config)
        rx.script("document.documentElement.setAttribute('lang','fr-CA');"),
        # Canonical tag — dynamic, based on current URL
        rx.script(
            "(function(){"
            "var l=document.createElement('link');"
            "l.rel='canonical';"
            "l.href=window.location.origin+window.location.pathname;"
            "document.head.appendChild(l);"
            "})();"
        ),
        # JSON-LD — Schema.org Person + WebSite (GEO: ChatGPT, Perplexity, Claude, Gemini)
        rx.el.script(
            type="application/ld+json",
            dangerously_set_inner_html=json.dumps(_SCHEMA_PERSON, ensure_ascii=False),
        ),
        rx.el.script(
            type="application/ld+json",
            dangerously_set_inner_html=json.dumps(_SCHEMA_WEBSITE, ensure_ascii=False),
        ),
    ],
)

# ── Pages ──────────────────────────────────────────────────────────────────────

app.add_page(
    index,
    title="Salim Houari | Amélioration continue & Automatisation — Laval, QC",
    description=(
        "Coordonnateur de service et expert en amélioration continue. "
        "Développe des outils opérationnels à fort impact terrain. "
        "Adm.A., M.Sc., membre ISO TC279. Laval, Québec."
    ),
    image="/Logo.png",
    meta=_meta(
        "/home",
        og_title="Salim Houari | Amélioration continue & Automatisation",
        og_desc="Expert en transformation opérationnelle et automatisation. 5 outils déployés en production. Laval, QC.",
        keywords="amélioration continue, automatisation processus, coordonnateur opérations, Lean Kaizen, BPMN, ISO TC279, Laval Québec, consultant PME",
    ),
)

app.add_page(
    about,
    title="À propos — Salim Houari | Adm.A., M.Sc., ISO TC279",
    description=(
        "15 ans d'opérations réelles. Algérie, Qatar, Canada. "
        "Administrateur agréé (Adm.A.), M.Sc. Génie mécanique, membre ISO TC279."
    ),
    image="/Logo.png",
    meta=_meta(
        "/about",
        og_title="À propos — Salim Houari | Adm.A., M.Sc., ISO TC279",
        og_desc="15 ans d'opérations réelles. Algérie, Qatar, Canada. Administrateur agréé (Adm.A.), M.Sc. Génie mécanique.",
    ),
)

app.add_page(
    manifeste,
    title="Manifeste — Salim Houari | CSA : Clarifier, Simplifier, Automatiser",
    description="La méthode CSA appliquée aux opérations réelles. Sans promesses creuses. Salim Houari, Laval QC.",
    image="/Logo.png",
    meta=_meta(
        "/manifeste",
        og_title="Manifeste — Salim Houari | CSA : Clarifier, Simplifier, Automatiser",
        og_desc="La méthode CSA appliquée aux opérations réelles. Sans promesses creuses.",
    ),
)

app.add_page(
    mapper,
    title="Cartographie de processus — Outil gratuit | Salim Houari",
    description="Outil gratuit pour cartographier et documenter vos processus opérationnels.",
    image="/Logo.png",
    meta=_meta(
        "/mapper",
        og_title="Cartographie de processus — Salim Houari",
        og_desc="Outil gratuit pour cartographier et documenter vos processus opérationnels.",
    ),
)

app.add_page(
    contact_page,
    title="Contact — Salim Houari",
    description="Contactez Salim Houari pour discuter de vos projets d'optimisation et d'automatisation.",
    image="/Logo.png",
    meta=_meta(
        "/contact",
        og_title="Contact — Salim Houari",
        og_desc="Contactez Salim Houari pour discuter de vos projets d'optimisation.",
    ),
)

app.add_page(
    projet_preparateur,
    route="/projets/preparateur",
    title="Préparateur d'intervention — Salim Houari",
    description="Brief IA avant chaque appel de service. Envoi automatique au technicien. Python · Reflex · Claude API.",
    image="/Logo.png",
    meta=_meta("/projets/preparateur", og_title="Préparateur d'intervention — Salim Houari", og_desc="Brief IA avant chaque appel de service. Standardisation à 100 % des interventions."),
)

app.add_page(
    projet_kpi_dashboard,
    route="/projets/kpi-dashboard",
    title="Dashboard KPI SAV — Salim Houari",
    description="Données SAV rendues lisibles et exploitables. Rapport mensuel automatisé. 2 ans d'historique. Python · Streamlit · Pandas · Plotly.",
    image="/Logo.png",
    meta=_meta("/projets/kpi-dashboard", og_title="Dashboard KPI SAV — Salim Houari", og_desc="Des données opérationnelles illisibles rendues exploitables. Rapport mensuel automatisé, KPI validés par la direction."),
)

app.add_page(
    projet_rma,
    route="/projets/rma",
    title="App RMA — Suivi des retours | Salim Houari",
    description="Traçabilité complète du cycle de retour produit. Python · Reflex · Supabase · Brevo.",
    image="/Logo.png",
    meta=_meta("/projets/rma", og_title="App RMA — Suivi des retours | Salim Houari", og_desc="Traçabilité 100 % du cycle RMA. Procédure standardisée, indépendante des individus."),
)

app.add_page(
    projet_call_logger,
    route="/projets/call-logger",
    title="Call Logger 3CX — Salim Houari",
    description="100 % des appels SAV documentés. Déclenchement automatique à la sonnerie 3CX. Python · Streamlit.",
    image="/Logo.png",
    meta=_meta("/projets/call-logger", og_title="Call Logger 3CX — Salim Houari", og_desc="100 % des appels entrants documentés. Déclenchement automatique, zéro friction."),
)

app.add_page(
    projet_qsys,
    route="/projets/qsys",
    title="Système Q-SYS AV/Domotique — Salim Houari",
    description="Framework d'interfaces HTML standalone pour piloter QSC Q-SYS. HTML · JS · QRC.",
    image="/Logo.png",
    meta=_meta("/projets/qsys", og_title="Système Q-SYS AV/Domotique — Salim Houari", og_desc="3 interfaces déployables hors-ligne sur tablette. Framework réutilisable pour intégrateurs AV."),
)
