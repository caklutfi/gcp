from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, DateField, FileField, PasswordField, TimeField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class LoginUser(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password')
    submit = SubmitField('Login')

class Register(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    name = StringField('Full Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')

class ClientForm(FlaskForm):
    fullname = StringField('Nama')
    email = EmailField('Email')
    phone = StringField('Nomor telepon/WA')
    address = StringField('Alamat')
    payment = FileField('Bukti transfer')
    dp = StringField('Besaran DP')
    service = StringField('Sesi')
    package = StringField('Paket')
    date = DateField('Tanggal')
    time = TimeField('Waktu')
    instagram = StringField('Social media')
    reference = StringField('Dari mana anda mengetathui kami?')
    submit = SubmitField('Submit')