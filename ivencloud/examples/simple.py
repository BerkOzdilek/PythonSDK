"""
simple example

Shows the basic steps for connecting to Iven Cloud:
    1) Activate device
    2) Send data
"""

import ivencloud

print 'started'

# activate device
acr = ivencloud.activate_device("your secret key goes here", "your device uid goes here")

# print return objects all properties
print acr.__dict__

# Prepare data to send
data = {
    'key1': 123,  # key name must match with hardware profile keys names
    'key2': 'value'
}

# Send data to cloud
response = ivencloud.send_data(data)

# print return objects all properties
print response.__dict__

print 'end'
