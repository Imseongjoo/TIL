# 2072 홀수만 더하기

T = int(input())
for T in range(1, T+1):
    sum = 0
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i % 2 == 1:
            sum += i
    print(f"#{T} {sum}")
