import cv2
import numpy as np

image = cv2.imread("img.png")
#Creating kernel
kernel = np.ones((3, 5), np.uint8)
#eroding the image according to the kernel
image = cv2.erode(image, kernel)

cv2.imshow("Image", image)
cv2.waitKey(0)