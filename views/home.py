import flask

from infrastructure import cookie

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def home():
    return flask.render_template('home/index.html', user_id=cookie.get_user_id_via_cookie(flask.request))