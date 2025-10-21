# Team Members: Angie Vasquez (USC ID: 5537473368) & VIctor Gutierrez (USC ID: 9841169875) 
# Lab 6
import sys, os
sys.path.append(os.path.expanduser('~/Dexter/GrovePi/Software/Python'))
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance_cm = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    threshold_cm = grovepi.analogRead(potentiometer)

    # TODO: format LCD text according to threshhold
    if distance_cm < threshold_cm:
      setRGB(0, 255, 0)
      setText_norefresh(f"{threshold_cm} OBJ PRES\n{distance_cm}")
    else:
      setRGB(255, 0, 0)
      setText_norefresh(f"{threshold_cm}           \n{distance_cm}")

  except IOError:
    print("Error")


