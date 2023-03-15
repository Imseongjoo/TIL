# 1204 [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2

T = int(input())
for i in range(T):
    idx = int(input())
    arr = list(map(int, input().split()))
    score = dict()
    for s in arr:
        if s in score:
            score[s] += 1
        else:
            score[s] = 1
    _max = max(score.values())

    print('#', end='')
    print(idx, next(key for key, value in score.items() if value == _max))
