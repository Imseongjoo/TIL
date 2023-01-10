# 정수형 숫자를 입력 받고, 10을 더해서 출력하세요.

number = int(input('숫자를 입력해주세요 > '))
print(number + 10)

# 좋아하는 음식을 입력 받고, 출력하세요.

Food = input('좋아하는 음식을 입력해주세요 > ')
print(Food)

# 이름과 태어난 년도를 입력 받고, 출력하세요.
# (단, 태어난 년도를 나이로 변환해서 출력하세요.)

name = input('이름을 입력해주세요 > ')
birth = int(input('태어난 년도를 입력해주세요 > '))
print("저의 이름은", name,"이고, 올해 나이는" ,2024 - birth,"세 입니다.")

# 문장 두 개를 입력 받고, 두 문장을 연결해서 출력하세요.

in1 = input('첫 번째 문장을 입력해주세요 > ')
in2 = input('두 번째 문장을 입력해주세요 > ')
print(in1 + in2)

# 정수형 숫자 한 개를 입력 받고, 
# 정수형 숫자의 부호를 바꿔서 출력하세요.

number = int(input('숫자를 입력해주세요 > '))
print((-1) * number)

# 정수형 숫자 두 개를 입력 받고, 
# 두 정수형 숫자에 대한 아래 산술 연산 결과를 출력하세요.
# 산술 연산
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# 4. 몫
# 5. 나머지

num1 = int(input('첫 번째 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 숫자를 입력해주세요 > '))
print(num1 + 13, num1 -7, num1*30, num1//3, num1%1)
print(num2 + 13, num2 -7, num2*30, num2//3, num2%1)

# 정수형 숫자 세 개를 입력 받고, 
# 세 정수형 숫자의 평균을 출력하세요.

num1 = int(input('첫 번째 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 숫자를 입력해주세요 > '))
num3  = int(input('세 번째 숫자를 입력해주세요 > '))
print(int((num1 + num2 + num3)/3))

# 정수형 숫자 다섯 개를 입력 받고, 
# 다섯 개의 정수형 숫자를 리스트 객체에 저장해서 출력하세요.

num1 = int(input('첫 번째 숫자를 입력해주세요 > '))
num2 = int(input('두 번째 숫자를 입력해주세요 > '))
num3 = int(input('세 번째 숫자를 입력해주세요 > '))
num4 = int(input('네 번째 숫자를 입력해주세요 > '))
num5 = int(input('다섯 번째 숫자를 입력해주세요 > '))
list = [num1, num2, num3, num4, num5]
print(list)

# 문자열 하나와 정수형 숫자 한 개를 입력 받고,
# 문자열을 정수형 숫자만큼 반복해서 출력하세요.

letter = input('문자열을 입력해주세요 > ')
number = int(input('숫자를 입력해주세요 > '))
print(letter*number)

# 문자열 하나와 정수형 숫자 한 개를 입력 받고, 
# 문자열을 정수형 숫자만큼 반복해서 출력하세요.

num1 = int(input('첫 번째 숫자를 입력해주세요 >'))
print(num1)
num2 = int(input('두 번째 숫자를 입력해주세요 >'))
print(num1 + num2)
num3 = int(input('세 번째 숫자를 입력해주세요 >'))
print(num1 + num2 + num3)
num4 = int(input('네 번째 숫자를 입력해주세요 >'))
print(num1 + num2 + num3 + num4)
num5 = int(input('다섯 번째 숫자를 입력해주세요 >'))
print(num1 + num2 + num3 + num4 + num5)

# result = 0
# n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n1
# print(result)
# n2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n2
# print(result)
# n3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n3
# print(result)
# n4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n4
# print(result)
# n5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
# result = result + n5
# print(result)

# result = 0
# n1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
# result += n1
# print(result)
# n2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))
# result += n2
# print(result)
# n3 = int(input('세 번째 정수형 숫자를 입력해주세요 > '))
# result += n3
# print(result)
# n4 = int(input('네 번째 정수형 숫자를 입력해주세요 > '))
# result += n4
# print(result)
# n5 = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
# result += n5
# print(result)