# website/theme.py
# Application theme configuration for Reflex
# This file defines the color palette and styles used throughout the application.

# Color palette: https://tools.picsart.com/color/palette-generator/?colors=0F172A-2F7294-372F94-7D2F94-942F50


import reflex as rx

PRIMARY_BG = "#0f172a"

TEXT_MAIN  = "#F1F5F9"  # l
ACCENT     = "#372F94"  # 
ACCENT_2   = "#372F94"  # 
WHITE      = "#FFFFFF"
CALYPSO_TRANSPARENT_20      = "#132238"
CTA_COLOR = "#9A2E44"



# Styles utilitaires
container_style = dict(

    padding_x=["1rem","1.5rem","2rem"],
)

# section_style = dict(
#     padding_y=["2.5rem","3rem","4rem"],
# )

heading_style = dict(color=TEXT_MAIN, font_weight="700", line_height="1")
text_style    = dict(color=TEXT_MAIN, opacity=1)

container_box_style = dict(
    width="100%",
    max_width="1200px",
    mx="auto",
)
