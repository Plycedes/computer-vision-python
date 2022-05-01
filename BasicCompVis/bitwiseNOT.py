import cv2
import numpy as np

img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')
#applying the bitwise NOT operation on the images
destination1 = cv2.bitwise_not(img1,  mask = None)
destination2 = cv2.bitwise_not(img2,  mask = None)


cv2.imshow('BitwiseNOTimg1', destination1)
cv2.imshow('BitwiseNOTImg2', destination2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()