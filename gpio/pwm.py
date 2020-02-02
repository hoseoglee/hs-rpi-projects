import RPi.GPIO as GPIO  
import time  

GPIO.setwarnings(False)
GPIO.setmode( GPIO.BOARD )  
  
#12번핀은 출력모드로 설정  
GPIO.setup(12, GPIO.OUT)  
#GPIO.setup(17, GPIO.OUT)

#GPIO.output(17,GPIO.HIGH)  

pwm = GPIO.PWM(12,50) #50hz  
pwm.start(0)  
  
for i in range(0,3):  
  
    for dc in range(0,101,5):  
        pwm.ChangeDutyCycle(dc)  
        time.sleep(0.1)  
    for dc in range(100,-1,-5):  
        pwm.ChangeDutyCycle(dc)  
        time.sleep(0.1)  
  
pwm.stop()  
GPIO.cleanup()
