# https://www.acmicpc.net/problem/1526
# 백준 1526 가장 큰 금민수

max_number = 0

# 파이썬은 1초에 1억번 연산(반복문)
N = 474747
for number in range(4, N + 1):
    string_temp = str(number)

    # 어떤 수가 4와 7을 제외한 숫자가 있는지 확인
    if not('0' in string_temp or 
        '1' in string_temp or
        '2' in string_temp or
        '3' in string_temp or
        '5' in string_temp or
        '6' in string_temp or
        '8' in string_temp or
        '9' in string_temp):
        # print(number,"금민수 입니다.")  
        max_number = number

print(max_number)

# https://www.acmicpc.net/problem/1436
# 백준 1436 영화감독 숌 

N = 500

# N번째
count = 0

movie_number = 666
while True:  
    # 숫자에 666 이 있는지?
    if '666' in str(movie_number):
        count += 1
 
    # 무한 반복문을 종료할 조건
    # N번째 나온 영화이름을 찾을 때
    if count == N:
        break

    # 3
    movie_number += 1

# N번째 영화 이름 출력
print(movie_number)