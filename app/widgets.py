import customtkinter as ctk


class ProbabilityBar:

    def __init__(self, parent, label):

        self.frame = ctk.CTkFrame(parent)

        self.frame.pack(fill="x", pady=5)

        self.label = ctk.CTkLabel(
            self.frame,
            text=label,
            width=90,
            anchor="w"
        )

        self.label.pack(side="left", padx=5)

        self.bar = ctk.CTkProgressBar(
            self.frame,
            width=180
        )

        self.bar.pack(
            side="left",
            padx=5
        )

        self.bar.set(0)

        self.value = ctk.CTkLabel(
            self.frame,
            text="0%"
        )

        self.value.pack(
            side="left",
            padx=5
        )

    def update(self, probability):

        self.bar.set(probability)

        self.value.configure(
            text=f"{probability*100:.1f}%"
        )