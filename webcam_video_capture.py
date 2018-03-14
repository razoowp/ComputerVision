import cv2
cap = cv2.VideoCapture(0)

#To write captured video
#cv2.VideoWriter_fourcc(*'XVID')

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 

vid = fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('video.avi', vid, 20.0,(int(w),int(h)))

while(True):
    ret, frame = cap.read()
    cv2.imshow('Color', frame)

    #To Write captured Video
    out.write(frame)
    
    #Displaying Grayscale
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', frame1)
    
    if cv2.waitKey(1) &0XFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()




# w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
# h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 
# fourcc = cv2.CV_FOURCC(*'XVID')
# out = cv2.VideoWriter('output.mp4',fourcc, 15.0, (int(w),int(h)))