import cv2
import matplotlib.pyplot as plt
img=cv2.imread(r'C:\Users\abhir\Desktop\opencv\photos\cats 2.jpg')
#cv2.imshow('Cats',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('GRAY',gray )

gray_hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('bins')
plt.ylabel('pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
