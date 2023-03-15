# 14649 신용카드 만들기 1

T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    A = []
    A = sum(numbers[0::2])*2
    B = sum(numbers[1::2])
    N = 0
    if A + B + N % 10 == 0:
        print(f"#{i+1} {N%10}")
    elif A + B + N % 10 > 0:
        N = 10 - ((A + B) % 10)
        print(f"#{i+1} {N%10}")
