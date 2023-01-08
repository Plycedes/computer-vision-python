import cv2

image = cv2.imread('img.png', cv2.IMREAD_COLOR)

window_name = 'theimage'

cv2.imshow("Abhay", image)
cv2.waitKey(0)
cv2.destroyAllWindows()