# Alexander James
# Nov. 2023
# Controls a distance sensor using a Pi Pico

# This imports required libraries and defines the pins
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A0)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:  # Prevents crashing when an error occurs 
        print("Retrying!")
    time.sleep(0.1)