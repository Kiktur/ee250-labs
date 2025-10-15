# Team Members: <your names>
# Lab 6 — Real Raspberry Pi + GrovePi (Python 2.7.16 compatible)

import os, sys, time

# Add GrovePi libs (expand ~ correctly)
sys.path.append(os.path.expanduser('~/Dexter/GrovePi/Software/Python'))
sys.path.append(os.path.expanduser('~/Dexter/GrovePi/Software/Python/grove_rgb_lcd'))

import grovepi
from grove_rgb_lcd import setText_norefresh, setText, setRGB

# Ports
ULTRASONIC_D = 2   # D2
POT_A = 0          # A0
grovepi.pinMode(POT_A, "INPUT")

# Map potentiometer 0..1023 -> 0..200 cm (adjust MAX_CM if you want)
MAX_CM = 200  # when the pot is turned all the way to 1023, 200 cm is the threshold

def pot_to_cm(raw):
    # clamp to 0..1023 and scale linearly to 0..MAX_CM
    raw = max(0, min(1023, raw))
    return int(round(raw * MAX_CM / 1023.0))

def safe_ultra_read(pin):
    """
    Reads distance from the ultrasonic sensor with simple retries.
    Returns a non-negative distance on success, or -1 on failure.
    """
    for _ in range(3):  # try up to 3 times
        d = grovepi.ultrasonicRead(pin)
        if d is not None and d >= 0:
            return d
        time.sleep(0.01)
    return -1

setText("")  # clear once

last_text = None
last_rgb = None

try:
    while True:
        try:
            # 1) Read sensors
            dist_cm = safe_ultra_read(ULTRASONIC_D)
            pot_raw = grovepi.analogRead(POT_A)
            thresh_cm = pot_to_cm(pot_raw)

            # 2) Decide presence
            obj = (dist_cm >= 0) and (dist_cm < thresh_cm)

            # 3) Choose LCD color
            rgb = (0, 255, 0) if obj else (255, 0, 0)

            # 4) Build LCD text (16 chars/line max)
            line1 = "{:>3} cm {}".format(thresh_cm, "OBJ PRES" if obj else "")
            line2_val = dist_cm if dist_cm >= 0 else "-"
            line2 = "{:>3} cm".format(line2_val)
            text = "{}\n{}".format(line1[:16], line2[:16])

            # 5) Update LCD only when changed (reduce flicker/I2C traffic)
            if rgb != last_rgb:
                setRGB(*rgb)
                last_rgb = rgb
            if text != last_text:
                setText_norefresh(text)
                last_text = text

            time.sleep(0.05)  # ~20 Hz
        except IOError:
            # Handle transient I2C errors gracefully
            setRGB(255, 0, 0)
            setText_norefresh("I/O Error       \nRetrying...")
            time.sleep(0.2)

except KeyboardInterrupt:
    # Clean exit
    setRGB(0, 0, 0)
    setText("")
