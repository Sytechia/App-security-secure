import flask
from infrastructure import cookie

blueprintAbout = flask.Blueprint('aboutus', __name__, template_folder='templates')


@blueprintAbout.route('/aboutus')
def aboutus():
    return flask.render_template('aboutus/aboutus.html', user_id=cookie.get_user_id_via_cookie(flask.request))