import RPi.GPIO as GPIO

#This GPIO 5 is controls the power to the BLE
BLEPWRCTL =  5           

#This function initializes the GPIO pins
def Init_GPIO():                
	GPIO.setmode(BLEPWRCTL.BCM)
	GPIO.setwarnings(False)

#This will turn on the power to the BLE
def BLEon():
	GPIO.setup(BLEPWRCTL, GPIO.OUT)
    GPIO.setup(BLEPWRCTL,GPIO.HIGH)

#This functon will turn off the power to the BLE 
def BLEoff():
	GPIO.setup(BLEPWRCTL,GPIO.OUT)
	GPIO.setup(BLEPWRCTL,GPIO.LOW)