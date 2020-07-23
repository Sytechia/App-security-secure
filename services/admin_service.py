from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import database_data.database_session as db_session
from flask_login import login_user
from database_data.models.admins import Admins


def get_admin_count() -> int:
    session = db_session.create_session()
    return session.query(Admins).count()


def get_admin():
    session = db_session.create_session()
    return session.query(Admins).all()


def find_admin_by_email(email):
    session = db_session.create_session()
    return session.query(Admins).filter(Admins.email == email).first()


def create_admin(name: str, email: str, password: str):
    if find_admin_by_email(email):
        return None
    admin = Admins()
    admin.email = email
    admin.name = name
    admin.hashed_password = hash_text(password)
    session = db_session.create_session()
    session.add(admin)
    session.commit()
    return admin

# def create_admin_test():
#     if find_admin_by_email('mistadmin@gmail.com'):
#         return None
#     admin = Admins()
#     admin.email = 'mistadmin@gmail.com'
#     admin.name = 'Mist'
#     admin.hashed_password = hash_text('12345')
#     session = db_session.create_session()
#     session.add(admin)
#     session.commit()
#     return admin


def hash_text(text: str):
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text, plain_text) -> bool:
    return crypto.verify(plain_text, hashed_text)


def validate_admin(email, password):
    session = db_session.create_session()
    admin = session.query(Admins).filter(Admins.email == email).first()
    if not admin:
        return None

    if not verify_hash(admin.hashed_password, password):
        return None

    return admin


def find_admin_by_id(user_id: int):
    session = db_session.create_session()
    admin = session.query(Admins).filter(Admins.id == user_id).first()
    return admin

def find_Admin_id_by_email(email):
    session = db_session.create_session()
    admin_email = session.query(Admins).filter(Admins.email == email).first()
    return admin_email.id


def check_admin_or_user(admin_id):
    session = db_session.create_session()
    return session.query(Admins).filter(Admins.id == admin_id).first()


def login_admin_self(email, password):
    session = db_session.create_session()
    try:
        admin = session.query(Admins).filter(Admins.email == email).first()
        if not admin:
            return None

        # if not verify_hash(admin.hashed_password, password):
        #     return None

        if password != admin.hashed_password:
            return None

        return admin
    finally:
        session.close()