import reflex as rx
import reflex_enterprise as rxe

config = rxe.Config(
    app_name="website",
    use_single_port=True,
    show_built_with_reflex=False,

    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)