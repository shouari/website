import reflex as rx
from website.state import ContactState
from website.components.layout import base_page
from website.components.sections import section_container
from website.theme import PRIMARY_BG, TEXT_MAIN, CTA_COLOR, heading_style, text_style

def contact_info_column() -> rx.Component:
    return rx.vstack(
        rx.heading("Contactez-nous", **heading_style, size="7"),
        rx.text(
            "Une question ? Un projet ? N'hésitez pas à nous écrire ou à réserver un créneau directement.",
            **text_style,
            size="3",
            margin_bottom="2rem"
        ),
        
        rx.vstack(
            rx.hstack(
                rx.icon("mail", color=CTA_COLOR),
                rx.link("salim@salimhouari.com", href="mailto:salim@salimhouari.com", color=TEXT_MAIN, _hover={"color": CTA_COLOR}),
                align="center", spacing="3"
            ),
            rx.hstack(
                rx.icon("phone", color=CTA_COLOR),
                rx.text("+1 (514) 499-0880", color=TEXT_MAIN),
                align="center", spacing="3"
            ),
            spacing="4",
            align="start",
            width="100%",
            margin_bottom="2rem"
        ),
        
        rx.box(
            rx.heading("Administrateur agréé", size="4", color=TEXT_MAIN, margin_bottom="1rem"),
            rx.text("Salim Houari, Adm.A.", color=TEXT_MAIN, weight="bold", margin_bottom="0.5rem"),
            rx.text("Numéro de permis: A25-53412", color=TEXT_MAIN, opacity=0.8, size="2"),
            rx.text("Ordre des administrateurs agréés du Québec", color=TEXT_MAIN, opacity=0.7, size="2", margin_top="0.5rem"),
            padding="1.5rem",
            bg="#13223850",
            border="1px solid rgba(255,255,255,0.1)",
            border_radius="12px",
            width="100%",
            margin_bottom="2rem"
        ),
        
        rx.box(
            rx.heading("Réserver un échange", size="4", color=TEXT_MAIN, margin_bottom="1rem"),
            rx.text("Discutons de vos besoins lors d'un appel de 30 minutes.", color=TEXT_MAIN, opacity=0.8, margin_bottom="1rem"),
            rx.link(
                rx.button(
                    "📅 Réserver un créneau (Calendly)",
                    size="3",
                    width="100%",
                    bg=CTA_COLOR,
                    color="white",
                    _hover={"opacity": 0.8}
                ),
                href="https://calendly.com/", # Placeholder
                is_external=True,
                width="100%"
            ),
            padding="2rem",
            bg="#13223850",
            border="1px solid rgba(255,255,255,0.1)",
            border_radius="12px",
            width="100%"
        ),
        
        align="start",
        spacing="2",
        width="100%"
    )

def contact_form_column() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.heading("Envoyez-nous un message", size="5", color=TEXT_MAIN, margin_bottom="1rem"),
                
                rx.text("Nom", color=TEXT_MAIN, size="2", weight="bold"),
                rx.input(name="name", placeholder="Votre nom", width="100%", required=True),
                
                rx.text("Email", color=TEXT_MAIN, size="2", weight="bold"),
                rx.input(name="email", placeholder="votre@email.com", type="email", width="100%", required=True),
                
                rx.text("Message", color=TEXT_MAIN, size="2", weight="bold"),
                rx.text_area(name="message", placeholder="Comment pouvons-nous vous aider ?", width="100%", min_height="150px", required=True),
                
                rx.button(
                    "Envoyer le message",
                    type="submit",
                    size="3",
                    width="100%",
                    bg=CTA_COLOR,
                    color="white",
                    margin_top="1rem",
                    _hover={"opacity": 0.8}
                ),
                spacing="3",
                align="stretch",
                width="100%"
            ),
            on_submit=ContactState.submit_contact_form,
            reset_on_submit=True,
            width="100%"
        ),
        width="100%",
        height="100%",
        padding="2rem",
        bg="#13223899",
        backdrop_filter="blur(10px)",
        border="1px solid rgba(255,255,255,0.1)"
    )

@rx.page(route="/contact", title="Contact - Salim Houari")
def contact_page() -> rx.Component:
    return base_page(
        rx.box(
            rx.center(
                section_container(
                    rx.heading("Contact", **heading_style, text_align="center", margin_bottom="2rem"),
                    rx.grid(
                        contact_info_column(),
                        contact_form_column(),
                        columns=rx.breakpoints(xs="1fr", md="repeat(2, 1fr)"),
                        gap="2rem",
                        width="100%",
                    ),
                    max_width="1200px",
                ),
            ),
            bg=PRIMARY_BG,
            padding_y=["3rem", "4rem", "5rem"],
        )
    )
