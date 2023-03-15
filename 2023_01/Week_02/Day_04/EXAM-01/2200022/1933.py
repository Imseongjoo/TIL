# 1933 간단한 N의 약수

N = int(input())
result = 0
for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')
