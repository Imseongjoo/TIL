class Person:

    def greeting(self):
        return 'hi....'

iu = Person()
jimin = Person()

# Person 타입을 가짐
print(type(iu))
print(type(jimin))
print(type([1, 2, 3]))
print(type([]))

# 메서드를 호출할 수 있음
print(iu.greeting())

# 속성을 부여할 수 있음 
iu.name = '아이유'
jimin.name = 'BTS 지민'
print(iu.name)
print(jimin.name)
print(type(iu.name))

class Person:

    # 생성자 메서드 
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕.. 난 {self.name}'

    # 소멸자 메서드
    def __del__(self):
        print('ㅠㅠ')

# 인스턴스 생성
p1 = Person('홍길동') # __init__메서드가 호출됨
print(p1.greeting()) # 직접 greeting을 호출!

# p2 = Person('뉴진스')
# print(p2.greeting())
# # print(Person.greeting(p2))

def foo(abc, d):
    return abc + d

foo(1, 2)
foo(100, 212312)

# 소개팅
# 사람 관련 정보 뭐가 있을까요?

class Person:

    def __init__(self, name, age, mbti):
        self.name = name 
        self.age = age
        self.mbti = mbti

    def greeting(self):
        return f'{self.name}입니다. {self.mbti}이구요...'

    # print(p1 > p2)
    def __gt__(self, other):
        if self.age > other.age:
            return self 
        else:
            return other 

    def __str__(self):
        return f'{self.name} ({self.age})'

    def __len__(self):
        return self.age

p1 = Person('재용', 30, 'istp')
p2 = Person('유영', 28, 'enfj')
print(p1.name)
print(p1.greeting())
print(p1 > p2)
print(p1)
print(len(p1))

print([1, 2, 3])
print(map(int, ['1', '2', '3']))

# 필수/선택

# 기능 설계 관점에서 
class MJ:
    pass

mj = MJ()

# 2068
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    print(f'#{test_case} {max(map(int, input().split()))}')

# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1