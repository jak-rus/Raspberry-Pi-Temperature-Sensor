# Blackjack Project

This Python Script uses existing libraries including smtplib, ssl, time, board, message, and adafruit_dht in order to run a script that monitors the temperature of a room and send an email if the room rises above 70 degrees farienheit warning the recipiant of the rising temperature. This script will be implemented by the Texas State Computer Science Deparment to monitor servers and research computers in the department server room. 

## Features

The following features have been currently implemented:

- Uses a secure SMTP connection to send emails from the bot email to the recipiant
- Uses a template script made for the DHT 22 Sensor to get the data from the sensor and calculate usable values from it
- use those values to determine whether or not an email needs to be sent
- only send one email an hour
- add a cooldown that only effect the sent email so that the user could still ssh into the pi and check the temperature manually

The following features are things I would like to implement in the future:

- create a central network of devices that all pass data and draw email info from one place

## Current Bugs that will be Fixed
- None at the momment, need to test it more.

###Sources for the Project
https://realpython.com/python-send-email/ 
https://www.youtube.com/watch?v=EcyuKni3ZTo
