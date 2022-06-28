from unicodedata import numeric
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError


class ProdiForm(FlaskForm):
    prodi = StringField('Prodi')

    def validate_prodi(self, field):
        if len(field.data) == 0 :
            raise ValidationError('**Data belum di isi.')


class SemesterForm(FlaskForm):
    semester = StringField('Semester')

    def validate_semester(self, field):
        if len(field.data) == 0 :
            raise ValidationError('**Data belum di isi.')
        

class PenghasilanOrtuForm(FlaskForm):
    penghasilan = StringField('Penghasilan')
    keterangan = StringField('Keterangan')

    def validate_penghasilan(self, field):
        if len(field.data) == 0 :
            raise ValidationError('**Data belum di isi.')
    
    def validate_keterangan(self, field):
        if len(field.data) == 0 :
            raise ValidationError('**Data belum di isi.')


class TanggunganForm(FlaskForm):
    tanggungan = StringField('Jumlah Tanggungan')
    
    def validate_tanggungan(self, field):
        if len(field.data) == 0 :
            raise ValidationError('**Data belum di isi.')
       