from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config['SECRET_KEY'] = '631840a1435f130c1da8850a0fde08d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes
