
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# User authentication
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Uniform Resource Identifier, to reach the datatbase
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'c6dfdae17a564734c768d579'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "danger"
from firstflask.views import view
