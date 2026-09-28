import os
import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin, sitemap_task


def _sitemap_task_https_fix(unevaluated_pages, trailing_slash):
    # reflex_base.plugins.sitemap.generate_xml() code en dur
    # xmlns="https://www.sitemaps.org/..." — le protocole sitemap exige
    # http:// pour cet identifiant de namespace (jamais résolu, sans rapport
    # avec le schéma https du fichier lui-même). Sans effet si Reflex corrige
    # ça en amont : le replace() ne trouve alors simplement rien à remplacer.
    path, xml = sitemap_task(unevaluated_pages, trailing_slash)
    xml = xml.replace(
        'xmlns="https://www.sitemaps.org/',
        'xmlns="http://www.sitemaps.org/',
        1,
    )
    return path, xml


class _SitemapPluginHttpsFix(SitemapPlugin):
    def pre_compile(self, **context):
        unevaluated_pages = context.get("unevaluated_pages", [])
        context["add_save_task"](_sitemap_task_https_fix, unevaluated_pages, self.trailing_slash)


config = rx.Config(
    app_name="website",
    api_url="https://www.salimhouari.com",
    deploy_url="https://www.salimhouari.com",
    backend_port=int(os.environ.get("PORT", 8080)),
    plugins=[
        _SitemapPluginHttpsFix(trailing_slash="always"),
        rx.plugins.TailwindV4Plugin(),
    ],
)