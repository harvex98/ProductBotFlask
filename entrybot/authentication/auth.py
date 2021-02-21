import functools
from flask import (
    Blueprint, flash, render_template, request, redirect, url_for,
    session)
from werkzeug.security import check_password_hash, generate_password_hash
from entrybot.database.db import Session
from entrybot.database.models.User import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        error = None
        dbSession = Session()

        if not username:
            error = 'Username required.'
        elif not email:
            error = 'Email required.'
        elif dbSession.query(User).filter(User.name == username).first() is not None:
            error = 'User {} already registered'.format(username)
        if error is None:
            newUser = User(username, email)
            dbSession.add(newUser)
            dbSession.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html', userid=session.get('userid'))


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        dbSession = Session()
        username = request.form['username']
        email = request.form['email']
        userRequesting = dbSession.query(User).filter(User.name == username).first()
        error = None

        if not username:
            error = 'Username required.'
        elif not email:
            error = 'Email required.'
        elif userRequesting is None:
            error = 'User not found'
        if error is None:
            session['userid'] = userRequesting.id

            return redirect(url_for('itemList.itemList'))

    return render_template('auth/login.html', userid=session.get('userid'))


@bp.route('/logout')
def logout():
    session.pop('userid', None)
    flash('You were logged out')

    return redirect(url_for('index.index'))
