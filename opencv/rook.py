import cv2 as cv
import numpy as np

# Create a blank canvas
blank = np.zeros((600, 500, 3), dtype=np.uint8)

# Make background white
blank[:] = 255, 255, 255


# =========================
# ROOK TOP / CROWN
# =========================

# Top rectangular base
cv.rectangle(
    blank,
    (150, 100),
    (350, 170),
    (0, 0, 0),
    -1
)

# Three gaps to create the rook's teeth
blank[100:130, 180:210] = 255, 255, 255
blank[100:130, 245:275] = 255, 255, 255
blank[100:130, 310:340] = 255, 255, 255


# =========================
# ROOK NECK
# =========================

cv.rectangle(
    blank,
    (175, 170),
    (325, 230),
    (0, 0, 0),
    -1
)


# =========================
# ROOK BODY
# =========================

# Upper body
cv.rectangle(
    blank,
    (150, 230),
    (350, 300),
    (0, 0, 0),
    -1
)

# Main body
cv.rectangle(
    blank,
    (170, 300),
    (330, 400),
    (0, 0, 0),
    -1
)


# =========================
# ROOK BASE
# =========================

# Upper part of base
cv.rectangle(
    blank,
    (130, 400),
    (370, 450),
    (0, 0, 0),
    -1
)

# Bottom part of base
cv.rectangle(
    blank,
    (100, 450),
    (400, 500),
    (0, 0, 0),
    -1
)


# =========================
# DISPLAY
# =========================

cv.imshow("Chess Rook", blank)

cv.waitKey(0)
cv.destroyAllWindows()