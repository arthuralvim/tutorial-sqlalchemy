# -*- coding: utf-8 -*-

from .conftest import session
from .profiling import profiling
from tutorial.models import Exemplo
from tutorial.base import is_mapped
import pytest


class TestSQLAlchemyMapped(object):

    def test_check_instance_is_sqlalchemy_mapped(self):
        assert is_mapped(Exemplo.random_instance())

    def test_only_work_with_sqlalchemy_instances(self):
        assert not is_mapped(Exemplo)


class TestModelBase(object):

    @profiling()
    def test_model_attrs(self):
        attrs = ['id', 'texto', 'numero', 'data', 'data_avancada',
                 'data_texto', 'condicao']

        model_instance = Exemplo.random_instance()
        model_attrs = model_instance.attrs

        for att in attrs:
            assert att in model_attrs

    @profiling()
    def test_model_dict(self):
        attrs = ['id', 'texto', 'numero', 'data', 'data_avancada',
                 'data_texto', 'condicao']
        model_instance = Exemplo.random_instance()
        model_attrs_dict = model_instance.attrs_dict

        for att in attrs:
            assert att in model_attrs_dict

    @profiling()
    def test_instances(self, session):
        session, transaction = session
        for _ in range(10):
            model_instance = Exemplo.random_instance()
            session.add(model_instance)
        assert 10 == session.query(Exemplo).count()

    @profiling()
    def test_raise_exception_from_csv_line(self):
        with pytest.raises(NotImplementedError):
            Exemplo.from_csv_line([])

    @profiling()
    def test_create(self, session):
        session, transaction = session
        exemplo_session = Exemplo(session)
        model_instance = Exemplo.random_instance()
        new_model_instance = exemplo_session.create(
            **model_instance.attrs_dict)
        assert model_instance.attrs_dict == new_model_instance.attrs_dict

    @profiling()
    def test_get(self, session):
        session, transaction = session
        exemplo_session = Exemplo(session)
        exemplo = Exemplo.random_instance()
        session.add(exemplo)
        session.commit()
        id_exemplo = exemplo.id
        exemplo_get = exemplo_session.get(id_exemplo)
        assert exemplo == exemplo_get

    @profiling()
    def test_get_by(self, session):
        session, transaction = session
        exemplo_session = Exemplo(session)
        exemplo = Exemplo.random_instance()
        session.add(exemplo)
        session.commit()
        id_exemplo = exemplo.id
        dict_get = {
            'id': id_exemplo,
            'texto': 'TEXTO',
        }
        exemplo_get_by = exemplo_session.get_by(**dict_get)
        assert exemplo == exemplo_get_by

    @profiling()
    def test_db_is_rolled_back(self, session):
        session, transaction = session
        assert 0 == session.query(Exemplo).count()
