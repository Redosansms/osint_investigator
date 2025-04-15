import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import sys

class OSINTTool:
    def __init__(self, root):
        self.root = root
        self.root.title("OSINT Investigator - Made by Redhos")  # Retiré "Pro"
        self.root.geometry("1000x700")
        
        # Configuration des logos
        self.setup_logos()
        
        # ... (le reste de votre __init__)

    def resource_path(self, relative_path):
        """Get absolute path for PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def setup_logos(self):
        """Configure les logos pour l'application et l'interface"""
        try:
            # Logo de l'application (logo2.png)
            icon_path = self.resource_path(os.path.join("img", "logo2.png"))
            if os.path.exists(icon_path):
                img = Image.open(icon_path)
                img.save('temp.ico', format='ICO', sizes=[(32,32), (48,48), (64,64)])
                self.root.iconbitmap('temp.ico')
                os.remove('temp.ico')
        except Exception as e:
            print(f"Erreur logo application: {e}")

        try:
            # Logo de l'interface (logo.png)
            logo_path = self.resource_path(os.path.join("img", "logo.png"))
            if os.path.exists(logo_path):
                self.logo_img = Image.open(logo_path)
                self.logo_img = self.logo_img.resize((400, 100), Image.LANCZOS)  # Taille ajustée
                self.logo_photo = ImageTk.PhotoImage(self.logo_img)
        except Exception as e:
            print(f"Erreur logo interface: {e}")
            self.logo_photo = None

    def create_widgets(self):
        # Frame principal
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header avec logo
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill=tk.X, pady=(10, 20))
        
        if hasattr(self, 'logo_photo'):
            logo_label = ctk.CTkLabel(header_frame, 
                                    image=self.logo_photo,
                                    text="")
            logo_label.pack()
        else:
            # Fallback textuel si le logo ne charge pas
            ctk.CTkLabel(header_frame,
                        text="OSINT Investigator",
                        font=("Helvetica", 24, "bold")).pack()
        
        # ... (le reste de votre code)