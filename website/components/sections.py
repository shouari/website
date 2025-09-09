# website/components/sections.py
# Section components for the Reflex application
# This file defines reusable section components with styles and layouts.


import reflex as rx
from website.theme import PRIMARY_BG, TEXT_MAIN, ACCENT, ACCENT_2, WHITE, container_style, heading_style, text_style, container_box_style


def section_container(*children, **kwargs) -> rx.Component:
    return rx.box(
        rx.vstack(*children, align="start", spacing="2"),
        # **section_style,
        **container_style,
        **kwargs,
    )



