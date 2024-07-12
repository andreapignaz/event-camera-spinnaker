import time
from socket import *

pings = 1

#Send ping 10 times 
while pings < 11:  

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = 'test'

    addr = ("130.192.163.100", 12000)

    #Send ping
    start = time.time()
    clientSocket.sendto(message.encode(), addr)

    pings = pings - 1

    time.sleep(2)
