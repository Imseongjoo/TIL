# 1225 [S/W 문제해결 기본] 7일차 - 암호생성기

from collections import deque
for tc in range(1,11):
    t = int(input())
    a = deque(map(int,input().split()))
    while True:
        for j in range(1,6): 
            s = a[0] - j
            a.append(s)
            a.popleft()  
            if s <= 0:
                s = 0
                break
        if(a[-1] <= 0):
            break
    a[7] = 0
    result = list(a)
    result2 = ' '.join(str(s) for s in result) 