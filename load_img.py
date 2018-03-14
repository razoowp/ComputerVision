import cv2

img = cv2.imread('ss.jpg', cv2.IMREAD_COLOR) #IMREAD_GRAYSCALE
cv2.imshow("Stephen Hawking", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
