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
month = date[2:4]
year = date[4:6]

fileDict = {
         "01":"/home/ubuntu/monthLogs/January.txt",
         "02":"/home/ubuntu/monthLogs/February.txt",
         "03":"/home/ubuntu/monthLogs/March.txt",
         "04":"/home/ubuntu/monthLogs/April.txt",
         "05":"/home/ubuntu/monthLogs/May.txt",
         "06":"/home/ubuntu/monthLogs/June.txt",
         "07":"/home/ubuntu/monthLogs/July.txt",
         "08":"/home/ubuntu/monthLogs/August.txt",
         "09":"/home/ubuntu/monthLogs/September.txt",
         "10":"/home/ubuntu/monthLogs/October.txt",
         "11":"/home/ubuntu/monthLogs/November.txt",
         "12":"/home/ubuntu/monthLogs/December.txt"
         }

filePath = fileDict.get(month)
data = open(filePath, "r")
line = data.readline()
data.close()

if line and year !=  line[14:16]:
    data = open(filePath, "w")
    data.write("")
    data.close()

logging.basicConfig(filename = filePath, level=logging.INFO)

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
        
logInfo =  date+": Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                    )

print(logInfo)
logging.info(logInfo)

sender= "[VALID SENDER EMAIL]"
receivers = [LIST OF EMAILS AS STRINGS WITH EACH STRING SEPARATED BY A COMMA]

message = MIMEText("The temperature of the server is currently "+str(temperature_f)+".\n the humidity is currently "+str(humidity)+".")

message["Subject"] = "Temperature/Humidity outside of range"
message["From"] = sender
message["To"] = COMMASPACE.join(receivers)

if(temperature_f > 80.0 or humidity < 40.0):
    try:
        smtpObj = smtplib.SMTP('[smtp server address]')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Successfully sent email")

    except SMTPException:
        print("Error: unable to send email")
        
if __name__=='__main__':
    sys.exit()
