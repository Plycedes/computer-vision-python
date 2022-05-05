import cv2
import numpy as np

image = cv2.imread("img.png")

image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, None, value = 0)
cv2.imshow("ThickBorder", image)
cv2.waitKey(0)

image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)
cv2.imshow("BrokenBorder", image)
cv2.waitKey(0)
