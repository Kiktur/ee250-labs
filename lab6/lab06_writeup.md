Team Members: Victor Gutierrez (USC ID: 9841169875) Angie Vasquez (USC ID: 5537473368)



Reflection Questions



4.1

git clone git@github.com:my-name/my-imaginary-repo.git

cd my-imaginary-repo

touch my\_second\_file.py

echo 'print("Hello World")' > my\_second\_file.py

git add my\_second\_file.py

git commit -m "Add my\_second\_file.py with Hello World"

git push origin main



4.2

For this lab, I wrote and tested my code on a VM since it was easier to edit the Python files from there. I then committed and pushed the code onto GitHub. Then I switched to my Raspberry Pi and used git pull and downloaded the latest updates, and ran the code with the Grove hardware. This helped keep the code organized and version-controlled. I think for the next lab, I will make small edits to the Raspberry Pi using a text-based editor, such as nano, and become more comfortable with Git commands to reduce the time spent switching between devices.



4.3

There's a built in 0.2s inside the GrovePi library’s grovepi.ultrasonicRead(pin) function, its caused by a time.sleep(0.2) line in the code. The Raspberry Pi communicates with the GrovePi’s ATmega328P using the I2C protocol.



4.4

The Grove Rotary Angle Sensor outputs an analog voltage between 0V and 5V. The GrovePi’s ATmega328P microcontroller converts the voltage into a 10-bit digital value(0-1023) with the help of its built in alalog to digital converter. The Raspberry Pi can’t do this directly because it doesn't have a built in ADC, so it can only read in digital signals.



4.5

I would check if the LCD is being detected on the I2C. It would show addresses like 0x3e being the text and 0x62 being the backlight. 

sudo i2cdetect -y 1



I would also test for communication by running: python3 -m grove\_rgb\_lcd



