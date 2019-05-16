# File to store all the application forms using WTF

# Import Flask-WTF
from flask_wtf import FlaskForm
# Import the Field types from WTForms 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
# Import the validators from WTForms 
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

# Create a LoginForm that inherits from FlaskForm 
class LoginForm(FlaskForm):
    # Create the fields that will be in the form. The first arg is the label and the second is the validator
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """ Validate that the username does not already exist in the database. """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already in use. Please choose a different one.")

    def validate_email(self, email):
        """ Validate that the email does not already exists in the database. """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already in use. Please enter a different one.")