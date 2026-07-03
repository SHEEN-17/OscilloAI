import customtkinter as ctk


class ExplainCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.title = ctk.CTkLabel(

            self,

            text="Explain AI",

            font=("Arial",18,"bold")

        )

        self.title.pack(pady=(10,5))

        self.description = ctk.CTkLabel(

            self,

            text="",

            wraplength=300,

            justify="left"

        )

        self.description.pack(
            padx=10,
            pady=5
        )

    def update(self, explanation):

        if explanation is None:

            self.description.configure(
                text=""
            )

            return

        text = explanation["description"]

        text += "\n\n"

        text += "Applications:\n"

        for app in explanation["applications"]:

            text += f"• {app}\n"

        text += "\nTips:\n"

        text += explanation["tips"]

        self.description.configure(
            text=text
        )