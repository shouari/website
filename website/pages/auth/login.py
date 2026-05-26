# website/pages/auth/login.py
import reflex as rx
from website.auth_state import AuthState
from website.theme import TEXT_MAIN, CTA_COLOR, PRIMARY_BG

def login_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Connexion", size="6", color=TEXT_MAIN),
                rx.text("Accédez à votre espace Process Mapper", color="gray", size="2"),
                
                rx.input(
                    placeholder="Email",
                    on_change=AuthState.set_email,
                    width="100%",
                ),
                
                rx.cond(
                    AuthState.error_message != "",
                    rx.callout(
                        AuthState.error_message,
                        icon="alert_triangle",
                        color_scheme="red",
                        width="100%"
                    )
                ),
                
                rx.cond(
                    AuthState.magic_link_sent,
                    rx.callout(
                        "Lien envoyé ! Vérifiez votre boîte mail pour vous connecter.",
                        icon="circle_check",
                        color_scheme="green",
                        width="100%"
                    ),
                    rx.button(
                        "Recevoir mon lien magique",
                        on_click=AuthState.send_magic_link,
                        bg=CTA_COLOR,
                        color="white",
                        width="100%",
                        size="3"
                    )
                ),
                
                spacing="4",
                align="center",
                width="100%",
                padding="2rem"
            ),
            width="100%",
            max_width="400px",
            bg="white"
        ),
        width="100%",
        height="100vh",
        bg=PRIMARY_BG
    )
