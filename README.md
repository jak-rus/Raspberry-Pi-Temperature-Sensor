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

### Sources for the Project
- https://realpython.com/python-send-email/ 
- https://www.youtube.com/watch?v=EcyuKni3ZTo

#### Raspberry Pi Implementation:
1) Download the Raspberry Pi Imager (https://www.raspberrypi.com/software/)
2) Download Raspian Lite
3) Once finished put the sd card in the Raspberry Pi and allow it to boot up
4) Take out the card and put it back into your computer
5) The SD card should now be called boot on your computer
6) Open the boot drive, navigate to the end of the cmdline text file and add
- cgroup_memory=1 cgroup_enable=memory ip=[IP Address]::[GATEWAY]:[NETMASK]:[NAME OF DEVICE]:eth0:off  
7) Then navigate to the config file and add this at the bottom
- arm64bit = 1
8) finally, to enable ssh, open powershell and change directories to the boot drive, then type "new-item ssh" after this you should be able to follow the resources above to complete the project.
   


