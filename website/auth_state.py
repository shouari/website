# website/auth_state.py
import reflex as rx
from website.utils.supabase_client import get_supabase_client
import json

class AuthState(rx.State):
    """State for authentication."""
    email: str = ""
    # password: str = "" # Not used for magic link
    user: dict = {}
    session: dict = {}
    is_authenticated: bool = False
    error_message: str = ""
    magic_link_sent: bool = False

    def send_magic_link(self):
        """Send a magic link to the user's email."""
        supabase = get_supabase_client()
        try:
            # Redirect to the current page or a specific callback URL
            # For localhost, it might be http://localhost:3000/mapper
            # But Supabase needs this URL to be allowed in Redirect URLs
            redirect_url = "http://localhost:3000/mapper" 
            
            response = supabase.auth.sign_in_with_otp({
                "email": self.email,
                "options": {
                    "email_redirect_to": redirect_url
                }
            })
            self.magic_link_sent = True
            self.error_message = ""
            return rx.toast.success("Lien magique envoyé ! Vérifiez votre email.")
        except Exception as e:
            self.error_message = str(e)
            self.magic_link_sent = False
            return rx.toast.error(f"Erreur: {e}")

    def check_login(self):
        """Check if the user is logged in."""
        # For magic link, we might need to handle the hash fragment processing
        # But typically Supabase client handles session recovery if persisted.
        # Here we just check if we have a session.
        # In a real app, we might need a useEffect or on_load to process the URL hash.
        if not self.is_authenticated:
            # Try to recover session (this is simplified, might need more logic for hash parsing)
            pass
            # return rx.redirect("/login") # Keep this for now


    def logout(self):
        """Log out the user."""
        supabase = get_supabase_client()
        try:
            supabase.auth.sign_out()
        except:
            pass
        self.reset()
        return rx.redirect("/login")

    def check_login(self):
        """Check if the user is logged in."""
        if not self.is_authenticated:
            return rx.redirect("/login")

    def set_email(self, email: str):
        self.email = email

    def set_password(self, password: str):
        self.password = password
