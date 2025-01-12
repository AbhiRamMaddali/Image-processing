#The Version of Python compiler 3.13.0
import cv2
img=cv2.imread(r"C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg")
blur=cv2.blur(img,(13,13))

cv2.imwrite(r"C:\Users\abhir\Desktop\j.jpg",blur)
