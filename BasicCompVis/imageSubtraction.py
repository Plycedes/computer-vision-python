import cv2
import numpy as np

img1 = cv2.imread('star.jpg', 1)
img2 = cv2.imread('dot.jpg', 1)

subImg = cv2.subtract(img1, img2)

cv2.imshow('Subtracted Image', subImg)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()