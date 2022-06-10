from collections import namedtuple

check = namedtuple('Check', ['name', 'age'])

a = []
a.append(check('Borko', 40))
a.append(check('St', 40))

print([result.name for result in a])
