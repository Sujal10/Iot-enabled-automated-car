import RPi.GPIO as GPIO
import time

# Define GPIO pins
IR_SENSOR_PIN = 15  # GPIO pin connected to the IR sensor output

# Setup GPIO
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Set IR_SENSOR_PIN as input

try:
    while True:
        ir_sensor_value = GPIO.input(IR_SENSOR_PIN)  # Read IR sensor output

        if ir_sensor_value == GPIO.HIGH:
            print("IR Sensor: Object detected")
        else:
            print("IR Sensor: No object detected")

        time.sleep(1)  # Delay for readability
except KeyboardInterrupt:
    GPIO.cleanup()
