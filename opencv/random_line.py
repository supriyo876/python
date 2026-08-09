import cv2 as cv
import numpy as np
import random

# Image size
window_width = 800
window_height = 600

# Create black image
image = np.zeros(
    (window_height, window_width, 3),
    dtype=np.uint8
)

window_name = "Drawing"


# --------------------------------------------------
# 1. Draw random lines
# --------------------------------------------------

def Drawing_Random_Lines(image):

    for i in range(20):

        start = (
            random.randint(0, window_width - 1),
            random.randint(0, window_height - 1)
        )

        end = (
            random.randint(0, window_width - 1),
            random.randint(0, window_height - 1)
        )

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        thickness = 2

        cv.line(
            image,
            start,
            end,
            color,
            thickness
        )

    return 0


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

Drawing_Random_Lines(image)

cv.imshow(window_name, image)

cv.waitKey(0)
cv.destroyAllWindows()