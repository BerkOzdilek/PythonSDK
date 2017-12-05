"""
simple example

Shows the basic steps for connecting to Iven Cloud:
    1) Activate device
    2) Send data
"""

import ivencloud
import Adafruit_DHT
from time import sleep

print 'started'

# activate device
acr = ivencloud.activate_device("2bb007aa67b39180b5896a5bf818c3db29e37a8f", "demo123")

# print return objects all properties
print "activation"
print acr.__dict__

# Prepare data to send
sensor = Adafruit_DHT.DHT11
pin = 17
if humidity is not None and temperature is not None:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	data = {
	    'temp': int(temperature),  # key name must match with hardware profile keys names
	    'hum': int(humidity)
	}

	# Send data to cloud
	response = ivencloud.send_data(data)

	# print return objects all properties
	print "send data"
	print response.__dict__
else:
	print "error on read"

print 'end'
