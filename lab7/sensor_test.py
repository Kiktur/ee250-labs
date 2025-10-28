# Note: need to run pip install mcp3008
# Note: need to run pip install RPi.GPIO
import mcp3008
import RPi.GPIO as GPIO
import time

# Opting to use board numbers (pin numbers on P1 header of RPi)
GPIO.setmode(GPIO.BOARD)
# or
# GPIO.setmode(GPIO.BCM)


LED = 11 # TODO: Change to correct number

# Set channel as input
# GPIO.setup(channel, GPIO.IN)

# Read value of input
#GPIO.input(channel)
# Set channel as output
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
# GPIO.output(channel, state) set output of channel
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

adc = mcp3008.MCP3008()

# Target function:
# 1. Blink the LED 5 times with on/off intervals of 500ms. .
# 2. For about 5 seconds, read the output of the Grove light sensor with intervals of 100 ms and print the raw value

# 3. Blink the LED 4 times with on/off intervals of 200ms.
# 4. For about 5 seconds, read the output of the Grove sound sensor with intervals of 100 ms and print the raw
# value. If the sound sensor is tapped (i.e. the sound magnitude goes above the threshold you decide from
# experimentation), the LED should turn on for 100 ms.

while True:
    # Blink LED 5 times
    GPIO.output(LED, GPIO.HIGH)
    light_val = adc.read([mcp3008.CH0])
    print("Light value is: ")
    print(light_val)
    sound_val = adc.read([mcp3008.CH1])
    print("Sound value is: ") # prints raw data [CH1]
    print(sound_val)
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)
    # for i in range(5):
    #     GPIO.output(LED, GPIO.HIGH)
    #     time.sleep(0.25)
    #     GPIO.output(LED, GPIO.LOW)
    
    # Read light values
    # for i in range(50):
    #     light_val = adc.read([mcp3008.CH0])
    #     print(light_val) # prints raw data [CH0]
    #     if (light_val < 500):
    #         print("Dark")
    #     else:
    #         print("Bright")
    #     time.sleep(0.1)

    # Blink LED 4 times
    # for i in range(4):
    #     GPIO.output(LED, GPIO.HIGH)
    #     time.sleep(0.2)
    #     GPIO.output(LED, GPIO.LOW)

    # # Read sound values
    # for i in range(50):
    #     sound_val = adc.read([mcp3008.CH1])
    #     print(f"Sound value is: {sound_val}") # prints raw data [CH1]
    #     if (sound_val > 500):
    #         print("Loud")
    #     else:
    #         print("Quiet")
    #     time.sleep(0.1)


adc.close()

# Cleanup all channels
GPIO.cleanup()
