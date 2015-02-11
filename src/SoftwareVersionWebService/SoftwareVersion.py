import json
import time

from flask import Flask, request,render_template

from Database import VersionDatabase


app = Flask(__name__)
app.debug = False
host = 'aivwiki.alma.cl'
dbname = 'aiv_ste_version'
user = 'queryuser'
password = 'YqGHWLuUvWpM8zxB'

db = VersionDatabase(host,dbname,user,password)

def __recoverinfo():
	ste = request.form['ste']
	if 'timestamp' in request.form:
		timestamp = request.form['timestamp']
	else:
		timestamp = time.time()

	if 'architecture' in request.form:
		arch = request.form['architecture']
	else:
		arch = None
	return [ste,timestamp, arch]

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/acs/', methods=['POST'])
def getAcsVersion():
	info = __recoverinfo()
	return json.dumps(db.getAcsVersion(info[0],timestamp=info[1],arch=info[2]))

@app.route('/build/', methods=['POST'])
def getBuild():
	info = __recoverinfo()
	return json.dumps(db.getBuild(info[0],timestamp=info[1],arch=info[2]))

@app.route('/antennas/', methods=['POST'])
def getAntennas():
	info = __recoverinfo()
	return json.dumps(db.getAntennas(info[0],timestamp=info[1],arch=info[2]))

@app.route('/patches/', methods=['POST'])
def getPatches():
	info = __recoverinfo()
	return json.dumps(db.getPatches(info[0],timestamp=info[1],arch=info[2]))

@app.route('/version/', methods=['POST'])
def getCompleteVersion():
	info = __recoverinfo()
	return json.dumps(db.getComplete(info[0],timestamp=info[1],arch=info[2]))


@app.route('/release/', methods=['POST'])
def get_release():
	info = __recoverinfo()
	return json.dumps(db.getRelease(info[0],timestamp=info[1],arch=info[2]))


if __name__ == '__main__':
	app.run('0.0.0.0')