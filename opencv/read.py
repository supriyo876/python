import cv2 as cv

print(" Script started")

path = r"D:\python\opencv\photoss\sup.jpg"
# r for raw string for avoiding escape sequence

img = cv.imread(path)

print("Image variable:", img)

if img is None:
    print("Image NOT loaded")
    input("Press Enter to exit...")
else:
    print("Image loaded")
    cv.imshow("sup", img) #open a window name with sup 
    cv.waitKey(0) #wait untill a key is pressed
    cv.destroyAllWindows() # when a key is pressed it destroyed
