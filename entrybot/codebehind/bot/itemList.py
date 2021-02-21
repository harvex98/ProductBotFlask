from flask import (
    Blueprint, render_template, session, request, redirect, url_for
)
import datetime
from entrybot.database.db import Session
from entrybot.database.models.User import User
from entrybot.database.models.Sale import Sale
from entrybot.database.models.Product import Product


bp = Blueprint('itemList', __name__, url_prefix='/bot')


@bp.route('/itemList')
def itemList():
    # authentiation to see if a user is logged in - if not redirect to index
    dbSession = Session()
    items = dbSession.query(Product).filter(Product.ownerId == session.get('userid')).all()
    return render_template('/bot/items.html', items=items)


@bp.route('/add', methods=('POST',))
def add():
    dbSession = Session()
    name = request.form['name']
    cost = request.form['cost']
    source = request.form['source']
    now = datetime.datetime.now()

    newProduct = Product(session.get('userid'), name, now, cost, False, source)
    dbSession.add(newProduct)
    dbSession.commit()

    return redirect(url_for('bot.itemList'))


# @bp.route('/<int>:id/sell', methods=('POST',))
# def sell(id):
#     dbSession = Session()
#     product = dbSession.query(Product).filter(Product.id == id).first()
#     product.isSold = True
#     sale = Sale(id, , datetime.now , )


