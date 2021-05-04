from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField

class AddPetForm(FlaskForm):
  name = StringField("Pet's Name")
  species = StringField("Species")
  photo_url = StringField("Photo URL")
  age = IntegerField("Age")
  notes = TextAreaField("Notes")