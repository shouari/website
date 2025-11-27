import reflex as rx
from website.state import ProcessMapperState
from website.theme import PRIMARY_BG, TEXT_MAIN, CTA_COLOR
from website.pages.mapper_app.steps.step1_onboarding import step1_onboarding
from website.pages.mapper_app.steps.step2_tasks import step2_tasks
from website.pages.mapper_app.steps.step3_process import step3_process
from website.pages.mapper_app.steps.step4_export import step4_export


def progress_bar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(f"Étape {ProcessMapperState.current_step} sur {ProcessMapperState.total_steps}", size="2", weight="medium", color=TEXT_MAIN),
            rx.spacer(),
            rx.text(f"{ProcessMapperState.progress_percentage}%", size="2", color="gray"),
            width="100%", align="center"
        ),
        rx.box(
            rx.box(width=f"{ProcessMapperState.progress_percentage}%", height="100%", bg=CTA_COLOR, border_radius="4px", transition="width 0.3s ease"),
            width="100%", height="8px", bg="#13223820", border_radius="4px", margin_top="0.5rem"
        ),
        width="100%", padding="1rem", bg=PRIMARY_BG, border_bottom="1px solid rgba(255,255,255,0.1)"
    )


def timeline_sidebar() -> rx.Component:
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
                rx.cond(is_completed, rx.icon("check-circle", size=20, color="green"), 
                    rx.cond(is_current, rx.icon(icon, size=20, color=CTA_COLOR), rx.icon(icon, size=20, color="gray"))),
                rx.text(label, weight=rx.cond(is_current, "bold", "medium"),
                    color=rx.cond(is_current, CTA_COLOR, rx.cond(is_completed, "green", "gray")), size="2"),
                spacing="2", align="center"
            ),
            on_click=lambda: ProcessMapperState.go_to_step(step_num),
            cursor="pointer", padding="0.75rem", border_radius="8px",
            _hover={"bg": "#13223820"}, width="100%"
        )
    
    return rx.desktop_only(
        rx.vstack(
            rx.heading("Étapes", size="4", margin_bottom="1rem", color=TEXT_MAIN),
            *[timeline_item(s["step"], s["label"], s["icon"]) for s in steps_config],
            spacing="1", align="start", width="100%", padding="1rem",
            bg="#13223820", border_radius="12px", position="sticky", top="1rem"
        )
    )


def navigation_buttons() -> rx.Component:
    return rx.hstack(
        rx.cond(ProcessMapperState.current_step > 1,
            rx.button(rx.icon("chevron-left", size=16), "Précédent", on_click=ProcessMapperState.prev_step,
                variant="outline", size="2", color=TEXT_MAIN),
            rx.box()),
        rx.spacer(),
        rx.cond(ProcessMapperState.current_step < ProcessMapperState.total_steps,
            rx.button("Suivant", rx.icon("chevron-right", size=16), on_click=ProcessMapperState.next_step,
                disabled=~ProcessMapperState.can_proceed_to_next, bg=CTA_COLOR,
                color="white", size="2", _hover={"opacity": 0.8}),
            rx.box()),
        width="100%", padding="1.5rem", border_top="1px solid rgba(255,255,255,0.1)", bg=PRIMARY_BG
    )


def app_content() -> rx.Component:
    return rx.cond(ProcessMapperState.current_step == 1, step1_onboarding(),
        rx.cond(ProcessMapperState.current_step == 2, step2_tasks(),
            rx.cond(ProcessMapperState.current_step == 3, step3_process(), step4_export())))


def app_layout() -> rx.Component:
    return rx.box(
        progress_bar(),
        rx.grid(
            timeline_sidebar(),
            rx.vstack(
                rx.box(app_content(), flex="1", width="100%", padding=["1rem", "1.5rem", "2rem"], overflow_y="auto"),
                navigation_buttons(),
                spacing="0", height="calc(100vh - 60px)", width="100%"
            ),
            columns=rx.breakpoints(xs="1fr", lg="250px 1fr"), width="100%", height="calc(100vh - 60px)"
        ),
        width="100%", height="100vh", bg=PRIMARY_BG
    )


def lead_capture_form() -> rx.Component:
    return rx.center(
        rx.card(
            rx.cond(ProcessMapperState.magic_link_sent,
                rx.vstack(
                    rx.icon("mail-check", size=60, color=CTA_COLOR),
                    rx.heading("Formulaire envoyé !", size="6", color=TEXT_MAIN),
                    rx.text("Votre demande d'accès a été soumise.", color="gray", text_align="center", size="3"),
                    rx.text("Vous allez recevoir un email avec votre lien d'accès.", color="gray", text_align="center", size="2", margin_top="1rem"),
                    spacing="4", align="center", padding="3rem"
                ),
                rx.form(
                    rx.vstack(
                        rx.heading("Cartographie de Processus", size="7", color=TEXT_MAIN),
                        rx.text("Outil gratuit pour cartographier vos processus.", color="gray", size="3", text_align="center", margin_bottom="2rem"),
                        rx.vstack(
                            rx.text("Votre prénom", weight="medium", size="2", color=TEXT_MAIN),
                            rx.input(name="name", placeholder="Ex: Marie", required=True, size="3", width="100%"),
                            rx.text("Votre email", weight="medium", size="2", color=TEXT_MAIN, margin_top="1rem"),
                            rx.input(name="email", placeholder="marie@entreprise.com", type="email", required=True, size="3", width="100%"),
                            rx.button("Recevoir mon lien d'accès", type="submit", bg=CTA_COLOR, color="white", size="3", width="100%", margin_top="2rem"),
                            spacing="1", width="100%"
                        ),
                        spacing="4", align="center", width="100%", padding="2rem"
                    ),
                    on_submit=ProcessMapperState.submit_mapper_form,
                    reset_on_submit=False,
                )
            ),
            width="100%", max_width="500px", bg="white", box_shadow="xl"
        ),
        width="100%", height="100vh", bg=PRIMARY_BG
    )


@rx.page(route="/mapper", title="Cartographie de processus", on_load=ProcessMapperState.validate_token_on_load)
def mapper():
    return rx.cond(ProcessMapperState.mapper_form_submitted, app_layout(), lead_capture_form())