from firstflask import app, db
from firstflask.models.model import *
from flask import render_template, redirect, url_for, flash
from ..views.forms import RegisterForm


@app.route("/")
@app.route("/index")
def index_page():
    s1tr = "asfdasdf"
    shopping_items = shopping_item.query.all()
    return render_template('index.html', item_name=333)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for("index_page"))
    if form.errors != {}:
        # if no errors from validations
        for err_msg in form.errors.values():
            flash(err_msg, category='danger')

    return render_template('register.html', form=form)


@app.route("/home")
def home_page():
    return render_template('home.html')
