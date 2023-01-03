# num1 = int(input('정수를 입력하세요 > '))
# num2 = 0
# if num1 > 0:
#     print('True')
# else:
#     print('False')

# num1 = int(input('첫 번째 정수를 입력하세요 > '))
# num2 = int(input('두 번째 정수를 입력하세요 > '))
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     print('False')

# num1 = int(input('정수를 입력하세요 > '))
# num2 = 1
# num3 = 10
# if num3 > num1 > num2:
#     print('True')
# else:
#     print('False')

# num1 = int(input('정수를 입력하세요 > '))
# if num1%2 == 0 and num1 > num2:
#     print('True')
# else:
#     print('False')

# num1 = int(input('정수를 입력하세요 > '))
# if 100 < num1 or num1 < 0:
#     print('에러')
# elif num1 >= 60:
#     print('합격')
# elif num1 < 60:
#     print('불합격')

# letter = input('문자열을 입력하세요 >  ')
# print(letter[::-1])

# num1 = int(input('첫 번째 정수를 입력하세요 > '))
# num2 = int(input('두 번째 정수를 입력하세요 > '))
# arr = (i for i in range(min(num1, num2)+1,max(num1, num2)))
# if arr:
#     print(*arr, sep='\n')
# elif num1 == num2:
#     print('False')

# num1 = int(input('첫 번째 정수를 입력하세요 > '))
# num2 = int(input('두 번째 정수를 입력하세요 > '))
# if num1 == num2:
#     print('False')
# elif num1 < num2:
#     for A in reversed(range(num1 + 1, num2)):
#         print(A, end = " ")
# else:
#     for B in reversed(range(num2 + 1, num1)):
#         print(B, end = " ")

# num1 = int(input('정수를 입력하세요 > '))
# num2 = 1
# if num1 < num2:
#     print('False')
# elif num1 >= num2:
#     for i in range(num2,num1):
#         if i % 2 ==1: 
#           print(i)

# for x in range(2, 10):
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)