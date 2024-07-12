import dv_processing as dv
import argparse
from socket import *

# Camera name for DAVIS346
# DAVIS346_00000499
# or launch dv-list-devices

parser = argparse.ArgumentParser(description='Stream events from a single iniVation camera to a server via UDP. Format of the message is:\n(timestamp,x,y,polarity)')
parser.add_argument("-c",
                    "--camera_name",
                    dest='camera_name',
                    default="",
                    type=str,
                    help="Camera name (e.g. DVXplorer_DXA00093). The application will open any supported camera "
                    "if no camera name is provided.")
parser.add_argument("-s",
                    "--server_address",
                    dest='server_address',
                    default="localhost",
                    type=str,
                    help="IP Address of the destination server. If nothing is set, localhost will be used.")
parser.add_argument("-p",
                    "--server_port",
                    dest='server_port',
                    default=12000,
                    type=str,
                    help="Port of the destination server. If nothing is set, 12000 will be used.")           
parser.add_argument("-r",
                    "--resize",
                    dest='scale_ratio',
                    default=1,
                    type=int,
                    help="Ratio to be used when scaling input. If nothing is set, no resize will happen.")           
args = parser.parse_args()

print("Configure camera")
# Open any camera that is discovered in the system
camera = dv.io.CameraCapture(args.camera_name)

# Check whether frames are available
if not(camera.isEventStreamAvailable()):
    print("Event streaming not available for this camera.")
    quit()

print("Configure UDP")
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
addr = (args.server_address, int(args.server_port))

print("Start streaming")

if scale_ratio = 1
    resize = False
else
    resize = True

try: 
    while camera.isConnected():
        # Get Events
        events = camera.getNextEventBatch()
        # Process  Events
        if events is not None:
            if not resize:
                for ev in events:
                    message = f"({ev.timestamp()}, {ev.x()}, {ev.y()}, {ev.polarity()})"
                    clientSocket.sendto(message.encode(), addr)
            else:
                for ev in events:
                    r_x = int(ev.x() * scale_ratio)
                    r_y = int(ev.y() * scale_ratio)
                    message = f"({ev.timestamp()}, {r_x}, {r_y}, {ev.polarity()})"
                    clientSocket.sendto(message.encode(), addr)

except KeyboardInterrupt:
    print("Ending streaming")
    pass