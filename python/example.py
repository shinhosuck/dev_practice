a = {'list':[
                {'first': 'Jack', 'last': 'Daniel', 'age': 33},
                {'first': 'Jim', 'last': 'Beam', 'age': 40},
            ]
    }

for k, v in a.items():
    for i in v:
        for k, v in i.items():
            print(f'{k}:{v}')
