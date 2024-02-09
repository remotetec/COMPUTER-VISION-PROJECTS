import numpy 
import cv2
img=cv2.imread('test1.jpeg',1)
# img=cv2.line(img,(0,0),(255,255),(147,96,44),10) #this is used to put line on image
# img=cv2.arrowedLine(img,(0,255),b(255,255),(255,0,0),10)#this is used to put arrow on image
# img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),1)#this is used to put rectangle on image
img=cv2.circle(img,(447,63),63,(0,255,0),-1)#this is used to put circle on image
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'openCv',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()