from flask import (
    Blueprint, render_template, session, request, redirect, url_for
)
import datetime
from entrybot.database.db import Session
from entrybot.database.models.User import User
from entrybot.database.models.Sale import Sale
from entrybot.database.models.Product import Product

bp = Blueprint('metrics', __name__, url_prefix='/bot')


@bp.route('/metrics')
def metricsHome():
    return render_template('/bot/metrics.html')

