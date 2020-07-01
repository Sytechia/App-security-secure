import sys
import os

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from database_data.modelbase import SqlAlchemyBase
__factory = None


def global_init(db_file : str):
    global __factory
    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception("You must raise specify a db file.")

    connection_str = 'sqlite:///' + db_file.strip()
    engine = sa.create_engine(connection_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from database_data import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()

