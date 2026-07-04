import cv2

from .detect_screen import detect_screen
from .find_screen import find_screen
from .draw_screen import draw_screen
from .warp import perspective_transform
from .preprocess import preprocess_image

from .extract_waveform import extract_waveform
from .trace_waveform import trace_waveform
from .draw_waveform import draw_waveform


def process(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(image_path)

    edges = detect_screen(image)

    screen = find_screen(image)

    detected = draw_screen(image, screen)

    warped = None
    waveform_image = None
    waveform = []

    if screen is not None:

        warped = perspective_transform(
            image,
            screen
        )

        binary = extract_waveform(
            warped
        )

        waveform = trace_waveform(
            binary
        )

        waveform_image = draw_waveform(
            warped,
            waveform
        )

    processed = preprocess_image(image_path)

    return (
        image,
        edges,
        detected,
        warped,
        waveform_image,
        waveform,
        processed
    )