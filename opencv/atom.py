import cv2 as cv
import numpy as np

# Image size
W = 500

# Create a black image
atom = np.zeros((W, W, 3), dtype=np.uint8)

# Center of the image
center = (W // 2, W // 2)

# Draw vertical ellipse
cv.ellipse(
    atom,
    center,
    (150, 50),
    90,
    0,
    360,
    (255, 0, 0),
    2
)

# Draw horizontal ellipse
cv.ellipse(
    atom,
    center,
    (150, 50),
    0,
    0,
    360,
    (255, 0, 0),
    2
)

# Draw diagonal ellipse: 45 degrees
cv.ellipse(
    atom,
    center,
    (150, 50),
    45,
    0,
    360,
    (255, 0, 0),
    2
)

# Draw diagonal ellipse: -45 degrees
cv.ellipse(
    atom,
    center,
    (150, 50),
    -45,
    0,
    360,
    (255, 0, 0),
    2
)

# Draw red nucleus
cv.circle(
    atom,
    center,
    20,
    (0, 0, 255),
    -1
)

# Show the atom
cv.imshow("Atom", atom)

# Wait for a key
cv.waitKey(0)

# Close the window
cv.destroyAllWindows()