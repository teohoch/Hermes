__author__ = 'teohoch'

import MySQLdb as mySql
import datetime
import time

class Database():
	"""
	General purpose class for connecting to a MySQL Database
	"""
	connected = False
	pointer = None



	def __init__(self, host, dbname, user, password):
		"""
		Initializes the instance, setting the path to the database
		:param confPath: path to the configuration file
		:return: None
		"""
		self.host = host
		self.name = dbname
		self.user = user
		self.password = password

	def connect(self):
		"""
		Connects to the specified database. If it doesn't exists, it creates it
		:return: If successful, returns True
		"""
		try:
			self.db = mySql.connect(host=self.host, user=self.user, passwd=self.password,db=self.name)
			self.pointer = self.db.cursor()
			self.connected = True
			return  True
		except mySql.Error, e:
			print "Error %s:" % e.args[0]
			return False


	def disconnect(self):
		"""
		Disconnects from the Database
		:return: None
		"""
		if self.pointer:
			self.pointer.close()
			self.connected = False

	def executeReadSQL(self,sentence):
		"""
		Executes a read SQL command, such as SELECT
		:param sentence: Command to be executed
		:return: The response from the Database
		"""
		if self.connect():
			self.pointer.execute(sentence)
			data = self.pointer.fetchall()
			self.disconnect()
			return data
		return False


	def executeWriteSQL(self,sentence):
		"""
		Executes a SQL Write command, such as Insert, Delete or Modify
		:param sentence: Command to be executed
		:return: None
		"""
		self.connect()
		resp = self.pointer.execute(sentence)
		self.pointer.commit()
		self.disconnect()

	def getTableDefinitions(self):
		table_names = self.executeReadSQL('SHOW TABLES;')
		definitions = {}

		for table in table_names:
			definitions[table[0]] = self.executeReadSQL('SHOW COLUMNS FROM ' + table[0])

		self.definitions = definitions

		return self.definitions

	def printDefinitions(self):
		for table, content in self.definitions.iteritems():
			print 'Name'.ljust(15) + '\t' + 'Type'.ljust(15) + '\t' + 'NULL'.ljust(15) + '\t' + 'Primary'.ljust(15) + '\t' 'Default'.ljust(15)

			for column in content:
				print str(column[0]).ljust(15) + '\t' + str(column[1]).ljust(15) + '\t' + str(column[2]).ljust(15) + '\t' + str(column[3]).ljust(15) + '\t' + str(column[4])
			print '\n' + ''.ljust(80,'_') + '\n'


class VersionDatabase(Database):
	def getVersion(self, ste, host, timestamp= (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))):
		sentence = "SELECT acs, acssw FROM data WHERE ste = '{0}' AND host = '{1}' AND date <= '{2}' ORDER BY date DESC LIMIT 1;".format(ste, host, timestamp)
		r = self.executeReadSQL(sentence)[0]
		return {'acs'   :   r[0],
		        'acssw' :   r[1]}

if __name__ == "__main__":
	import json

	host = 'aivwiki.alma.cl'
	dbname = 'aiv_ste_version'
	user = 'queryuser'
	password = 'YqGHWLuUvWpM8zxB'

	db = VersionDatabase(host,dbname,user,password)

	a = db.getVersion('aos','gns')
	print a
	print json.dumps(a)


