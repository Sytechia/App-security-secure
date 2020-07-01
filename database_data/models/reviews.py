import datetime
import sqlalchemy
from database_data.modelbase import SqlAlchemyBase

class Reviews(SqlAlchemyBase):
    __tablename__ = 'reviews'

    review_ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    game_ID = sqlalchemy.Column(sqlalchemy.Integer)
    review_Desc = sqlalchemy.Column(sqlalchemy.String)
    user_ID = sqlalchemy.Column(sqlalchemy.Integer)
    rating = sqlalchemy.Column(sqlalchemy.Boolean)