from flask_sqlalchemy import SQLAlchemy
from firstflask import db
# db = SQLAlchemy(app)

class shopping_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=3000),
                            nullable=False, unique=True)

    def __repr__(self):
        return f"shopping item {self.name}"

