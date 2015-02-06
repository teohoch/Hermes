__author__ = 'teohoch'

import pika

class RabbitConnection():

	def __init__(self, host, user, password, queue='hello'):
		self.host = host
		self.user = user
		self.password = password
		self.queue = queue
		self.credentials = pika.PlainCredentials(self.user, self.password)
		self.parameters = pika.ConnectionParameters(host=self.host, credentials=self.credentials)

	def send(self, message):
		#print 'Connecting...'
		connection = pika.BlockingConnection(self.parameters)
		#print 'Connected!'
		channel = connection.channel()
		channel.queue_declare(queue=self.queue)
		channel.basic_publish(exchange='', routing_key=self.queue, body=message)
		connection.close()

	def callback(self, ch, method, properties, body):
		print " [x] Received %r" % (body,)

	def receive(self):
		connection = pika.BlockingConnection(pika.ConnectionParameters(self.host,credentials=self.credentials))
		channel = connection.channel()
		channel.queue_declare(queue=self.queue)
		print ' [*] Waiting for messages. To exit press CTRL+C'

		channel.basic_consume(self.callback, queue=self.queue, no_ack=True)

		channel.start_consuming()

if __name__ == "__main__":
	host = 'localhost'
	user = 'alma'
	password = 'Carl.Sagan'

	instance = RabbitConnection(host,user,password)
	instance.send()
	instance.receive()