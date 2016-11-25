from os import getenv, listdir, getcwd, path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('got', template_folder=path.join(getcwd(), __name__, 'views'), static_folder=path.join(getcwd(), 'static'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///got'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
