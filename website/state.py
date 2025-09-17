import reflex as rx


class Blog_FormState(rx.State):
    """The state for the blog form."""
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
