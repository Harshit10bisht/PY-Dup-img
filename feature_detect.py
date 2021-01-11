import cv2
import numpy as np

img1 = cv2.imread("jj-1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("jj-2.jpg", cv2.IMREAD_GRAYSCALE)

brisk = cv2.BRISK_create()

kp1, des1 = brisk.detectAndCompute(img1, None)
kp2, des2 = brisk.detectAndCompute(img2, None)

# Brute Force Matching

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
print(len(matches))

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)



cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.imshow("Matching result", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
