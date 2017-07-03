from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name")])
	last_name = StringField('last name', validators=[DataRequired("Please enter your last name")])
	email = StringField('Email', validators=[DataRequired("Please enter your email"),Email("Please enter a valid email")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password"), Length(min=6,message="Password must be at least 6 characters")])
	submit = SubmitField('Sign up')