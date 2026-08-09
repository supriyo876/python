import cv2 as cv
import numpy as np

# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw an ellipse
cv.ellipse(
    img,                  # Image
    (250, 250),           # Center of ellipse (x, y)
    (150, 80),            # Axes lengths
    0,                    # Rotation angle
    0,                    # Starting angle
    360,                  # Ending angle
    (255, 0, 0),          # Color: Blue (B, G, R)
    2                     # Thickness
)

# Display the image
cv.imshow("Ellipse", img)

# Wait until any key is pressed
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()