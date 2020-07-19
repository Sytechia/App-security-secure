import flask
from flask import jsonify, redirect, request, render_template, Response
from flask_login import logout_user
import infrastructure.cookie as cookie_auth
from infrastructure.view_modifiers import response
from services import user_service, admin_service, log_service
import xml.etree.ElementTree as ET
from lxml import etree
from datetime import date, datetime

from viewmodels.account.accountIndexViewModel import accountIndexViewModel
from viewmodels.account.login_viewmodel import LoginViewModel

blueprintaccounts = flask.Blueprint('accounts', __name__, template_folder='templates')


@blueprintaccounts.route('/accounts')
@response(template_file='account/accountpage_user.html')
def index():
    vm = accountIndexViewModel()
    if not vm.user:
        return flask.redirect('/accounts/login')

    return vm.convert_to_dict()


#### Start of Register

@blueprintaccounts.route('/accounts/register')
def render_register():
    return flask.render_template('account/register.html')


@blueprintaccounts.route('/accounts/register', methods=["POST", "GET"])
def register():
    if flask.request.method == "POST":
        try:
            # Getting xml data from request
            xml = etree.fromstring(request.data)
            xml_validator = etree.DTD(file = 'db/register.dtd')
            isvalid = xml_validator.validate(xml)
            # if xml input matches DTD it will proceed
            if isvalid:
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
            # If xml does not match DTD it will return an error message
            else:
                return Response("TA",mimetype='text/xml')
            # If xml input contains external Entities it will return error message
        except:
            return Response("TA", mimetype='text/xml')


    elif flask.request.method == "GET":
        return {
            'user_id': cookie_auth.get_user_id_via_cookie(flask.request),
        }


#### Login
@blueprintaccounts.route('/accounts/login')
def render_login():
    return flask.render_template('account/login.html')


@blueprintaccounts.route('/accounts/login', methods=["GET", "POST"])
@response(template_file='account/login.html')
def login():
    if flask.request.method == "POST":
        vm = LoginViewModel()
        vm.validate()

        if vm.error:
            return vm.convert_to_dict()

        user = user_service.login_user_self(vm.email, vm.password)

        if not user:
            today = date.today()
            time = datetime.now()
            current_time = time.strftime("%H:%M:%S")
            log_DateTime = str(today) + " " + str(current_time)
            log_Account = vm.email
            log_AttemptedPassword = vm.password
            log_service.createLog(log_DateTime, log_Account, log_AttemptedPassword)

            f = open("loginLog.txt", "a")
            f.write("FAILED LOGIN ATTEMPT FOR " + vm.email + " at " + str(today) + " " + str(
                current_time) + " with password: " + vm.password + "\n")
            f.close()

        if not user:
            vm.error = "The account does not exist or the password is wrong."
            return vm.convert_to_dict()

        if user:
            resp = flask.redirect('/accounts')
            cookie_auth.set_auth(resp, user.id)
            return resp


@blueprintaccounts.route('/accounts/adminlogin')
def render_login_admin():
    return flask.render_template('account/loginadmin.html')


@blueprintaccounts.route('/accounts/adminlogin', methods=["GET", "POST"])
@response(template_file='account/loginadmin.html')
def loginadmin():
    if flask.request.method == "POST":
        vm = LoginViewModel()
        vm.validate()

        if vm.error:
            return vm.convert_to_dict()

        admin = admin_service.login_admin_self(vm.email, vm.password)

        if not admin:
            vm.error = "The account does not exist or the password is wrong(admin)."
            return vm.convert_to_dict()

        if admin:
            resp = flask.redirect('/admin')
            cookie_auth.set_auth(resp, admin.id)
            admin_service.check_admin_or_user(admin.id)

            return resp


@blueprintaccounts.route('/accounts/logout')
def logout():
    logout_user()
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp
