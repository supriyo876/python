
import cv2 as cv

# Load Haar Cascade
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read image
read = cv.imread(r"D:\photos\shitakundo\20250108_100603.jpg")

img = cv.resize(read,(700,600))

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Improve contrast
gray = cv.equalizeHist(gray)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=4,
    minSize=(30, 30)
)

print("Faces detected:", len(faces))

# Draw rectangles
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()

