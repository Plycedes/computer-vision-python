import cv2
import numpy as np

image = cv2.imread("img.png", 1)

kernel = np.ones((5,5), np.uint8)

imgErosion = cv2.erode(image, kernel, iterations = 1)
imgDilation = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow("Input", image)
cv2.imshow("Erosion", imgErosion)
cv2.imshow("Dilation", imgDilation)

cv2.waitKey(0)