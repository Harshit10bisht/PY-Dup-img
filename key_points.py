import cv2
import numpy as np

img = cv2.imread("dd-1.jpg",cv2.IMREAD_GRAYSCALE)

brisk = cv2.BRISK_create()

kp = brisk.detect(img, None)

img = cv2.drawKeypoints(img, kp, None)

cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()