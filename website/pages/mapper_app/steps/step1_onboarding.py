# website/pages/app/steps/step1_onboarding.py

import reflex as rx
from website.state import ProcessMapperState
from website.theme import TEXT_MAIN

def step1_onboarding() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Bienvenue ! 👋",
            size="7",
            margin_bottom="0.5rem",
            color=TEXT_MAIN
        ),
        rx.text(
            "Ce formulaire vous aidera à cartographier vos processus opérationnels. "
            "Prenez 5 minutes pour répondre, vous recevrez une documentation complète par email.",
            color="gray",
            size="3",
            margin_bottom="2rem"
        ),
        
        # Formulaire
        rx.vstack(
            # Prénom
            rx.text("Votre prénom *", color=TEXT_MAIN, size="2", weight="medium"),
            rx.input(
                placeholder="Ex: Marie",
                value=ProcessMapperState.user_name,
                on_change=ProcessMapperState.set_user_name,
                size="3",
                width="100%"
            ),
            
            # Email
            rx.text("Votre email *", color=TEXT_MAIN, size="2", weight="medium", margin_top="1rem"),
            rx.input(
                placeholder="marie@entreprise.com",
                value=ProcessMapperState.user_email,
                on_change=ProcessMapperState.set_user_email,
                type="email",
                size="3",
                width="100%"
            ),
            
            # Entreprise
            rx.text("Nom de votre entreprise *", color=TEXT_MAIN, size="2", weight="medium", margin_top="1rem"),
            rx.input(
                placeholder="Ex: Boulangerie du Coin",
                value=ProcessMapperState.company_name,
                on_change=ProcessMapperState.set_company_name,
                size="3",
                width="100%"
            ),
            
            # Secteur
            rx.text("Secteur d'activité *", color=TEXT_MAIN, size="2", weight="medium", margin_top="1rem"),
            rx.select(
                ["Alimentaire", "Services", "Commerce", "Manufacturier", "Construction", "Technologie", "Autre"],
                placeholder="Sélectionnez...",
                value=ProcessMapperState.sector,
                on_change=ProcessMapperState.set_sector,
                size="3",
                width="100%"
            ),
            
            # Friction
            rx.text("Quelle est votre principale friction opérationnelle ?", color=TEXT_MAIN, size="2", weight="medium", margin_top="1rem"),
            rx.input(
                placeholder="Ex: Trop de temps perdu en coordination entre départements",
                value=ProcessMapperState.main_pain_point,
                on_change=ProcessMapperState.set_main_pain_point,
                size="3",
                width="100%",
                rows=3
            ),
            
            spacing="1",
            align="start",
            width="100%",
            max_width="600px"
        ),
        
        spacing="4",
        align="start",
        width="100%"
    )