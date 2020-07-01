import database_data.database_session as db_session
from database_data.models.game_list import Game


def get_games():
    session = db_session.create_session()
    lst = session.query(Game).all()
    return lst





