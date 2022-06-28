from distutils.log import error
from flask_wtf import FlaskForm
import requests 
from wtforms import StringField, PasswordField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.url import base_url
import re

class FormRegisterUser(FlaskForm):
    stambuk = StringField('Stambuk')
    nama = StringField('Nama')
    gender = SelectField('Gender')
    prodi = SelectField('Prodi')
    email = StringField('Email')
    password = PasswordField('Password')
    # submit = SubmitField('Simpan Data')

    def __init__(self, msg = None, **kwargs):
        super().__init__(**kwargs)
        self.msg = msg
   
   
    # url = base_url + '/auth/get-stambuk'
    # req = requests.get(url)
    # resp = req.json().get('data')

    def validate_stambuk(self, stambuk):
        if stambuk.data == "":
            raise ValidationError('* Stambuk tidak boleh kosong.')
        for i in self.resp:
            if stambuk.data in i['stambuk']:
                raise ValidationError('* Stambuk Sudah terdaftar.')

    def validate_nama(self, nama):
        if nama.data == '':
            raise ValidationError('* Nama tidak boleh kosong.')
    
    def validate_gender(self, gender):
        if gender.data == '':
            raise ValidationError('* Gender belum di pilih.')

    def validate_prodi(self, prodi):
        if len(prodi.data) <= 0:
            raise ValidationError('* Prodi harus di pilih.')

    def validate_email(self, email):
        if email.data == '':
            raise ValidationError('* Email harus di isi.')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
        if not (re.search(regex, email.data)):
            raise ValidationError('* Email tidak Valid.')


    def validate_password(self, password):
        if password.data == '':
            raise ValidationError('* Password harus di isi')
        
        elif len(password.data) < 6:
            raise ValidationError('* Password minimal 6 karakter')


