import RPi.GPIO as GPIO
import time
import datetime
import csv


#This the function used to toggle the watchdog gpio pin of the WDT to stop RESET

def watch_dog_start_stop(i):
    GPIO.setup(i,GPIO.LOW)
    GPIO.setup(i,GPIO.HIGH)
    time.sleep(1)
    GPIO.setup(i,GPIO.LOW)


done = 6                    #GPIO 6 is used to control the watchdog function
wake = 16                   #Is used to receive the Wake pulses
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(done, GPIO.OUT)
GPIO.setup(done,GPIO.LOW)
GPIO.setup(wake, GPIO.IN)
watch_dog_start_stop(done)
  

delay = 6                   # This will tells after this intevel the Watchdog reset will happend
seconds = 0;
time.sleep(15)


fieldnames = ['TIME DATE', 'ON/OFF']
k = 0
k = datetime.datetime.now()
with open('/home/pi/Desktop/LOG_REAL.csv', 'a+') as csv_file:    #Restart time will be stored into a file
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'TIME DATE': seconds, 'ON/OFF': "ON"})


print("I AM READY")

for i in range(1,delay):                                        
    for m in range(1,330):                                      #This is 330 depends on the reset time resister we set or we used on the board
        time.sleep(1)
        seconds +=1
    watch_dog_start_stop(done)


time.sleep(330)

t = 0
t = datetime.datetime.now()
with open('/home/pi/Desktop/watchdogtimer/LOG_REAL.csv', 'a+') as csv_file: #This stores the time stamp of the restart time
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'TIME DATE': seconds, 'ON/OFF': "OFF"})
    # csv_file.close()
print("let reset the R pi 3 B+, bye")

