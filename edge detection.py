import cv2
img=cv2.imread(r"C:\Users\abhir\Desktop\cat.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,150,175)
cv2.imshow('canny',canny)
cv2.waitKey(0)
