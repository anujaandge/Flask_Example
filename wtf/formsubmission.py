#flask-wtf
#creating Form
from ipaddress import summarize_address_range
from tkinter import Label
from flask_wtf import  FlaskForm 
from wtforms import StringField, PasswordField,IntegerField,TextAreaField,RadioField,SubmitField
from wtforms.validators import ValidationError, DataRequired


class MayinsoftRegistarionForm( FlaskForm ):
    name = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    phoneNumber = StringField(label="Enter mobile number", validators=[DataRequired()])  # Use StringField for phone numbers
    address = TextAreaField(label="Address")
    gender = RadioField(label="Gender", choices=[('male', 'Male'), ('female', 'Female')])  # Tuples for choices
    age = IntegerField(label="Age")
    submit = SubmitField("Send")
    
        
