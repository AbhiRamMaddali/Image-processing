import cv2

# Load the RGB image
rgb_image = cv2.imread(r"C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg")  

# Converting RGB to HSV
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

# Saveing the HSV image
cv2.imwrite(r"C:\Users\abhir\Desktop\PX.jpg", hsv_image)
