import cv2

image = cv2.imread("dd-1.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image 1",gray_image)
cv2.imshow("Image 1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
