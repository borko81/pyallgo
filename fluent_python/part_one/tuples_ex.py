from collections import namedtuple

idx = [('USA', '31195855'),
       ('BRA', 'CE342567'),
       ('ESP', 'XDA205856')
       ]

Country = namedtuple('Country', ['Abr', 'Code'])

idx_represent = [Country(Abr, Code) for Abr, Code in idx]

for result in sorted(idx_represent, key=lambda x: x.Abr, reverse=True):
    print("{Abr}:{Code}".format(**result._asdict()))
