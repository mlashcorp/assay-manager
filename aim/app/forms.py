from wtforms import Form, BooleanField, TextField, PasswordField,DateField, validators,DecimalField

class RegistrationForm(Form):
    assay_id = TextField('Assay ID', [validators.Length(min=2, max=25),validators.Required()])
    assay_number = DecimalField('Assay number', [validators.Required()])
    assay_date = DateField('Date', [validators.Required()],format='%d-%m-%Y')
    jc_sample = TextField('JC Sample ID', [validators.Length(min=4, max=25),validators.Required()])