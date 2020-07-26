import os

class Config(object):
    DEBUG = True
    Testing = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "eH'HXv+`J%hOQPqb#Cut5pV=S:unfA4l-!P/hFM>x[,Z{4Ut.w_vpTM~9}_%>ga"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'db','appSecurity.sqlite').strip()
    UPLOAD_FOLDER = 'templates/static/images'



class DevelopmentConfig(Config):
    pass