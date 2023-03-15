result = divmod(4, 3)
print(result)
print(type(result))

my_dict = {'name': '더 글로리', 'cast': '송혜교'}
print(my_dict.items())
print(type(my_dict.items()))

for a in my_dict.items():
    print(a)
    print(type(a))

locations = ['서울', '서울', '대전', '부산', '대전']
result = []

# 지역을 하나씩 반복
for location in locations:
    # 만약에 결과 통에 없다면,
    if location not in result:
        # 결과 통에 추가
        result.append(location)

print(result)
print(len(result))
print(set(locations))
print(len(set(locations)))

# dictionary : 키와 값의 모음

locations = ['서울', '서울', '대전', '부산', '대전']

# 지역별 갯수를 구하세요.
# {'서울': 2, '대전': 2, '부산': 1}
result = {}
for location in locations:
    # 만약에 result에 있으면 값 추가
    if location in result:
        result[location] += 1
    # 만약에 result에 없으면 키 값 추가
    else:
        result[location] = 1
print(result)

result = {}
for location in locations:
    # 만약에 result에 있으면 값 추가
    # if location in result:
    result[location] = result.get(location, 0) + 1

print(result)

# print('hello'.index('a'))
# Traceback (most recent call last):
#   File "C:\Users\hphk\Desktop\TIL\02_python\수업\day6\04_string.py", line 1, in <module>

#     'hello'.index('a')
# ValueError: substring not found
print('hello'.find('a'))
# -1

a, b = map(int, input().split())
print(a + b)

result = ['1', '5', '3', '4']

# 1534을 출력해야한다...?

# (1) print의 키워드(end)를 써서 출력한다.
# (2-1) 반복하면서 문자열을 만든다.

text = ''
for elem in result:
    text = text + elem
print(text)

# (2-2) join 메서드
print(''.join(result))

# 1 5 3 4
print(' '.join(result))

text = 'hello!'
print(text[::-1])
numbers = [3, 2, 10]
print(numbers[::-1])

drama = {'name': '더 글로리', 'writer': '김은숙'}
print(drama['name'])
# print(drama['director']) # KeyError
print(drama.get('director'))  # None

students = {'홍엽': 89, '민지': 20, '소담': 47}
print(students['홍엽'])
print(students.get('길동', 0))
