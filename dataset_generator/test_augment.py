import cv2

from augment import *

image = cv2.imread("../test_images/test.png")

image = random_brightness(image)
image = random_blur(image)
image = random_noise(image)

cv2.imshow("Augmented", image)

cv2.waitKey(0)
cv2.destroyAllWindows()