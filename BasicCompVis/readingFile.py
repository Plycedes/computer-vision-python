import cv2

image = cv2.imread('img.png', 1)

window_name = 'theimage'

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()