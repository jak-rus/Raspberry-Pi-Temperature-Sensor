# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from email import message
import smtplib
import ssl
import time
import board
import adafruit_dht


# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT22(board.D18)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

port = 465 #for SSL
password = [INSERT BOT EMAIL PASSWORD HERE]
coolDownBoolean = False #added this boolean variable
warningEventTime = 0.0
passedTimeSinceWarnign = 0.0

context = ssl.create_default_context()

    
with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login([INSERT BOT EMAIL HERE], password)
    while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
	    #check to see if cooldown is running and over
            if(temperature_f > 70 and not coolDownBoolean):
                message = "The temperature of the server room as recorded by Temperature Senor - 01 is currently "+temperature_f+" which is higher than the recommended temperature."
                server.sendmail([INSERT BOT EMAIL HERE],  [INSERT RECIPIANTS EMAIL HERE] , message)
                print(message)

                warningEventTime = time.time()
                coolDownBoolean = True
            elif(coolDownBoolean and (time.time() - warningEventTime >= 3600.0)):
                coolDownBoolean = False
        except RuntimeError as error:
            #Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        #new test to see if this can get the program to stall two seconds between running the loop
        time.sleep(2.0)