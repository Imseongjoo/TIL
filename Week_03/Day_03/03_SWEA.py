# 2047 신문 헤드라인

T = input('')
print(T.upper())

# 2025 N줄덧셈

T = int(input())
sum = 0
for i in range(1, T+1):
    sum += i
print(sum)

# 1936 1대1 가위바위보

a, b = map(int, input().split())
if a == 1:
    if b == 2:
        print("B")
    else:
        print("A")
elif a == 2:
    if b == 1:
        print("A")
    else:
        print("B")
else:
    if b == 1:
        print("B")
    else:
        print("A")

# 2027 대각선 출력하기

print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')

for i in range(5) :
    for j in range(5) :
        if i == j :
            print('#', end='')
        else :
            print('+', end='')
    print()

# 2058 자릿수 더하기

n =  int(input())
if n < 0:
    print(-1)
else:
    result =0
    while n > 0:
        result += n%10
        n //= 10
    print(result)

number=list(input())
number=list(map(int,number))
sum_number=sum(number)
print(sum_number)

# 2019 더블더블

N = int(input())
for i in range(0, N+1):
    print(2**i, end='')
