from firstflask import app
from firstflask.models.model import *
from flask import render_template


@app.route("/")
@app.route('/index')
def index():
    s1tr = "asfdasdf"
    shopping_items = shopping_item.query.all()
    return render_template('index.html', item_name=shopping_items)


# @app.route("/")
# # @app.route("/index")
# def index():
#     return render_template('index.html')
