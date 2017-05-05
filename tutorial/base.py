# -*- coding: utf-8 -*-

from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.base import object_mapper
from sqlalchemy.orm.exc import UnmappedInstanceError


Base = declarative_base()


def is_mapped(obj):
    try:
        object_mapper(obj)
    except UnmappedInstanceError:
        return False
    return True


class BaseModel(object):

    """ Metaclass for the Model base class."""

    # Only include these attributes when serializing using __json__. If
    # relationships should be serialized, then they need to be whitelisted.
    __json_whitelist__ = None

    _session = None

    def __init__(self, session=None, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.session = session

    def get(self, id):
        return self.session.query(self.__class__).get(id)

    def get_by(self, **kw):
        return self.session.query(self.__class__).filter_by(**kw).first()

    @classmethod
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)
        if r:
            return r

        return cls.create(**kw)

    def create(self, **kw):
        r = self.__class__(**kw)
        self.session.add(r)
        return r

    def insert(self, **kw):
        self.session.execute(self.__class__.__table__.insert(
            values=kw)).close()

    def insert_many(self, iter):
        self.session.execute(self.__class__.__table__.insert(),
                             list(iter)).close()

    def all(self):
        return self.session.query(self.__class__).all()

    def count(self):
        return self.session.query(self.__class__).count()

    def delete_all(self):
        self.session.query(self.__class__).delete()

    def delete(self):
        self.session.delete(self)

    def refresh(self):
        self.session.refresh(self)

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n))
                           for n in self.__table__.c.keys())
        return "%s(%s)" % (self.__class__.__name__, values)

    def __json__(self):
        if self.__json_whitelist__ is not None:
            return dict((k, getattr(self, k)) for k in self.__json_whitelist__)

        return dict((k, getattr(self, k)) for k in self.__table__.c.keys())

    @classmethod
    def from_csv_line(cls, line):
        raise NotImplementedError("You must implement from_csv_line.")

    @property
    def attrs(self):
        return self.__class__.__table__.columns.keys()

    @property
    def attrs_dict(self):
        return dict((k, getattr(self, k)) for k in self.__table__.c.keys())


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
