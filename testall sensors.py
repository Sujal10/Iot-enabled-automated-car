import RPi.GPIO as GPIO
import time

# Define GPIO pins
MQ5_SENSOR_PIN = 13  
IR_SENSOR_PIN = 15  
ULTRASONIC_TRIGGER_PIN = 7  
ULTRASONIC_ECHO_PIN = 11  

# Setup GPIO
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(MQ5_SENSOR_PIN, GPIO.IN)  # Set MQ5_SENSOR_PIN as input
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Set IR_SENSOR_PIN as input
GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)  # Set ULTRASONIC_TRIGGER_PIN as output
GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)  # Set ULTRASONIC_ECHO_PIN as input

try:
    while True:
        # Read MQ-5 gas sensor output
        mq5_sensor_value = GPIO.input(MQ5_SENSOR_PIN)
        mq5_sensor_status = "Gas Detected" if mq5_sensor_value == GPIO.LOW else "No Gas"

        # Read IR sensor output
        ir_sensor_value = GPIO.input(IR_SENSOR_PIN)
        ir_sensor_status = "Object Detected" if ir_sensor_value == GPIO.HIGH else "No Object"

        # Read ultrasonic sensor output
        GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(ULTRASONIC_TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ULTRASONIC_ECHO_PIN) == 0:
            pulse_start = time.time()
        while GPIO.input(ULTRASONIC_ECHO_PIN) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150  # Speed of sound in cm/s

        # Display sensor outputs
        print("MQ-5 Gas Sensor:", mq5_sensor_status)
        print("IR Sensor:", ir_sensor_status)
        print("Ultrasonic Sensor Distance:", round(distance, 2), "cm")

        time.sleep(1)  # Delay for readability
except KeyboardInterrupt:
    GPIO.cleanup()
