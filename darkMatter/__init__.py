from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
from darkMatter.Models import Planet
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Database.db'
