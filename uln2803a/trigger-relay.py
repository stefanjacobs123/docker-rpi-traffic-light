# based on the sample code
# from http://www.bobrathbone.com/pi_traffic_led.htm

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
# http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# GPIO.BOARD relates to Pi 2 Physical numbers
GPIO.setmode(GPIO.BOARD)

#  +-----+-----+---------+------+---+---Pi 2---+---+------+---------+-----+-----+
#  | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
#  +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
#  |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
#  |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
#  |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
#  |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
#  |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
#  |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
#  |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |


# Setup pin numbers for each rela
# pin number (relay nr. refer to channel of ULN2803A)
RELAY_1 = 31
RELAY_2 = 33
RELAY_3 = 35
RELAY_4 = 37
RELAY_5 = 32
RELAY_6 = 36
RELAY_7 = 38
RELAY_8 = 40

# Define all pins as output pins - need to give current
GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(RELAY_2, GPIO.OUT)
GPIO.setup(RELAY_3, GPIO.OUT)
GPIO.setup(RELAY_4, GPIO.OUT)
GPIO.setup(RELAY_5, GPIO.OUT)
GPIO.setup(RELAY_6, GPIO.OUT)
GPIO.setup(RELAY_7, GPIO.OUT)
GPIO.setup(RELAY_8, GPIO.OUT)

# Reset all pins to low (some pins are default high)
GPIO.output(RELAY_1, GPIO.LOW)
GPIO.output(RELAY_2, GPIO.LOW)
GPIO.output(RELAY_3, GPIO.LOW)
GPIO.output(RELAY_4, GPIO.LOW)
GPIO.output(RELAY_5, GPIO.LOW)
GPIO.output(RELAY_6, GPIO.LOW)
GPIO.output(RELAY_7, GPIO.LOW)
GPIO.output(RELAY_8, GPIO.LOW)

# enough time to run 'docker run --rm --cap-add SYS_RAWIO --device /dev/mem hypriot/rpi-gpio readall' and see if pins are low
time.sleep(15)

# This loop runs forever and handles the button and LEDs
while True:
    # Turn on the green LED for cars
    GPIO.output(RELAY_1, GPIO.HIGH)
    GPIO.output(RELAY_2, GPIO.HIGH)
    GPIO.output(RELAY_3, GPIO.HIGH)
    GPIO.output(RELAY_4, GPIO.HIGH)
    GPIO.output(RELAY_5, GPIO.HIGH)
    GPIO.output(RELAY_6, GPIO.HIGH)
    GPIO.output(RELAY_7, GPIO.HIGH)
    GPIO.output(RELAY_8, GPIO.HIGH)

GPIO.cleanup()
