# website/pages/mapper_app/steps/step3_process.py

import reflex as rx
import reflex_enterprise as rxe
from website.state import ProcessMapperState
from website.theme import TEXT_MAIN, CTA_COLOR, PRIMARY_BG

def draggable_block(type_name: str, icon: str, color: str) -> rx.Component:
    return rxe.dnd.draggable(
        rx.card(
            rx.hstack(
                rx.icon(icon, size=20, color="white"),
                rx.text(type_name, weight="bold", color="white", size="2"),
                spacing="2", align="center"
            ),
            bg=color, padding="0.875rem 1rem", width="100%", cursor="grab",
            border_radius="8px", box_shadow="sm",
            _hover={"box_shadow": "md", "transform": "translateY(-2px)", "transition": "all 0.2s"}
        ),
        id=type_name, item=type_name, group="process_blocks"
    )

def process_block_item(block: dict, index: int) -> rx.Component:
    colors = {"Start": "#10b981", "Action": "#3b82f6", "Decision": "#f59e0b", "End": "#ef4444"}
    block_color = colors.get(block["type"], "#6366f1")
    
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(block["type"], color_scheme="gray", style={"background": block_color, "color": "white"}),
                rx.text(f"#{index + 1}", size="1", color="gray"),
                rx.spacer(),
                rx.icon("trash-2", size=16, color="#ef4444", cursor="pointer",
                    on_click=lambda: ProcessMapperState.remove_block(block["id"]), _hover={"opacity": 0.7}),
                width="100%"
            ),
            rx.input(value=block["label"], placeholder="Nom de l'étape...",
                on_change=lambda val: ProcessMapperState.update_block_label(block["id"], val),
                variant="soft", width="100%", size="3"),
            spacing="2", width="100%"
        ),
        width="100%", padding="1rem", margin_bottom="0.75rem",
        bg="rgba(241, 245, 249, 0.05)", border=f"1px solid {block_color}40", border_radius="8px"
    )

def step3_process() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading("🎯 Cartographiez vos processus", size="6", color=TEXT_MAIN, margin_bottom="0.5rem"),
            rx.text("Glissez-déposez les blocs pour construire votre processus.", color="#94a3b8", size="3", margin_bottom="2rem"),
            width="100%"
        ),
        rx.grid(
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading("📦 Blocs disponibles", size="4", color=TEXT_MAIN, margin_bottom="1rem"),
                        rx.text("Glissez vers la droite", size="2", color="#94a3b8", margin_bottom="1rem"),
                        draggable_block("Start", "play", "#10b981"),
                        draggable_block("Action", "zap", "#3b82f6"),
                        draggable_block("Decision", "git-branch", "#f59e0b"),
                        draggable_block("End", "check", "#ef4444"),
                        spacing="3", width="100%"
                    ),
                    padding="1.5rem", bg="rgba(15, 23, 42, 0.6)", border="1px solid rgba(241, 245, 249, 0.1)"
                ),
                rx.divider(margin_y="1.5rem", opacity=0.2),
                rx.card(
                    rx.vstack(
                        rx.heading("🎯 Tâche sélectionnée", size="4", color=TEXT_MAIN, margin_bottom="1rem"),
                        rx.select(ProcessMapperState.task_names, placeholder="Choisir une tâche...",
                            on_change=ProcessMapperState.select_task_by_name,
                            value=ProcessMapperState.selected_task_name, size="3", width="100%"),
                        rx.cond(ProcessMapperState.selected_task_id.to(bool),
                            rx.text("✓ Tâche sélectionnée !", size="2", color="#10b981", margin_top="0.5rem"),
                            rx.text("Sélectionnez une tâche", size="2", color="#94a3b8", margin_top="0.5rem")),
                        spacing="2", width="100%"
                    ),
                    padding="1.5rem", bg="rgba(15, 23, 42, 0.6)", border="1px solid rgba(241, 245, 249, 0.1)"
                ),
                width="100%", align="start", spacing="0"
            ),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading(
                                rx.cond(ProcessMapperState.selected_task_name != "", 
                                    f"🔨 {ProcessMapperState.selected_task_name}", "🔨 Votre processus"),
                                size="4", color=TEXT_MAIN
                            ),
                            rx.spacer(),
                            rx.badge(f"{ProcessMapperState.process_blocks.length()} blocs", color_scheme="gray", size="2"),
                            width="100%"
                        ),
                        rxe.dnd.drop_target(
                            rx.vstack(
                                rx.cond(ProcessMapperState.process_blocks.length() > 0,
                                    rx.foreach(ProcessMapperState.process_blocks, lambda block, idx: process_block_item(block, idx)),
                                    rx.center(
                                        rx.vstack(
                                            rx.icon("package-open", size=48, color="#475569"),
                                            rx.text("Glissez des blocs ici", color="#94a3b8", size="3", weight="medium"),
                                            rx.text("Commencez par 'Start'", color="#64748b", size="2"),
                                            spacing="2", align="center"
                                        ),
                                        padding="4rem", width="100%"
                                    )
                                ),
                                width="100%", min_height="400px", padding="1rem", border_radius="8px",
                                border="2px dashed rgba(241, 245, 249, 0.2)", _hover={"border_color": CTA_COLOR + "80"}
                            ),
                            accepts=["process_blocks"], on_drop=lambda data: ProcessMapperState.add_block_to_process(data)
                        ),
                        spacing="3", width="100%"
                    ),
                    padding="1.5rem", bg="rgba(15, 23, 42, 0.4)", border="1px solid rgba(241, 245, 249, 0.1)", min_height="500px"
                ),
                width="100%"
            ),
            columns="2", spacing="6", width="100%"
        ),
        width="100%", align="start", spacing="4"
    )
