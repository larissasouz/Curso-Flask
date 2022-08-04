from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


Curso_Flask = Flask(__name__)
Curso_Flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(Curso_Flask)
migrate = Migrate(Curso_Flask, db)

manager = Manager(Curso_Flask)
manager.add_command('db', MigrateCommand)

from Curso_Flask.controllers import default
