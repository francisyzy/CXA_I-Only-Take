import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

#def LEDon():
GPIO.output(19,GPIO.HIGH)
GPIO.output(7,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(29,GPIO.HIGH)
time.sleep(1)
    #return;

#def LEDoff():
GPIO.output(19,GPIO.LOW)
GPIO.output(7,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(29,GPIO.LOW)
time.sleep(1)
    #return;

#LEDoff
#LEDon

while True:

    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://cxapi-c8d4d.firebaseio.com/', None)
    result = firebase.get('/Pi1/Pi1/inBook', None)
    print result
    
    if result == "true":
        GPIO.output(19,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(29,GPIO.HIGH)
        time.sleep(1)
        print "LightON"
    else:
        GPIO.output(19,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(29,GPIO.LOW)
        time.sleep(1)
        print "LightOff"
    time.sleep(3)
    print "One loop done resting 3s"