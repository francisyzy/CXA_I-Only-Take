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
LK=True

while True:
    GPIO.setmode(GPIO.BCM)
        
    TRIG=6
    ECHO=23
    
        
    print "Distance Measurement In Progress"
    
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
	
    GPIO.output(TRIG,GPIO.IN)
	
    GPIO.output(TRIG, False)
	
    GPIO.output(TRIG, True)
	
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
	
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
	
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
	
    pulse_duration = pulse_end - pulse_start
	
    distance = pulse_duration * 17150
	
    distance = round(distance, 2)
	
    print "Distance:", distance, "cm"
	
    GPIO.cleanup()
    if LK:
        if distance > 1000:
            time.sleep(5)
            GPIO.setmode(GPIO.BCM)

            TRIG=6
            ECHO=23
    
    
            print "Distance Measurement In Progress"
            GPIO.setup(TRIG,GPIO.OUT)
            GPIO.setup(ECHO,GPIO.IN)
    
            GPIO.output(TRIG,GPIO.IN)
    
            GPIO.output(TRIG, False)
    
            GPIO.output(TRIG, True)
    
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
    
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
    
            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
    
            distance = round(distance, 2)
    
            print "Distance:", distance, "cm"
            if distance > 1000:
                db.child("Pi1").child("Pi1").update({"inUse": "false"})
                LK = False
    else:
        if distance < 1000:
            time.sleep(5)
            GPIO.setmode(GPIO.BCM)
            
            TRIG=6
            ECHO=23
            
            
            print "Distance Measurement In Progress"
            GPIO.setup(ECHO,GPIO.IN)
            
            GPIO.output(TRIG,GPIO.IN)
            
            GPIO.output(TRIG, False)
            
            GPIO.output(TRIG, True)
            
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
            
            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
        
            pulse_duration = pulse_end - pulse_start
            
            distance = pulse_duration * 17150
            
            distance = round(distance, 2)
            
            print "Distance:", distance, "cm"
            if distance < 1000:
                db.child("Pi1").child("Pi1").update({"inUse": "true"})
                LK = False
