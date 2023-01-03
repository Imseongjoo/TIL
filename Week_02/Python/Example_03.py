# 홀수/짝수
num = int(input('입력'))
if num%2 == 1:
    print('홀수')
else: 
    print('짝수')

# 미세먼지
dust = 80
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료')

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
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print('==============')
# 1.
# 반복가능한  객체: 각 요소를 원할 때
for char in a:
    print(char)
# 2.
# 반복가능한  객체: 인덱스가 필요할 때
print('==============')
for i in range(5):
    print(a[i])

word = 'apple'
# a가 있으면, 1을 출력
for char in word:
    # print(char)
    if char == 'a':
        print(1)
print('===============')
if 'a' in word:
    print(1)

word = 'banana'
# a를 만나면 1을 출력하고 종료하세요
# break: 반복 종료
for  char in word:
    if char == 'a':
        print(1)
        break
print('============')
# a를 제외하고 모두 출력하세요
# continue: 다음 반복을 실행
for char in word:
    if char == 'a':
        continue
    print(char)
for char in word:
    if char !== 'a':
        print(char)

word = 'mango'
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