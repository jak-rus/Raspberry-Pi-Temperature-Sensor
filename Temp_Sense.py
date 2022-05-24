#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE
import board
import adafruit_dht
from datetime import datetime
import sys

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

print(

    date+": Temp: {:.1f} F / {:.1f} C Humidity: {}% ".format(
        temperature_f, temperature_c, humidity
        )
)

sender= "[VALID SENDER EMAIL]"
receivers = [LIST OF EMAILS AS STRINGS WITH EACH STRING SEPARATED BY A COMMA]

message = MIMEText("The temperature of the server is currently "+str(temperature_f)+".\n the humidity is currently "+str(humidity)+".")

message["Subject"] = "Test temperature sensor is too hot"
message["From"] = sender
message["To"] = COMMASPACE.join(receivers)

if(temperature_f > 80.0 or humidity < 40.0):
    try:
        smtpObj = smtplib.SMTP('smtp.txstate.edu')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")
if __name__=='__main__':
    sys.exit()
