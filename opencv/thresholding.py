import cv2

image = cv2.imread(r"D:\python\opencv\photoss\ades_mosquito.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)

_, thresh = cv2.threshold(
    gray,
    100,
    255,
    cv2.THRESH_BINARY
)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()