# -*- coding: utf-8 -*-

import csv


class ExtractInput(object):

    """docstring for TransformInput"""

    def __init__(self, path_to_input):
        super(ExtractInput, self).__init__()
        self.path_to_input = path_to_input

    def load_input(self, path_to_input=None):
        with open(path_to_input, 'r') as f:
            reader = csv.reader(f, delimiter=';', quotechar='|')
            return list(reader)

    def run(self):
        valores = self.load_input(self.path_to_input)
        for val in valores:
            print(val)
        return valores
