__author__ = 'teohoch'
import SoftwareVersion

import unittest
import time
from datetime import datetime
import json

headers={'Content-Type': 'application/json'}

class SoftwareVersionTestCase(unittest.TestCase):

	def setUp(self):
		SoftwareVersion.app.config['TESTING'] = True
		self.app = SoftwareVersion.app.test_client()

	def tearDown(self):
		return None

	def test_root(self):
		rv = self.app.get('/')
		assert 'ALMA Software Version Web Service' in rv.data

	# ### Tests for /version/ ###

	def test_version_basic(self):

		rv = self.app.post(headers=headers, path='/version/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_time(self):
		rv = self.app.post(headers=headers, path='/version/', data=json.dumps(dict(ste='AOS',timestamp=datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))))
		# print rv.data 
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_arch(self):
		rv = self.app.post(headers=headers, path='/version/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data 
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data
		rv = self.app.post(headers=headers, path='/version/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/version/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_without_params(self):
		rv = self.app.post(headers=headers, path='/version/')
		# print rv.data 
		assert '400' in rv.data

	# ### Tests for /release/ ###

	def test_release_basic(self):
		rv = self.app.post(headers=headers, path='/release/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_time(self):
		rv = self.app.post(headers=headers, path='/release/', data=json.dumps(dict(ste='AOS',timestamp=time.time())))
		# print rv.data 
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_arch(self):
		rv = self.app.post(headers=headers, path='/release/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data 
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post(headers=headers, path='/release/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/release/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_without_params(self):
		rv = self.app.post(headers=headers, path='/release/')
		# print rv.data 
		assert '400' in rv.data

	# ### Tests for /build/ ###

	def test_build_basic(self):
		rv = self.app.post(headers=headers, path='/build/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_time(self):
		rv = self.app.post(headers=headers, path='/build/', data=json.dumps(dict(ste='AOS',timestamp=time.time())))
		# print rv.data 
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_arch(self):
		rv = self.app.post(headers=headers, path='/build/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data 
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post(headers=headers, path='/build/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/build/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_without_params(self):
		rv = self.app.post(headers=headers, path='/build/')
		# print rv.data 
		assert '400' in rv.data

	# ### Tests for /antennas/ ###

	def test_antennas_basic(self):
		rv = self.app.post(headers=headers, path='/antennas/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_time(self):
		rv = self.app.post(headers=headers, path='/antennas/', data=json.dumps(dict(ste='AOS',timestamp=time.time())))
		# print rv.data 
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_arch(self):
		rv = self.app.post(headers=headers, path='/antennas/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data 
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post(headers=headers, path='/antennas/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/antennas/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_without_params(self):
		rv = self.app.post(headers=headers, path='/antennas/')
		assert '400' in rv.data

	# ### Tests for /acs/ ###

	def test_acs_basic(self):
		rv = self.app.post(headers=headers, path='/acs/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_time(self):
		rv = self.app.post(headers=headers, path='/acs/', data=json.dumps(dict(ste='AOS',timestamp=time.time())))
		# print rv.data 
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_arch(self):
		rv = self.app.post(headers=headers, path='/acs/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data
		assert 'acsversion' in rv.data

		assert 'ste'  in rv.data
		assert 'timestamp'  in rv.data

		rv = self.app.post(headers=headers, path='/acs/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/acs/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_without_params(self):
		rv = self.app.post(headers=headers, path='/acs/')
		assert '400' in rv.data

	# ### Tests for /patches/ ###

	def test_patches_basic(self):
		rv = self.app.post(headers=headers, path='/patches/', data=json.dumps(dict(ste='AOS')))
		# print rv.data 
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_time(self):
		rv = self.app.post(headers=headers, path='/patches/', data=json.dumps(dict(ste='AOS',timestamp=time.time())))
		# print rv.data 
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_arch(self):
		rv = self.app.post(headers=headers, path='/patches/', data=json.dumps(dict(ste='AOS', architecture=32)))
		# print rv.data 
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post(headers=headers, path='/patches/', data=json.dumps(dict(ste='AOS', architecture=64)))
		# print rv.data 
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_time_and_arch(self):
		rv = self.app.post(headers=headers, path='/patches/', data=json.dumps(dict(ste='AOS',timestamp=time.time(),architecture=64)))
		# print rv.data 
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_without_params(self):
		rv = self.app.post(headers=headers, path='/patches/')
		# print rv.data 
		assert '400' in rv.data

if __name__ == '__main__':
    unittest.main()