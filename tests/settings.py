# -*- coding: utf-8 -*-

from unipath import Path
from decouple import config
APP_DIR = Path(__file__).absolute().ancestor(2)
print(APP_DIR)
DATABASE_SQLITE3_URI = 'sqlite:///{0}/test_sqlalchemy.db'.format(APP_DIR)
DATABASE_POSTGRESQL_URI = config('POSTGRESQL_DATABASE_URI')
SQLALCHEMY_ECHO = config('SQLALCHEMY_ECHO', default=False, cast=bool)
ALEMBIC_CONFIG = APP_DIR.child('alembic.ini')
