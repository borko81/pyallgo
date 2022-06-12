data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":<9} | {"longitude":>9}')
    # for unpack tuple need variable to be in parentasie
    for name, _, _, (lat, lon) in data:
        print(f'{name:15} | {lat:>9.4f} | {lon:>9.4f}')


def work_with_match():
    for record in data:
        match record:
            case [name, _, _, (_, lon)] if lon <= 0:
                print(f'{name}')


if __name__ == '__main__':
    work_with_match()
    
