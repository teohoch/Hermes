__author__ = 'teohoch'

import time
import json

import requests
import dateutil.parser
from RabbitConnection import RabbitConnection

headers = {'Content-Type': 'application/json'}


class ALMAEventSender():
	def __init__(self, rabbit_config):
		self.host = rabbit_config['Host']
		self.user = rabbit_config['User']
		self.password = rabbit_config['Password']
		self.routing_key = rabbit_config['Routing_key']
		self.exchange = rabbit_config['Exchange']
		self.sender = RabbitConnection(self.host, self.user, self.password, self.routing_key, self.exchange)



	def __send(self, message):
		self.sender.send(json.dumps(message))
		return

	def __getversion(self, ste, timestamp, architecture=32):
		url = 'http://sstudent01.osf.alma.cl:800/version/'
		payload = {'ste': ste, 'time': timestamp, 'architecture': architecture}
		r = requests.post(url=url, data=json.dumps(payload))
		rj = r.json()
		return rj['release']

	def __generate_message(self, input):
		if isinstance(input,str):
			decoded_input = json.loads(input)
			if not isinstance(decoded_input, dict):
				raise ValueError('Input is not a Valid Json Dictionary')
		elif isinstance(input, dict):
			decoded_input = input
		else:
			raise ValueError('Input is not Valid Json Dictionary or a Dictionary')

		message = {}

		# #### Get the correct Timestamp #####
		if 'timestamp' in decoded_input:
			if isinstance(decoded_input['timestamp'], int):
				time_real = float(decoded_input['timestamp'])
			else:
				time_real = time.mktime((dateutil.parser.parse(decoded_input['timestamp'])).timetuple())
		else:
			time_real = time.time()

		message['timestamp'] = time_real

		# ### Get the key ####

		if 'key' not in decoded_input:
			raise ValueError('Parameter "key" must be in the Input Json')
		else:
			message['key'] = decoded_input['key']

		# ### Get Environment Information ####

		if 'environment' in decoded_input:
			message['environment'] = decoded_input['environment']
			environment = True
		else:
			environment = False

		# ### Get Release ####

		if 'release' in decoded_input:
			release = decoded_input['release']
			if release == 'required':
				if environment:
					ste = decoded_input['environment']
					architecture = decoded_input['architecture']
					message['release'] = self.__getversion(ste, time_real, architecture)
				else:
					raise ValueError('Environment is required to retrieve the Release Information')
			else:
				message['release'] = decoded_input['release']

		# ### Get Other Keys ####

		stablished_keys = ['timestamp', 'key', 'environment', 'release']

		for key, value in decoded_input.iteritems():
			if key not in stablished_keys:
				message[key] = value


		return message


	def sendEvent(self, input):
		message = self.__generate_message(input)
		self.__send(message)

		return message



if __name__ == "__main__":
	input_json = '{"release": "required",' \
	            '"value_int": 234234,' \
	            '"architecture": 64,' \
	            '"key": "ERROR",' \
	            '"environment": "AOS"' \
				'}'

	rabbit_config = {'Host'         :   'localhost',
	                 'User'         :   'alma',
	                 'Password'     :   'Carl.Sagan',
	                 'Routing_key'  :   'AlmaEvent',
	                 'Exchange'     :   'alma_events'}

	ca = ALMAEventSender(rabbit_config)

	print(input_json)
	print len(input_json)
	print ca.sendEvent(input_json)
	#ca.sender.receive()



