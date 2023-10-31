from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length,DataRequired,Email



class RegistrationForm(FlaskForm):
  fname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=25)])
  lname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=25)])
  username = StringField('User Name', validators=[DataRequired(),Length(min=2,max=25)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  