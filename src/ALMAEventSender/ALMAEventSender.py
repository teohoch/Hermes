__author__ = 'teohoch'

import time
import json

import requests
import dateutil.parser


class ALMAEventSender():
	def __init__(self):
		# TODO Define self.host, self.user, self.password, self.channel
		# self.sender = RabbitConnection(self.host, self.user, self.password, self.channel)
		return


	def __send(self, message):
		self.sender.send()
		return

	def __getversion(self, ste, timestamp):
		url = 'http://localhost:5000/version/'
		payload = {'ste': ste, 'time': timestamp}
		r = requests.post(url=url, data=payload)
		rj = r.json()
		return rj['RELEASE']

	def sendEvent(self, inputJson):
		decoded_json = json.loads(inputJson)
		message = {}

		# #### Get the correct Timestamp #####
		if 'timestamp' in decoded_json:
			if isinstance(decoded_json['timestamp'], int):
				time_real = float(decoded_json['timestamp'])
			else:
				time_real = time.mktime((dateutil.parser.parse(decoded_json['timestamp'])).timetuple())
		else:
			time_real = time.time()

		message['timestamp'] = time_real

		# ### Get the key ####

		if 'key' not in decoded_json:
			raise ValueError('Parameter "key" must be in the Input Json')
		else:
			message['key'] = decoded_json['key']

		# ### Get Environment Information ####

		if 'environment' in decoded_json:
			message['environment'] = decoded_json['environment']
			environment = True
		else:
			environment = False
		# ### Get Release ####

		if 'release' in decoded_json:
			release = decoded_json['release']
			if release == 'required':
				if environment:
					ste = decoded_json['environment']
					message['release'] = self.__getversion(ste, time_real)
				else:
					raise ValueError('Environment is required to retrieve the Release Information')
			else:
				message['release'] = decoded_json['release']

		return message


if __name__ == "__main__":


	inputjson = '{"release": "required",' \
	            '"timestamp": "2015-02-09T23:23:23",' \
	            '"value_int": 234234,' \
				'"key": "event",' \
				'"environment": "AOS"' \
	            '}'

	inputjson2 = '{"release": "required",' \
	            '"timestamp": 1423151422,' \
	            '"value_int": 234234' \
	            '}'
	inputjson3 = '{"release": "required",' \
	            '"value_int": 234234' \
	            '}'


	ca = ALMAEventSender()

	print(inputjson)
	print len(inputjson)
	print ca.sendEvent(inputJson=inputjson)



