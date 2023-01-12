import random

numbers = range(1, 46)
lucky = sorted(random.sample(numbers, 6))
print(lucky)

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

print(get_lotto(2))
# (2000, [[8, 10, 17, 19, 23, 39], [7, 15, 28, 32, 43, 45]])

def get_lotto_price(n):
    return n*1000

NUM_OF_LOTTO = 2
print(get_lotto(2))
print(get_lotto_price)    
# [[8, 11, 23, 33, 2, 3], [4, 29, 28, 32, 43, 11]])
# 2000

import lotto
import lotto_1

