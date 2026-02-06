import cv2 as cv



capture = cv.VideoCapture(r"D:\python\opencv\videos\orientation.mp4")

while True:
    istrue, frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

