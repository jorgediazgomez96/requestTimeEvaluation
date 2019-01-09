import csv
import time 
import datetime
import flask
import pandas as pd
import requests

def tiempoDeLlamada(URI,flag):
	total = 0
	times = [0,1,2,3,4,5,6,7,8,9,10]
	tDif = []

	for i in times: 
		tReq = time.time()
		if (flag == 'csv'):
			pd.read_csv(URI)
		elif(flag == 'image'):
			requests.get(URI, stream=True)
		else:
			pd.read_json(URI)
		tRes = time.time()
		tDif.append(round(tRes-tReq,2))
		print(URI + ' singleTime ========> ' + str(tDif[i]))
	for i in tDif:
		total = total + i
	average = total/10
	print(URI + ' AVERAGE ======> ' + str(average))
	print('========>')
	print('========>')
	print('========>')

tiempoDeLlamada('http://filesystem.heliohost.org/flask/files','json')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/anaconda.png','image')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/flask.png','image')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/google_datastudio.jpg','image')
tiempoDeLlamada('https://filesystem.heliohost.org/flask/download/image/yoFeliz.jpg','image')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/zeppelin.jpg','image')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/magneto.jpg','image')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/services','csv')
tiempoDeLlamada('http://filesystem.heliohost.org/flask/download/image/trimagneto.jpg', 'image')

