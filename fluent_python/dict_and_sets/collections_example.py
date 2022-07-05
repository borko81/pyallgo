import collections

name = 'abracadabra'

ct = collections.Counter(name)

print(ct)
ct.update('azzaz')
print(ct.most_common(3))
print(collections.Counter(name).most_common(2))

