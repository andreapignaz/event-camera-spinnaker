# event-camera-spinnaker

Some simple scripts to enable streaming of event camera data to Spinnaker2 hardware.
Event camera used: DAVIS 346

## Host
The event camera should be connected to the host via USB. 

The host computer should have the dvs_processing Python library installed. I'd suggest to create a Python virtual environment, and install in them the libraries through `pip install dv_processing 'numpy<2'` 

Then, the `dvs_event_streaming.py` can be used to stream event camera data via UDP on Ethernet. 

```
```

## Server
An example application for the server is `simple_udp_server.py` that prints on stdout received packets. 
