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

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break   # 循环被break终止不执行else
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')



