n, m = map(int, input().split())
board = [input() for _ in range(n)]
min_changes = n * m # 최솟값 초기화
for i in range(n - 7):
    for j in range(m - 7):
        changes1, changes2 = 0, 0 # 맨 왼쪽 위가 'W'인 경우와 'B'인 경우 각각 최소 변경 횟수
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W': # 'W'로 바꿔야 하는 경우
                        changes1 += 1
                    if board[x][y] != 'B': # 'B'로 바꿔야 하는 경우
                        changes2 += 1
                else:
                    if board[x][y] != 'B': # 'B'로 바꿔야 하는 경우
                        changes1 += 1
                    if board[x][y] != 'W': # 'W'로 바꿔야 하는 경우
                        changes2 += 1
        min_changes = min(min_changes, changes1, changes2)
print(min_changes)