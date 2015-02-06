__author__ = 'teohoch'

from RabbitConnection import RabbitConnection

class ALMAEventSender():

	def __init__(self):
		# TODO Define self.host, self.user, self.password, self.channel
		self.sender = RabbitConnection(self.host, self.user, self.password, self.channel)


	def __send(self, message):
		self.sender.send()
		return

	def __getVersion(self,TimeStamp,Ste):
		return







