# Raspberry Pi Temperature Sensor

> Version 1.0 -  *last updated 08/19/2022*


 

---

## Table of Contents
1. [Documentation](#documentation)
2. [Scenario](#scenario)
3. [Technologies](#technologies)
4. [Libraries](#libraries)
5. [Sources](#sources)
6. [Setup](#setup)
7. [Python Scripts](#python-scripts)
8. [Services](#services)
9. [Nginx Website](#nginx-website)
10. [Persistence](#persistence)
11. [Communication](#communication)

---

## Documentation

The following documentation contains all of the different sevices, files, libraries, and installation steps for the Raspberry Pi Temperature Sensor. This repository includes all of the files needed to run the sensor effectively, however it is important to use the setup section to make sure those files are in the correct directory. Multiple facets of functionality are spread out between different scripts that have different jobs, and each one is managed by a service running on the Raspberry Pi. Some of the scripts utilize a logging functionality to store and manage data collected by the sensor. It will be explained below how the different parts of the repository interact to produce this temperature sensor. 

---

## Scenario

At my job, we used a thermostat to regulate, observe, and report statistics in order to monitor the environment of a server room. Eventually, the thermostat began to warn us a day or two after the environment became hazardous for the servers. This disconnect created a system that was not reliable for keeping the server's environment within the specified conditions. The purpose of this project was to remedy that disconnect. We first looked at an assortment of IoT devices and services that would help us solve the issue. However, with our budget, none of them were feasible. This is when I suggested we use my experience working with Raspberry Pis and a DHT22 environment sensor to create our own IoT environment sensor. We determined this was the most feasible option because we already owned the hardware, and the only other cost would have been a few hours of labor to write the scripts and deploy it. So, my team member and I built a prototype to see if it was reliable. After which we tested it, and refactored the code and configuration as a service. Our team manager then asked us to implement a user story that consisted of the user being able to walk up to the sensor and see data on a screen. This idea led to the implementation of a website to display the most recent data available.

___

## Tecnologies

* **Python**
* **Nginx**
* **Linux**

___

## Libraries

Each of these libraries are required to achieve full functionality of the temperature sensor, and can be found within the python scripts.

* **smtplib**
* **MIMEText**
* **COMMASPACE**
* **logging**
* **adafruit-circuitpython-dht**
---

## Sources

This project contains a lot of code that was refactored from open source projects and tutorials online. Here you will find a list of the sources that we used. This list may not be exhaustive, and if you see that I have not given credit where it is due, please leave a comment or send me a message!

* https://realpython.com/python-send-email/
* https://www.youtube.com/watch?v=EcyuKni3ZTo
* https://stackoverflow.com/questions/2006648/email-multiple-contacts-in-python
* [adafruit/Adafruit_CircuitPython_DHT#33](https://github.com/adafruit/Adafruit_CircuitPython_DHT/issues/33)
* https://gist.github.com/ewenchou/be496b2b73be801fd85267ef5471458c
* https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6
* https://realpython.com/python-time-module/#the-epoch
* https://stackoverflow.com/questions/2006648/email-multiple-contacts-in-python
* https://www.codingem.com/log-file-in-python/


## Setup

These setup instructions are designed to get the current version of the Raspberry Pi Temperature Sensor running from scratch, and should be used in conjunction with the files provided. These instructions assume you have already completely set up your Raspberry Pi, and properly installed Python.  

1. After the initial setup of the Raspberry Pi, install the required libraries for the Python scripts using these commands. Also, when setting up postfix follow the directions on screen. You should take the opportunity to set up the email domain of your Raspberry Pi, then select the internet server option as this will allow you to use SMTP to send emails.

- sudo apt install pip -y
- sudo pip3 install adafruit-circuitpython-dht package
- sudo apt install -f postfix

2. Create the Python scripts as needed using what is in this repository as a template and adding functionality as you see fit. If you would also like to store the data in a log file, create a log file either in the home directory with the Python scripts or in a custom directory. Both are presented here and each serves different functionality.
3. If you desire to set up an nginx website to display the data recorded by the temperature sensor run the command "sudo apt install nginx", then "sudo systemctl start nginx.service", then update the html file in the proper directory to reference the log file where you store the data.



## Python Scripts

Included in this section are some notes about the developement of the Python scripts used to create this project that many may not already know. 

- All of the Python scripts should be located in the home directory of the user
- #!/usr/bin/python3 (This tells the service to run this file as a Python program)
- The try catch method is important to avoid letting hardware errors from the sensor stop the program, and the while loop should be included so that if you do get an error it keeps getting data until it has done so cleanly and continues on with the rest of the program
- the line smtpObj = smtplib.SMTP('[SMTP SERVER ADDRESS]') gives you an smtp server object that allows you to send emails from your postfix server to other emails through the smtp server adress you specified.

## Services

We utilized systemctl services in order to manage and run our Python scripts, and in this section there are some notes about the developement of the service files used to create this project that many may not already know.

- Store the service files within this directory "/lib/systemd/system"
- in the resart field we used "always" that way whenever it ends (which with our script should only happen if the whole script is ran and finished) it will always restart after a certain amount of time indicated in the next field
- in the restart sec field we used 3600 because that is how often we wanted the Temperature Sensor to check the temperature of the room it is in (once every hour)
- To start the service run these two commands:
      - sudo systemctl start [service name]
      - sudo systemctl enable [service name] (this will make the service start on boot up)
- Any time you make changes to this file or the Python file you should run these two commands to update the service and restart its daemon:
      - sudo systemctl restart [service name]
      - sudo systemctl daemon-reload

## Nginx Website
We also created an Nginx server to output our most recent data to an HTML front end, and in this section are some notes about the developement of the Nginx Server used to create the website for this project.

- install Nginx with the command "sudo apt install nginx"
- then start the Nginx service by using the command "sudo systemctl start nginx.service"
- to update the html file to manipulate what displays to your website navigate to the directory and file "/var/www/html/index.nginx-debian.html"
- In order to make sure that the correct temperature is displayed on the webpage, create an empty file named "current.html"
- The data in this file will be read in order to update the homepage, and written to with tempSense data ~ every 5 seconds.
- We use an AJAX call to read the current.html file, and the setInterval functionality to refresh the data on the page every 5 seconds.
- Update the second parameter of the setInterval function to change how often the page data is refreshed.
- We currently have a button that also refreshes the page, but it may be removed in a future version.

## Persistence

Logs are kept by a few of the Python scripts, they store every recorded temperature for a recorded month in the properly named file. They will keep this data for one year until that month is reached again, at which point it will clear the file for the new years data. 
Logging is used heavily in a few of the scripts, one to store the data in a file designated for what month is currently is, an another to store the hourly temperatures for each day. Eventually, a possible switch to a database system might be fiesable, but this was the optimal solution for now. 

---

## Communication

The Python scripts will send emails under a few select conditions determined by the user. Using Postfix, SMTP, MIMEText, and COMMASPACE to set the sender, an array of recievers stored as strings, and a message using MIMEText. Once all of these have been created and set you can set the variables in the message dictionary and send the message using the SMTP Object you create when you need to send an email. 

---
