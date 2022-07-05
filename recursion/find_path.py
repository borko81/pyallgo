LAB = [['-', '-', '-'], ['-', '*', '-'], ['-', '-', 'e']]
row = 3
col = 3


def find_ex(lab, x=0, y=0):
    if x + 1 > row or x - 1