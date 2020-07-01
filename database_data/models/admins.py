import datetime
import sqlalchemy
from database_data.modelbase import SqlAlchemyBase
from flask_login import current_user
from flask_admin import AdminIndexView


class Admins(SqlAlchemyBase):
    __tablename__ = 'admin'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url = sqlalchemy.Column(sqlalchemy.String)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
