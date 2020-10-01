from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, Email

  
class CommentForm(FlaskForm):
  comment = TextAreaField('Comment', validators=[InputRequired('Comment is required.'), Length(min=5, max=400, message="Comment is too long or too short.")])
  submit = SubmitField('Add Comment')

class LoginForm(FlaskForm):

    email=StringField("Email", validators=[InputRequired('Enter email'), Email("Please enter a valid email")])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):

    email_id = StringField("Email Address", validators=[InputRequired('Email is required'), Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired('Password is required')])
    confirm = PasswordField("Confirm Password", validators=[EqualTo('password', message="Passwords should match")])
    #submit button
    submit = SubmitField("Register")
