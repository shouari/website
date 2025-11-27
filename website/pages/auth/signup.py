# website/pages/auth/signup.py
import reflex as rx
from website.auth_state import AuthState
from website.theme import TEXT_MAIN, CTA_COLOR, PRIMARY_BG

def signup_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Inscription", size="6", color=TEXT_MAIN),
                rx.text("Créez votre compte Process Mapper", color="gray", size="2"),
                
                rx.input(
                    placeholder="Email",
                    on_change=AuthState.set_email,
                    width="100%",
                ),
                rx.input(
                    placeholder="Mot de passe",
                    type="password",
                    on_change=AuthState.set_password,
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
                
                rx.button(
                    "S'inscrire",
                    on_click=AuthState.signup,
                    bg=CTA_COLOR,
                    color="white",
                    width="100%",
                    size="3"
                ),
                
                rx.hstack(
                    rx.text("Déjà un compte ?", color="gray", size="2"),
                    rx.link("Se connecter", href="/login", color=CTA_COLOR, size="2"),
                    spacing="2",
                    margin_top="1rem"
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
