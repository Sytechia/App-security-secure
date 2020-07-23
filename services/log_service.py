import database_data.database_session as db_session
from database_data.models.logs import Logs

def createLog(logDateTime, logAccount, logPassword, logHostName, logIPAddress, logbrowser):
    log_Content = Logs()
    log_Content.log_DateTime = logDateTime
    log_Content.log_Account = logAccount
    log_Content.log_Attempted_Password = logPassword
    log_Content.log_HostName = logHostName
    log_Content.log_IP_Address = logIPAddress
    log_Content.log_browser = logbrowser

    session = db_session.create_session()
    session.add(log_Content)
    session.commit()