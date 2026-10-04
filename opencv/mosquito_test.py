import cv2

# Open video
cap = cv2.VideoCapture(r"D:\python\opencv\videos\mosquito_room_test.mp4")


# Get FPS
fps = cap.get(cv2.CAP_PROP_FPS)

print("FPS:", fps)

# Delay between frames
delay = int(1000 / fps)

# Background subtractor
background = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=25,
    detectShadows=False
)

while True:

    # Read frame
    ret, frame = cap.read()

    # If video ends
    if not ret:
        break

    # Resize
    frame = cv2.resize(frame, (1280, 720))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Background subtraction
    mask = background.apply(gray)

    # Threshold
    _, thresh = cv2.threshold(
        mask,
        200,
        255,
        cv2.THRESH_BINARY
    )

    # Morphological operation
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (3, 3)
    )

    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Process contours
    for contour in contours:

        # Calculate area
        area = cv2.contourArea(contour)

        # Ignore tiny noise
        if area < 5:
            continue

        # Bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Ignore very large objects
        if area > 1000:
            continue

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display area
        cv2.putText(
            frame,
            f"Area: {int(area)}",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1
        )

    # Display results
    cv2.imshow("Mosquito Detection", frame)
    cv2.imshow("Threshold", thresh)

    # Wait according to video FPS
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()