import cv2
img=cv2.imread(r"C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,150,175)
cv2.imwrite(r"C:\Users\abhir\Desktop\P.jpg",canny)
