from flask import jsonify
from flask import request
import requests

from . import api

@api.route('/todos',methods=['GET','POST'])
def todos():
	if request.method == 'POST':
		res = requests.post('https://hooks.slack.com/services/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',json={
			'text': 'Hello world'}, headers={'Content-Type':'application/json'})

	elif request.method == 'GET':
		pass

	data = request.get_json()
	return jsonify(data)


@api.route('/test',methods=['POST'])
def test():
	res = request.form['text']
	print(res)
	return jsonify(res)