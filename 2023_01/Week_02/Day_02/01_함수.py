def add(a, b):  # 정의
    return a + b


print(add(-10, -20))  # 호출
print(add(10, 20))

# 하나의 숫자를 입력 받아서 세제곱을 반환하는
# 함수 cube를 작성


def cube(number):
    return number**3


# 함수 호출
# 2의 세제곱
print(cube(2))
# 100의 세제곱
print(cube(100))

n = 43 + 55
print(n)


def foo():
    return 1, 2, 3


print(foo())
print(type(foo()))


def boo():
    a = 1 + 2


print(boo())

# return
# 명시적인 return문 없는 경우 : None
# 여러 값을 return 하는 경우 : tuple

a = divmod(4, 2)
print(a)

print('홍엽', '유영', '윤원', '진아')


def add(*numbers):
    # print(type(numbers)) # tuple
    result = 0
    for n in numbers:
        result += n
    return result


print(add(1, 2, 3, 10, 23))


def movie(**kwargs):
    return kwargs


print(movie(name='더 글로리', writer='김은숙'))

# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# open('README.md', 'r', encoding='UTF8')
# open('README.md', mode='r', encoding='UTF8')
# open('README.md', 'r', 'UTF8') # 다르게 동작! 왜? buffering이 세번째!

print(sum)

# global scope
a = 10

# local scope


def foo():
    b = 10


foo()
print(b)  # NameError!

# sum : Built-in scope
print(sum([1, 2, 3]))

# sum : Global scope
sum = 1 + 2

print(type(sum), sum)
print(sum([1, 2, 3]))

a = 5


def foo():
    print(a)  # Local scope에 a가 없네?


foo()

a = 5


def boo():
    global a
    a = 3
    print(a)


boo()
print(a)
# a = 5 + 6
# boo()
# a = foo()

for i in range(3):
    print(i)

print(i)  # 2 존재

# for, if는 별도의 scope를 가지지 않습니다.
