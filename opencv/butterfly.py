import cv2 as cv
import numpy as np

# Create a blank canvas
blank = np.zeros((600, 800, 3), dtype=np.uint8)

# Make background white
blank[:] = 255, 255, 255


# =========================
# LEFT WINGS
# =========================

# Upper left wing
cv.ellipse(
    blank,
    (300, 230),       # center
    (170, 120),       # axes
    -30,              # angle
    0,
    360,
    (255, 100, 0),
    -1
)

# Lower left wing
cv.ellipse(
    blank,
    (300, 370),
    (150, 100),
    30,
    0,
    360,
    (255, 180, 0),
    -1
)


# =========================
# RIGHT WINGS
# =========================

# Upper right wing
cv.ellipse(
    blank,
    (500, 230),
    (170, 120),
    30,
    0,
    360,
    (255, 100, 0),
    -1
)

# Lower right wing
cv.ellipse(
    blank,
    (500, 370),
    (150, 100),
    -30,
    0,
    360,
    (255, 180, 0),
    -1
)


# =========================
# BODY
# =========================

cv.ellipse(
    blank,
    (400, 320),
    (35, 150),
    0,
    0,
    360,
    (0, 0, 0),
    -1
)


# =========================
# HEAD
# =========================

cv.circle(
    blank,
    (400, 160),
    45,
    (0, 0, 0),
    -1
)


# =========================
# ANTENNAE
# =========================

cv.line(
    blank,
    (380, 130),
    (320, 70),
    (0, 0, 0),
    5
)

cv.line(
    blank,
    (420, 130),
    (480, 70),
    (0, 0, 0),
    5
)


# =========================
# ANTENNA TIPS
# =========================

cv.circle(
    blank,
    (320, 70),
    10,
    (0, 0, 0),
    -1
)

cv.circle(
    blank,
    (480, 70),
    10,
    (0, 0, 0),
    -1
)


# =========================
# DISPLAY
# =========================

cv.imshow("Butterfly", blank)

cv.waitKey(0)
cv.destroyAllWindows()