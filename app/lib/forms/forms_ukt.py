from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import ValidationError

class FormAddUkt(FlaskForm):
    idUser = SelectField('Nama')
    prodi = SelectField('Prodi')
    sms = SelectField('Semester')
    kip = SelectField('Status KIP/Bidik Misi')
    penghasilan = SelectField('Penghasilan Orang Tua')
    tanggungan = SelectField('Jumlah Tanggungan')
    pkh = SelectField('Penerima PKH/KKS')
    keputusan = SelectField('Kelayakan')


    def validate_idUser(self, field):
        if field.data == '':
            raise ValidationError(
                '* User belum di pilih.'
            )

    def validate_prodi(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
   
    def validate_sms(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
      
    def validate_kip(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
  
    def validate_penghasilan(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')

    def validate_tanggungan(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
    
    def validate_pkh(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
  
    def validate_keputusan(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')


class FormUjiData(FlaskForm):
    idUser = SelectField('Nama')
    prodi = SelectField('Prodi')
    sms = SelectField('Semester')
    kip = SelectField('Status KIP/Bidik Misi')
    penghasilan = SelectField('Penghasilan Orang Tua')
    tanggungan = SelectField('Jumlah Tanggungan')
    pkh = SelectField('Penerima PKH/KKS')

    def validate_idUser(self, field):
        if field.data == '':
            raise ValidationError(
                '* User belum di pilih.'
            )

    def validate_prodi(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
   
    def validate_sms(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')

   
    def validate_kip(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
  
    def validate_penghasilan(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')

    def validate_tanggungan(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
    
    def validate_pkh(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
