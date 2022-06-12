name = 'bicycle'
invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella $17.50 3 $52.50
1489 6mm Tactile Switch x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201 $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
 """

# reverse
print(name[::-1])

# get only char % 2
print(name[::2])

YEAR = slice(0, 4)
PRICE = slice(44-7, 44)
line_items = invoice.split("\n")[2:]

for line in line_items:
    print(line[YEAR], line[PRICE])

print("-" * 20)

my_list = [['_'] * 3 for _ in range(3)]
my_list_two = []
for i in range(3):
    row = ['_'] * 3
    my_list_two.append(row)

l = list(range(10))
l[2:5] = [20, 30]
del l[-1]
my_list[1][0] = 'X'
print(my_list)
print(my_list_two)