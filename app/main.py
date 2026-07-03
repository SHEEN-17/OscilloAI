import customtkinter as ctk
from tkinter import filedialog
from PIL import Image

from predictor import predict_image
from ui import create_title

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("OscilloAI")
app.geometry("1000x650")

selected_image = None


# ==========================================
# UPLOAD IMAGE
# ==========================================

def upload_image():

    global selected_image

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

    selected_image = file_path

    image = Image.open(file_path)

    photo = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(350,280)
    )

    preview.configure(
        image=photo,
        text=""
    )

    preview.image = photo


# ==========================================
# PREDICT
# ==========================================

def predict():

    if selected_image is None:
        return

    wave, confidence, probabilities = predict_image(
        selected_image
    )

    wave_label.configure(
        text=f"Waveform : {wave}"
    )

    confidence_label.configure(
        text=f"{confidence:.2f}%"
    )

    confidence_bar.set(confidence/100)


# ==========================================
# TITLE
# ==========================================

create_title(app)

main = ctk.CTkFrame(
    app,
    width=900,
    height=500
)

main.pack(pady=10)

main.pack_propagate(False)

left = ctk.CTkFrame(
    main,
    width=420,
    height=450
)

left.pack(
    side="left",
    padx=20,
    pady=20
)

left.pack_propagate(False)

right = ctk.CTkFrame(
    main,
    width=420,
    height=450
)

right.pack(
    side="right",
    padx=20,
    pady=20
)

right.pack_propagate(False)

preview = ctk.CTkLabel(
    left,
    text="Image Preview",
    width=350,
    height=280
)

preview.pack(pady=20)

upload_button = ctk.CTkButton(
    left,
    text="Upload Image",
    command=upload_image
)

upload_button.pack(pady=20)

result_title = ctk.CTkLabel(
    right,
    text="Prediction Result",
    font=("Arial",22,"bold")
)

result_title.pack(pady=20)

wave_label = ctk.CTkLabel(
    right,
    text="Waveform : -",
    font=("Arial",20)
)

wave_label.pack(pady=15)

ctk.CTkLabel(
    right,
    text="Confidence",
    font=("Arial",16)
).pack()

confidence_bar = ctk.CTkProgressBar(
    right,
    width=300
)

confidence_bar.pack(pady=10)

confidence_bar.set(0)

confidence_label = ctk.CTkLabel(
    right,
    text="-",
    font=("Arial",18)
)

confidence_label.pack()

predict_button = ctk.CTkButton(
    right,
    text="Predict",
    command=predict
)

predict_button.pack(pady=35)

app.mainloop()