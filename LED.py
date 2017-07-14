import RPi.GPIO as GPIO
import time
import pyrebase

config = {
    "apiKey": "AIzaSyD6cr3TxbHq8WPPVc9vaHfwjp--6FlRIdA",
    "authDomain": "cxapi-c8d4d.firebaseapp.com",
    "databaseURL": "https://cxapi-c8d4d.firebaseio.com/",
    "storageBucket": "cxapi-c8d4d.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(29,GPIO.OUT)

    def stream_handler(message):
    	print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    my_stream = db.child("Pi1").child("Pi1").stream(stream_handler)

    my_stream.close()

    # print "LED on"
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(7,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(29,GPIO.HIGH)
    time.sleep(1)
    # print "LED off"
    GPIO.output(19,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(29,GPIO.LOW)
    time.sleep(1)
