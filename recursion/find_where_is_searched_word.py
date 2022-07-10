def find_it(what, letter, i=0):
    if i >= len(letter):
        return None
    if letter[i: i + len(what)] == what:
        return i
    return find_it(what, letter, i + 1)


result = find_it('name', 'The only thing i learn is the name of this')
if result:
    print('Found at position %d' % result)
else:
    print("Not found match")
