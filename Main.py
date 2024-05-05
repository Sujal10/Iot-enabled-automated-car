import RPi.GPIO as GPIO
import time
import sys

# Define GPIO pins for motors
MOTOR1_PIN1 = 29  # Motor 1 - Pin 1
MOTOR1_PIN2 = 31  # Motor 1 - Pin 2
MOTOR2_PIN1 = 33  # Motor 2 - Pin 1
MOTOR2_PIN2 = 35  # Motor 2 - Pin 2
MOTOR3_PIN1 = 37  # Motor 3 - Pin 1
MOTOR3_PIN2 = 38  # Motor 3 - Pin 2

# Define GPIO pins for sensors
MQ5_SENSOR_PIN = 13  
IR_SENSOR_PIN = 15  
ULTRASONIC_TRIGGER_PIN = 7  
ULTRASONIC_ECHO_PIN = 11  

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MQ5_SENSOR_PIN, GPIO.IN)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)

# Setup motor GPIO
GPIO.setup(MOTOR1_PIN1, GPIO.OUT)
GPIO.setup(MOTOR1_PIN2, GPIO.OUT)
GPIO.setup(MOTOR2_PIN1, GPIO.OUT)
GPIO.setup(MOTOR2_PIN2, GPIO.OUT)
GPIO.setup(MOTOR3_PIN1, GPIO.OUT)
GPIO.setup(MOTOR3_PIN2, GPIO.OUT)

# Function to stop all motors
def stop_motors():
    GPIO.output(MOTOR1_PIN1, GPIO.LOW)
    GPIO.output(MOTOR1_PIN2, GPIO.LOW)
    GPIO.output(MOTOR2_PIN1, GPIO.LOW)
    GPIO.output(MOTOR2_PIN2, GPIO.LOW)
    GPIO.output(MOTOR3_PIN1, GPIO.LOW)
    GPIO.output(MOTOR3_PIN2, GPIO.LOW)

try:
    cycles = 0
    while cycles < 30:  # Run for 30 cycles
        # Read keyboard input
        char = sys.stdin.read(1)

        # Stop all motors initially
        stop_motors()

        # Check input and control motors
        if char == 'w':  # Move forward
            GPIO.output(MOTOR1_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR1_PIN2, GPIO.LOW)
            GPIO.output(MOTOR2_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR2_PIN2, GPIO.LOW)
            GPIO.output(MOTOR3_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR3_PIN2, GPIO.LOW)
        elif char == 'a':  # Turn left
            GPIO.output(MOTOR1_PIN1, GPIO.LOW)
            GPIO.output(MOTOR1_PIN2, GPIO.HIGH)
            GPIO.output(MOTOR2_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR2_PIN2, GPIO.LOW)
            GPIO.output(MOTOR3_PIN1, GPIO.LOW)
            GPIO.output(MOTOR3_PIN2, GPIO.HIGH)
        elif char == 'd':  # Turn right
            GPIO.output(MOTOR1_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR1_PIN2, GPIO.LOW)
            GPIO.output(MOTOR2_PIN1, GPIO.LOW)
            GPIO.output(MOTOR2_PIN2, GPIO.HIGH)
            GPIO.output(MOTOR3_PIN1, GPIO.HIGH)
            GPIO.output(MOTOR3_PIN2, GPIO.LOW)
        elif char == 's':  # Stop
            stop_motors()

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

        cycles += 1
        time.sleep(1)  # Delay between cycles

except KeyboardInterrupt:
    GPIO.cleanup()
