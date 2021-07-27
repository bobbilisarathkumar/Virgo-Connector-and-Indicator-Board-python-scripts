import RPi.GPIO as GPIO

BLUE = 22       # This GPIO 22 is connected to the RED colour LED

GREEN = 27      # This GPIO 27 is connected to the GREEN colour LED

RED = 17        # This GPIO 17 is connected to the RED colour LED

def Init_GPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def GREENon():
	GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(GREEN,GPIO.HIGH)

def GREENoff():
	GPIO.setup(GREEN,GPIO.OUT)
	GPIO.setup(GREEN,GPIO.LOW)

def BLUEon():
	GPIO.setup(BLUE, GPIO.OUT)
    GPIO.setup(BLUE,GPIO.HIGH)

def BLUEoff():
	GPIO.setup(BLUE,GPIO.OUT)
	GPIO.setup(BLUE,GPIO.LOW)

def REDon():
	GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(RED,GPIO.HIGH)

def REDoff():
	GPIO.setup(RED,GPIO.OUT)
	GPIO.setup(RED,GPIO.LOW)

