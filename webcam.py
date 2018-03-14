import cv2
capture = cv2.VideoCapture(0)

#To write captured video
vid = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', vid, 20.0, (640, 480))

while(True):
    ret, frame = capture.read()
    cv2.imshow('Color', frame)

    #To Write captured Video
    out.write(frame)
    
    #Displaying Grayscale
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', frame1)
    
    if cv2.waitKey(1) &0XFF == ord('q'):
        break
capture.release()
out.release()
cv2.destroyAllWindows()