from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.fields.html5 import URLField
from wtforms.validators import Optional, NumberRange

class PetForm(FlaskForm):
  name = StringField("Pet's Name")
  species = SelectField("Species", choices=[
      ('cat', 'Cat'), 
      ('dog', 'Dog'), 
      ('porcupine', 'Porcupine')
    ])
  photo_url = URLField("Photo URL", validators=[Optional()])
  age = IntegerField("Age", validators=[NumberRange(min=0, max=30), Optional()])
  notes = TextAreaField("Notes")
  available = BooleanField("Available", default=True)
