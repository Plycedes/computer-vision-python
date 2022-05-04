import cv2
import numpy as np

image = cv2.imread("img.png")

image = cv2.Canny(image, 100, 200)

cv2.imshow("Image", image)
cv2.waitKey(0)