from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class SignupForm(Form):
	username = StringField('Username', validators=[DataRequired("You need to enter a Username")])
	password = PasswordField('Password',validators=[DataRequired("Confirm your password"), Length(min = 5, message="Needs to be longer") ])
	copy_password = PasswordField('Confirm Password',validators=[EqualTo('password', message='Passwords must match')])
	submit = SubmitField('Sign Up')
		
class LogInForm(Form):
	username = StringField('Username', validators=[DataRequired("Enter Your Username")])
	password = PasswordField('Password',validators=[DataRequired("Enter Your Password")])
	submit = SubmitField('Login')

class ReviewForm(Form):
	title = StringField('Title', validators=[DataRequired("You need a title")])
	coffee_shop = StringField('Shop Name', validators=[DataRequired("You need a title")])
	rating = SelectField('Rating', validators=[DataRequired("You need a rating")], choices = [("1", '1'),("2", '2'),("3", '3'),("4", '4'),("5", '5')])
	description = TextAreaField('Description')
	submit = SubmitField('Submit')