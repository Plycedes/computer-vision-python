#Importing the OpenCV library
import cv2

#Reading the image
image = cv2.imread('img.png')
#Extracting the height and width of the image
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

#Extracting RGB values of a random pixel, here the pixel at (100, 100) coordinate
(B, G, R) = image[100, 100]
print("R = {}, G = {}, B = {}".format(R, G, B))

#Extracting the value for a specific channel here the blue value of a pixel at coordinate (100, 100, 0)
B = image[100, 100, 0]
print("B = {}".format(B))

