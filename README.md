# Raspberry Pi Temperature and Humidity Sensor using a DHT22 Sensor

This Python Script uses existing libraries including smtplib, MIMEText, COMMASPACE, and multiple libraries from the adafruit-circuitpython-dht package. We also created a postfix server on the raspberry pi in order to allow the pi to send emails. All together, this temperature sensor will be used to monitor hundreds of thousands of dollars of research computers and servers in order to ensure that the air conditioning is working as intended in keeping the server room within certain climate conditions.    

## Features

The following features have been currently implemented:

- The raspberry pi hosts a postfix server, and uses SMTP, COMMASPACE, and MIMEText in order to parse, structure, and send emails 
- Uses pieces of a template script that utilizes the functions from the adafruit package to get data from the sensor and compare that data to condition that we specify
- utilize a while loop and a try catch function to avoid the errors caused by the hardware
- Created a service on the pi using the temperature sensor script to run once every our and to start on bootup

The following features are things I would like to implement in the future:

- Send data to a database that we can draw from and display on a website
- Display data on a screen connected to the pi so someone can just walk up and see what the current temperature is

## Current Bugs that will be Fixed
- After testing there are no current known bugs

### Sources for the Project
- https://realpython.com/python-send-email/ 
- https://www.youtube.com/watch?v=EcyuKni3ZTo
- https://stackoverflow.com/questions/2006648/email-multiple-contacts-in-python
- https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/33
- https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c
- https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6

#### Raspberry Pi Implementation:
1) Download the Raspberry Pi Imager (https://www.raspberrypi.com/software/)
2) Install Ubuntu 20.04 Server 
3) Once finished put the sd card in the Raspberry Pi and allow it to boot up
4) Go through the initial boot steps for ubuntu
5) Then run these commands
- sudo apt upgrade && sudo apt update -y
- sudo apt install pip -y
- sudo pip3 install adafruit-circuitpython-dht package
- sudo apt install -f postfix
6) When setting up postfix set your email domain and what not, but when it gives you the option for what kind of server you want to run make sure you select internet server as this will allow you to use SMTP to send emails

### The Python Script
Feel free to use the python script I have included here to run your own sensor, but I will include a few notes about things that we had to learn in order for it to work:
- #!/usr/bin/python3 (This tells the service to run this file as a python program)
- The try catch method is important to avoid letting errors stop the program, and you can include the while loop the way we did so that if you do get an error it keeps getting data until it has done so cleanly and continues on with the rest of the program
- the line  smtpObj = smtplib.SMTP('[SMTP SERVER ADDRESS]') gives you an smtp server object that allows you to send emails from your postfix server to other emails through the smtp server adress you specified.

### Creating the Service
Again feel free to use the link above as a template and our version as a template but here are the specfic configuration tips we used:
- in the resart field we used always that way whenever it ends (which with our script should only happen if the whole script is ran and finished) it will always restart after a certain amount of time indicated in the next field
- in the restart sec field we used 3600 because that is how often we wanted the temperature sensor to check the temperature of the room it is in (once every hour)
- To start the service run these two commands:
     sudo systemctl start [service name]
     sudo systemctl enable [service name] (this will make the service start on boot up
- Any time you make changes to this file or the py file you should run these two commands to update the service and restart its daemon:
     sudo systemctl restart [service name]
     sudo systemctl daemon-reload
- also make sure you know whether to add /usr/ to your exec start directory or not this tripped us up a bit

   


