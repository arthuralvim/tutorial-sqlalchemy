# -*- coding: utf-8 -*-

from contextlib import contextmanager


@contextmanager
def PostgreSQLConnection(session_maker):

    """Provide a transactional scope around a series of operations."""

    session = session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def PostgreSQLCursor(connection):

    """Provide a transactional scope around a series of operations."""

    try:
        cursor = connection.cursor()
        yield cursor
    except Exception as e:
        raise e
    finally:
        cursor.close()
