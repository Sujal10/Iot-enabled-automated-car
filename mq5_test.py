import RPi.GPIO as GPIO
import time

# Define GPIO pins
DIGITAL_PIN = 13  # GPIO pin connected to D0 on the MQ-5 sensor

# Setup GPIO
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(DIGITAL_PIN, GPIO.IN)  # Set DIGITAL_PIN as input

try:
    while True:
        digital_output = GPIO.input(DIGITAL_PIN)  # Read digital output from MQ-5 sensor

        print("Digital Output:", digital_output)

        time.sleep(1)  # Delay for readability
except KeyboardInterrupt:
    GPIO.cleanup()
