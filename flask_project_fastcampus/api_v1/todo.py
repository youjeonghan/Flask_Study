from flask import jsonify
from flask import request
from flask import Blueprint
from flask import session
from models import Todo, db
import datetime
import requests
from . import api

def send_slack(msg):
	res = requests.post('https://hooks.slack.com/services/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',json={\
		'text': msg}, headers={'Content-Type':'application/json'})

@api.route('/todos',methods=['GET','POST', 'DELETE'])
def todos():
	if request.method == 'POST':
		userid = session.get('userid', None)
		if not userid:
			return jsonify(), 401

		data = request.get_json()

		todo = Todo()
		todo.title = data.get('title')
		todo.fcuser_id = userid

		db.session.add(todo)
		db.session.commit()


		send_slack('TODO가 생성되었습니다')		# 사용자 정보, 할일 제목, 기한
		return jsonify(), 201

	elif request.method == 'GET':
		pass

	elif request.method == 'DELETE':
		pass

	
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
		ret_msg = 'Todo가 생성되었습니다'


		send_slack('[%s] "%s" 할일을 만들었습니다.' % (str(datetime.datetime.now()), todo_name))

	elif cmd == 'list':
		todos = Todo.query.all()
		for idx, todo in enumerate(todos):
			ret_msg += '%d. %s (~ %s)\n' % (idx + 1, todo.title, str(todo.tstamp))
		
	return ret_msg