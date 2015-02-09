
from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
from Database import VersionDatabase
import time

app = Flask(__name__)
app.debug = True
host = 'aivwiki.alma.cl'
dbname = 'aiv_ste_version'
user = 'queryuser'
password = 'YqGHWLuUvWpM8zxB'

db = VersionDatabase(host,dbname,user,password)

@app.route('/acs/', methods=['POST'])
def getAcsVersion():
	ste = request.form['ste']
	if 'time' in request.form:
		timestamp = request.form['time']
	else:
		timestamp = time.time()
	return json.dumps(db.getAcsVersion(ste, timestamp=timestamp))

@app.route('/build/', methods=['POST'])
def getBuild():
	ste = request.form['ste']
	if 'time' in request.form:
		timestamp = request.form['time']
	else:
		timestamp = time.time()
	return json.dumps(db.getBuild(ste,timestamp=timestamp))

@app.route('/antennas/', methods=['POST'])
def getAntennas():
	ste = request.form['ste']
	if 'time' in request.form:
		timestamp = request.form['time']
	else:
		timestamp = time.time()
	return json.dumps(db.getAntennas(ste,timestamp=timestamp))

@app.route('/patches/', methods=['POST'])
def getPatches():
	ste = request.form['ste']
	if 'time' in request.form:
		timestamp = request.form['time']
	else:
		timestamp = time.time()
	return json.dumps(db.getPatches(ste,timestamp=timestamp))


if __name__ == '__main__':
	app.run('0.0.0.0')