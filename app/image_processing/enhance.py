import cv2


def enhance(image):

    gray=cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    gray=cv2.equalizeHist(gray)

    blur=cv2.GaussianBlur(

        gray,

        (3,3),

        0

    )

    return blur