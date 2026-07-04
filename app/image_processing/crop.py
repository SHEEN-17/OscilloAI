import cv2


def largest_contour(edges):

    contours,_=cv2.findContours(

        edges,

        cv2.RETR_EXTERNAL,

        cv2.CHAIN_APPROX_SIMPLE

    )

    if len(contours)==0:

        return None

    return max(contours,key=cv2.contourArea)