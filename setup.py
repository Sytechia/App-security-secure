import flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from database_data import database_session as db_session
from database_data.models.admins import MyAdminView,Admins

from database_data.models.game_list import Game
from database_data.models.reviews import Reviews
from database_data.models.users import User, MyModelView
from database_data.models.logs import Logs

app = flask.Flask(__name__, instance_path="/App-Security/templates/shared", static_folder='templates/static')
db = SQLAlchemy()
admin = Admin(app, index_view=MyAdminView())
app.config.from_object('config.DevelopmentConfig')
login = LoginManager(app)
db.init_app(app)


@login.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(Admins).get(user_id)

def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)

def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__), 'db', 'appSecurity.sqlite')
    db_session.global_init(db_file)


def register_blueprints():
    from views import home, shop, account, about

    app.register_blueprint(home.blueprint)
    app.register_blueprint(shop.blueprintShop)
    app.register_blueprint(account.blueprintaccounts)
    app.register_blueprint(about.blueprintAbout)


admin.add_view(ModelView(Admins, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_view(ModelView(Game, db.session))
admin.add_view(ModelView(Reviews, db.session))
admin.add_view(ModelView(Logs, db.session))