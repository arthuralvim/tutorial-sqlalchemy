# -*- coding: utf-8 -*-

from .settings import ALEMBIC_CONFIG
from .settings import DATABASE_POSTGRESQL_URI
from .settings import SQLALCHEMY_ECHO
from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tutorial.base import Base
import pytest


def apply_migrations():
    config = Config(ALEMBIC_CONFIG)
    upgrade(config, 'head')


@pytest.fixture(scope='session')
def sqlengine(request):
    """
    Creates a new engine connection with a Postgresql database.
    """

    engine = create_engine(DATABASE_POSTGRESQL_URI, pool_recycle=3600,
                           echo=SQLALCHEMY_ECHO)
    Base.metadata.create_all(engine)
    # apply_migrations()

    def teardown():
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture()
def session(sqlengine, request):
    """
    Creates a new session/transaction using SQLAlchemy.
    """

    connection = sqlengine.connect()
    transaction = connection.begin()

    session_maker = sessionmaker(bind=connection)
    session = session_maker()

    def teardown():
        session.close()
        transaction.rollback()
        connection.close()

    request.addfinalizer(teardown)

    return (session, transaction)
