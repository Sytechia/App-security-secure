import flask
from infrastructure import cookie
from services.game_service import get_games
from services.review_service import create_Reviews, get_reviews
from services.user_service import get_user

blueprintShop = flask.Blueprint('shop', __name__, template_folder='templates')


@blueprintShop.route('/shop', methods=["POST", "GET"])
def shop():
    if flask.request.method == "POST":

        review_Desc = flask.request.form.get('review_Desc')
        userid = cookie.get_user_id_via_cookie(flask.request)
        checkbox = flask.request.form.get('checkboxval')
        game_ID = flask.request.form.get('game_ID')
        create_Reviews(game_ID, review_Desc, userid, checkbox)
        return flask.redirect('/shop')
    else:
        gamelist = get_games()
        reviewlst = get_reviews()
        userlst = get_user()
        gamelistname = []
        for i in gamelist:
            gamelistname.append(i.game_Name)
        return flask.render_template('games/games.html', gamelistname=gamelistname, gamelist=gamelist,
                                     userlst=userlst, reviewlst=reviewlst,
                                     user_id=cookie.get_user_id_via_cookie(flask.request))
