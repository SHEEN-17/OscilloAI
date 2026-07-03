import csv
import os


# ===========================================
# Membuat file metadata.csv
# ===========================================

def create_metadata():

    # Folder utama project (OscilloAI)
    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    # Lokasi file metadata.csv
    metadata_path = os.path.join(
        base_dir,
        "dataset",
        "metadata.csv"
    )

    # Membuat file CSV baru beserta header
    with open(
        metadata_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "filename",
            "waveform",
            "frequency",
            "amplitude"
        ])

    return metadata_path


# ===========================================
# Menambahkan data ke metadata.csv
# ===========================================

def append_metadata(
    metadata_path,
    filename,
    waveform,
    frequency,
    amplitude
):

    with open(
        metadata_path,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            filename,
            waveform,
            frequency,
            amplitude
        ])


# ===========================================
# TEST PROGRAM
# ===========================================

if __name__ == "__main__":

    metadata_path = create_metadata()

    append_metadata(
        metadata_path,
        "sinus_0001.png",
        "sine",
        50,
        5
    )

    append_metadata(
        metadata_path,
        "sinus_0002.png",
        "sine",
        20,
        8
    )

    append_metadata(
        metadata_path,
        "sinus_0003.png",
        "sine",
        75,
        3
    )

    print("=" * 50)
    print("✅ metadata.csv berhasil dibuat")
    print(f"📁 Lokasi : {metadata_path}")
    print("=" * 50)