import customtkinter as ctk
from .main_screen import app

# CTkScrollableFrame create scrolable element

class VerticalMenu(ctk.CTkScrollableFrame):
    def __init__ (self, master_ch: ctk.CTk, width_ch: int, height_ch: int, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self = self,
            master = master_ch,
            width = width_ch,
            height = height_ch,
            fg_color = "#096C82",
            **kwargs
        )
        self.grid(row=0, column=0)

menu = VerticalMenu(app, 275, 800)
