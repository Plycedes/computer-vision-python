import cv2
import numpy as np

img1 = cv2.imread('bit1.png')
img2 = cv2.imread('bit2.png')
#applying the bitwise OR operation on the images
destination = cv2.bitwise_or(img2, img1, mask = None)

cv2.imshow('BitwiseORImg', destination)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()