#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess

# Connect GPIO3 to shutdown button.
SHUTDOWN_GPIO = 3

# Set mode of GPIO to BCM.
GPIO.setmode(GPIO.BCM)
# Set the GPIO as input, and enable its internal pull-up resistor.
GPIO.setup(SHUTDOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Wait for falling edge on GPIO3.
GPIO.wait_for_edge(SHUTDOWN_GPIO, GPIO.FALLING)

# Halt Raspberry PI, that can awake by GPIO.
subprocess.call(['sudo', 'halt'], shell=False)
# Shutdown Raspberry PI, that can NOT awake.
#subprocess.call(['shutdown', '-h', 'now'], shell=False)