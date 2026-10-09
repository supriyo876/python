
import cv2 as cv

# 1. Load the photo
path = cv.imread(r"D:\photos\shitakundo\20250108_100603.jpg")

image = cv.resize(path,(800,600))

# 2. Check whether the photo loaded
if image is None:
    print("Error: Image not found!")
    exit()

# 3. Convert the photo to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# 4. Load the pre-trained face detector
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# 5. Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# 6. Draw a rectangle around every detected face
for (x, y, w, h) in faces:
    cv.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# 7. Display the result
print("Number of faces detected:", len(faces))

cv.imshow("Face Detection", image)
cv.waitKey(0)
cv.destroyAllWindows()


