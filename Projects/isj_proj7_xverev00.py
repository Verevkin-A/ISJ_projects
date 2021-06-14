#!/usr/bin/env python3
import collections

my_counter = collections.Counter()


def log_and_count(key=None, counts=None):
    def outer(f):
        def inner(*args, **kwargs):
            print('called {} with {} and {}'.format(f.__name__, args, kwargs))
            counts[key_arg] += 1
            return f(*args, **kwargs)
        if key is None:
            key_arg = f.__name__
        else:
            key_arg = key
        return inner
    return outer


@log_and_count(key='basic functions', counts=my_counter)
def f1(a, b=2):
    return a ** b


@log_and_count(key='basic functions', counts=my_counter)
def f2(a, b=3):
    return a ** 2 + b


@log_and_count(counts=my_counter)
def f3(a, b=5):
    return a ** 3 - b
