from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hello123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_rt():
  '''Get home page.'''
  pets = Pet.query.all()
  return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
  '''GET new pet form. POST new pet to database'''
  form = AddPetForm()

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data

    flash(f'{name} the {species} was added.')
    return redirect('/')
  else:
    return render_template('add_pet.html', form=form)
    
