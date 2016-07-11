import ivencloud

print 'started'

acr = ivencloud.activate_device("your secret key goes here", "your device uid goes here")
print acr.__dict__

data = {'key1': 123,  # key name must match with hardware profile keys names
        'key2': 'value'
        }

response = ivencloud.send_data(data)

print response.__dict__

print 'end'
