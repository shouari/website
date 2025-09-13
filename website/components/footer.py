# 
# website/components/footer.py
# Footer component for the Reflex application
# This file defines the footer with links and styles.   


import reflex as rx
from website.theme import *

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("© Salim Houari ", color=TEXT_MAIN),
                rx.spacer(),
                rx.hstack(
                    rx.link(rx.icon(tag="linkedin", size=30, color="#0A66C2"),
                            href="https://www.linkedin.com/in/salim-houari/",
                            is_external=True,
                            aria_label="Mon profile LinkedIn" ,                    
                                   ),
                    justify="center",
                    align="center",                  
                ),
                align="center",
                width="100%",
            ),
            rx.text(
                "Clarifier. Simplifier. Automatiser.",
                color=TEXT_MAIN,
                opacity=0.8,
                font_size="1.2rem",
                text_align="center",
            ),
            align="center", 
        ),
        **container_style,
        width="100%",
        padding_y="0.5rem",
        border_top="1px solid rgba(0,0,0,0.06)",
        bg=CALYPSO_TRANSPARENT_20,
    )
