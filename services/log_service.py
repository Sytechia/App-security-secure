import database_data.database_session as db_session
from database_data.models.logs import Logs

def createLog(logDateTime, logAccount, logPassword):
    log_Content = Logs()
    log_Content.log_DateTime = logDateTime
    log_Content.log_Account = logAccount
    log_Content.log_Attempted_Password = logPassword

    session = db_session.create_session()
    session.add(log_Content)
    session.commit()