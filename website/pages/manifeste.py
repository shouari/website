import reflex as rx
from website.components.layout import base_page
from website.theme import PRIMARY_BG, container_style, heading_style, text_style            



with open("website/content/manifeste.md", "r", encoding="utf-8") as f:
    manifeste_text = f.read()

def manifeste_content() -> rx.Component:
    return  rx.box(
            rx.center(
                rx.markdown(manifeste_text,
                            font_size=["1rem","1.05rem","1.1rem"],
                            text_align="justify",
                            **text_style,
                            max_width="850px",
                            ),
            ),
        bg= PRIMARY_BG,
        padding_y=["2.5rem","3rem","4rem"],
        padding_x=["1rem","1.5rem","2rem"],
        width="100%",
        )

@rx.page(route="/manifeste", title="Manifeste - Clarifier, Simplifier, Automatiser")
def manifeste() -> rx.Component:
    return base_page(
        manifeste_content(),
    )