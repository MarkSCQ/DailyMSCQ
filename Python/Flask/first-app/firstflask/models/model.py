from flask_sqlalchemy import SQLAlchemy
from firstflask import db
# db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=100),
                              unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    # backref, when using the items and want to get the user, we can use backref, lazy=True will get all the items
    items = db.relationship('shopping_item', backref='owned_user', lazy=True)
    # So what do backref and lazy mean? backref is a simple way to also declare a new property on the Address class.
    # You can then also use my_address.person to get to the person at that address.
    # lazy defines when SQLAlchemy will load the data from the database:

    def __repr__(self):
        return f"User name {self.username}"


class shopping_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=3000),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"shopping item {self.name}"
