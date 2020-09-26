from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address:',validators=[Required(),Email()])
    username = StringField('Enter your username:',validators = [Required()])
    password = PasswordField('Password:',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password:',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email', 'danger')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is not available', 'danger')

    def validate_password(self,password1=password,password2=password_confirm):
        if password1 is not password2:
            raise ValidationError('Passwords must match','danger')