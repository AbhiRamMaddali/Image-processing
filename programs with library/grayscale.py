import cv2
# Reading an image 
img = cv2.imread(r'C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg')
# Convert to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Saving the grayscale image
cv2.imwrite(r'C:\Users\abhir\Desktop\gray_image.jpg', gray_image)
