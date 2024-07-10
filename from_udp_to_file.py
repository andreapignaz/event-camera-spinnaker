from socket import *
import dv_processing as dv

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('130.192.163.100', 12000))

# Create a EventsStore object to buffer some data before writing to file
store = dv.EventStore()
i = 0

# Create a Writer object for file output
writer = dv.io.MonoCameraWriter("output.aedat4", dv.io.MonoCameraWriter.EventOnlyConfig("DAVIS346_sample", (346,260)))

while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.decode().upper()
    #print(f"Received {message} from {address}")
    message = message.strip('()').split(', ')
    store.push_back(int(message[0]), int(message[1]), int(message[2]), True if (message[3] == 'TRUE') else False)
    i = i+1
    if (i > 1000):
        i = 0
        writer.writeEvents(store, streamName='events')
        store = dv.EventStore()
