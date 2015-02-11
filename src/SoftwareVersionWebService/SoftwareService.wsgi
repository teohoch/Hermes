mport sys
 import logging
 import os

 logging.basicConfig(stream=sys.stderr)
 sys.path.insert(0,"/var/www/html/Hermes/")
 activate_this = '/opt/virtual_env/Hermes/bin/activate_this.py'
 execfile(activate_this, dict(__file__=activate_this))

 from src.SoftwareVersionWebService.SoftwareVersion import app as application
