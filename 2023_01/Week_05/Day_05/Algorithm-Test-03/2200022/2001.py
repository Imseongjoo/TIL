# 2001 파리 퇴치

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for l in range(i, i+M):
                for k in range(j, j+M):
                    tmp += fly[l][k]
            if tmp > result:
                result = tmp
    print("#{} {}".format(test_case, result))
