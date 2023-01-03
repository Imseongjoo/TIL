# 홀수/짝수

num = int(input('입력'))
if num%2 == 1:
    print('홀수')
else: 
    print('짝수')

# 미세먼지

dust = 80
if dust  > 150:
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