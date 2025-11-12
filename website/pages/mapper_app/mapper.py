
import reflex as rx
from website.state import ProcessMapperState
from website.theme import PRIMARY_BG, TEXT_MAIN, CTA_COLOR

# Import des steps (à créer après)
from website.pages.mapper_app.steps.step1_onboarding import step1_onboarding
from website.pages.mapper_app.steps.step2_tasks import step2_tasks
# from website.pages.app.steps.step3_process import step3_process
# from website.pages.app.steps.step4_export import step4_export


def progress_bar() -> rx.Component:
    """Barre de progression en haut"""
    return rx.box(
        rx.hstack(
            rx.text(
                f"Étape {ProcessMapperState.current_step} sur {ProcessMapperState.total_steps}",
                size="2",
                weight="medium",
                color=TEXT_MAIN
            ),
            rx.spacer(),
            rx.text(
                f"{ProcessMapperState.progress_percentage}%",
                size="2",
                color="gray"
            ),
            width="100%",
            align="center"
        ),
        rx.box(
            rx.box(
                width=f"{ProcessMapperState.progress_percentage}%",
                height="100%",
                bg=CTA_COLOR,
                border_radius="4px",
                transition="width 0.3s ease"
            ),
            width="100%",
            height="8px",
            bg="#13223820",
            border_radius="4px",
            margin_top="0.5rem"
        ),
        width="100%",
        padding="1rem",
        bg=PRIMARY_BG,
        border_bottom="1px solid rgba(255,255,255,0.1)"
    )


def timeline_sidebar() -> rx.Component:
    """Timeline simple sur le côté (desktop only)"""
    
    steps_config = [
        {"step": 1, "label": "Informations", "icon": "user"},
        {"step": 2, "label": "Tâches", "icon": "list-checks"},
        {"step": 3, "label": "Processus", "icon": "workflow"},
        {"step": 4, "label": "Export", "icon": "download"},
    ]
    
    def timeline_item(step_num: int, label: str, icon: str):
        is_current = ProcessMapperState.current_step == step_num
        is_completed = ProcessMapperState.current_step > step_num
        
        return rx.box(
            rx.hstack(
                rx.cond(
                    is_completed,
                    rx.icon("check-circle", size=20, color="green"),
                    rx.cond(
                        is_current,
                        rx.icon(icon, size=20, color=CTA_COLOR),
                        rx.icon(icon, size=20, color="gray")
                    )
                ),
                rx.text(
                    label,
                    weight=rx.cond(is_current, "bold", "medium"),
                    color=rx.cond(
                        is_current, 
                        CTA_COLOR,
                        rx.cond(is_completed, "green", "gray")
                    ),
                    size="2"
                ),
                spacing="2",
                align="center"
            ),
            on_click=lambda: ProcessMapperState.go_to_step(step_num),
            cursor="pointer",
            padding="0.75rem",
            border_radius="8px",
            _hover={"bg": "#13223820"},
            width="100%"
        )
    
    return rx.desktop_only(
        rx.vstack(
            rx.heading("Étapes", size="4", margin_bottom="1rem", color=TEXT_MAIN),
            *[timeline_item(s["step"], s["label"], s["icon"]) for s in steps_config],
            spacing="1",
            align="start",
            width="100%",
            padding="1rem",
            bg="#13223820",
            border_radius="12px",
            position="sticky",
            top="1rem"
        )
    )


def navigation_buttons() -> rx.Component:
    """Boutons Précédent / Suivant"""
    return rx.hstack(
        rx.cond(
            ProcessMapperState.current_step > 1,
            rx.button(
                rx.icon("chevron-left", size=16),
                "Précédent",
                on_click=ProcessMapperState.prev_step,
                variant="outline",
                size="2",
                color=TEXT_MAIN
            ),
            rx.box()
        ),
        rx.spacer(),
        rx.cond(
            ProcessMapperState.current_step < ProcessMapperState.total_steps,
            rx.button(
                "Suivant",
                rx.icon("chevron-right", size=16),
                on_click=ProcessMapperState.next_step,
                disabled=~ProcessMapperState.can_proceed_to_next,
                bg=CTA_COLOR,
                color="white",
                size="2",
                _hover={"opacity": 0.8}
            ),
            rx.box()
        ),
        width="100%",
        padding="1.5rem",
        border_top="1px solid rgba(255,255,255,0.1)",
        bg=PRIMARY_BG
    )


def app_content() -> rx.Component:
    """Contenu dynamique selon l'étape"""
    return rx.cond(
        ProcessMapperState.current_step == 1,
        step1_onboarding(),
        rx.cond(
            ProcessMapperState.current_step == 2,
            step2_tasks(),
            rx.box(
                rx.heading("Step 3 & 4 - Coming soon", color=TEXT_MAIN),
                rx.text("En cours de développement...", color="gray")
            )
        )
    )


def app_layout() -> rx.Component:
    """Layout principal de l'app"""
    return rx.box(
        progress_bar(),
        
        rx.grid(
            # Sidebar gauche : Timeline
            timeline_sidebar(),
            
            # Contenu principal
            rx.vstack(
                rx.box(
                    app_content(),
                    flex="1",
                    width="100%",
                    padding=["1rem", "1.5rem", "2rem"],
                    overflow_y="auto"
                ),
                navigation_buttons(),
                spacing="0",
                height="calc(100vh - 60px)",
                width="100%"
            ),
            
            columns=rx.breakpoints(xs="1fr", lg="250px 1fr"),
            width="100%",
            height="calc(100vh - 60px)"
        ),
        
        width="100%",
        height="100vh",
        bg=PRIMARY_BG
    )


@rx.page(route="/mapper", title="Cartographie de processus - Salim Houari")
def mapper():
    """Page principale de l'application (fullscreen, pas de navbar/footer)"""
    return app_layout()