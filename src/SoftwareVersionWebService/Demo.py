import  json
import time

import requests
url = 'http://sstudent01.osf.alma.cl:800/version/'
payload = {'ste': 'AOS', 'time': time.time(), 'architecture': 64}
r = requests.post(url=url, data=json.dumps(payload))
rj = r.json()
print rj