import cv2
import numpy as np

image = cv2.imread("img.png")

cv2.imshow("Original", image)
cv2.waitKey(0)

image = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("GaussianBlur", image)
cv2.waitKey(0)

image = cv2.medianBlur(image, 5)
cv2.imshow("MedianBlur", image)
cv2.waitKey(0)

image = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("BilateralBlurring", image)
cv2.waitKey(0)