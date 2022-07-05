dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
shano = {code: country.upper() for code, country in sorted(dial_codes) if code > 50}

print(shano)

# marging mapping
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

print(d1 | d2)
d1 |= d2
print(d1)

check = [
    ('Bul', 1),
    ('USA', 2),
    ('Bul', 3)
]

result = {}

for code, pos in check:
    if not code in result:
        result[code] = []
    result[code].append(pos)

print(result)