import datetime
import sqlalchemy
from database_data.modelbase import SqlAlchemyBase

class Logs(SqlAlchemyBase):
    __tablename__ = 'logs'

    logs_ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    log_DateTime = sqlalchemy.Column(sqlalchemy.String)
    log_Account = sqlalchemy.Column(sqlalchemy.String)
    log_Attempted_Password = sqlalchemy.Column(sqlalchemy.String)
    log_HostName = sqlalchemy.Column(sqlalchemy.String)
    log_IP_Address = sqlalchemy.Column(sqlalchemy.String)