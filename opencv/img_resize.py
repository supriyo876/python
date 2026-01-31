import cv2 as cv

print("Script started")

path = r"D:\python\opencv\photoss\sup.jpg"

# Read the image
img = cv.imread(path)

if img is None:
    print("Image NOT loaded")
    input("Press Enter to exit...")
else:
    print("Image loaded")
    
    # Resize the image to 300x300 pixels (for example)
    resized_img = cv.resize(img, (500, 500))  # (width, height)
    
    # Display the resized image
    cv.imshow("Resized sup", resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    # Optionally, save the resized image
    cv.imwrite(r"D:\python\opencv\photoss\sup_resized.jpg", resized_img)
    print("Resized image saved")
