__author__ = 'teohoch'
import SoftwareVersion

import unittest
import time


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
		rv = self.app.post('/version/', data=dict(ste='AOS'))
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_time(self):
		rv = self.app.post('/version/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_arch(self):
		rv = self.app.post('/version/', data=dict(ste='AOS', architecture=32))
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data
		rv = self.app.post('/version/', data=dict(ste='AOS', architecture=64))
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_with_time_and_arch(self):
		rv = self.app.post('/version/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'release' in rv.data
		assert 'build' in rv.data
		assert 'environment' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_version_without_params(self):
		rv = self.app.post('/version/')
		assert '400' in rv.data

	# ### Tests for /release/ ###

	def test_release_basic(self):
		rv = self.app.post('/release/', data=dict(ste='AOS'))
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_time(self):
		rv = self.app.post('/release/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_arch(self):
		rv = self.app.post('/release/', data=dict(ste='AOS', architecture=32))
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post('/release/', data=dict(ste='AOS', architecture=64))
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_with_time_and_arch(self):
		rv = self.app.post('/release/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'release' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_release_without_params(self):
		rv = self.app.post('/release/')
		assert '400' in rv.data

	# ### Tests for /build/ ###

	def test_build_basic(self):
		rv = self.app.post('/build/', data=dict(ste='AOS'))
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_time(self):
		rv = self.app.post('/build/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_arch(self):
		rv = self.app.post('/build/', data=dict(ste='AOS', architecture=32))
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post('/build/', data=dict(ste='AOS', architecture=64))
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_with_time_and_arch(self):
		rv = self.app.post('/build/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'build' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_build_without_params(self):
		rv = self.app.post('/build/')
		assert '400' in rv.data

	# ### Tests for /antennas/ ###

	def test_antennas_basic(self):
		rv = self.app.post('/antennas/', data=dict(ste='AOS'))
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_time(self):
		rv = self.app.post('/antennas/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_arch(self):
		rv = self.app.post('/antennas/', data=dict(ste='AOS', architecture=32))
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post('/antennas/', data=dict(ste='AOS', architecture=64))
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_with_time_and_arch(self):
		rv = self.app.post('/antennas/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'antennas' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_antennas_without_params(self):
		rv = self.app.post('/antennas/')
		assert '400' in rv.data

	# ### Tests for /acs/ ###

	def test_acs_basic(self):
		rv = self.app.post('/acs/', data=dict(ste='AOS'))
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_time(self):
		rv = self.app.post('/acs/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_arch(self):
		rv = self.app.post('/acs/', data=dict(ste='AOS', architecture=32))
		assert 'acsversion' in rv.data

		assert 'ste'  in rv.data
		assert 'timestamp'  in rv.data

		rv = self.app.post('/acs/', data=dict(ste='AOS', architecture=64))
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_with_time_and_arch(self):
		rv = self.app.post('/acs/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'acsversion' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_acs_without_params(self):
		rv = self.app.post('/acs/')
		assert '400' in rv.data

	# ### Tests for /patches/ ###

	def test_patches_basic(self):
		rv = self.app.post('/patches/', data=dict(ste='AOS'))
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_time(self):
		rv = self.app.post('/patches/', data=dict(ste='AOS',timestamp=time.time()))
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_arch(self):
		rv = self.app.post('/patches/', data=dict(ste='AOS', architecture=32))
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

		rv = self.app.post('/patches/', data=dict(ste='AOS', architecture=64))
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_with_time_and_arch(self):
		rv = self.app.post('/patches/', data=dict(ste='AOS',timestamp=time.time(),architecture=64))
		assert 'patches' in rv.data
		assert 'number' in rv.data

		assert 'ste' in rv.data
		assert 'timestamp' in rv.data

	def test_patches_without_params(self):
		rv = self.app.post('/patches/')
		assert '400' in rv.data

if __name__ == '__main__':
    unittest.main()