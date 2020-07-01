import database_data.database_session as db_session
from database_data.models.reviews import Reviews


def create_Reviews(game_ID, review_Desc, userid, rating):
    review = Reviews()
    review.game_ID = game_ID
    review.review_Desc = review_Desc
    review.user_ID = userid
    if rating == "True":
        review.rating = True
    else:
        review.rating = False

    session = db_session.create_session()
    session.add(review)
    session.commit()
    return review

def get_reviews():
    session = db_session.create_session()
    lst = session.query(Reviews).all()
    return lst

