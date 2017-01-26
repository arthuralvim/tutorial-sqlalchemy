# -*- coding: utf-8 -*-

from decouple import config
from etl.extract import ExtractInput
from etl.transform import TransformInput
from etl.load import LoadToPostgres

path_to_input = config('TABELADADOS')


if __name__ == '__main__':
    extract = ExtractInput(path_to_input=path_to_input).run()
    print('extracao finalizada!')
    transform = TransformInput(extract=extract).run()
    print('transformacao finalizada!')
    to_postgres = LoadToPostgres(rows=transform).run()
    print('carregamento finalizado!')
    print('ETL finalizado!')
