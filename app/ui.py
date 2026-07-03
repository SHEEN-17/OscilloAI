import customtkinter as ctk
from theme import *


def create_title(parent):

    title = ctk.CTkLabel(
        parent,
        text="OscilloAI",
        font=TITLE_FONT
    )

    title.pack(pady=(20,5))

    subtitle = ctk.CTkLabel(
        parent,
        text="AI Oscilloscope Waveform Analyzer",
        font=SUBTITLE_FONT
    )

    subtitle.pack(pady=(0,20))

    return title, subtitle