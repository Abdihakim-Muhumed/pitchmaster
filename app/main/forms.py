from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField,  BooleanField, TextAreaField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Required
from app.models import User, Pitch, Comment

class PitchForm(FlaskForm):
    category= RadioField('Pitch category', choices = [ ('interviewpitch', 'Interview Pitch'), ('pickuplines', 'Pick-Up Lines')], validators = [Required()])
    pitch_title = StringField('Title', validators = [Required()])
    pitch_content = TextAreaField("Enter your 60sec pitch", validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    description = TextAreaField('Add a comment:', validators = [Required()])
    submit = SubmitField('Submit')

class EditProfileForm(FlaskForm):
    bio = TextAreaField('Edit your bio:',validators = [Required()])
    submit = SubmitField('Submit')
