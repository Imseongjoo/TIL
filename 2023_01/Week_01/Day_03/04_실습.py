# 문제 1
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.
# 단, abs() 함수는 사용하지 마세요.

num = int(input('정수를 입력하세요 > '))
if num >= 0:
    print(num)
else:
    print(num*-1)

# number = int(input("정수를 입력하세요 > "))
# if number > 0:
#     print(number)
# else:
#     print(number * -1)

# 문제 2
# 정수만 저장한 리스트가 주어집니다.
# 리스트 요소의 개수를 출력하세요.
# 단, len() 함수는 사용하지 마세요

number_list = [1, 2, 3, 4, 5]
cnt = 0
for number in number_list:
    cnt += 1
print(cnt)

# number_list = [1, 2, 3, 4, 5]
# count = 0

# for number in number_list:
#     count = count + 1

# print(count)

number_list = [0]
cnt = 0
for number in number_list:
    cnt += 1
print(cnt)

# 문제 3
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 합을 출력하세요.
# 단, sum() 함수는 사용하지 마세요.

number_list = [1, 2, 3, 4, 5]
result = 0
for number in number_list:
    result += number
print(result)

# number_list = [1, 2, 3, 4, 5]
# total = 0

# for number in number_list:
#     total = total + number

# print(total)

number_list = [-1, -2, -3, -4, -5]
result = 0
for number in number_list:
    result += int(number)
print(result)

# 문제 4
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 평균을 출력하세요.
# 단, len() / sum() 함수는 사용하지 마세요.

number_list = [2, 4, 6]
result = 0
cnt = 0
for number in number_list:
    result += int(number)
    cnt += 1
print(int(result/cnt))

number_list = [2, 4, 6]

# total = 0
# count = 0
# for number in number_list:
#     total = total + number
#     count = count + 1

# print(total / count)

number_list = [2, 3, 5, 7]
result = 0
cnt = 0
for number in number_list:
    result += int(number)
    cnt += 1
print(int(result/cnt))

# 문제 5
# 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수들의 곱을 출력하세요.

number_list = [1, 2, 3, 4, 5]
result = 1
for number in number_list:
    result *= int(number)
print(result)

number_list = [-1, -2, 3]
result = 1
for number in number_list:
    result *= int(number)
print(result)

# number_list = [-1, -2, 3]
# prod = 1
# for number in number_list:
#     prod = prod * number
# print(prod)

# 문제 6
# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.
# 단, max() 함수는 사용하지 마세요.

number_list = [1, 2, 3, 4, 5]
big = number_list[0]
for i in number_list:
    if i > big:
        big = i
print(big)

# number_list = [1, 2, 5, 4, 3]
# max_value = 0
# for number in number_list:
#     if number > max_value:
#         max_value = number
# print(max_value)

number_list = [1, 1, 1]
big = number_list[0]
for i in number_list:
    if i > big:
        big = i
print(big)

# 문제 7
# 양의 정수만 저장한 리스트가 주어집니다.
# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.
# 단, min() 함수는 사용하지 마세요.

number_list = [1, 2, 3, 4, 5]
small = number_list[0]
for i in number_list:
    if i < small:
        small = i
print(small)

number_list = [5, 5, 5, 2]
small = number_list[0]
for i in number_list:
    if i < small:
        small = i
print(small)

# number_list = [5, 2, 5, 5]
# min_value = number_list[0]
# for number in number_list:
#     if number < min_value:
#         min_value = number
# print(min_value)
