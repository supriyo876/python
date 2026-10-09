
import cv2 as cv
import os

# Image and model paths
image_path = r"D:\photos\shitakundo\20250107_120417.jpg"
model_path = r"D:\python\opencv\models\face_detection_yunet_2023mar.onnx"

# Check whether files exist
if not os.path.exists(image_path):
    print("Image file not found!")
    exit()

if not os.path.exists(model_path):
    print("YuNet model not found!")
    exit()

# Read the original image
img = cv.imread(image_path)

if img is None:
    print("Could not read image!")
    exit()

# Resize the image
img = cv.resize(img, (700, 600))

# Get the resized image dimensions
height, width = img.shape[:2]

# Create YuNet face detector
detector = cv.FaceDetectorYN.create(
    model_path,
    "",
    (width, height),
    0.5,   # Confidence threshold
    0.3,   # NMS threshold
    5000   # Maximum detections
)

# Detect faces
_, faces = detector.detect(img)

count = 0

if faces is not None:
    count = len(faces)

    for face in faces:
        x, y, w, h = face[:4].astype(int)

        cv.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

print("Faces detected:", count)

cv.imshow("YuNet Face Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()