import cv2

# 1. Read image
image = cv2.imread(r"D:\python\opencv\photoss\images.jpeg")

# 2. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)

# 3. Thresholding
_, thresh = cv2.threshold(
    gray,
    100,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Threshold", thresh)

# 4. Create kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (3, 3)
)

# 5. Erosion
eroded = cv2.erode(
    thresh,
    kernel,
    iterations=1
)

cv2.imshow("Erosion", eroded)

# 6. Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()