import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width =  int (frame.shape[1] * scale)   
    height =  int (frame.shape[0] * scale)

    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(r'D:\python\opencv\videos\orientation.mp4')

while True:
    isTrue ,frame =  capture.read()

    if not isTrue:
        break

    frame_resized = rescaleFrame(frame,)

    cv.imshow('video_resized', frame_resized,)
    
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)



# FOR WAIT UNTILL PRESS ANY KEY TO CLOSE THE WINDOW
"""
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(r'D:\python\opencv\videos\orientation.mp4')

last_frame = None  # 👈 store last frame

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break

    frame_resized = rescaleFrame(frame)
    last_frame = frame_resized  # 👈 save it

    cv.imshow('video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

# 🔒 show last frame & wait
if last_frame is not None:
    cv.imshow('video_resized', last_frame)
    cv.waitKey(0)

cv.destroyAllWindows()


"""