import cv2

image = cv2.imread('rgb.png', 1)
#splitting the image in its colors
R, G, B = cv2.split(image)

cv2.imshow("original", image)
cv2.waitKey(0)
#showing the image with different color spaces of RGB
cv2.imshow("red", R)
cv2.waitKey(0)

cv2.imshow("green", G)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)

cv2.destroyAllWindows()