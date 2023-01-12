import random

def get_lotto(n):
    # Input : 
     # n 로또 번호 세트 수
    # Output :
     # 오늘 지른 로또 금액
     # 번호 
    result = []
    for i in range(n):
        result.append(sorted(random.sample(range(1, 46), 6)))
    return n*1000, result

# # 사용하는 사람..
# print(get_lotto(2))
# (2000, [[3, 4, 24, 29, 41, 45], [18, 20, 26, 33, 39, 45]])   

import random

def get_lotto_1(n):
    result = []
    for i in range(n):
        result.append(sorted(random.sample(range(1, 46), 6)))
    return result

def get_lotto_price_1(n):
    return n*1000

# 사용하는 사람.. 
# NUM_OF_LOTTO = 2
# print(get_lotto(2))
# print(get_lotto_price(2))
# [[5, 17, 19, 33, 41, 42], [3, 12, 26, 27, 37, 39]]            
# 2000 
# Input : 
    # n 로또 번호 세트 수
# Output :
    # 오늘 지른 로또 금액
    # 번호 
# ===========================
# Data :
    # N 세트 수 
    # Lotto 번호 
# 기능 : 
    # 로또 구매 금액 계산
import random

class Lotto:

    def __init__(self, n):
        self.n = n 
        self.lotto_numbers = []
        for i in range(n):
            self.lotto_numbers.append(sorted(random.sample(range(1, 46), 6)))

    def update_numbers(self):
        self.lotto_numbers = []
        for i in range(self.n):
            self.lotto_numbers.append(sorted(random.sample(range(1, 46), 6)))
        return self.lotto_numbers

    def pprint(self):
        print('여러분의 행운번호-!')
        for numbers in self.lotto_numbers:
            print(numbers)
            print('=================')

    def get_price(self):
        return self.n * 1000

from lotto import get_lotto
from lotto_1 import get_lotto_1, get_lotto_price_1
from lotto_oop import Lotto

NUM_OF_LOTTO = 2

# 버전 1
print(get_lotto(NUM_OF_LOTTO))

# 버전 2
print(get_lotto_1(NUM_OF_LOTTO))
print(get_lotto_price_1(NUM_OF_LOTTO))

# OOP 버전
l = Lotto(5)
print(l.lotto_numbers)
print(l.n)
print(l.update_numbers())
print(l.lotto_numbers)
l.pprint()
print(l.get_price())

lotto2 = Lotto(1)

l.pprint()
lotto2.pprint()

import requests

print(requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json())

value = num if num >= 0 else -num

if num >= 0:
    value = num
else:
    value = -num    

members = ['홍엽', '세정']
print(enumerate(members))
print(list(enumerate(members, 1)))

numbers = ['1', '2', '3']
# [1, 2, 3]으로 바꾸고 싶다면?
# int : 함수
new_numbers = list(map(int, numbers))
print(new_numbers)

numbers = [[2, 1], [1, 3]]
# [[1, 2], [1, 3]]
# sorted : 함수
print(list(map(sorted, numbers)))

numbers = [2, 4]
# 2로 나눈 몫으로만 구성된
# [1, 2]
def div_2(n):
    return n//2
print(list(map(div_2, numbers)))
print(list(map(lambda n: n//2, numbers)))
print([ n//2 for n in numbers])

new_numbers = []
for n in numbers:
    new_numbers.append(n//2)
print(new_numbers)

def f(x, y):
    return x + y

def g(x :int, y :asdf) -> int:
    return x + y 