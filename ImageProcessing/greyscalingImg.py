import cv2

image = cv2.imread("img.png")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("greyscale", image)
cv2.waitKey(0)