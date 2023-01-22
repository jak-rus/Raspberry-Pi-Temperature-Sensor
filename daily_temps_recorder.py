#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE
import board
import adafruit_dht
from datetime import datetime
import sys
import logging
import sqlite3


now = datetime.now()
date = now.strftime("%d%m%y %H:%M:%S")
#parses out the hour and minute from the date above 
hour = date[7:9]
minute = date[10:12]

filePath = "/home/[INSERT USERNAME HERE]/daily_hourly_temperatures.txt"

logging.basicConfig(filename = filePath, level=logging.INFO)

#if a new hour has begun (basically if the minute is 00, you can assume a new hour has begun and the temperature needs to be recorded)
if minute == "00":
    error = True
    while error:
        try:
            dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            error = False

        except RuntimeError as er:
            print(er.args[0])
            continue


    logInfo =  date+": Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format( temperature_f, temperature_c, humidity)
    print(logInfo)
    logging.info(logInfo)
    print("Recorded Temperature")

# if it is 5 oclock (i am assuming that this uses military time), then send the email, and clear the file for the next day
if hour == "17" and minute == "00":
    data = open(filePath, "r")
    todaysTemperatures = data.read()
    data.close()
    sender= [VALID SENDER EMAIL]
    receivers = [LIST OF EMAILS AS STRINGS WITH EACH STRING SEPARATED BY A COMMA]

    message = MIMEText(todaysTemperatures)

    message["Subject"] = "Hourly Temperatures for last 24 hours in Server Room"
    message["From"] = sender
    message["To"] = COMMASPACE.join(receivers)
    
    try:
        smtpObj = smtplib.SMTP('[smtp server address]')
        smtpObj.sendmail(sender, receivers, message.as_string())
        data = open(filePath, "w")
        data.write("")
        data.close()
        print("Successfully sent email")

    except SMTPException:
       print("Error: unable to send email")

    if __name__=='__main__':
        sys.exit()

#important note: i structured the program where the sensor will record the 5 oclock temp before it sends the email, that way we dont have to record the five oclock temp inside that if statement
#tldr: hourly recording first, so we can send email knowing we have all recorded temps
