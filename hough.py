import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
import math
from houghspace import hough_line

#im = cv2.imread(base_dir + "Image.jpg")
cdst = cv2.imread("Image.jpg")
im = cv2.cvtColor(cdst, cv2.COLOR_BGR2GRAY)
#print(im)
im = cv2.Canny(im, 150, 210)

# cv2.imshow("img",im)

# cv2.waitKey(0)
cv2.imwrite("canny.jpg", im)


#im = cv2.HoughLines(im, )
thresh = 65
#lines = cv2.HoughLines(im, 1, 2*np.pi / 180, thresh)
lines = hough_line(im)
# print(lines)

# Draw the lines
#cdst = np.copy(im)
#cv2_imshow(cdst)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(cdst, pt1, pt2, (0,255,0), 1, cv2.LINE_AA)
cv2.imwrite("hough.jpg_"+str(thresh), cdst)
# cv2.imshow("hough",cdst)
# cv2.waitKey(0)