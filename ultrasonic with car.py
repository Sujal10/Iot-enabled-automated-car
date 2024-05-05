
import RPi.GPIO as GPIO	#This line imports the RPi.GPIO library
import time
GPIO.setmode(GPIO.BOARD)	#This line sets the pin numbering mode to "BOARD," which means that the pin numbers will be referenced by their physical location on the Raspberry Pi's GPIO header.
PIN_TRIGGER=16  #these are variables assigned to specific GPIO pin numbers on the Raspberry Pi.
PIN_ECHO=18
PIN_IN1=29
PIN_IN2=31
PIN_IN3=33
PIN_IN4=35
GPIO.setwarnings(False)
GPIO.setup(PIN_TRIGGER,GPIO.OUT)
GPIO.setup(PIN_IN1,GPIO.OUT)
GPIO.setup(PIN_IN2,GPIO.OUT)
GPIO.setup(PIN_IN3,GPIO.OUT)
GPIO.setup(PIN_IN4,GPIO.OUT)
GPIO.setup(PIN_ECHO,GPIO.IN)
def stop():							#This function turns off all motor outputs by setting the associated pins to GPIO.LOW
    GPIO.output(PIN_IN1,GPIO.LOW)
    GPIO.output(PIN_IN2,GPIO.LOW)
    GPIO.output(PIN_IN3,GPIO.LOW)
    GPIO.output(PIN_IN4,GPIO.LOW)
def forward():						#This function appears to set the motor configuration for moving forward.
    GPIO.output(PIN_IN1,GPIO.HIGH)
    GPIO.output(PIN_IN2,GPIO.LOW)
    GPIO.output(PIN_IN3,GPIO.HIGH)
    GPIO.output(PIN_IN4,GPIO.LOW)
def left():							#This function seems to set the motor configuration for turning left
    GPIO.output(PIN_IN1,GPIO.HIGH)
    GPIO.output(PIN_IN2,GPIO.LOW)
    GPIO.output(PIN_IN3,GPIO.LOW)
    GPIO.output(PIN_IN4,GPIO.LOW)
stop()
i=0;
while True:
    GPIO.output(PIN_TRIGGER,GPIO.LOW)
    #print("Waiting for sensor to settle")
    #time.sleep(0.00001)
    #print("Calculating distance")
    GPIO.output(PIN_TRIGGER,GPIO.HIGH)
    #time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER,GPIO.LOW)
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time=time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time=time.time()
    pulse_duration=pulse_end_time-pulse_start_time
    distance=round(pulse_duration*17150,2)
    print("Disatnce: ",distance,"cm")
    #time.sleep(0.00001)
    if distance < 30:	#If the measured distance is less than 30 cm, the left() function is called, which suggests the vehicle should turn left.

        left()
        #time.sleep(0.00001)
    else:
        forward()		#Otherwise, the forward() function is called, indicating the vehicle should move forward.
        #time.sleep(0.00001)
stop()
