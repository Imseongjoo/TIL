# 1. 모듈을 가져오는 것!
import random
import datetime
import os

menu = ['햄버거', '국밥', '초밥']
print(random.choice(menu))
# 로또 추첨 코드 작성
# random.sample(population, k)
# Return a k length list   6개 숫자
# the population sequence. 1~45개 숫자 중 : range(1, 46)

for i in range(5):
    numbers = range(1, 46)
    lucky_numbers = random.sample(numbers, 6)
    print(sorted(lucky_numbers))

students = ['민욱', '홍엽', '현석', '정은']
print(students)
random.shuffle(students)
print(students)

# print(datetime.datetime.now())
# print(datetime.date(2023, 1, 5))

today = datetime.datetime.today()
# print(today)
# print(type(today))
# print(today.year)
# print(today.day)

end = datetime.datetime(2023, 6, 14)
print(f'우리가 개발자가 되는 시간... {end - today}')

# .sort() : 메서드
# return : None
# 해당 리스트 자체를 정렬!
numbers = [10, 2, 5]
result = numbers.sort()
print(result)  # None
print(numbers)

numbers = [10, 2, 5]
numbers.sort()
print(numbers)

# sorted() : 함수
# return : 정렬된 리스트
numbers = [10, 2, 5]
result = sorted(numbers)
print(result)  # [2, 5, 10]

print(os.listdir())
