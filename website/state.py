
import reflex as rx
from website.utils.supabase_client import get_supabase_client
from typing import List, Dict, Optional
from datetime import datetime
import json

class Blog_FormState(rx.State):
    """The state for the blog form."""
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        supabase = get_supabase_client()
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


# State for mapper app
class ProcessMapperState(rx.State):
    """State global de l'application de cartographie"""
    
    # === Lead Capture ===
    mapper_form_submitted: bool = False
    mapper_user_name: str = ""
    mapper_user_email: str = ""
    magic_link_sent: bool = False
    
    # === Navigation ===
    current_step: int = 1
    total_steps: int = 4
    
    # === Step 1 : Onboarding ===
    user_name: str = ""
    user_email: str = ""
    company_name: str = ""
    sector: str = ""
    main_pain_point: str = ""
    
    # === Step 2 : Tasks ===
    tasks: List[Dict] = []
    current_task_name: str = ""
    current_task_frequency: str = ""
    current_task_description: str = ""
    current_task_tools: str = ""
    current_task_priority: str = "Moyenne"
    
    # === Step 3 : Process builder ===
    selected_task_id: Optional[int] = None
    process_blocks: List[Dict] = []
    
    # === Step 4 : Export ===
    generating_pdf: bool = False
    pdf_generated: bool = False
    
    # ============ NAVIGATION ============
    
    def next_step(self):
        """Passe à l'étape suivante"""
        if self.current_step < self.total_steps:
            if self.validate_current_step():
                self.current_step += 1
            else:
                yield rx.toast.error("Veuillez remplir tous les champs requis")
    
    def prev_step(self):
        """Retourne à l'étape précédente"""
        if self.current_step > 1:
            self.current_step -= 1
    
    def go_to_step(self, step: int):
        """Va directement à une étape (via timeline)"""
        if 1 <= step <= self.total_steps:
            self.current_step = step
    
    def validate_current_step(self) -> bool:
        """Valide l'étape actuelle"""
        if self.current_step == 1:
            return bool(self.user_name and self.user_email and self.company_name)
        elif self.current_step == 2:
            return len(self.tasks) > 0
        elif self.current_step == 3:
            return len(self.process_blocks) > 0
        return True
    
    # ============ TASKS MANAGEMENT ============
    
    def add_task(self):
        """Ajoute une tâche à la liste"""
        if self.current_task_name:
            new_task = {
                "id": len(self.tasks) + 1,
                "name": self.current_task_name,
                "frequency": self.current_task_frequency,
                "description": self.current_task_description,
                "tools": self.current_task_tools,
                "priority": self.current_task_priority,
                "created_at": datetime.now().isoformat()
            }
            self.tasks.append(new_task)
            
            # Reset form
            self.current_task_name = ""
            self.current_task_frequency = ""
            self.current_task_description = ""
            self.current_task_tools = ""
            
            yield rx.toast.success(f"Tâche '{new_task['name']}' ajoutée")
    
    def remove_task(self, task_id: int):
        """Supprime une tâche"""
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        yield rx.toast.info("Tâche supprimée")
    
    def select_task_for_mapping(self, task_id: int):
        """Sélectionne une tâche pour mapper son processus"""
        self.selected_task_id = task_id
        self.process_blocks = []
    
    # ============ PROCESS BUILDER ============
    
    def add_block_to_process(self, block_type: str):
        """Ajoute un bloc au processus (via Drag & Drop)"""
        if self.selected_task_id is None:
            return rx.toast.warning("Veuillez sélectionner une tâche d'abord")
            
        new_block = {
            "id": len(self.process_blocks) + 1,
            "type": block_type, # "Start", "Action", "Decision", "End"
            "label": block_type,
            "description": "",
            "position": len(self.process_blocks),
            "task_id": self.selected_task_id
        }
        self.process_blocks.append(new_block)
        yield rx.toast.success(f"Bloc '{block_type}' ajouté")

    def add_block(self, block_type: str):
         """Legacy method kept for compatibility if needed, redirects to add_block_to_process"""
         return self.add_block_to_process(block_type)
    
    def update_block_label(self, block_id: int, new_label: str):
        """Met à jour le label d'un bloc"""
        for block in self.process_blocks:
            if block["id"] == block_id:
                block["label"] = new_label
                break
    
    def remove_block(self, block_id: int):
        """Supprime un bloc"""
        self.process_blocks = [b for b in self.process_blocks if b["id"] != block_id]
        for idx, block in enumerate(self.process_blocks):
            block["position"] = idx
    
    # ============ COMPUTED VARS ============
    
    @rx.var
    def progress_percentage(self) -> int:
        """Calcul du pourcentage de progression"""
        return int((self.current_step / self.total_steps) * 100)
    
    @rx.var
    def selected_task_name(self) -> str:
        """Nom de la tâche sélectionnée"""
        if self.selected_task_id:
            task = next((t for t in self.tasks if t["id"] == self.selected_task_id), None)
            return task["name"] if task else ""
        return ""
    
    @rx.var
    def can_proceed_to_next(self) -> bool:
        """Peut-on passer à l'étape suivante ?"""
        return self.validate_current_step()

    @rx.var
    def task_names(self) -> List[str]:
        """Liste des noms de tâches pour le select"""
        return [t["name"] for t in self.tasks]

    @rx.var
    def selected_task_name(self) -> str:
        """Nom de la tâche sélectionnée"""
        if self.selected_task_id is None:
            return ""
        task = next((t for t in self.tasks if t["id"] == self.selected_task_id), None)
        return task["name"] if task else ""

    def select_task_by_name(self, name: str):
        """Sélectionne une tâche par son nom"""
        task = next((t for t in self.tasks if t["name"] == name), None)
        if task:
            self.selected_task_id = task["id"]
            self.process_blocks = []

    # ============ LEAD CAPTURE ============
    
    def submit_mapper_form(self, form_data: dict):
        """Handle lead capture form submission and generate access token"""
        import uuid
        
        try:
            self.mapper_user_name = form_data.get("name", "")
            self.mapper_user_email = form_data.get("email", "")
            
            if not self.mapper_user_name or not self.mapper_user_email:
                return rx.toast.error("Veuillez remplir tous les champs")
            
            # Generate unique token for magic link
            access_token = str(uuid.uuid4())
            
            # Save to Supabase with token
            supabase = get_supabase_client()
            supabase.table("mapper_users").insert({
                "name": self.mapper_user_name,
                "email": self.mapper_user_email,
                "access_token": access_token,
                "token_used": False,
                "created_at": datetime.now().isoformat()
            }).execute()
            
            # Email sending is handled externally by n8n + Brevo
            # They will receive a webhook with the token and send the magic link
            
            # For testing, show the magic link in console/toast
            magic_link = f"http://localhost:3000/mapper?token={access_token}"
            print(f"🔗 Test Magic Link: {magic_link}")
            
            # Show success message
            self.magic_link_sent = True
            
            yield rx.toast.success(f"Formulaire envoyé ! (Check console for test link)")
        except Exception as e:
            yield rx.toast.error(f"Erreur : {str(e)}")
    process_blocks: List[Dict] = []
    
    # === Step 4 : Export ===
    generating_pdf: bool = False
    pdf_generated: bool = False
    
    # ============ NAVIGATION ============
    
    def next_step(self):
        """Passe à l'étape suivante"""
        if self.current_step < self.total_steps:
            if self.validate_current_step():
                self.current_step += 1
            else:
                yield rx.toast.error("Veuillez remplir tous les champs requis")
    
    def prev_step(self):
        """Retourne à l'étape précédente"""
        if self.current_step > 1:
            self.current_step -= 1
    
    def go_to_step(self, step: int):
        """Va directement à une étape (via timeline)"""
        if 1 <= step <= self.total_steps:
            self.current_step = step
    
    def validate_current_step(self) -> bool:
        """Valide l'étape actuelle"""
        if self.current_step == 1:
            return bool(self.user_name and self.user_email and self.company_name)
        elif self.current_step == 2:
            return len(self.tasks) > 0
        elif self.current_step == 3:
            return len(self.process_blocks) > 0
        return True
    
    # ============ TASKS MANAGEMENT ============
    
    def add_task(self):
        """Ajoute une tâche à la liste"""
        if self.current_task_name:
            new_task = {
                "id": len(self.tasks) + 1,
                "name": self.current_task_name,
                "frequency": self.current_task_frequency,
                "description": self.current_task_description,
                "tools": self.current_task_tools,
                "priority": self.current_task_priority,
                "created_at": datetime.now().isoformat()
            }
            self.tasks.append(new_task)
            
            # Reset form
            self.current_task_name = ""
            self.current_task_frequency = ""
            self.current_task_description = ""
            self.current_task_tools = ""
            
            yield rx.toast.success(f"Tâche '{new_task['name']}' ajoutée")
    
    def remove_task(self, task_id: int):
        """Supprime une tâche"""
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        yield rx.toast.info("Tâche supprimée")
    
    def select_task_for_mapping(self, task_id: int):
        """Sélectionne une tâche pour mapper son processus"""
        self.selected_task_id = task_id
        self.process_blocks = []
    
    # ============ PROCESS BUILDER ============
    
    def add_block_to_process(self, block_type: str):
        """Ajoute un bloc au processus (via Drag & Drop)"""
        if self.selected_task_id is None:
            return rx.toast.warning("Veuillez sélectionner une tâche d'abord")
            
        new_block = {
            "id": len(self.process_blocks) + 1,
            "type": block_type, # "Start", "Action", "Decision", "End"
            "label": block_type,
            "description": "",
            "position": len(self.process_blocks),
            "task_id": self.selected_task_id
        }
        self.process_blocks.append(new_block)
        yield rx.toast.success(f"Bloc '{block_type}' ajouté")

    def add_block(self, block_type: str):
         """Legacy method kept for compatibility if needed, redirects to add_block_to_process"""
         return self.add_block_to_process(block_type)
    
    def update_block_label(self, block_id: int, new_label: str):
        """Met à jour le label d'un bloc"""
        for block in self.process_blocks:
            if block["id"] == block_id:
                block["label"] = new_label
                break
    
    def remove_block(self, block_id: int):
        """Supprime un bloc"""
        self.process_blocks = [b for b in self.process_blocks if b["id"] != block_id]
        for idx, block in enumerate(self.process_blocks):
            block["position"] = idx
    
    # ============ COMPUTED VARS ============
    
    @rx.var
    def progress_percentage(self) -> int:
        """Calcul du pourcentage de progression"""
        return int((self.current_step / self.total_steps) * 100)
    
    @rx.var
    def selected_task_name(self) -> str:
        """Nom de la tâche sélectionnée"""
        if self.selected_task_id:
            task = next((t for t in self.tasks if t["id"] == self.selected_task_id), None)
            return task["name"] if task else ""
        return ""
    
    @rx.var
    def can_proceed_to_next(self) -> bool:
        """Peut-on passer à l'étape suivante ?"""
        return self.validate_current_step()

    @rx.var
    def task_names(self) -> List[str]:
        """Liste des noms de tâches pour le select"""
        return [t["name"] for t in self.tasks]

    @rx.var
    def selected_task_name(self) -> str:
        """Nom de la tâche sélectionnée"""
        if self.selected_task_id is None:
            return ""
        task = next((t for t in self.tasks if t["id"] == self.selected_task_id), None)
        return task["name"] if task else ""

    def select_task_by_name(self, name: str):
        """Sélectionne une tâche par son nom"""
        task = next((t for t in self.tasks if t["name"] == name), None)
        if task:
            self.selected_task_id = task["id"]
            self.process_blocks = []

    # ============ LEAD CAPTURE ============
    
    def submit_mapper_form(self, form_data: dict):
        """Handle lead capture form submission and generate access token"""
        import uuid
        
        try:
            self.mapper_user_name = form_data.get("name", "")
            self.mapper_user_email = form_data.get("email", "")
            
            if not self.mapper_user_name or not self.mapper_user_email:
                return rx.toast.error("Veuillez remplir tous les champs")
            
            # Generate unique token for magic link
            access_token = str(uuid.uuid4())
            
            # Save to Supabase with token
            supabase = get_supabase_client()
            supabase.table("mapper_users").insert({
                "name": self.mapper_user_name,
                "email": self.mapper_user_email,
                "access_token": access_token,
                "token_used": False,
                "created_at": datetime.now().isoformat()
            }).execute()
            
            # Email sending is handled externally by n8n + Brevo
            # They will receive a webhook with the token and send the magic link
            
            # For testing, show the magic link in console/toast
            magic_link = f"http://localhost:3000/mapper?token={access_token}"
            print(f"🔗 Test Magic Link: {magic_link}")
            
            # Show success message
            self.magic_link_sent = True
            
            yield rx.toast.success(f"Formulaire envoyé ! (Check console for test link)")
        except Exception as e:
            yield rx.toast.error(f"Erreur : {str(e)}")
    
    def validate_token(self, token: str):
        """Validate magic link token and grant access"""
        try:
            # Hardcoded test token for development
            if token == "test123":
                self.mapper_user_name = "Test User"
                self.mapper_user_email = "test@example.com"
                self.user_name = "Test User"
                self.user_email = "test@example.com"
                self.mapper_form_submitted = True
                yield rx.toast.success("Bienvenue Test User ! 🎉 (Dev Mode)")
                return
            
            supabase = get_supabase_client()
            result = supabase.table("mapper_users").select("*").eq("access_token", token).eq("token_used", False).execute()
            
            if result.data and len(result.data) > 0:
                user_data = result.data[0]
                supabase.table("mapper_users").update({"token_used": True}).eq("access_token", token).execute()
                
                self.mapper_user_name = user_data.get("name", "")
                self.mapper_user_email = user_data.get("email", "")
                self.user_name = self.mapper_user_name
                self.user_email = self.mapper_user_email
                self.mapper_form_submitted = True
                
                yield rx.toast.success(f"Bienvenue {self.mapper_user_name} ! 🎉")
            else:
                yield rx.toast.error("Lien invalide ou déjà utilisé")
    def export_json_data(self) -> str:
        """Génère les données JSON pour l'export"""
        data = {
            "user": {
                "name": self.user_name,
                "email": self.user_email,
                "company": self.company_name,
                "sector": self.sector
            },
            "tasks": self.tasks,
            "process_blocks": self.process_blocks
        }
        return json.dumps(data, indent=2, ensure_ascii=False)

    @rx.var
    def export_markdown_data(self) -> str:
        """Génère le rapport Markdown"""
        md = f"# Cartographie des Processus - {self.company_name}\n\n"
        md += f"**Généré par :** {self.user_name} ({self.user_email})\n"
        md += f"**Secteur :** {self.sector}\n\n"
        
        md += "## Tâches Identifiées\n"
        for task in self.tasks:
            md += f"- **{task['name']}** ({task['frequency']}) : {task['description']}\n"
            
        md += "\n## Détail des Processus\n"
        # Group blocks by task
        if self.process_blocks:
             md += "### Blocs de processus\n"
             for block in self.process_blocks:
                 md += f"- [{block['type']}] {block['label']}\n"
        
        return md
