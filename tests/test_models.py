# -*- coding: utf-8 -*-

from models import Customer
from models import Base
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker


def connect(user, password, db, host='localhost', port=5432, create_tables= True):
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    con = create_engine(url, client_encoding='utf8')

    meta = MetaData(bind=con, reflect=True)

    if create_tables:
        Base.metadata.create_all(con)

    return con, meta

con, meta = connect('postgres', '', 'alembic_example')

session = sessionmaker()
session.configure(bind=con)
s = session()
