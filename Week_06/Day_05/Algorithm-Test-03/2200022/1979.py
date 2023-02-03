# 1979 어디에 단어가 들어갈 수 있을까

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(N)]
    sum = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if ls[i][j] == 1:
                cnt += 1
            if ls[i][j] == 0 or j == N-1:
                if cnt == K:
                    sum += 1
                cnt = 0
        for j in range(N):
            if ls[j][i] == 1:
                cnt += 1
            if ls[j][i] == 0 or j == N-1:
                if cnt == K:
                    sum += 1
                cnt = 0
    print(f"#{_+1} {sum}")