
import reflex as rx
import reflex_enterprise as rxe

from website.pages.index import index
from website.pages.about import about
from website.pages.blog import blog
from website.pages.manifeste import manifeste
from rxconfig import config


meta = [
    {"charset": "UTF-8"},
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    {"name": "theme-color", "content": "#2563EB"},
    {"name": "author", "content": "Salim Houari"},
    {"name": "robots", "content": "index, follow"},
    {"name": "keywords", "content": "optimisation, automatisation, PME, Québec, consultant, Salim Houari"},
    {"property": "og:type", "content": "website"},
    {"property": "og:url", "content": "https://www.salimhouari.com"},
    {"property": "og:image", "content": "/screenshot_home.png"},
    {"property": "og:site_name", "content": "Salim Houari"},
]


style={
    "font_family": "Sora, sans-serif",
}
app = rxe.App(style=style,
             head_components=[
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

             ])

app.add_page(index,
             title="Salim Houari - Consultant en optimisation des opérations",
             description="Clarifier, Simplifier, Automatiser les opérations de votre entreprise.",
             image="/Logo.png",
             meta=meta)
app.add_page(about,
             title="À propos - Salim Houari",
             description="Découvrez mon parcours et ma mission pour aider les entreprises à optimiser leurs opérations.",
             image="/Logo.png",
             meta=meta)
             

# app.add_page(blog,
#              title="Blog - Salim Houari",
#              description="Bienvenue sur le blog! Articles, conseils et ressources pour optimiser vos opérations et automatiser vos processus.",
#              image="/Logo.png",
#              meta=meta)

app.add_page(manifeste,
             title="Manifeste - Salim Houari",
             description="Découvrez le manifeste qui guide ma mission: Clarifier, Simplifier, Automatiser les opérations pour une efficacité maximale.",
             image="/Logo.png",
             meta=meta)

