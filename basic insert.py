import os
import sys
import database_data.database_session as db_session

# Make it run more easily outside of PyCharm
from database_data.models.admins import Admins

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))


def main():
    init_db()
    while True:
        insert_a_package()


def init_db():
    db_file = os.path.join(
        os.path.dirname(__file__), 'db', 'appSecurity.sqlite')
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()