import reflex as rx
from website.components.layout import base_page
from website.theme import PRIMARY_BG, container_style, heading_style, text_style            



with open("website\content\\about.md", "r", encoding="utf-8") as f:
    about_text = f.read()

def about_section() -> rx.Component:
    return  rx.box(
            rx.center(
                rx.markdown(about_text,
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

@rx.page(route="/about")
def about() -> rx.Component:
    return base_page(
        about_section(),
    )