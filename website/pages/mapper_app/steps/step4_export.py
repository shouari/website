# website/pages/app/steps/step4_export.py

import reflex as rx
from website.state import ProcessMapperState
from website.theme import TEXT_MAIN, CTA_COLOR

def step4_export() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Exportation et Synthèse",
            size="6",
            color=TEXT_MAIN,
            margin_bottom="1rem"
        ),
        rx.text(
            "Voici le résumé de votre cartographie. Vous pouvez vous exporter ces données.",
            color="gray",
            size="3",
            margin_bottom="2rem"
        ),
        
        # Résumé
        rx.card(
            rx.vstack(
                rx.heading("Résumé du projet", size="4"),
                rx.text(f"Entreprise : {ProcessMapperState.company_name}"),
                rx.text(f"Secteur : {ProcessMapperState.sector}"),
                rx.divider(),
                rx.text(f"Nombre de tâches identifiées : {ProcessMapperState.tasks.length()}"),
                rx.text(f"Nombre d'étapes de processus : {ProcessMapperState.process_blocks.length()}"),
                
                width="100%",
                spacing="2"
            ),
            width="100%",
            padding="1.5rem",
            margin_bottom="2rem"
        ),
        
        # Actions d'export
        rx.hstack(
            rx.button(
                rx.hstack(rx.icon("file-json", size=20), rx.text("Exporter en JSON"), spacing="2"),
                on_click=rx.download(
                    data=ProcessMapperState.export_json_data,
                    filename="process_map.json",
                ),
                variant="outline",
                size="3"
            ),
            rx.button(
                rx.hstack(rx.icon("file-text", size=20), rx.text("Exporter en Markdown"), spacing="2"),
                on_click=rx.download(
                    data=ProcessMapperState.export_markdown_data,
                    filename="process_map.md",
                ),
                variant="outline",
                size="3"
            ),
            spacing="4",
            width="100%",
            justify="center"
        ),
        
        # Navigation Finale
        rx.hstack(
            rx.button(
                "Retour",
                on_click=ProcessMapperState.prev_step,
                variant="outline",
                color="gray",
                size="3"
            ),
            rx.spacer(),
            rx.button(
                "Recommencer",
                on_click=rx.redirect("/mapper"), # Reload or reset
                bg=CTA_COLOR,
                color="white",
                size="3"
            ),
            width="100%",
            margin_top="4rem"
        ),
        
        width="100%",
        align="start"
    )
