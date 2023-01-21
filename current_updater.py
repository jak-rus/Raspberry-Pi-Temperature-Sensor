#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE
import board
import adafruit_dht
from datetime import datetime
import sys
import time

error = True
while error:
        try:
            dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            now = datetime.now()
            date = now.strftime("%d%m%y %H:%M:%S")
            error = False
        except RuntimeError as er:
            print(er.args[0])
            continue
text = date+": Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(temperature_f, temperature_c, humidity)

website = open("/var/www/html/current.html", "w")
print("this is the text that should write to the file"+ text)
website.write(text)
website.close()
