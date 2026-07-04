import cv2

from preprocess import preprocess_image
from detect_screen import detect_screen


IMAGE = "../test_images/test.png"


image = cv2.imread(IMAGE)

edges = detect_screen(image)

processed = preprocess_image(IMAGE)

cv2.imshow("Original", image)
cv2.imshow("Edges", edges)
cv2.imshow(
    "Processed",
    cv2.cvtColor(
        (processed * 255).astype("uint8"),
        cv2.COLOR_RGB2BGR
    )
)

cv2.waitKey(0)
cv2.destroyAllWindows()