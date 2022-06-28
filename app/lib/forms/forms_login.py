from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import ValidationError


class FormLogin(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    status = SelectField('Status')

    def validate_username(self, field):
        if len(field.data) == 0:
            raise ValidationError('** Username')
    
    def validate_password(self, field):
        if len(field.data) == 0:
            raise ValidationError('** Password ')
        if len(field.data) < 6:
            raise ValidationError('** Password minimal 6 digit')

    def validate_status(self, field):
        if len(field.data) == 0:
            raise ValidationError('** Pilih hak akses')

       