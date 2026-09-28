
import json
import re
import reflex as rx
from starlette.responses import RedirectResponse
from starlette.middleware.gzip import GZipMiddleware

from website.pages.index import index
from website.pages.about import about
from website.pages.manifeste import manifeste
from website.pages.publications import publications
# Désactivé temporairement (routes /mapper et /contact retirées, 404) — décommenter pour réactiver.
# from website.pages.mapper_app.mapper import mapper
# from website.state import ProcessMapperState
from website.pages.auth.login import login_page
# from website.pages.contact import contact_page
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
    {"name": "geo.region", "content": "CA-QC"},
    {"name": "geo.placename", "content": "Laval, Québec, Canada"},
    {"property": "og:type", "content": "website"},
    {"property": "og:site_name", "content": "Salim Houari"},
    {"property": "og:image", "content": "https://www.salimhouari.com/screenshot_home.png"},
    {"property": "og:locale", "content": "fr_CA"},
    {"name": "twitter:card", "content": "summary"},
]


def _canonical_url(route: str) -> str:
    # Chaque route sans "/" final fait un 307 vers sa forme avec "/" (voir
    # api_transformer plus bas) : le canonical doit pointer sur l'URL qui
    # répond 200 directement, jamais sur une URL qui redirige.
    if route == "/":
        return "https://www.salimhouari.com/"
    return f"https://www.salimhouari.com{route}/"


def _meta(
    route: str, og_title: str, og_desc: str, keywords: str = "", noindex: bool = False
) -> list:
    m = _META_BASE + [
        {"name": "robots", "content": "noindex, follow" if noindex else "index, follow"},
        {"property": "og:url", "content": f"https://www.salimhouari.com{route}"},
        {"property": "og:title", "content": og_title},
        {"property": "og:description", "content": og_desc},
        rx.el.link(rel="canonical", href=_canonical_url(route)),
    ]
    if keywords:
        m.append({"name": "keywords", "content": keywords})
    return m


# ── App ────────────────────────────────────────────────────────────────────────
# Railway termine le TLS à l'edge et transmet en HTTP en interne. Sans ceci, le
# scope ASGI voit scheme="http" et la redirection de canonisation de barre
# oblique (/about → /about/) part en http://, provoquant une boucle de
# redirection pour les clients qui refusent la rétrogradation https→http.

def _trust_railway_proxy(asgi_app):
    async def wrapped(scope, receive, send):
        if scope["type"] == "http":
            headers = dict(scope.get("headers", []))
            proto = headers.get(b"x-forwarded-proto", b"").decode()
            if proto:
                scope["scheme"] = proto
        await asgi_app(scope, receive, send)
    return wrapped


# /home est remplacé par / comme accueil unique — les anciens liens/favoris
# doivent atterrir sur l'URL canonique en un seul saut, pas sur une page morte.
_LEGACY_REDIRECTS = {"/home": "/", "/home/": "/"}


def _redirect_legacy_routes(asgi_app):
    async def wrapped(scope, receive, send):
        if scope["type"] == "http" and scope.get("path") in _LEGACY_REDIRECTS:
            target = _LEGACY_REDIRECTS[scope["path"]]
            query = scope.get("query_string", b"").decode()
            if query:
                target = f"{target}?{query}"
            response = RedirectResponse(url=target, status_code=301)
            await response(scope, receive, send)
            return
        await asgi_app(scope, receive, send)
    return wrapped


# Fichiers Vite à empreinte de contenu : "-<hash 8 car.>.<ext>" en fin de nom,
# ex. "chunk-OE4NN4TA-D7kNFO7C.js", "__reflex_global_styles-rbAStlxI.css".
# Restreint à /assets/ (seul dossier où vivent ces fichiers).
_HASHED_ASSET_RE = re.compile(r"-[A-Za-z0-9_-]{8}\.(?:js|css|woff2?)$")
_STATIC_IMAGE_RE = re.compile(r"\.(?:png|ico|jpe?g|gif|svg|webp)$", re.IGNORECASE)


