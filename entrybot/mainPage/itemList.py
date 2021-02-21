from flask import (
    Blueprint, render_template, session, request, redirect, url_for
)
import datetime
from entrybot.database.db import Session
from entrybot.database.models.User import User
from entrybot.database.models.Product import Product


bp = Blueprint('itemList', __name__, url_prefix='/itemList')


@bp.route('/itemList')
def itemList():
    # authentiation to see if a user is logged in - if not redirect to index
    dbSession = Session()
    items = dbSession.query(Product).filter(Product.ownerId == session.get('userid')).all()
    return render_template('/itemList/itemList.html', items=items)


@bp.route('/add', methods=('POST',))
def add():
    dbSession = Session()
    name = request.form['name']
    cost = request.form['cost']

    newProduct = Product(name, datetime.datetime.now(), cost, False, session.get('userid'))
    dbSession.add(newProduct)
    dbSession.commit()

    return redirect(url_for('itemList.itemList'))
