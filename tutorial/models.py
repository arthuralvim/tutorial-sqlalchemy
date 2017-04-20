# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Exemplo(Base):

    __tablename__ = 'exemplo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String, nullable=True)
    numero = Column(Integer, nullable=True)
    data = Column(DateTime, nullable=True)
    data_avancada = Column(DateTime, nullable=True)
    data_texto = Column(String, nullable=True)

    def __repr__(self):
        return "<Input('%s','%s', '%s')>" % (self.texto, self.numero,
                                             self.data)

    def __init__(self, row):
        self.texto = row.texto
        self.numero = row.numero
        self.data = row.data
        self.data_avancada = row.data_avancada
        self.data_texto = row.data_texto
