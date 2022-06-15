from distutils.log import error
from flask_wtf import FlaskForm
import requests 
from wtforms import StringField, PasswordField, EmailField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.url import base_url

class FormRegisterUser(FlaskForm):
    stambuk = StringField('Stambuk', validators=[DataRequired("Stambuk belum diisi")])
    nama = StringField('Nama')
    # nama = StringField('Nama', validators=[DataRequired("Nama belum diisi")])
    gender = SelectField('Gender', validators=[DataRequired("Gender belum dipilih")])
    prodi = SelectField('Prodi', validators=[DataRequired("Prodi belum dipilih")])
    email = EmailField('Email', validators=[Email("Email tidak sesuai")])
    password = PasswordField('Password', validators=[DataRequired("Minimal 6 Karakter")])
    # submit = SubmitField('Simpan Data')

    def __init__(self, msg = None, **kwargs):
        super().__init__(**kwargs)
        self.msg = msg
   
   
    url = base_url + '/auth/get-stambuk'
    req = requests.get(url)
    resp = req.json().get('data')

    print('repsol == ', resp)

    # msg = 
    # print('msggg', msg)

    def validate_stambuk(self, stambuk):
        for i in self.resp:
            if stambuk.data in i['stambuk']:
                raise ValidationError('Nim Sudah terdaftar')

    def validate_nama(self, nama):
        if nama.data == '':
            raise ValidationError('Nama tidak boleh kosong')