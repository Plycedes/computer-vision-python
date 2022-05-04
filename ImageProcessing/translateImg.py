import cv2
import numpy as np

img = cv2.imread("img.png")

(height , width) = img.shape[:2]
#creating the translation matrix
#shifting the image 69 on x and 420 on y
transMatrix = np.float32([[1, 0, 69], [0, 1, 420]])
#applying the translation parameters on the image using warpAffine function
img = cv2.warpAffine(img, transMatrix, (height, width))

cv2.imshow("Image", img)
cv2.waitKey(0)