# minitask 4
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase.update({'A': mcase.get('a')+mcase.get('A')})
wanted = dict((k.lower(), v) for k, v in mcase.items())
print(wanted)
#wanted = {'a': 17, 'b': 34, 'z': 3}