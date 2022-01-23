#!/usr/bin/env python3

def first_with_given_key(iterable, key=lambda y: y):
    it_obj = iter(iterable)
    answer = []
    while True:
        try:
            var = next(it_obj)
            if key(var) not in answer:
                yield var
                answer.insert(-1, key(var))
        except StopIteration:
            break
