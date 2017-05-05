# -*- coding: utf-8 -*-

from .base import Base
from .base import BaseModel
from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String


class Exemplo(BaseModel, Base):

    __tablename__ = 'exemplo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String, nullable=True)
    numero = Column(Integer, nullable=True)
    data = Column(DateTime, nullable=True)
    data_avancada = Column(DateTime, nullable=True)
    data_texto = Column(String, nullable=True)
    condicao = Column(Boolean, nullable=True)

    def __repr__(self):
        return "<Exemplo('%s','%s', '%s')>" % (self.texto, self.numero,
                                               self.data)

    @classmethod
    def random_instance(cls):
        kl = cls()
        kl.texto = 'TEXTO'
        kl.numero = 10
        kl.data = datetime.utcnow()
        kl.data_avancada = datetime.utcnow()
        kl.data_texto = kl.data.isoformat()
        kl.condicao = True
        return kl
