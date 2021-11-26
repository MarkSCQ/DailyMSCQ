from flask import Flask
from flask import request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

db = SQLAlchemy(app)

from firstflask.views import view
# Uniform Resource Identifier, to reach the datatbase

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"




# if __name__ == '__main__':
#     app.run(debug=True)
