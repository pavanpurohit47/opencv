import cv2
img = cv2.imread("images/cat.jpg")
cv2.imshow("pavan",img)

# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
