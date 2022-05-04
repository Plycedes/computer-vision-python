import cv2


import cv2
import numpy as np

image = cv2.imread("img.png")

(height, width) = image.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
rotMatrix = cv2.getRotationMatrix2D((height / 2, width / 2), 45, 1)

image = cv2.warpAffine(image, rotMatrix, (height, width))

cv2.imshow("Image", image)
cv2.waitKey(0)