import cv2
def rescaleFrame(frame, scale=0.75):
    '''works for images videos and also live videos'''
    Width =  int(frame.shape[1] * scale)
    Height = int(frame.shape[0] * scale)
    print(Width,Height)
    dimensions = (Width, Height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

#rescale the images
img = cv2.imread("images/cat.jpg")
cv2.imshow("pavan",img)
resized_image = rescaleFrame(img,scale=.3)# scale is the percentage here
cv2.imshow("rescale image",resized_image)



#rescale the video
capture = cv2.VideoCapture("videos/Cat.mp4")
while True:
    isTrue, Frame = capture.read()
    frame_resized = rescaleFrame(Frame, scale=.25)
    cv2.imshow('video', Frame)
    cv2.imshow('Rescaled_video', frame_resized)

    if cv2.waitKey(20) and 0xFF == ord('d'):#if the letter d is pressed it will break out of the loop
         break

capture.release()
cv2.destroyAllWindows()