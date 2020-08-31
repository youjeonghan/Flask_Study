import os
from flask import Flask
from flask import request
from api_v1 import api as api_v1
from models import db

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'QWERQEWRQWERQWER'


db.init_app(app)		# 초기화
db.app = app 			# 등록
db.create_all()			# 반영

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)