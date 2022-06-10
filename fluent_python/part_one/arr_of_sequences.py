from collections import namedtuple

symbols = '$¢£¥€¤'
x = 'ABC'
colors = ['black', 'white']
sizes = list('SML')

codes_one = []
codes_two = [ord(s) for s in symbols]

for symbol in symbols:
    codes_one.append(ord(symbol))

codes = [last := ord(c) for c in x]
print(codes)
print(last)

r = list(filter(lambda i: i > 162, map(ord, symbols)))
print(r)

Shirt = namedtuple('Shirt', ['color', 'size'])

tshirts = [last_shirt := Shirt(color, size) for size in sizes for color in colors]
print(last_shirt.color)
print(tshirts)