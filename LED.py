import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(29,GPIO.OUT)
    print "LED on"
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(29,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(19,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
