import cv2
img=cv2.imread('rohit.jpeg',-1)
print(img)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('rohits.png',img)
    cv2.destroyAllWindows()
