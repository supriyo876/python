import cv2

# --------------------------------
# 1. Read image
# --------------------------------
image = cv2.imread(r"D:\python\opencv\photoss\images.jpeg")

# --------------------------------
# 2. Convert to grayscale
# --------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------------
# 3. Threshold
# --------------------------------
_, thresh = cv2.threshold(
    gray,
    100,
    255,
    cv2.THRESH_BINARY
)

# --------------------------------
# 4. Create kernel
# --------------------------------
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (3, 3)
)

# --------------------------------
# 5. Erosion
# --------------------------------
erosion = cv2.erode(
    thresh,
    kernel,
    iterations=1
)

# --------------------------------
# 6. Dilation
# --------------------------------
dilation = cv2.dilate(
    thresh,
    kernel,
    iterations=1
)

# --------------------------------
# 7. Opening
# --------------------------------
opening = cv2.morphologyEx(
    thresh,
    cv2.MORPH_OPEN,
    kernel
)

# --------------------------------
# 8. Closing
# --------------------------------
closing = cv2.morphologyEx(
    thresh,
    cv2.MORPH_CLOSE,
    kernel
)

# --------------------------------
# 9. Show results
# --------------------------------
cv2.imshow("Original", image)
cv2.imshow("Threshold", thresh)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()