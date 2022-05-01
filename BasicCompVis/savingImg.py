import cv2
import os

imgPath = r'D:\CodingProjects\computer-vision-python\BasicCompVis\img.png'
directory = r'D:\CodingProjects\computer-vision-python\BasicCompVis'

img = cv2.imread(imgPath, 1)
#Change the current directory to specified directory
os.chdir(directory)
#Saving the image syntax argument (newfilename, filesource)
cv2.imwrite('savedImg.png', img)