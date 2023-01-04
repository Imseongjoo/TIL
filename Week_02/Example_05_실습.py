# 문제 1
# 정수 한 개를 입력 받고, 
# 해당 숫자가 0보다 큰 숫자라면 
# True 아니면 False를 출력하세요.

num1 = int(input('정수를 입력하세요 > '))
num2 = 0
if num1 > 0:
    print('True')
else:
    print('False')

# number = int(input("정수를 입력하세요 > "))
# if number > 0:
#     print(True)
# else:
#     print(False)

# 문제 2
# 정수 두 개를 입력 받고, 
# 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('False')

# number1 = int(input("첫 번째 정수를 입력하세요 > "))
# number2 = int(input("두 번째 정수를 입력하세요 > "))

# if number1 == number2:
#     print(False)
# if number1 > number2:
#     print(number1)
# if number1 < number2:
#     print(number2)

# 문제 3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 
# 10보다 작다면 True 아니면 False를 출력하세요.

num1 = int(input('정수를 입력하세요 > '))
num2 = 1
num3 = 10
if num3 > num1 > num2:
    print('True')
else:
    print('False')

# number = int(input("정수를 입력하세요 > "))

# if 1 < number and number < 10:
#     print(True)
# else:
#     print(False)

# 문제 4
# 정수 한 개를 입력 받고 0 보다 크고, 
# 짝수라면 True 아니면 False를 출력하세요.

num1 = int(input('정수를 입력하세요 > '))
if num1%2 == 0 and num1 > num2:
    print('True')
else:
    print('False')

# number = int(input("정수를 입력하세요 > "))

# if number > 0:
#     if number % 2 == 0:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

# 문제 5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
# 값이 100 초과 / 0 미만이면 "에러" 출력
# 값이 60 이상이면 "합격" 출력
# 값이 60 미만이면 "불합격" 출력

num1 = int(input('정수를 입력하세요 > '))
if 100 < num1 or num1 < 0:
    print('에러')
elif num1 >= 60:
    print('합격')
elif num1 < 60:
    print('불합격')

# number = int(input("정수를 입력하세요 > "))

# if number > 100 or number < 0:
#     print("에러")
# else:
#     if number >= 60:
#         print("합격")
#     else:
#         print("불합격")

# 문제 6
# 문자열을 입력 받고, 
# 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
# 힌트 : 문자열 역슬라이싱

letter = input('문자열을 입력하세요 > ')
print(letter[::-1])

# string = input("문자열을 입력하세요 > ")

# for element in string[::-1]:
#     print(element)

# 문제 7
# 정수 두 개를 입력 받고, 
# 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요

num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
arr = (i for i in range(min(num1, num2)+1,max(num1, num2)))
if arr:
    print(*arr, sep='\n')
elif num1 == num2:
    print('False')

# number1 = int(input("첫 번째 정수를 입력하세요 > "))
# number2 = int(input("두 번째 정수를 입력하세요 > "))

# if number1 < number2:
#     for element in range(number1 + 1, number2):
#         print(element)

# elif number1 > number2:
#     for element in range(number2 + 1, number1):
#         print(element)

# else:
#     print(False)

# 문제 8
# 정수 두 개를 입력 받고, 
# 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력하세요

num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))
if num1 == num2:
    print('False')
elif num1 < num2:
    for A in reversed(range(num1 + 1, num2)):
        print(A, end = " ")
else:
    for B in reversed(range(num2 + 1, num1)):
        print(B, end = " ")

# number1 = int(input("첫 번째 정수를 입력하세요 > "))
# number2 = int(input("두 번째 정수를 입력하세요 > "))

# if number1 < number2:
#     for element in range(number2 - 1, number1, -1):
#         print(element, end=" ")

# elif number1 > number2:
#     for element in range(number1 - 1, number2, -1):
#         print(element, end=" ")

# else:
#     print(False)

# 문제 9
# 정수 한 개를 입력 받고, 
# 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

num1 = int(input('정수를 입력하세요 > '))
num2 = 1
if num1 < num2:
    print('False')
elif num1 >= num2:
    for i in range(num2,num1):
        if i % 2 ==1: 
          print(i)

# number = int(input("정수를 입력하세요 > "))

# if number < 1:
#     print(False)
# else:
#     for element in range(1, number):
#         if element % 2 == 1:
#             print(element)

# 문제 10
# 구구단을 출력하세요.

for x in range(2, 10):
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)

# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f"{i} X {j} = {i*j}")


