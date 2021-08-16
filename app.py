from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hello123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_rt():
  '''Get home page.'''
  pets = Pet.query.all()
  return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
  '''GET new pet form. POST new pet to database'''
  form = PetForm()

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data

    new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

    db.session.add(new_pet)
    db.session.commit()

    flash(f'{name} the {species} was added.')
    return redirect('/')
  else:
    return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def display_pet(pet_id):
  '''GET pet page. POST edits to pet.'''
  pet = Pet.query.get_or_404(pet_id)
  form = PetForm(obj=pet)

  if form.validate_on_submit():
    pet.photo_url = form.photo_url.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.commit()

    return redirect('/')
  else:
    return render_template('pet.html', form=form, pet=pet)