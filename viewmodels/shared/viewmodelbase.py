from typing import Optional

import flask

from infrastructure import request_dict, cookie


class ViewModelBase:
    def __init__(self):
        self.request = flask.request
        self.request_dict = request_dict.create('')

        self.error: Optional[str] = None
        self.user_id: Optional[int] = cookie.get_user_id_via_cookie(self.request)

    def convert_to_dict(self):
        return self.__dict__
