"""
simple example

Shows the basic steps for connecting to Iven Cloud:
	1) Activate device
	2) Send data
"""

import ivencloud
import Adafruit_DHT

# credentials
secret_key = "<your secret key>"
device_uid = "<your device uid>"

# server address
hostname = "staging.iven.io"
ivencloud.set_cloud_address(hostname)  # defaults to staging.iven.io

# activate device
activate_request = ivencloud.activate_device(secret_key, device_uid)
if activate_request.error is None and activate_request.status == 200:
	print "Activation Successful, api key: {0}".format(activate_request.api_key)
else:
	if activate_request.error is not None:
		print "Error on activation with code: {0}, message: {1}".format(activate_request.error.iven_code, activate_request.error.message)
	print "Error on activation status: {0}, description: {1}".format(activate_request.status, activate_request.description)


# Prepare data to send
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
	print('Failed to get reading. Try again!')
	sys.exit(1)

data = {
	'temperature': temperature,
	'humidity': humidity
}
print "Sending temp: {0}, hum: {1}".format(data['temp'], data['hum'])

# Send data to cloud
response = ivencloud.send_data(data)
if response.error is None and response.status == 200:
	print "Data is sent successfully"
	if response.task is not None:
		print "There is a task, iven_code: {0}, task value: {1}".format(response.task.iven_code, response.task.value)
		task_response = ivencloud.task_done(response.task.iven_code)
		if task_response.error is None and task_response.status == 200:
			print "Task done is sent successfully"
else:
	if response.error is not None:
		print "Error on send data with code: {0}, message: {1}".format(response.error.iven_code, response.error.message)
	print "Error on send data status: {0}".format(response.status)

