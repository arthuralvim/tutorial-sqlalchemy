# -*- coding: utf-8 -*-

from decouple import config
import json
import logging

LOG_LEVEL = config('LOG_LEVEL', default=None)


class StructuredLogger(object):

    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))

_l = StructuredLogger


def log(func):
    func._log = True
    return func


def create_logger(name='app_logger', log_name="test_and_profiling.log",
                  log_level=logging.INFO):
    """
    Creates a logging object and returns it
    """

    # logging.config.dictConfig(logging_conf_dict)
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL or log_level)

    # fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    fmt = '%(levelname)-8s - %(asctime)-15s - %(message)s'
    formatter = logging.Formatter(fmt)

    # ch = logging.StreamHandler()
    # ch.setLevel(LOG_LEVEL or log_level)
    # ch.setFormatter(formatter)

    # create the logging file handler
    fh = logging.FileHandler(log_name)
    fh.setLevel(LOG_LEVEL or log_level)
    fh.setFormatter(formatter)

    # add handler to logger object
    # logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

test_logger = create_logger('test_profiling')
