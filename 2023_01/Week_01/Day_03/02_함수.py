print(sum(range(1, int(input())+1)))

# 함수를 사용할 때 Input으로....

# print(*objects)
# *objects : *은 여러 값을 무한하게 받을 수 있다.
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')

# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 space
# end='\n' : end라는 키워드는 기본 값이 개행
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')

# 함수의 반환 값(return)

# print 함수는 반환 값이 없습니다.
print(print('hi'))  # None

# sum 함수는 합을 반환합니다.
print(sum([1, 2, 3]))  # 6

a = 5
result = print(a)
print(result)

numbers = [10, 20, 5]

# 길이?
cnt = 0
for number in numbers:
    cnt += 1
print(cnt)

# 함수!
print(len(numbers))

numbers = [10, 20, 5]
print(max(numbers))
print(max(1, 5, 7))

print(ord('a'))
print(chr(97))

a = [10, 20, 5]
print(sorted(a))

# 함수 객체
# 함수는 그 자체로 객체이다!
print(len)
print(type(len))

# 함수 호출
# Input을 넣어서 함수를 실행시켰다!
print(len([1, 2, 3]))

# map 함수

numbers = ['1', '2', '3']
result = 0
for number in numbers:
    result += int(number)
print(result)

numbers = ['1', '2', '3']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
numbers = ['1', '2', '3']
new_new_numbers = map(int, numbers)
print(new_new_numbers)
print(list(new_new_numbers))

a = input()
print(a)  # '2 5'
# 원하는 것은 숫자 2와 숫자 5

# 1. 문자열을 각각 쪼갠 요소를 가진 리스트로 변환 -> .split()
b = a.split()
print(b)  # ['2', '5']

# 2. 각 요소를 숫자로 변환 -> map()
c = map(int, b)
print(c)  # map

# 3. 각각 변수에 저장
d, e = list(c)  # list(c)가 [2, 5]
print(d, e)  # 각각 2, 5

# # 2 5
# d, e = map(int, input().split())
# print(d, e)
# # 2 5 7
# d, e, f = map(int, input().split())
# print(d, e, f)

# 결론
numbers = list(map(int, input().split()))
print(numbers)
d = numbers[0]
e = numbers[1]
