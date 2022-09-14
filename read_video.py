import cv2
capture = cv2.VideoCapture("videos/Cat.mp4")
while True:  
    isTrue, Frame = capture.read()
    cv2.imshow('video',Frame)

    if cv2.waitKey(20) and 0xFF == ord('d'):#if the letter d is pressed it will break out of the loop
         break

capture.release()
cv2.destroyAllWindows()



