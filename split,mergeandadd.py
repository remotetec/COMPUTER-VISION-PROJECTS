import numpy as np
import cv2

img=cv2.imread('rohit.jpeg')
img2=cv2.imread('rohit.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

ball=img[280:340,330:390]
img[273:333,100:160]=ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.addWeighted(img,2,img2,0.8,0)
cv2.imshow('image',dst)
cv2.waitkey(0)
cv2.destroyAllWindows()