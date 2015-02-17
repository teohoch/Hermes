__author__ = 'teohoch'

import MySQLdb as mySql
import time
from datetime import datetime


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
			self.db = mySql.connect(host=self.host, user=self.user, passwd=self.password, db=self.name)
			self.pointer = self.db.cursor()
			self.connected = True
			return True
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

	def executeReadSQL(self, sentence):
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


	def executeWriteSQL(self, sentence):
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
			print 'Name'.ljust(15) + '\t' + 'Type'.ljust(15) + '\t' + 'NULL'.ljust(15) + '\t' + 'Primary'.ljust(
				15) + '\t' 'Default'.ljust(15)

			for column in content:
				print str(column[0]).ljust(15) + '\t' + str(column[1]).ljust(15) + '\t' + str(column[2]).ljust(
					15) + '\t' + str(column[3]).ljust(15) + '\t' + str(column[4])
			print '\n' + ''.ljust(80, '_') + '\n'


class VersionDatabase(Database):

	def __compose(self, ste, timestamp, arch):
		timestamp = datetime.fromtimestamp(float(timestamp))
		if ste.lower() == 'aos':
			arch_statement = 'AND version LIKE "%{0}%"'.format(('(x86)' if not arch else ('(x86)' if arch==32 else '(x86_64)')))
		else:
			arch_statement = ''

		return "SELECT version  FROM status WHERE ste = '{0}' AND date <= '{1}' AND version LIKE '%=> Using ACS%' {2} ORDER BY date DESC LIMIT 1;".format(ste, timestamp,arch_statement)

	def getAcsVersion(self, ste, timestamp=(time.time()), arch=None):
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)

		if r:
			r = r[0][0]
			r = r.split('\n')[1].split(' : ')[1]
			return dict(acsversion=r, ste=ste,timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
		return {}

	def getBuild(self, ste, timestamp=(time.time()), arch=None):
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)
		if r:
			r = r[0][0]
			r = r.split('\n')[2].split(' : ')[1]
			return dict(build=r, ste=ste,timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))

		return {}

	def getRelease(self, ste, timestamp=(time.time()), arch=None):
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)

		if r:
			r = r[0][0]
			r = r.split('\n')[2].split(' : ')[1]
			r = r.split('-B')
			if len(r) == 2:
				r = r[0]+'-B'
			return dict(release=r, ste=ste,timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))

		return {}

	def getAntennas(self, ste, timestamp=(time.time()), arch=None):
		"""
		Return a dictionary with the antennas configured and the number of antennas configured
		:param ste: The STE in question
		:param timestamp: The Timestamp to query, in Unix Timestamp
		:return: A dictionary with 2 keys: number -> the number of antennas configured. and a dictionary.
		In this inner dictionary, each configured antenna is a key, and the corresponding value is the configured slot
		"""
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)

		if r:
			r = r[0][0]
			r = r.split('=>')[2].split(':\n')[1].replace('\n', ' ').split(' | ')

			r2 = {}

			for entry in r:
				if entry.strip():
					k = entry.split(' -> ')
					r2[k[0]] = k[1]

			return dict(number=len(r2), antennas=r2, ste=ste, timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
		return {}


	def getPatches(self, ste, timestamp=(time.time()), arch=None):
		"""
		Return a dictionary with the Patches applied and the number of patches applied
		:param ste: The STE in question
		:param timestamp: The Timestamp to query
		:return: A dictionary with 2 keys: number -> the number of the number of patches applied. and a dictionary.
		In this inner dictionary, each Patch name is a key, and the corresponding value is the associated comments
		"""
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)

		if r:
			r = r[0][0]
			r = r.split('=>')

			r2 = {}

			for entry in r:
				if 'Patch' in entry:
					k = entry.split('\n')
					r2[k[0].split('Patch: ')[1]] = k[1].split('Responsible: ')[1]

			return dict(number=len(r2), patches=r2, ste=ste, timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
		return ''

	def getComplete(self, ste, timestamp=(time.time()), arch=None):
		sentence = self.__compose(ste,timestamp, arch)
		r = self.executeReadSQL(sentence)
		if r:
			r = r[0][0]

			release = r.split('\n')[2].split(' : ')[1]
			release = release.split('-B')
			if len(release) == 2:
				release = release[0]+'-B'

			build = r.split('\n')[2].split(' : ')[1]

			antennas = {}
			rtemp = r.split('=>')[2].split(':\n')[1]
			if ' -> ' in rtemp:
				rtemp = rtemp.replace('\n', ' ').split(' | ')
				for entry in rtemp:
					if entry.strip():
						k = entry.split(' -> ')
						antennas[k[0]] = k[1]
			elif ' in pad ' in rtemp:
				rtem = rtemp.split('\n')
				for entry in rtemp:
					if entry.strip():
						k = entry.split('  in pad ')
						antennas[k[0]] = k[1]

			patches = {}
			rtemp = r.split('=>')
			for entry in rtemp:
				if 'Patch' in entry:
					k = entry.split('\n')
					patches[k[0].split('Patch: ')[1]] = k[1].split('Responsible: ')[1]

			environment = r

			return dict(release=release, build=build, environment=environment, ste=ste,
				timestamp=datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S"))
		return {}


if __name__ == "__main__":
	import json

	host = 'aivwiki.alma.cl'
	dbname = 'aiv_ste_version'
	user = 'queryuser'
	password = 'YqGHWLuUvWpM8zxB'

	db = VersionDatabase(host, dbname, user, password)

	a = db.getBuild('aos',arch=64)
	b = db.getRelease('aos',arch=64)
	c = db.getAntennas('aos',arch=64)
	d = db.getPatches('aos',arch=64)
	f = db.getComplete('aos',arch=64)
	e = db.getAcsVersion('aos',arch=64)

	print a
	print b
	print c
	print d
	print f
	print e

