import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
print "LED on"
GPIO.output(19,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(19,GPIO.LOW)

#from gpiozero import LED

#led = LED(22)

#led.on()
