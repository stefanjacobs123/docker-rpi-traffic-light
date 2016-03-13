# based on the sample code from http://www.bobrathbone.com/pi_traffic_led.htm

# First we need to import the libraries that
# we need
# Import the time library so that we can make
# the program pause for a fixed amount of time
import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins

# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up the pin numbers we are using for each LED
# pin number          # Adafruit T-Cobbler
CARS_RED=15           # #22
CARS_YELLOW=13        # #27
CARS_GREEN=11         # #17

PEDESTRIANS_RED=18    # #24
PEDESTRIANS_GREEN=16  # #23

# Define the pin for the switch
SWITCH=22             # #25

# Set Pin 11, 16 and 7 on the GPIO header to act as an output
GPIO.setup(CARS_RED,GPIO.OUT)
GPIO.setup(CARS_YELLOW,GPIO.OUT)
GPIO.setup(CARS_GREEN,GPIO.OUT)

GPIO.setup(PEDESTRIANS_RED,GPIO.OUT)
GPIO.setup(PEDESTRIANS_GREEN,GPIO.OUT)

# Set up pin 22 (SWITCH) to act as an input
GPIO.setup(SWITCH,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

# Reset all LEDs
GPIO.output(CARS_RED,GPIO.LOW)
GPIO.output(CARS_YELLOW,GPIO.LOW)
GPIO.output(CARS_GREEN,GPIO.LOW)
GPIO.output(PEDESTRIANS_RED,GPIO.LOW)
GPIO.output(PEDESTRIANS_GREEN,GPIO.LOW)

# This loop runs forever and flashes the LED
while True:
    # Turn on the green LED for cars
    GPIO.output(CARS_GREEN,GPIO.HIGH)
    GPIO.output(PEDESTRIANS_RED,GPIO.HIGH)
    print "Green"
    ButtonPressed = False

    # Wait until a pedestrian presses the switch
    print "Press button"
    while not ButtonPressed:
        # Wait for 2 seconds
        time.sleep(1)
        ButtonPressed = GPIO.input(SWITCH)

    print "Button pressed"
    # Turn off the green LED
    GPIO.output(CARS_GREEN,GPIO.LOW)
    # Turn on the yellow LED
    GPIO.output(CARS_YELLOW,GPIO.HIGH)
    print "Yellow"
    # Wait for 2 seconds
    time.sleep(2)
    GPIO.output(CARS_YELLOW,GPIO.LOW)
    # Turn on the red LED for cars
    GPIO.output(CARS_RED,GPIO.HIGH)
    print "Red"
    # Wait for 4 seconds
    time.sleep(4)
    GPIO.output(PEDESTRIANS_RED,GPIO.LOW)
    # Turn on the green LED for pedestrians
    GPIO.output(PEDESTRIANS_GREEN,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(PEDESTRIANS_GREEN,GPIO.LOW)
    # Turn on the red LED for pedestrians
    GPIO.output(PEDESTRIANS_RED,GPIO.HIGH)
    # Wait for 2 seconds
    time.sleep(2)

    print "Red and yellow"
    GPIO.output(CARS_YELLOW,GPIO.HIGH)
    time.sleep(4)
    GPIO.output(CARS_YELLOW,GPIO.LOW)
    GPIO.output(CARS_RED,GPIO.LOW)
