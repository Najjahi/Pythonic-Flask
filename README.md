Flask App developed for Flask course on https://youtube.com/playlist?list=PL6X8IkNltYY_MgJNuEX- ◦ S1OABlAGOVUUw
 projet
python -m venv venv
venv\Scripts\activate
pip install flask
pip install flask-admin flask-sqlalchemy
from flask_admin.contrib.sqla import ModelView
pip install --upgrade flask-admin flask flask-sqlalchemy wtforms
pip install wtforms-sqlalchemy flask-ckeditor Flask-Mail
pip install flask-modals Flask-Mail flask-admin Pillow
pip install Flask-WTF Flask-Login
pip install Flask-Bcrypt Flask-Migrate

pip install Werkzeug==2.2.3
pip install python-dotenv


Ctrl + Shift + P tape "Python: Select Interpreter" et sélectionne l'interpréteur dans ton venv
C:\Users\lenovo\Desktop\Pythonic-Flask\venv\Scripts\python.exe













pip install flask_wtf 
 pip install flask_bcrypt from flask_bcrypt import Bcrypt 
pip install flask_login
bcrypt  =Bcrypt() instance de la clase bcrypt
password = bcrypt.generate_password_hash('password').decode('utf-8')
 bcrypt.check_password_hash(hashed_password,'password123').decode('utf-8')
hashed_password = bcrypt.generate_password_hash('form.password.data').decode('utf-8')

def validate_username(self, username):username = User.query.filter_by(username.data).first()
 if user : raise ValidationError('username existe deja') methode wtform

from wtforms import Stringfield, PasswordField, submitField, BooleanField
from wtforms.validators import dataRequired, Length, Email, Regexp, Equalto, validationerror
from pythonic.models import User

ctr d pour modifier un plusiuers fois
lazy pour telecharger
formhidden_tag est 1 attribut de form instance pour proteger le formulaire
flash(f"compte cree for ^form.username.data",'succes') pour message

from flask import Flask, render_template, url_for,flask, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrqtionForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_login import db, LoginManager
from flask_login import UserMixin
from flask_login import login_user
login_manager = LoginManager(app) instance de la classe

login_user



@login_manager.user_loader   methode cherche user de la bd
def load_user(user_id):
	return User.query.get(int(user_id))

% with messages = get_flashed_messages(with_categories=true)% %if message% %for category, message%
div message /div %endfor% %endif% %endwith%



pyton import secrets 
secrets.token_hex(32) Click entree on copie on colle ds secret-KEY
pip install --upgrade flask


pip install -r requirements.txt
python.exe -m pip install --upgrade pip
.\.venv\Scripts\activate
$env:FLASK_APP = "run.py" 
venv) PS C:\Users\lenovo\Desktop\projetcnam>
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = "1"
flask run
>>

Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: Could not import 'app'.
(venv) PS C:\Users\lenovo\Desktop\projetcnam> 
from flask_bcrypt import Bcrypt
>>> Bcrypt()
bcrypt.generate_password_hash('password')

bcrypt.generate_password_hash('password').decode('utf-8')
<flask_bcrypt.Bcrypt object at 0x000001CDC4924C20>                  ode('utf-8')
>>> bcrypt = Bcrypt()
>>> hashed_password = bcrypt.generate_password_hash('password').deccode('utf-8')
>>> bcrypt.check_password_hash(hashed_password, 'password')
hashed_password = bcrypt.generate_password_hash('form.password.data').decode('utf-8')
omar@gmail.com
PASS!!word123
password R@yane2017

from projet import db
from projet.models import User

from projet import User, recette, Cuisine

user_1 = User(fname = 'imane', lname = 'najjahi', username = 'imane' email = 'imane@gmail.com', password = 'R@yane1917')
db.session.add(user_1)

user_2 = User(fname='anas', lname='najjahi', username='anas', email='anas@gmail.com', password='R@yane1917')

db.session.add(user_2)
db.session.add(user_1)
db.session.commit()

db.drop_all()
db.create_all()
User.query.all()


RDV : https://www.jdoodle.com/online-java-compiler