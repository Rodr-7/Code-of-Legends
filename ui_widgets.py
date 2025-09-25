# ui_widgets.py
import tkinter as tk

class StyledButton(tk.Button):
    def __init__(self, parent, text="", command=None, **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Verdana", 14, "bold"),
            bg="#4a4a4a",   # fondo
            fg="white",     # texto
            activebackground="#6a6a6a",  # color al hacer click
            activeforeground="yellow",
            relief="raised",
            bd=4,
            **kwargs
        )

class StyledLabel(tk.Label):
    def __init__(self, parent, text="", **kwargs):
        super().__init__(
            parent,
            text=text,
            font=("Arial", 12),
            bg="#2e2e2e",
            fg="white",
            **kwargs
        )

class StyledFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            bg="#1e1e1e",
            padx=10,
            pady=10,
            **kwargs
        )
