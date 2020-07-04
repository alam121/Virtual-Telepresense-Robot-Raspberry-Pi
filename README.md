# Virtual Telepresense Robot

Tele-presence is the use of virtual reality technology, especially for remote control of machinery or for apparent participation in distant events. 

The robot used in this project uses a 12-V rechargeable battery to wirelessly control H-Bridge [l298n](https://www.sparkfun.com/datasheets/Robotics/L298_H_Bridge.pdf).
The H-bridge is controlled using a RF reciever and transmitter circuit to operate its wheels wirelessly

The telepresense part of the robot includes the following items:

* Raspberry Pi-3
* Pi-Cam
* Servo motor
* Mobile phone with accelerometer sensor



<img src="https://github.com/alam121/picam/blob/master/1.JPG" width="250" height="250">

The mobile phone accelerometer transmits the data through Wifi UDP communication to the Raspberry Pi(according to the reciever and transmitter IP address).
The Pi converts the accelometers values into degrees.
The degrees are then converted into duty cycle to operate the servo motor 


<img src="https://github.com/alam121/picam/blob/master/1.JPG" width="250" height="250">
