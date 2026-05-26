import reflex as rx
from markdown_it import MarkdownIt
from website.state import ProcessMapperState
from website.theme import PRIMARY_BG, TEXT_MAIN, CTA_COLOR

_INTRO_MD = MarkdownIt("commonmark").render("""
Trop souvent, on perd du temps sans savoir pourquoi.
On répète les mêmes tâches, on cherche les mêmes informations, on attend les mêmes validations.

**Le Process Mapper est un outil gratuit pour documenter vos processus.**

Pas pour faire joli.
Pas pour remplir des cases.
Mais pour **voir clair**.

En quelques minutes, vous allez :
- **Identifier** ce qui ralentit vraiment
- **Cartographier** vos flux actuels (pas l'idéal, le réel)
- **Repérer** les frictions, les doublons, les points de blocage

C'est la première étape de la méthode **CSA** : **Clarifier**.

Parce qu'on ne peut pas simplifier ce qu'on ne comprend pas.
Et on ne peut pas automatiser ce qui n'est pas clair.

**Commencez maintenant. C'est gratuit. Aucune installation requise.**
""")

_INTRO_HTML = (
    f'<style>'
    f'.mapper-intro{{color:{TEXT_MAIN};opacity:0.85;font-size:1rem;line-height:1.8;}}'
    f'.mapper-intro p{{margin:0.6rem 0;}}'
    f'.mapper-intro strong{{font-weight:700;color:{TEXT_MAIN};}}'
    f'.mapper-intro ul{{margin:0.5rem 0 0.5rem 1.5rem;padding:0;}}'
    f'.mapper-intro li{{margin:0.25rem 0;}}'
    f'</style>'
    f'<div class="mapper-intro">{_INTRO_MD}</div>'
)
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
            rx.button(
                rx.hstack(rx.icon("chevron-left", size=16), rx.text("Précédent"), spacing="1"),
                on_click=ProcessMapperState.prev_step,
                variant="outline", size="2", color=TEXT_MAIN),
            rx.box()),
        rx.spacer(),
        rx.cond(ProcessMapperState.current_step < ProcessMapperState.total_steps,
            rx.button(
                rx.hstack(rx.text("Suivant"), rx.icon("chevron-right", size=16), spacing="1"),
                on_click=ProcessMapperState.next_step,
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
        rx.box(
            # Description section above the form
            rx.vstack(
                rx.heading(
                    "Cartographier pour clarifier",
                    size="8",
                    color=TEXT_MAIN,
                    text_align="center",
                    margin_bottom="1rem"
                ),
                rx.text(
                    "Avant de simplifier, il faut voir.",
                    font_size="1.2rem",
                    color=TEXT_MAIN,
                    opacity=0.9,
                    text_align="center",
                    weight="medium",
                    margin_bottom="2rem"
                ),
                rx.box(
                    rx.html(_INTRO_HTML),
                    max_width="800px",
                    text_align="left",
                    padding="2rem",
                    bg="#13223850",
                    border="1px solid rgba(255,255,255,0.1)",
                    border_radius="12px",
                    backdrop_filter="blur(5px)",
                    margin_bottom="3rem"
                ),
                width="100%",
                align="center",
                padding_x="1rem"
            ),
            
            # Original form
            rx.cond(ProcessMapperState.magic_link_sent,
                rx.vstack(
                    rx.icon("mail-check", size=60, color=CTA_COLOR),
                    rx.heading("Formulaire envoyé !", size="6", color=TEXT_MAIN),
                    rx.text("Votre demande d'accès a été soumise.", color=TEXT_MAIN, opacity=0.8, text_align="center", size="3"),
                    rx.text("Vous allez recevoir un email avec votre lien d'accès.", color=TEXT_MAIN, opacity=0.6, text_align="center", size="2", margin_top="1rem"),
                    rx.button("Retour au formulaire", variant="ghost", color=TEXT_MAIN, on_click=ProcessMapperState.reset_lead_capture, margin_top="1rem"),
                    spacing="4", align="center", padding="1rem"
                ),
                rx.form(
                    rx.vstack(
                        rx.heading("Cartographie de Processus", size="6", color=TEXT_MAIN, margin_bottom="1rem"),
                        rx.text("Outil gratuit pour cartographier vos processus.", color=TEXT_MAIN, opacity=0.7, size="3", text_align="center", margin_bottom="2rem"),
                        rx.text("Nom", color=TEXT_MAIN, size="2", weight="bold"),
                        rx.input(name="name", placeholder="Votre nom", width="100%", required=True),
                        rx.text("Email", color=TEXT_MAIN, size="2", weight="bold", margin_top="1rem"),
                        rx.input(name="email", placeholder="votre@email.com", type="email", width="100%", required=True),
                        rx.button("Commencer", type="submit", size="3", width="100%", bg=CTA_COLOR, color="white", margin_top="1.5rem", _hover={"opacity": 0.8}),
                        spacing="2", align="stretch", width="100%"
                    ),
                    on_submit=ProcessMapperState.submit_mapper_form,
                    reset_on_submit=False,
                    width="100%"
                )
            ),
            
            # Existing user dialog
            rx.dialog.root(
                rx.dialog.content(
                    rx.vstack(
                        rx.dialog.title("Accès existant détecté", text_align="center", color=TEXT_MAIN),
                        rx.text(f"Un lien d'accès a déjà été envoyé à {ProcessMapperState.mapper_user_email}.", color=TEXT_MAIN, text_align="center", size="2"),
                        rx.text("Vérifiez votre boîte email ou demandez un nouveau lien.", color=TEXT_MAIN, opacity=0.7, text_align="center", size="2", margin_top="0.5rem"),
                        rx.hstack(
                            rx.dialog.close(
                                rx.button("Annuler", variant="soft", on_click=ProcessMapperState.close_existing_user_dialog)
                            ),
                            rx.button("Renvoyer le lien", bg=CTA_COLOR, color="white", on_click=ProcessMapperState.resend_magic_link, _hover={"opacity": 0.8}),
                            spacing="3", justify="center", width="100%", margin_top="1rem"
                        ),
                        spacing="3", align="center", padding="1rem"
                    ),
                    bg="#13223899", backdrop_filter="blur(10px)", border="1px solid rgba(255,255,255,0.1)"
                ),
                open=ProcessMapperState.show_existing_user_dialog
            ),
            
            max_width="900px",
            width="100%",
            padding=["1rem", "2rem", "3rem"],
            bg="#13223899",
            backdrop_filter="blur(10px)",
            border="1px solid rgba(255,255,255,0.1)",
            border_radius="16px"
        ),
        min_height="100vh",
        padding_y="3rem",
        bg=PRIMARY_BG,
        width="100%"
    )


@rx.page(route="/mapper", title="Cartographie de processus", on_load=ProcessMapperState.check_token_on_load)
def mapper():
    return rx.cond(ProcessMapperState.mapper_form_submitted, app_layout(), lead_capture_form())