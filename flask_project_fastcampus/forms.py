from models import Fcuser
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
	userid = StringField('userid', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	repassword = PasswordField('repassword', validators=[DataRequired()])