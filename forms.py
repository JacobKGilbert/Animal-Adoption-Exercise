from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, URLField
from wtforms.validators import Optional

class AddPetForm(FlaskForm):
  name = StringField("Pet's Name")
  species = SelectField("Species", choices=[
      ('cat', 'Cat'), 
      ('dog', 'Dog'), 
      ('pcpn', 'Porcupine')
    ])
  photo_url = URLField("Photo URL", validators=[Optional()])
  age = IntegerField("Age")
  notes = TextAreaField("Notes")