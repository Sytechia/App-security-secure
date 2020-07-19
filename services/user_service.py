from random import random
from typing import Optional

from flask_login import login_user
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import database_data.database_session as db_session
from database_data.models.users import User


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()

def get_user():
    session = db_session.create_session()
    return session.query(User).all()

charstrLst="1234567890"
def makeRandom_Id():
    char = ''
    for i in range(22):
        char += charstrLst[random.randint(0,9)]
    return char


def find_user_by_email(email):
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()

def login_user_self(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    try:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return None

        if not verify_hash(user.hashed_password, password):
            return None

        return user
    finally:
        session.close()

def create_user(id:int, name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    if find_user_by_id(id):
        return None

    user = User()
    user.id = id
    user.email = email
    user.name = name
    user.hashed_password = hash_text(password)
    session = db_session.create_session()
    session.add(user)
    session.commit()
    return user


def hash_text(text: str):
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text, plain_text) -> bool:
    return crypto.verify(plain_text, hashed_text)


def validate_user(email, password):
    session = db_session.create_session()
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user


def find_user_by_id(user_id: int):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    return user


def check_admin_or_user(user_id):
    session = db_session.create_session()
    user_id = session.query().filter(User.id == user_id).first()
    return login_user(user_id)
