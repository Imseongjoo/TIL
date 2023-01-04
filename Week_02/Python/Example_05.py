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

letter = input('문자열을 입력하세요 > ')
print(letter[::-1])

# string = input("문자열을 입력하세요 > ")

# for element in string[::-1]:
#     print(element)

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

for x in range(2, 10):
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)

# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f"{i} X {j} = {i*j}")


