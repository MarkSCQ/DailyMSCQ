from flask_sqlalchemy import SQLAlchemy
from firstflask import db, login_manager
from flask_login import UserMixin
from firstflask import bcrypt
# db = SQLAlchemy(app)

# You will need to provide a user_loader callback.
# This callback is used to reload the user object from the user ID stored in the session.
# It should take the unicode ID of a user, and return the corresponding user object.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}$"

    def can_purchase(self, item_obj):
        return self.budget-item_obj.price >= 0

    def can_sell(self, item_obj):
        return item_obj in self.items

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

    def bug(self, current_user):
        self.owner = current_user.id
        current_user.budget -= self.price
        db.session.commit()

    def sell(self, current_user):
        self.owner = None
        current_user.budget += self.price
        db.session.commit()
