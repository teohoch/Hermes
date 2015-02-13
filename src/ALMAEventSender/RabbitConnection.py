__author__ = 'teohoch'

import pika

class RabbitConnection():

	def __init__(self, host, user, password, routing_key='hello', exchange='', queue = 'alma_events_queue'):
		self.host = host
		self.user = user
		self.password = password
		self.routing_key = routing_key
		self.exchange = exchange
		self.credentials = pika.PlainCredentials(self.user, self.password)
		self.queue = queue
		self.parameters = pika.ConnectionParameters(host=self.host, credentials=self.credentials)

	def send(self, message):
		connection = pika.BlockingConnection(self.parameters)
		channel = connection.channel()
		channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=message)
		connection.close()

	def callback(self, ch, method, properties, body):
		print " [x] Received %r" % (body,)

	def receive(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(self.host,credentials=self.credentials))
		channel = connection.channel()
		print ' [*] Waiting for messages. To exit press CTRL+C'

		channel.basic_consume(self.callback, queue=self.queue, no_ack=True)

		channel.start_consuming()

if __name__ == "__main__":
	host = 'localhost'
	user = 'alma'
	password = 'Carl.Sagan'

	instance = RabbitConnection(host,user,password)
	instance.send()
	#instance.receive()