from flask import (
    Blueprint, render_template, session
)

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    userid = session.get('userid')

    return render_template('itemList/index.html', userid=userid)
