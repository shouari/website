import reflex as rx
import reflex_enterprise as rxe

config = rx.Config(
    app_name="website",

    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)