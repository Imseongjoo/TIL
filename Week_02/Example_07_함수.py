# print(*object)
# *object: *은 여러 값을 무한하게 받을 수 있다
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')

# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 Space
# end='＼n': end라는 키워드는 기본 값이 개행 
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')

# 함수의 반환 값(return)

# print 함수는 반환 값이 없습니다
print('hi') # None

# sum 함수는 합을 반환합니다
sum([1, 2, 3]) # 6 

a = 5
result = print(a)
print(result)

numbers = [10, 20,  5]
print(max(numbers))
print(max(1, 5, 7))

# 길이?
cnt = 0
for number in numbers:
    cnt += 1
print(cnt)

# 함수!
print(len(numbers))