from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
	__tablename__ = 'todo'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(256))
	tstamp = db.Column(db.DateTime, server_default = db.func.now())

	@property
	def serialize(self):
		return{
			'id': self.id,
			'title': self.title,
			'tstamp': self.tstamp
		}