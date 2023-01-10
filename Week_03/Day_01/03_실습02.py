# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.
# 단, index() / find() 메서드는 사용하지마세요.

# 출력 예시1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1

str = input('문자열을 입력하세요 > ')
i = ''
cnt = 0
for i in str:
    if 'e' not in str:
            print(int(-1))
            break
    elif 'e' not in i:
            cnt += 1     
    elif 'e' in i:
            print(int(cnt))

# string = input("문자열을 입력하세요 > ")
# for index in range(len(string)):
#     if string[index] == 'e':
#         print(index)
#         break
# else:
#     print(-1)

# string = input("문자열을 입력하세요 > ")
# result = -1
# for index in range(len(string)):
#     if string[index] == 'e':
#         result = index
# print(result)
 
# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# hello 1

str = input('문자열을 입력하세요 > ').split()
print(len(str))

# string = input("문자열을 입력하세요 > ").split()
# dict_var = {}

# for word in string:
#     if word in dict_var:
#         dict_var[word] += 1

#     elif word not in dict_var:
#         dict_var[word] = 1

# for key, value in dict_var.items():
#     print(f"{key} {value}")

# 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple # 사용자 입력
# appl

x = input("문자열을 입력하세요 > ")
num = x.index('e')
strx = x[:num] + x[num+1:]
print(strx)

# string = input("문자열을 입력하세요 > ")
# new_string = ""
# for char in string:
#     if char != 'e':
#         new_string += char
# print(new_string)

# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고, 
# 문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple p # 사용자 입력
# 2

a, b = input('문자열 알파벳').split()
i = ''
cnt = 0
for i in a:
    if b in i:
            cnt += 1     
    elif b in i:
            cnt = 0
print(int(cnt))

# string, alpha = input("문자열을 입력하세요 > ").split()
# count = 0
# for char in string:
#     if char == alpha:
#         count += 1

# print(count)

# 문제 5
# 양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > 010 1234 5678 # 사용자 입력
# 010-1234-5678

a = int(input('자연수를 입력하세요 > '))
b = int(input('자연수를 입력하세요 > '))
c = int(input('자연수를 입력하세요 > '))
k = str(a)+'-'+str(b)+'-'+str(c)
print(k)

# string_list = input("문자열을 입력하세요 > ").split()

# #### 방법 1
# print(string_list[0], string_list[1], string_list[2], sep='-')

# #### 방법 2
# print(*string_list, sep="-")

# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > 244 # 사용자 입력
# 10

n =  int(input())

if n < 0:
    print(-1)
else:
    result =0
    while n > 0:
        result += n%10
        n //= 10
    print(result)

# # while 사용 
# # 반복적으로 n을 10으로 나눈 몫, 
# # n이 0보다 클 때 계속 반복!
# # 결과값은 n을 10으로 나눈 나머지를 더해나갈 것이다!

# n = int(input())

# if n < 0: 
#     print(-1)
# else:
#     result = 0
#     while n > 0:
#         result += n%10
#         n //= 10
#     print(result)

# n = input()

# result = 0
# for i in n:
#     result += int(i)

# print(result)