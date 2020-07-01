import flask
from flask import jsonify,redirect,request,render_template,Response
from flask_login import logout_user
import infrastructure.cookie as cookie_auth
from services import user_service
import xml.etree.ElementTree as ET


blueprintaccounts = flask.Blueprint('accounts', __name__, template_folder='templates')


@blueprintaccounts.route('/accounts')
def index():
    user_id = cookie_auth.get_user_id_via_cookie(flask.request)
    if user_id is None:
        return flask.redirect('/accounts/login')
    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect('/accounts/login')

    return flask.render_template('account/acountpage_user.html', user=user,
                                 user_id=cookie_auth.get_user_id_via_cookie(flask.request))


#### Start of Register

@blueprintaccounts.route('/accounts/register')
def render_register():
    return flask.render_template('account/register.html')


@blueprintaccounts.route('/accounts/register', methods=["POST", "GET"])
def register():
    if flask.request.method == "POST":

        xml = ET.fromstring(request.data)
        data = []
        for i in xml:
            data.append(i.text)
        name = data[0]
        email = data[1]
        password = data[2]
        if not name or not email or not password:
            error = "MF"
            return Response(error, mimetype='text/xml')

        user = user_service.create_user(name, email, password)
        if not user:
            error = 'EE'
            return Response(error, mimetype='text/xml')

        resp = flask.redirect('/accounts')
        cookie_auth.set_auth(resp, user.id)

        return resp

    elif flask.request.method == "GET":
        return {
            'user_id': cookie_auth.get_user_id_via_cookie(flask.request),
        }

#### Login
@blueprintaccounts.route('/accounts/login')
def render_login():
    return flask.render_template('account/login.html')

@blueprintaccounts.route('/accounts/login', methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        email = flask.request.form.get('email').lower().strip()
        password = flask.request.form.get('password')
        if not email or not password:
            return flask.render_template('account/login.html', missing_fields="Some fields are missing",
                                         email=email,
                                         password=password,
                                         user_id=cookie_auth.get_user_id_via_cookie(flask.request))

        user = user_service.validate_user(email, password)

        if not user:
            return flask.render_template('account/login.html',
                                         missing_user="The user does not exist or the password is wrong",
                                         email=email,
                                         password=password,
                                         user_id=cookie_auth.get_user_id_via_cookie(flask.request))

        if user:
            resp = flask.redirect('/accounts')
            cookie_auth.set_auth(resp, user.id)
            if user.email == 'warlords47@gmail.com':
                user_id = 1
                user_service.check_admin_or_user(user_id)

            return resp

@blueprintaccounts.route('/accounts/logout')
def logout():
    logout_user()
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp





