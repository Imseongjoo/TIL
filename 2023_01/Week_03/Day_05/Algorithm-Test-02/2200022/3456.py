# 3456 직사각형 길이 찾기

T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    d = 0
    if a == c:
        d += b
    elif a == b:
        d += c
    elif b == c:
        d += a
    print(f"#{i+1} {d}")
