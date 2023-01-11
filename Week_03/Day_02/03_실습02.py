# 2029 몫과 나머지 출력하기

T = int(input())
for T in range(1, T+1):
    a, b = list(map(int,input().split()))
    q = a//b
    r = a%b
    print(f"#{T} {q} {r}")

# 방법 1
# string = input("문자열을 입력하세요 > ")
# for index in range(len(string)):
#     if string[index] == 'e':
#         print(index)
#         break
# else:
#     print(-1)

# 방법 2
# string = input("문자열을 입력하세요 > ")
# result = -1
# for index in range(len(string)):
#     if string[index] == 'e':
#         result = index
# print(result)

# 2071 평균값 구하기

T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = sum(numbers)/len(numbers)
    a = round(a)
    print(f"#{T} {a}")

# string = input("문자열을 입력하세요 > ").split()
# dict_var = {}

# for word in string:
#     if word in dict_var:
#         dict_var[word] += 1

#     elif word not in dict_var:
#         dict_var[word] = 1

# for key, value in dict_var.items():
#     print(f"{key} {value}")

# 1938 아주 간단한 계산기

a, b = list(map(int,input().split()))
print(a+b)
print(a-b)
print(a*b)
print(round(a/b))

# string = input("문자열을 입력하세요 > ")
# new_string = ""
# for char in string:
#     if char != 'e':
#         new_string += char
# print(new_string)

# 2046 스탬프 찍기

number = int(input())
print(number*'#')

# string, alpha = input("문자열을 입력하세요 > ").split()
# count = 0
# for char in string:
#     if char == alpha:
#         count += 1

# print(count)

string_list = input("문자열을 입력하세요 > ").split()

# #### 방법 1
# print(string_list[0], string_list[1], string_list[2], sep='-')

# #### 방법 2
# print(*string_list, sep="-")

# 2068 최대수 구하기

T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = max(numbers)
    print(f"#{T} {a}")

# number = int(input("양의 정수를 입력하세요 > "))
# if number < 0:
#     print(-1)

# else:
#     total = 0
#     while number > 0:
#         n = number % 10
#         total = total + n
#         number = number // 10
#     print(total)