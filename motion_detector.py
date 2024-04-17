"""
https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
"""
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR -- Cannot open camera")
    exit()

ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
while True:
    ret, frame = cap.read()
     # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    diff_frame = cv2.subtract(frame, gray)
    thr, diff_frame = cv2.threshold(diff_frame, 100, 180, cv2.THRESH_BINARY)
    cv2.imshow('frame', diff_frame)
    if diff_frame.sum() > 100_000:
        print("Motion detected!")

    if cv2.waitKey(1) == ord('q'):
        break
    gray = frame
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()