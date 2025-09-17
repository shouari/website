import reflex as rx
from website.theme import PRIMARY_BG, container_style, heading_style, text_style, CTA_COLOR
from website.components.layout import base_page
from website.state import Blog_FormState



card_style = dict(
        
        border="1px solid rgba(0,0,0,0.06)",
        padding="2rem",
        border_radius="12px",
        height="100%",
    )


def blog_section() -> rx.Component:
    return  rx.box(
            rx.center(
                rx.markdown("# Blog\n\nBienvenue sur le blog! Ici, je posterais des articles, des conseils et des études de cas. Restez à l'écoute pour des mises à jour régulières!",
                            font_size=["1rem","1.05rem","1.1rem"],
                            text_align="justify",
                            
                            max_width="850px",
                            ),
            ),
            
        bg= PRIMARY_BG,
        padding_y=["2.5rem","3rem","4rem"],
        padding_x=["1rem","1.5rem","2rem"],
        width="100%",
        )

def blog_subscription():
    return rx.flex(
        rx.box(
            rx.vstack(
                rx.heading("Inscription au blog", size="6", margin_bottom="1rem"),
                rx.form(
                    rx.vstack(
                        rx.input(
                            placeholder="Prénom",
                            name="first_name",
                            required=True,
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Nom",
                            name="last_name",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Email",
                            name="email",
                            type="email",
                            required=True,
                            width="100%",
                        ),
                        rx.button(
                            "Soumettre",
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
            **card_style,
            bg="#372F9442",
            width=["90%", "70%", "400px"],  # responsive
        ),
        justify="center",
        align="center",
        padding="2rem",
    )


@rx.page(route="/blog")
def blog() -> rx.Component:
    return base_page(
        blog_section(),
        blog_subscription(),
    )