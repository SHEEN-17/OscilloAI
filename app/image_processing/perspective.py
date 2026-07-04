import cv2
import numpy as np


def order_points(points):

    rect = np.zeros((4,2),dtype="float32")

    s = points.sum(axis=1)

    rect[0]=points[np.argmin(s)]

    rect[2]=points[np.argmax(s)]

    diff=np.diff(points,axis=1)

    rect[1]=points[np.argmin(diff)]

    rect[3]=points[np.argmax(diff)]

    return rect


def four_point_transform(image,pts):

    rect=order_points(pts)

    (tl,tr,br,bl)=rect

    widthA=np.linalg.norm(br-bl)

    widthB=np.linalg.norm(tr-tl)

    maxWidth=max(int(widthA),int(widthB))

    heightA=np.linalg.norm(tr-br)

    heightB=np.linalg.norm(tl-bl)

    maxHeight=max(int(heightA),int(heightB))

    dst=np.array([

        [0,0],

        [maxWidth-1,0],

        [maxWidth-1,maxHeight-1],

        [0,maxHeight-1]

    ],dtype="float32")

    M=cv2.getPerspectiveTransform(rect,dst)

    warped=cv2.warpPerspective(

        image,

        M,

        (maxWidth,maxHeight)

    )

    return warped