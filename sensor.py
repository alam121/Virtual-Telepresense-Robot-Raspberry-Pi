import socket
import time
from struct import *
import math
# Prepare the UDP connection
UDP_IP = "192.168.18.7"
print "Receiver IP: ", UDP_IP
UDP_PORT = 50000
print "Port: ", UDP_PORT
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# Continuously read from the UDP socket
while True:
    time.sleep(.5)
    data, addr = sock.recvfrom(1024)
    raw = data
    limited=raw.split(',')
    x=(limited[2])
    y=(limited[3])
    z=(limited[4])
    
    print x, y,z
    x1 = 0.2
    y1 = 9.59
    z1 = 0.1
    xreal=x1-float(x)
    yreal=y1-float(y)
    zreal=z1-float(z)

    result = (zreal*zreal)+(yreal*yreal)
    result1=math.sqrt(result)
    Ax=xreal/result1
    degree= math.degrees(math.atan(Ax))
    if degree < 0:
        degree = 180+degree

    print degree
