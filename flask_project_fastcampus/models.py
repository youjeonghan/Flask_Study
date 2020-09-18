from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
	__tablename__ = 'todo'

	id = db.Column(db.Integer, primary_key=True)
	fcuser_id = db.Column(db.Integer, db.ForeignKey('fcuser.id'), nullable = False)
	title = db.Column(db.String(256))
	tstamp = db.Column(db.DateTime, server_default = db.func.now())

	@property
	def serialize(self):
		return{
			'id': self.id,
			'title': self.title,
			'tstamp': self.tstamp
		}

class Fcuser(db.Model):
	__tablename__ = 'fcuser'
	id = db.Column(db.Integer, primary_key=True)
	userid = db.Column(db.String(32))
	password = db.Column(db.String(128))
	todos = db.relationship('Todo', backref='fcuser', lazy=True)		# 나를 'Todo'라는 객체가 가져갈때 fcuser로 등록하겠다는뜻 	# lazy=True는 데이터베이스에서 가져올때 로드를 하겠다는 뜻