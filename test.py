from def_class.student import Student
from def_class.dog import Dog
import types

print('hello world')

s = Student('John', 90)
print(s)
# print(s.__name)
# print(s.__score)
print(s.print_score())
s.__name = 'bob'
print(s.__name)
print(s._Student__name)

s.set_name('Zoro')
# s.set_score('101')

dog = Dog()

print(dog.run())


def fn():
    pass


print(isinstance(type(fn), types.FunctionType))

print(dir(dog))
print(dir(s))

