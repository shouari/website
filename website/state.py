import reflex as rx
from website.utils.supabase_client import get_supabase_client


supabase = get_supabase_client()
class Blog_FormState(rx.State):
    """The state for the blog form."""
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print("Form data received:", form_data)
        print("Submitting to Supabase...", supabase)
        try:
            response = supabase.table("newsletter_subscribers").insert({
                "first_name": form_data["first_name"],
                "last_name": form_data["last_name"],
                "email": form_data["email"]
            }).execute()
            print("✅ Enregistrement réussi :", response)
        except Exception as e:
            print("❌ Erreur d'enregistrement :", e)


class CTA_State(rx.State):
    dialog_open: bool = False

    def open_dialog(self):
        self.dialog_open = True
    def close_dialog(self):
        self.dialog_open = False
