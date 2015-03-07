import  json
import time

import requests

headers = {'Content-Type': 'application/json'}
url = 'http://sstudent01.osf.alma.cl:800/version/'
payload = dict(ste='AOS', time=time.time(), architecture=64)
r = requests.post(url=url, data=json.dumps(payload), headers=headers)
print r
rj = r.json()
print rj