# website/pages/app/steps/step2_tasks.py

import reflex as rx
from website.state import ProcessMapperState
from website.theme import TEXT_MAIN, CTA_COLOR

def step2_tasks() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Listez vos tâches principales",
            size="6",
            color=TEXT_MAIN,
            margin_bottom="1rem"
        ),
        rx.text(
            "Ajoutez les tâches clés que vous souhaitez cartographier.",
            color="gray",
            size="3",
            margin_bottom="2rem"
        ),
        
        # Formulaire d'ajout de tâche
        rx.vstack(
            rx.input(
                placeholder="Nom de la tâche",
                value=ProcessMapperState.current_task_name,
                on_change=ProcessMapperState.set_current_task_name,
                size="3",
                width="100%"
            ),
            rx.select(
                ["Quotidienne", "Hebdomadaire", "Mensuelle", "Ponctuelle"],
                placeholder="Fréquence",
                value=ProcessMapperState.current_task_frequency,
                on_change=ProcessMapperState.set_current_task_frequency,
                size="3",
                width="100%"
            ),
            rx.button(
                "Ajouter la tâche",
                on_click=ProcessMapperState.add_task,
                bg=CTA_COLOR,
                color="white",
                size="2"
            ),
            spacing="2",
            width="100%",
            max_width="600px",
            margin_bottom="2rem"
        ),
        
        # Liste des tâches
        rx.cond(
            ProcessMapperState.tasks.length() > 0,
            rx.vstack(
                rx.foreach(
                    ProcessMapperState.tasks,
                    lambda task: rx.card(
                        rx.hstack(
                            rx.text(task["name"], weight="bold", color=TEXT_MAIN),
                            rx.spacer(),
                            rx.button(
                                rx.icon("trash-2", size=16),
                                on_click=lambda: ProcessMapperState.remove_task(task["id"]),
                                variant="ghost",
                                size="1",
                                color="red"
                            ),
                            width="100%",
                            align="center"
                        ),
                        padding="1rem",
                        width="100%"
                    )
                ),
                spacing="2",
                width="100%",
                max_width="600px"
            ),
            rx.text("Aucune tâche ajoutée pour l'instant.", color="gray")
        ),
        
        spacing="4",
        align="start",
        width="100%"
    )