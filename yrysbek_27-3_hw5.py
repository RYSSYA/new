GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del GeekTech['bag']

GeekTech['address'] = 'ibraimova 103'

GeekTech['phone'] = '0507 052 018'

GeekTech['instagram'] = '@geektech_edu'

GeekTech['courses'].extend(['fullstack', 'UX|UI ', ' osnovy programmirovania' ])

GeekTech['courses'] = set(GeekTech['courses'])

GeekTech['foundation_date'] = '2018'

GeekTech['kol-vo kursov'] = 5

print(len(GeekTech['courses']))

for key, value in GeekTech.items():
    print(f'{key}: {value}')

    