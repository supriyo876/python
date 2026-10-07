import cv2

image = cv2.imread(r"D:\python\opencv\photoss\images.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)


thresh = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2

)
cv2.imshow("threshold" ,thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
