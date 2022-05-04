import cv2
import numpy as np

image = cv2.imread("img.png")

(height, width) = image.shape[:2]
#cv2.INTER_CUBIC for zooming on an image
image = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)

cv2.imshow("Image", image)
cv2.waitKey(0)

#cv2.INTER_AREA for shrinking the image
image = cv2.resize(image, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_AREA)

cv2.imshow("Image", image)
cv2.waitKey(0)