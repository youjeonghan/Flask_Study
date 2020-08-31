from flask import jsonify
from flask import request
from flask import Blueprint
from models import Todo, db
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


@api.route('/slack/todos', methods=['POST'])
def slack_todos():
	res = request.form['text'].split(' ')
	cmd, *args = res 		# 맨앞 명령어와 나머지 것들을 언패킹하는 것 (첫번째 변수는 cmd에 들어가고 나머지는 args에 리스트로 들어간다.)

	ret_msg = ''
	if cmd == 'create':
		todo_name = args[0]

		todo = Todo()
		todo.title = todo_name

		db.session.add(todo)
		db.session.commit()
		ret_msg = 'Todo가 생성되었습니다.'

	if cmd == 'list':
		pass
		
	return ret_msg