def _cache_control_for(path: str, content_type: str) -> str | None:
    if path.startswith("/assets/") and _HASHED_ASSET_RE.search(path):
        return "public, max-age=31536000, immutable"
    if content_type.startswith("text/html"):
        return "no-cache"
    if _STATIC_IMAGE_RE.search(path):
        return "public, max-age=86400"
    return None  # API, redirections, sitemap.xml, robots.txt : inchangé


def _add_cache_control(asgi_app):
    async def wrapped(scope, receive, send):
        path = scope.get("path", "")
        if (
            scope["type"] != "http"
            or scope.get("method") not in ("GET", "HEAD")
            or path.startswith("/_event")
            or path.startswith("/_upload")
        ):
            await asgi_app(scope, receive, send)
            return

        async def send_with_cache_control(message):
            if message["type"] == "http.response.start":
                headers = message.get("headers", [])
                if any(k.lower() == b"cache-control" for k, v in headers):
                    await send(message)  # déjà défini en aval : on ne touche pas
                    return
                content_type = ""
                for k, v in headers:
                    if k.lower() == b"content-type":
                        content_type = v.decode(errors="ignore")
                        break
                value = _cache_control_for(path, content_type)
                if value is not None:
                    message = {**message, "headers": [*headers, (b"cache-control", value.encode())]}
            await send(message)

        await asgi_app(scope, receive, send_with_cache_control)
    return wrapped


def _gzip_excluding_realtime(asgi_app):
    # GZipMiddleware ignore déjà les scopes non-http (donc les WebSocket), mais
    # Socket.IO expose aussi un transport HTTP long-polling sur /_event.
    compressed = GZipMiddleware(asgi_app, minimum_size=500, compresslevel=6)

    async def wrapped(scope, receive, send):
        path = scope.get("path", "")
        if scope["type"] == "http" and (path.startswith("/_event") or path.startswith("/_upload")):
            await asgi_app(scope, receive, send)
            return
        # Granian annonce l'extension ASGI "http.response.pathsend" ; Starlette
        # l'utilise alors pour un envoi de fichier "zero-copy" qui contourne
        # http.response.body -- et GZipMiddleware ignore explicitement ces
        # réponses (rien à compresser dans son propre flux). On retire
        # l'extension pour forcer l'envoi classique, seul chemin compressible.
        extensions = scope.get("extensions")
        if scope["type"] == "http" and extensions and "http.response.pathsend" in extensions:
            scope = {
                **scope,
                "extensions": {k: v for k, v in extensions.items() if k != "http.response.pathsend"},
            }
        await compressed(scope, receive, send)
    return wrapped


app = rx.App(
    api_transformer=[
        _redirect_legacy_routes,
        _gzip_excluding_realtime,
        _add_cache_control,
        _trust_railway_proxy,
    ],
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
        # Ahrefs Web Analytics
        rx.script(src="https://analytics.ahrefs.com/analytics.js", custom_attrs={"data-key": "vM7QrhHoNCp9Fn3zHpXKrA"}, async_=True),
        # lang="fr-CA" on <html> (Reflex 0.9.x doesn't expose html_lang in config)
        rx.script("document.documentElement.setAttribute('lang','fr-CA');"),
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
        "/",
        og_title="Salim Houari | Amélioration continue & Automatisation",
        og_desc="Expert en transformation opérationnelle et automatisation. 5 outils déployés en production. Laval, QC.",
        keywords="amélioration continue, automatisation processus, coordonnateur opérations, Lean Kaizen, BPMN, ISO TC279, Laval Québec, consultant PME",
    ),
    context={"sitemap": {"priority": 1.0}},
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
    context={"sitemap": {"priority": 0.8}},
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
    context={"sitemap": {"priority": 0.8}},
)

app.add_page(
    publications,
    title="Publications — Salim Houari | Ordre des administrateurs agréés du Québec",
    description=(
        "Article et balado sur les irritants opérationnels, publiés par l'Ordre "
        "des administrateurs agréés du Québec. Salim Houari, Adm.A."
    ),
    image="/Logo.png",
    meta=_meta(
        "/publications",
        og_title="Publications — Salim Houari",
        og_desc="Article et balado publiés par l'Ordre des administrateurs agréés du Québec.",
    ),
    context={"sitemap": {"priority": 0.8}},
)

