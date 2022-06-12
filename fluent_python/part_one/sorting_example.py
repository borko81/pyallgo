fruits = ['grape', 'raspberry', 'apple', 'banana']
mixed_list = ['ala', 'Borko']

print(sorted(fruits, key=len, reverse=True))

print(min(fruits, key=lambda x: x[0]))

fruits.sort(key=len)
print(fruits)

# sort first by upper letter
print(sorted(mixed_list, key=lambda x: x[0].lower()))



