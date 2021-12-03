from firstflask import app, db
from firstflask.models.model import *
from flask import render_template, redirect, url_for, flash, request
from ..views.forms import (RegisterForm,
                           LoginForm,
                           PurchaseItemForm,
                           SellItemForm)
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    # s1tr = "asfdasdf"
    # shopping_items = shopping_item.query.all()
    return render_template('home.html')


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f"Created successfully! {attempted_user.username}", category="success")
        return redirect(url_for("home_page"))
    if form.errors != {}:
        # if no errors from validations
        for err_msg in form.errors.values():
            flash(err_msg, category='danger')

    return render_template('register.html', form=form)


# @app.route("/home")
# def home_page():
#     return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        print(form.password.data)
        print(attempted_user.check_password_correction(
            attempted_password=form.password.data))

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(
                f"Login successfully! {attempted_user.username}", category="success")
            # ! url_for accept the function name
            return redirect(url_for('home_page'))
        else:
            return redirect(url_for('home_page'), category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Logout Successfully", category='info')
    return redirect('home')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    pForm = PurchaseItemForm()

    sForm = SellItemForm()
    if request.method == 'POST':
        purchased_item = request.form.get('purchased_item')
        p_item_obj = shopping_item.query.filter_by(name=purchased_item).first()
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                p_item_obj.buy(current_user)
                flash(
                    f"Congratuation! {p_item_obj.name} has been added to your inventory!", category="success")
            else:
                flash("Cannnot buy it, not enough money", category="danger")

        sold_item = request.form.get('sold_item')
        s_item_obj = shopping_item.query.filter_by(name=sold_item).first()
        if s_item_obj:
            if current_user.can_sell(s_item_obj):
                s_item_obj.sell(current_user)
                flash(
                    f"Congratuation! {s_item_obj.name} has been sold!", category="success")
        return redirect(url_for("market_page"))

    if request.method == "GET":
        items = shopping_item.query.filter_by(owner=None)
        owned = shopping_item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, owned=owned, purchase_form=pForm, sell_form=sForm)
# shopping_item(name="ip6",price=11235,barcode="233345",description="des5")
# db.session.add(t)
# db.commit()
# conda config --set auto_activate_base false