# Désactivé temporairement — /mapper et /contact renvoient 404. Décommenter
# (et les imports correspondants plus haut) pour réactiver.
# app.add_page(
#     mapper,
#     route="/mapper",
#     title="Cartographie de processus — Outil gratuit | Salim Houari",
#     description="Outil gratuit pour cartographier et documenter vos processus opérationnels.",
#     image="/Logo.png",
#     on_load=ProcessMapperState.check_token_on_load,
#     meta=_meta(
#         "/mapper",
#         og_title="Cartographie de processus — Salim Houari",
#         og_desc="Outil gratuit pour cartographier et documenter vos processus opérationnels.",
#         noindex=True,
#     ),
#     context={"sitemap": None},
# )
#
# app.add_page(
#     contact_page,
#     route="/contact",
#     title="Contact — Salim Houari",
#     description="Contactez Salim Houari pour discuter de vos projets d'optimisation et d'automatisation.",
#     image="/Logo.png",
#     meta=_meta(
#         "/contact",
#         og_title="Contact — Salim Houari",
#         og_desc="Contactez Salim Houari pour discuter de vos projets d'optimisation.",
#         noindex=True,
#     ),
#     context={"sitemap": None},
# )

app.add_page(
    projet_preparateur,
    route="/projets/preparateur",
    title="Préparateur d'intervention — Salim Houari",
    description="Brief IA avant chaque appel de service. Envoi automatique au technicien. Python · Reflex · Claude API.",
    image="/Logo.png",
    meta=_meta("/projets/preparateur", og_title="Préparateur d'intervention — Salim Houari", og_desc="Brief IA avant chaque appel de service. Standardisation à 100 % des interventions."),
    context={"sitemap": {"priority": 0.6}},
)

app.add_page(
    projet_kpi_dashboard,
    route="/projets/kpi-dashboard",
    title="Dashboard KPI SAV — Salim Houari",
    description="Données SAV rendues lisibles et exploitables. Rapport mensuel automatisé. 2 ans d'historique. Python · Streamlit · Pandas · Plotly.",
    image="/Logo.png",
    meta=_meta("/projets/kpi-dashboard", og_title="Dashboard KPI SAV — Salim Houari", og_desc="Des données opérationnelles illisibles rendues exploitables. Rapport mensuel automatisé, KPI validés par la direction."),
    context={"sitemap": {"priority": 0.6}},
)

app.add_page(
    projet_rma,
    route="/projets/rma",
    title="App RMA — Suivi des retours | Salim Houari",
    description="Outil de suivi du cycle de retour produit — prototype fonctionnel, validation terrain en cours. Python · Reflex · Supabase · Brevo.",
    image="/Logo.png",
    meta=_meta("/projets/rma", og_title="App RMA — Suivi des retours | Salim Houari", og_desc="Outil de suivi RMA de bout en bout — prototype fonctionnel, validation terrain en cours.", noindex=True),
    context={"sitemap": None},
)

app.add_page(
    projet_call_logger,
    route="/projets/call-logger",
    title="Call Logger 3CX — Salim Houari",
    description="100 % des appels SAV documentés. Déclenchement automatique à la sonnerie 3CX. Python · Streamlit.",
    image="/Logo.png",
    meta=_meta("/projets/call-logger", og_title="Call Logger 3CX — Salim Houari", og_desc="100 % des appels entrants documentés. Déclenchement automatique, zéro friction."),
    context={"sitemap": {"priority": 0.6}},
)

app.add_page(
    projet_qsys,
    route="/projets/qsys",
    title="Système Q-SYS AV/Domotique — Salim Houari",
    description="Framework d'interfaces HTML standalone pour piloter QSC Q-SYS. HTML · JS · QRC.",
    image="/Logo.png",
    meta=_meta("/projets/qsys", og_title="Système Q-SYS AV/Domotique — Salim Houari", og_desc="3 interfaces déployables hors-ligne sur tablette. Framework réutilisable pour intégrateurs AV.", noindex=True),
    context={"sitemap": None},
)
