#The Version of Python compiler 3.13.0
import cv2
img=cv2.imread(r"C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg")
new_width = 800
new_height = 600

# Resize the image
resized_image = cv2.resize(img, (new_width, new_height))

# Save the resized image
cv2.imwrite(r"C:\Users\abhir\Desktop\rt.jpg",resized_image)
