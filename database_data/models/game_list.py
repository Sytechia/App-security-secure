import datetime
import sqlalchemy
from database_data.modelbase import SqlAlchemyBase


class Game(SqlAlchemyBase):
    __tablename__ = 'games'

    game_ID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    game_Name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    game_price = sqlalchemy.Column(sqlalchemy.Numeric(5, 2), nullable=False)



