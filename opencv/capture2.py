import cv2 

path="/home/pi/jarvis/public/img/"

webcam = cv2.VideoCapture(0)
check, frame = webcam.read()
print(check)
print(frame)
cv2.imwrite(filename=path+'img1.jpg', img=frame)
webcam.release()


webcam2 = cv2.VideoCapture(2)
check, frame = webcam2.read()
print(check)
print(frame)
cv2.imwrite(filename=path+'img2.jpg', img=frame)
webcam2.release()
