
some_list = []
class SomeClass:
    """docstring for """
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def someFunc(self, name, age):
        profile = some_list.append({'name': self.name, 'age': self.age})
        return None

people = [
    SomeClass(name='Jack', age=44),
    SomeClass(name='Eric', age=49),
    SomeClass(name='Jack', age=44),
    SomeClass(name='Eric', age=49),
    SomeClass(name='Jack', age=44),
    SomeClass(name='Eric', age=49),
    SomeClass(name='Jack', age=44),
    SomeClass(name='Eric', age=49)
]
def new_func(people):
    for arg in people:
        name = arg.name
        age = arg.age
        arg.someFunc(name, age)
    return None
new_func(people)

for i in some_list:
    for k, v in i.items():
        print(k, v)


