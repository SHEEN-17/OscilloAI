import cv2


def draw_screen(image, screen):

    output = image.copy()

    if screen is not None:

        cv2.drawContours(

            output,

            [screen],

            -1,

            (0, 255, 0),

            3

        )

    return output