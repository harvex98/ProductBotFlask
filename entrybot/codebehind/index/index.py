from flask import (
    Blueprint, render_template, session
)

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    userid = session.get('userid')

    return render_template('index/index.html', userid=userid)
