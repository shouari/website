# website/theme.py
# Application theme configuration for Reflex
# This file defines the color palette and styles used throughout the application.



import reflex as rx

PRIMARY_BG = "#F6F4F4F8"  # Fond clair
TEXT_MAIN  = "#111827"  # Texte principal
ACCENT     = "#2563EB"  # Bleu CTA
ACCENT_2   = "#2564EB28"  # Orange secondaire
WHITE      = "#FFFFFF"

# Styles utilitaires
container_style = dict(

    padding_x=["1rem","1.5rem","2rem"],
)

# section_style = dict(
#     padding_y=["2.5rem","3rem","4rem"],
# )

heading_style = dict(color=TEXT_MAIN, font_weight="700", line_height="1")
text_style    = dict(color=TEXT_MAIN, opacity=0.9)

container_box_style = dict(
    width="100%",
    max_width="1200px",
    mx="auto",
)
