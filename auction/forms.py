from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DecimalField
from wtforms.validators import InputRequired, Length, EqualTo, Email, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}  

class LoginForm(FlaskForm):

    user_name=StringField("Username", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    user_name=StringField("Username", validators=[InputRequired('Username is required')])
    email_id = StringField("Email Address", validators=[InputRequired('Email is required'), Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired('Password is required')])
    confirm = PasswordField("Confirm Password", validators=[EqualTo('password', message="Passwords should match")])
    #submit button
    submit = SubmitField("Register")

class CreateListingForm(FlaskForm):
      title = StringField('Title', validators=[InputRequired('Title is required')])
      # adding two validators, one to ensure input is entered and other to check if the 
      #description meets the length requirements
      description = TextAreaField('Description', 
                validators=[InputRequired('Description Required - MAX 300 characters'), 
                Length(min=10, max=300, message='Description too small or too large!')])
      image = FileField('Upload Image', 
                    validators=[FileRequired(message="Image can not be empty"),
                    FileAllowed(ALLOWED_FILE, message="ONLY supports png, jpg, PNG, JPG")])
      start_bid = StringField('Starting Bid', validators=[InputRequired('Starting bid is required')])
      #startingBid = DecimalField('Starting Bid', validators=[InputRequired('Starting Bid is required'), NumberRange(min=1, max=10, message='Value must be more than $1')])
      submit = SubmitField("Create")