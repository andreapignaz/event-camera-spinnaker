# event-camera-spinnaker

Some simple scripts to enable streaming of event camera data to Spinnaker2 hardware.
Event camera used: DAVIS 346

## Host
The event camera should be connected to the host via USB. 

The host computer should have the dvs_processing Python library installed. I'd suggest to create a Python virtual environment, and install in them the libraries through `pip install dv_processing 'numpy<2'` 

Then, the `dvs_event_streaming.py` can be used to stream event camera data via UDP on Ethernet. 

```
usage: dvs_event_streaming.py [-h] [-c CAMERA_NAME] [-s SERVER_ADDRESS] [-p SERVER_PORT]

Stream events from a single iniVation camera to a server via UDP. Format of the message is: (timestamp,x,y,polarity)

options:
  -h, --help            show this help message and exit
  -c CAMERA_NAME, --camera_name CAMERA_NAME
                        Camera name (e.g. DVXplorer_DXA00093). The application will open any supported camera if no camera name is provided.
  -s SERVER_ADDRESS, --server_address SERVER_ADDRESS
                        IP Address of the destination server. If nothing is set, localhost will be used.
  -p SERVER_PORT, --server_port SERVER_PORT
                        Port of the destination server. If nothing is set, 12000 will be used.
```

The host can test the connection to the UDP server via the `test_udp_connection.py` script, available in the `tools` directory (remember to customize it with the correct IP address and port).

## Server

The script `from_udp_to_file.py` script receives packets from UDP and saves them to a aedat4 file that can be read via the DV application to check the quality of the received data. 
An example called `output.aedat4` is provided.

An example application for the server is available in the `tools` directory, it is called `simple_udp_server.py` and it prints on stdout received packets.
