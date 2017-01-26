# -*- coding: utf-8 -*-

from .models import Input
from .models import Base
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresConnection(object):

    postgresql_database_url = config('POSTGRESQL_DATABASE_URL')

    def __init__(self):
        self.engine = self.get_engine()
        self.create_tables()
        self.Session = sessionmaker(bind=self.engine)

    def create_connection(self):
        return self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_engine(self):
        return create_engine(self.postgresql_database_url)


class LoadToPostgres(PostgresConnection):

    """docstring for LoadToPostgres"""

    def __init__(self, rows):
        super(LoadToPostgres, self).__init__()
        self.rows = rows
        self.elements = []

    def rows_to_models(self):
        for row in self.rows:
            elemento = Input(row)
            self.elements.append(elemento)
            print(elemento)

    def save_models(self):

        session = self.create_connection()

        for el in self.elements:
            try:
                session.add(el)
                session.commit()
            except:
                session.rollback()
                raise Exception('Elemento nao salvo: %s' % el)
            finally:
                session.close()

    def run(self):
        self.rows_to_models()
        self.save_models()
