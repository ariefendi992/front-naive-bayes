from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import ValidationError

class FormAddUkt(FlaskForm):
    idUser = SelectField('Nama')
    nik = StringField('NIK')
    prodi = SelectField('Prodi')
    sms = SelectField('Semester')
    statusMhs = SelectField('Status Mahasiswa')
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

    def validate_nik(form, field):
        if field.data == '':
            raise ValidationError('* NIK belum di isi.')        
        elif len(field.data) < 16  :
            raise ValidationError(f'* Jumlah NIK tidak sesuai( {len(field.data)})')
        elif len(field.data) > 16  :
            raise ValidationError('* Jumlah NIK lebih ({})'.format(len(field.data)))        

    def validate_prodi(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
   
    def validate_sms(form, field):
        if len(field.data) == 0:
            raise ValidationError('* Data belum di pilih.')
   
    def validate_statusMhs(form, field):
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
    statusMhs = SelectField('Status Mahasiswa')
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
   
    def validate_statusMhs(form, field):
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
