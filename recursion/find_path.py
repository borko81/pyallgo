# LAB = [['-', '-', '-'], ['-', '*', '-'], ['-', '-', 'E']]

row = 3
col = 3


def find_ex(x, y, lab, direction, path):
    if x < 0 or y < 0 or x >= len(LAB) or y >= len(LAB[0]):
        return

    if lab[x][y] == '*':
        return

    if lab[x][y] == 'v':
        return

    path.append(direction)

    if lab[x][y] == 'e':
        print("".join(path))
    else:
        lab[x][y] = 'v'
        find_ex(x, y + 1, LAB, 'R', path)
        find_ex(x, y - 1, LAB, 'L', path)
        find_ex(x + 1, y, LAB, 'D', path)
        find_ex(x - 1, y, LAB, 'U', path)
        lab[x][y] = '-'

    path.pop()


LAB = []
for _ in range(row):
    LAB.append(list(input()))

for r in LAB:
    print(r)

find_ex(0, 0, LAB, '', [])
