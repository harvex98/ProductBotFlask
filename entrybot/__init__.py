import os
from flask import Flask


def create_app():
    from entrybot.database.db import init_db
    from .authentication import auth
    from .mainPage import index
    from .mainPage import itemList

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # put these in config file
        SECRET_KEY='dev',
        DATABASE='C:\\Users\\Klugman\\Documents\\pyDev\\ProductEntry\\entrybot\\database\\sqlite3\\entrybot.db'
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_db()
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(itemList.bp)
    app.add_url_rule('/', endpoint='index')
    return app
