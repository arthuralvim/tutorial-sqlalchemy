# -*- coding: utf-8 -*-

from datetime import datetime
from collections import namedtuple


Row = namedtuple('Row', ['texto', 'numero', 'data'])


class TransformInput(object):

    """docstring for TransformInput"""

    def __init__(self, extract):
        super(TransformInput, self).__init__()
        self.extracted_data = extract
        self.rows = []

    def transform_texto(self, value, default=None):

        if not value:
            value = None

        return value

    def transform_numero(self, value, default=None):
        try:
            value = int(value)
        except ValueError as e:
            if value:
                value = -1
            else:
                if default is not None:
                    value = default

        return value

    def transform_data(self, value, default=None):
        try:
            value = datetime.strptime(value, '%d/%m/%y')
        except ValueError as e:
            if value:
                value = -1
            else:
                value = None

        return value

    def run(self):
        for data in self.extracted_data:
            texto = self.transform_texto(data[0])
            numero = self.transform_numero(data[1], default=0)
            data = self.transform_data(data[2])
            row = Row(texto, numero, data)
            self.rows.append(row)
            print(row)
        return self.rows
