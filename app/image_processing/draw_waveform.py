import cv2


def draw_waveform(image, waveform):

    output = image.copy()

    for point in waveform:

        cv2.circle(

            output,

            point,

            1,

            (0, 0, 255),

            -1

        )

    return output