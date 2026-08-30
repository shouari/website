import os
import reflex as rx

config = rx.Config(
    app_name="website",
    api_url="https://www.salimhouari.com",
    deploy_url="https://www.salimhouari.com",
    backend_port=int(os.environ.get("PORT", 8080)),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)