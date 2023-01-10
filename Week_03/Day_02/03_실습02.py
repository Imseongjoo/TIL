# 2029 몫과 나머지 출력하기

T = int(input())
for T in range(1, T+1):
    a, b = list(map(int,input().split()))
    q = a//b
    r = a%b
    print(f"#{T} {q} {r}")

# 2071 평균값 구하기

T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = sum(numbers)/len(numbers)
    a = round(a)
    print(f"#{T} {a}")

# 1938 아주 간단한 계산기

a, b = list(map(int,input().split()))
print(a+b)
print(a-b)
print(a*b)
print(round(a/b))

# 2046 스탬프 찍기

number = int(input())
print(number*'#')

# 2068 최대수 구하기

T = int(input())
for T in range(1, T+1):
    numbers = list(map(int,input().split()))
    a = max(numbers)
    print(f"#{T} {a}")
