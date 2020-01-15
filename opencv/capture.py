import cv2 

path="/home/pi/jarvis/public/img/"

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)

check1, frame1 = cam1.read()
cv2.imwrite(filename=path+'img1.jpg', img=frame1)
cam1.release()

check2, frame2 = cam2.read()
cv2.imwrite(filename=path+'img2.jpg', img=frame2)
cam2.release()

