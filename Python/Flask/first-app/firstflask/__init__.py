
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

db = SQLAlchemy(app)


# Uniform Resource Identifier, to reach the datatbase
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'c6dfdae17a564734c768d579'

from firstflask.views import view 