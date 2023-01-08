import cv2

img = cv2.imread("img.png", cv2.IMREAD_COLOR)

cv2.imshow("Abhay", img)

cv2.waitKey(0)

cv2.destroyAllWindows()