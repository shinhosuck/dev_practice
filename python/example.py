# a = {'list':[
#                 {'first': 'Jack', 'last': 'Daniel', 'age': 33},
#                 {'first': 'Jim', 'last': 'Beam', 'age': 40},
#             ]
#     }

# for k, v in a.items():
#     for i in v:
#         for k, v in i.items():
#             print(f'{k}:{v}')

def some_func(data):
    some_dict = [
        {'first': 'Eric', 'middle': 'Mark', 'last': 'Anderson'},
        {'first': 'Don', 'middle': 'Macho', 'last': 'Julio'},
    ]
    some_dict.append(data)
    return some_dict

def get_data():
    new_dict = {'first': 'Jim', 'middle': 'Boise', 'last': 'Beam'}
    data = some_func(new_dict)
    return data
r_data = get_data()


