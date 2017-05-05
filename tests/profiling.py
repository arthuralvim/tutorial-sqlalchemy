# -*- coding: utf-8 -*-

import time
import decorator
from logtest import test_logger
from logtest import _l

milli_time = (lambda x: int(round(x * 1000)))


def profiling(msg=None, records=None):
    def deco(func):
        def wrapper(func, *args, **kwargs):
            start = time.time()
            v = func(*args, **kwargs)
            end = time.time()

            test_obj = args[0]

            dict_float = {
                'width': 10,
                'prec': 3,
            }

            dict_info = {
                'function_name': func.__name__,
                'test_case': '{0}.{1}'.format(test_obj.__class__.__module__,
                                              test_obj.__class__.__name__),
                'records': records,
                'start': '{:{width}.{prec}f}'.format(start, **dict_float),
                'end': '{:{width}.{prec}f}'.format(end, **dict_float),
                'duration': '{:{width}.{prec}f}'.format(end - start,
                                                        **dict_float),
            }
            if records is not None:
                _msg = '{function_name} - {records}: {duration} s'

            if msg is None:
                _msg = '{function_name} - {duration} s'
            else:
                _msg = msg

            test_logger.info(_l(_msg.format(**dict_info), **dict_info))

            return v

        return decorator.decorator(wrapper, func)

    return deco
