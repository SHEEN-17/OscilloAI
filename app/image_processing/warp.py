import cv2
import numpy as np


def order_points(points):

    points = points.reshape(4, 2)

    rect = np.zeros((4, 2), dtype="float32")

    s = points.sum(axis=1)

    rect[0] = points[np.argmin(s)]
    rect[2] = points[np.argmax(s)]

    diff = np.diff(points, axis=1)

    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    return rect


def perspective_transform(image, screen):

    rect = order_points(screen)

    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)

    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxHeight = int(max(heightA, heightB))

    destination = np.array(

        [

            [0, 0],

            [maxWidth - 1, 0],

            [maxWidth - 1, maxHeight - 1],

            [0, maxHeight - 1]

        ],

        dtype="float32"

    )

    matrix = cv2.getPerspectiveTransform(

        rect,

        destination

    )

    warped = cv2.warpPerspective(

        image,

        matrix,

        (maxWidth, maxHeight)

    )

    return warped