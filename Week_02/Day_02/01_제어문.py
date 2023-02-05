if 5 < 3:
    print('크다!')
    print('!!!!!')
else: 
    print('작다!')

# 홀수/짝수 
n = int(input())
if n%2 == 1:
    print('홀수')
else:
    print('짝수')

# if n%2 != 0:
#     print('홀수')
# else:
#     print('짝수')

a = range(4)
print(a) # range(0, 4)
print(list(a)) # [0, 1, 2, 3]

b = range(0, -6, -1)
print(b) # range(0, -6, -1)
print(list(b)) # [0, -1, -2, -3, -4, -5]

a = 'apple'

for char in a:
    print(char)

l = ['윤원', '용진', '필진']

for name in l:
    print(name)
    # print(l[0])
    # print(l[1])
    # print(l[2])

for num in range(3):
    print(num**2)

a = 'pineapple'

# 'apple' => 0 ~ 4 : len('apple')-1
# 'pineapple' => 0 ~ 8 : len('pineapple')-1
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print('=================')
# 1. 
# 반복 가능한 객체 : 각 요소가 필요할 때
for char in a:
    print(char)
print('=================')
# 2. 
# 반복 가능한 객체 : 인덱스가 필요할 때 
for i in range(len(a)):
    print(i, a[i])

word = 'banana'

# a가 있으면, 1을 출력
for char in word:
    # print(char)
    if char == 'a':
        print(1)

print('===============')
if 'a' in word:
    print(1)

word = 'banana'

# a를 만나면 1을 출력하고 종료하세요.
# break : 반복 종료
for char in word:
    if char == 'a':
        print(1)
        break

print('============')
# a를 제외하고 모두 출력하세요.

# continue : 다음 반복을 실행
for char in word:
    if char == 'a':
        continue
    print(char)

for char in word:
    if char != 'a':
        print(char)

word = 'emango'

# 'e' 있으면 1을 출력
# 'e' 없으면 0을 출력
is_end = False # T/F 
for char in word:
    if char == 'e':
        is_end = True
        break

if is_end:
    print(1)
else:
    print(0)

for char in word:
    if char == 'e':
        print(1)
        break
else:
    print(0)